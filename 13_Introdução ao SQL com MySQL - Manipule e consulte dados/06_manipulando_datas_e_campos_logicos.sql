USE SUCOS;

# Inserindo uma primary key
ALTER TABLE tbcliente ADD PRIMARY KEY (CPF);
# Add uma nova coluna a tabela
ALTER TABLE tbcliente ADD COLUMN (DATA_NASCIMENTO DATE);

INSERT INTO tbcliente(
CPF, NOME, ENDERECO1, ENDERECO2, BAIRRO, CIDADE, ESTADO, CEP, IDADE, SEXO, LIMITE_CREDITO, VOLUME_COMPRA, PRIMEIRA_COMPRA, DATA_NASCIMENTO)
VALUES ('00388934505', 'João da Silva', 'Rua projetada A número 10','', 'Vila Roman', 'Caratinga', 'Amazonas', '22222222', 30, 'M', 10000.00, 2000, 0, '1990-10-05');

SELECT * FROM tbcliente;