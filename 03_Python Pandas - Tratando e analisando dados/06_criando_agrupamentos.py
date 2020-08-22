''' Relatórios de Análise VII
Criando Agrupamentos '''

import pandas as pd 
dados = pd.read_csv('dados\\aluguel_residencial_3.csv', sep=';')
print(dados.head(10))

# Filtrando todos os bairros da nossa base
# dados = dados['Bairro'].unique()

# Criando uma lista com todos os bairros disponíveis
bairros = ['Copacabana', 'Jardim Botânico', 'Centro', 'Higienópolis', 'Cachambi'
 'Barra da Tijuca', 'Ramos', 'Grajaú', 'Lins de Vasconcelos', 'Taquara'
 'Freguesia (Jacarepaguá)', 'Tijuca', 'Olaria', 'Ipanema', 'Campo Grande'
 'Botafogo', 'Recreio dos Bandeirantes', 'Leblon', 'Jardim Oceânico'
 'Humaitá', 'Península', 'Méier', 'Vargem Pequena', 'Maracanã', 'Jacarepaguá'
 'São Conrado', 'Vila Valqueire', 'Gávea', 'Cosme Velho', 'Bonsucesso'
 'Todos os Santos', 'Laranjeiras', 'Itanhangá', 'Flamengo', 'Piedade', 'Lagoa'
 'Catete', 'Jardim Carioca', 'Benfica', 'Glória', 'Praça Seca', 'Vila Isabel'
 'Engenho Novo', 'Engenho de Dentro', 'Pilares', 'Água Santa', 'São Cristóvão'
 'Ilha do Governador', 'Jardim Sulacap', 'Oswaldo Cruz', 'Vila da Penha'
 'Anil', 'Vargem Grande', 'Tanque', 'Vaz Lobo', 'Madureira'
 'São Francisco Xavier', 'Pechincha', 'Leme', 'Irajá', 'Quintino Bocaiúva'
 'Urca', 'Penha', 'Gardênia Azul', 'Rio Comprido', 'Andaraí', 'Santa Teresa'
 'Inhaúma', 'Marechal Hermes', 'Curicica', 'Santíssimo', 'Moneró', 'Camorim'
 'Cascadura', 'Praia da Bandeira', 'Saúde', 'Joá', 'Realengo', 'Fátima'
 'Inhoaíba', 'Rocha', 'Jardim Guanabara', 'Jabour', 'Braz de Pina'
 'Praça da Bandeira', 'Vila Kosmos', 'Vista Alegre', 'Encantado', 'Campinho'
 'Guaratiba', 'Riachuelo', 'Bangu', 'Lapa', 'Catumbi', 'Penha Circular'
 'Abolição', 'Tomás Coelho', 'Colégio', 'Pavuna', 'Santa Cruz'
 'Alto da Boa Vista', 'Cidade Nova', 'Bento Ribeiro', 'Estácio'
 'Jardim América', 'Cordovil', 'Caju', 'Pedra de Guaratiba', 'Padre Miguel'
 'Paciência', 'Del Castilho', 'Arpoador', 'Sampaio', 'Anchieta', 'Icaraí'
 'Senador Vasconcelos', 'Rocha Miranda', 'Gamboa', 'Maria da Graça'
 'Barra de Guaratiba', 'Vicente de Carvalho', 'Paquetá', 'Largo do Machado'
 'Parada de Lucas', 'Freguesia (Ilha do Governador)', 'Portuguesa'
 'Guadalupe', 'Parque Anchieta', 'Turiaçu', 'Pitangueiras', 'Vila Militar'
 'Vidigal', 'Senador Camará', 'Usina', 'Vigário Geral', 'Cosmos', 'Jacaré'
 'Cocotá', 'Honório Gurgel', 'Engenho da Rainha', 'Cachamorra', 'Zumbi', 'Tauá'
 'Santo Cristo', 'Ribeira', 'Magalhães Bastos', 'Cacuia', 'Bancários'
 'Cavalcanti', 'Rio da Prata', 'Cidade Jardim', 'Coelho Neto']


# Realizando uma seleção e criando um novo DataFrame
selecao = dados['Bairro'].isin(bairros)                 # Criamos uma seleção onde a minha lista tem que ser igual a minha coluna Bairro
dados = dados[selecao]                                  # Criamos um novo DataFrame
sem_duplicadas = dados['Bairro'].drop_duplicates()      # Removemos as duplicadas com o drop_duplicates
print(sem_duplicadas)

# Criamos um grupo com os dados 
grupo_bairro = dados.groupby('Bairro')                  # Criamos um grupo com os valores da coluna Bairro
v = (grupo_bairro[['Valor', 'Condominio']].mean()).round(2)             # No meu grupo, eu peço o Valor de cada item e passo o metodo mean para apresentar a media deles
print(v)