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


class Pessoa:
    def __init__ (self, idade, sexo, salario, intencao_de_voto):
        self.idade = idade
        self.sexo = sexo
        self.salario = salario
        self.intencao_de_voto = intencao_de_voto
    def __str__ (self):
        return f'idade: {self.idade}, sexo: {self.sexo}, salario: {self.salario},intencao_de_voto: {self.intencao_de_voto}'

def gera_base (n):
    l = []
    for i in range (n):
#aleatorio no intervalo [a, b]
        idade = random.randint(18, 35)
        sexo = random.choice(['M', 'F'])
# aleatorio no intervalo [0.0, 1.0)
        salario = 1200 + random.random() * 1300
        intencao_de_voto = random.choice(['Haddad', "Bolsonaro"])
        p = Pessoa (idade, sexo, salario, intencao_de_voto)
        l.append(p)
    return l


def rotulo_de_maior_frequencia_sem_empate (pessoas):
    frequencias = Counter (pessoas)
    rotulo, frequencia = frequencias.most_common(1)[0]
    qtde_de_mais_frequentes = len([count for count in frequencias.values() if count == frequencia])
    if qtde_de_mais_frequentes == 1:
        return rotulo
    return rotulo_de_maior_frequencia_sem_empate(pessoas[:-1])

def distance (p1, p2):
    i = math.pow((p1.idade - p2.idade), 2)
    s = math.pow((1 if p1.sexo == 'M' else 0) - (1 if p2.sexo == 'M' else 0), 2)
    sal = math.pow((p1.salario - p2.salario), 2)
    return math.sqrt(i + s + sal)

def knn (k, observacoes_rotuladas, nova_observacao):
    ordenados_por_distancia = sorted (observacoes_rotuladas, key= lambda obs: distance (obs, nova_observacao))
    k_mais_proximos = ordenados_por_distancia[:k]
    resultado = rotulo_de_maior_frequencia_sem_empate(k_mais_proximos)
    return resultado.intencao_de_voto

def cvloo():
    base = gera_base(10)
    baseNova=[]
    for x in range(base):
        i=+1
        minus = len(base) - i
        for p in base:
            y=+1
            if y == minus:  
                continue
            baseNova.append(p)
        print(knn(5, baseNova, Pessoa (19, 'M', 1700, None)))






def main():
    print (cvloo)


main()
