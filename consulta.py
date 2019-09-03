import banco

pesquisa = input("Digite o nome a ser pesquisado: ")

list = banco.DbConnection("SELECT NOME, CPF FROM ALUNOS WHERE TIPO = 'AL' AND NOME LIKE '%{}%'".format(pesquisa).upper())

for i in list:
    print(i)

