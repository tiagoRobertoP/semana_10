import random
from collections import Counter
import matplotlib.pyplot as plt
import math

# multiplica um vetor por um escalar
def scalar_multiply(escalar, vetor):
    return [escalar * i for i in vetor]


def vector_sum(vetores):
    resultado = vetores[0]
    for vetor in vetores[1:]:
        resultado = [resultado[i] + vetor[i] for i in range(len(vetor))]
    return resultado


def vector_mean(vetores):
    return scalar_multiply(1 / len(vetores), vector_sum(vetores))


def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def vector_subtract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def sum_of_squares(v):
    return dot(v, v)


def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v, w))


class KMeans:
    def __init__(self, k, means=None):
        self.k = k
        self.means = means

    def classify(self, ponto):
        return min(range(self.k), key=lambda i: squared_distance(ponto, self.means[i]))

    def train(self, pontos):
        # escolher k elementos
        self.means = random.sample(pontos, self.k)
        assigments = None
        while True:
            # associa cada instância a um inteiro 0 <= i < k
            new_assigments = list(map(self.classify, pontos))
            if new_assigments == assigments:
                return
            assigments = new_assigments
            for i in range(self.k):
                # [1, 2, 3] e [1, 2, 2]
                i_points = [p for p, a in zip(pontos, assigments) if a == i]
                if i_points:
                    self.means[i] = vector_mean(i_points)


def test_kmeans():
    dados = [[1], [2], [3], [6], [7], [10], [11]]
    kmeans = KMeans(3, [[2], [10], [11]])
    kmeans.train(dados)
    print(kmeans.means)




def gera_sexo(quantidade_de_usuarios_na_rede):
    sexo =[]
    for i in range(quantidade_de_usuarios_na_rede):
        if (((random.randint(0,10))%2) == 0):
            sexo.append((i,"M"))
        else:
            sexo.append((i,"F"))
    return sexo                




def quantidade_de_amigos_por_sexo(gera_sexo):
    cont_sexo = []
    m = 0
    f = 0
    for j , i in gera_sexo:
        if (i == "M"):
            m += 1
        else:
            f += 1
    cont_sexo.append(m)  
    cont_sexo.append(f)      
    return (cont_sexo)        
    



def gera_idade(quantidade_de_usuarios_na_rede):
    idades = []
    for i in range(quantidade_de_usuarios_na_rede):
        idades.append((i,random.randint(18,60)))
    return idades


def gera_histograma_amigo_por_sexo(quantidade_de_amigos_por_sexo, qtde_usuarios_na_rede):
    x= ["M", "F"]
    xs = x
    ys = quantidade_de_amigos_por_sexo
    plt.bar(xs, ys)
    plt.axis([-1, 2, 0, qtde_usuarios_na_rede ])
    plt.title("Histograma da Contagem de Amigos por sexo")
    plt.xlabel("sexo")
    plt.ylabel("# de amigos")
    plt.show()




def quantidade_de_usuarios_na_rede():
    return 100


def gera_amizades(numero_conexoes_desejado, qtde_usuarios_na_rede):
    conexoes = []
    for i in range(numero_conexoes_desejado):
        while True:
            u1 = random.randint(0, qtde_usuarios_na_rede - 1)
            u2 = random.randint(0, qtde_usuarios_na_rede - 1)
            if u1 != u2:
                conexoes.append((u1, u2))
                break
    return [aux for aux in set(conexoes)]


def quantidade_de_amigos(amizades):
    a = Counter(i for i, _ in amizades)
    b = Counter(i for _, i in amizades)
    tudo = a + b
    return Counter(x for x in tudo.values())



def gera_intencao(quantidade_de_usuarios_na_rede):
    intencao =[]
    for i in range(quantidade_de_usuarios_na_rede):
        if (((random.randint(0,10))%2) == 0):
            intencao.append((i,"Haddad"))
        else:
            intencao.append((i,"Bolsonaro"))
    return intencao     











def main():
    print (gera_intencao(100))


main()
