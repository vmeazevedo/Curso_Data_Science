select * from produtos;

update produtos set preco_lista = 5 where codigo = '1040107';

update produtos set embalagem = 'PET', tamanho = '2 Litros', descritor = 'Light - 2 Litros - Graviola' where codigo = '1040108';

update produtos set preco_lista = preco_lista * 1.10 where sabor = 'Açai';