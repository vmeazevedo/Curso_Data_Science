
''' SQLITE '''

from sqlalchemy import create_engine, MetaData, Table

# Importando a base
matriculas_por_curso = pd.read_csv('matriculas_por_cursos.csv')

# Criando nossa engine localmente
engine = create_engine('sqlite:///:memory:')
print(engine)

print(matriculas_por_curso.head(3))

# Passando nosso DataFrame para SQL
matriculas_por_curso.to_sql('matriculas', engine)

# Visualizando as tabelas dentro da engine
print(engine.table_names())



''' Buscando no banco sql '''

# Criando uma var para utilizar como a query
query = 'select * from matriculas where quantidade_de_alunos < 20'

# Realizando a query com o metodo .read_sql
print(pd.read_sql(query, engine))

# Realizando uma query diretamente na tabela
muitas_matriculas = pd.read_sql_table('matriculas', engine, columns=['nome_do_curso', 'quantidade_de_alunos'])
print(muitas_matriculas)

# Utilizando uma query do proprio pandas
muitas_matriculas = muitas_matriculas.query('quantidade_de_alunos > 70')
print(muitas_matriculas)

''' Escrevendo no banco '''
# Criando uma tabela com os valores da query anterior
muitas_matriculas.to_sql('muitas_matriculas', con=engine)
print(engine.table_names())
