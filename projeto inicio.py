import numpy as np

if __name__ == '__main__':
    primeiro = [1,2,3]
    segundo = [5,6,7]
    Resultado_final = []

    for i in range(len(primeiro)):
        Resultado = primeiro[i] * segundo[i]
        Resultado_final.append(Resultado)
    print(Resultado_final)

    num_primeiro = np.array(primeiro)
    num_segundo = np.array(segundo)
    num_resultado = num_primeiro * num_segundo

    print(num_resultado.itemsize)














