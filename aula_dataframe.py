import numpy as np
import pandas as pd

if __name__ == '__main__':

    dados_concursos = {
        'banca': ['cespe', 'cesgranrio'],
        'instituicao': ['tcu', 'bb'],
        'saalrio': [2500,3300],
        'data da prova': [pd.to_datetime('20/01/2018'),
                            pd.to_datetime('10/01/2021')]

    }

    tabela_concursos = pd.DataFrame(dados_concursos)

    print(tabela_concursos)
    #print(tabela_concursos.dtypes)

    print('_____________________________________________')

    alunos = [
        ['Joao', 10,'aprovado'],
        ['jaqueline', 10,'aprovado'],
        ['dayane', 10,'aprovado'],
        ['teste', 5,'reprovado'],
    ]



    dados_alunos = pd.DataFrame(alunos, columns= ['Aluno', 'Nota', 'Resultado'])
    print(dados_alunos)



