import numpy as np

if __name__ == '__main__':
    anos_nascimento = np.loadtxt('anos_de_nascimento.txt')
    idades = 2021 - anos_nascimento
    print(anos_nascimento)
    print(idades)

    media = idades.sum() / idades.size
    print(media)