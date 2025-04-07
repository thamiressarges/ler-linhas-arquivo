def ler_linhas_arquivos(fnome, nLinhas):
    from itertools import islice
    with open(fnome, encoding='utf-8') as arquivo:
        for linha in islice(arquivo, nLinhas):
            print(linha.strip())

ler_linhas_arquivos('dados/texto.txt', 3)


