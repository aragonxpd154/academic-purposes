import heapq

class Fila:
    def __init__(self):
        self.itens = []
    
    # Função para adicionar um novo item a fila
    
    def enqueue(self, item):
        self.itens.append(item)
    
    def dequeue(self):
        return self.itens.pop(0)
    
    def inEmpty(self):
        return self.itens == []
    
    def size(self):
        return len(self.itens)
    
    # Instanciandno um objeto estacionamento que recebe a clasee Fila()
    
# Verificando se a fila está vazia ou não
print("\n")
    
estacionamento = Fila()
    
if Fila.inEmpty:
    print("Não há elementos na fila!!")
else:
    print("Há elementos na fila!!")
    
print("\n")

# Inserindo carros na fila do estacionamento

estacionamento.enqueue("Carro Azul")
estacionamento.enqueue("Carro Verde")
estacionamento.enqueue("Carro Vermelho")

print("Esses são os carros que estão na fila do estacionamento: \n" , estacionamento.itens)
print("\n")

# Estacionando o carro que chegou primeiro na fila
estacionamento.dequeue()

class FilaPrioridade:
    
    def __init__(self):
        self.itens = []
        self._indice = 0
    
    def __str__(self):
        return '\n'.join([str(i) for i in self.itens])
    
    def isEmpty(self):
        return self.itens == []
    
    def enqueue(self, item, prioridade):
        heapq.heappush(self.itens, (-prioridade, self._indice, item))
        self._indice += 1
        
    def dequeue(self):
        return heapq.heappop(self.itens)[-1]

fila_prioridade = FilaPrioridade()
fila_prioridade.enqueue('Info Dados', 1) # empresa
fila_prioridade.enqueue('Gabriel Gomes', 2) # Cliente Normal
fila_prioridade.enqueue('Mariana Lima', 5) # Cliente idosa
print(fila_prioridade)
    
print ('\n')

print(fila_prioridade.dequeue())
print(fila_prioridade.dequeue())
print(fila_prioridade.dequeue())

print("\n")

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.itens = []
        self._indice = 0
    def __repr__(self):
        return self.nome
    
    def enqueue(self, item, prioridade):
        heapq.heappush(self.itens, (-prioridade, self._indice, item))
        self._indice += 1

pronto_socorro = FilaPrioridade()
pronto_socorro.enqueue(Pessoa('Idoso'), 20)
pronto_socorro.enqueue(Pessoa('Gestante'), 30)
pronto_socorro.enqueue(Pessoa('Idosa'), 20)
print("Pessoas na fila:\n")
print(pronto_socorro)

while not pronto_socorro.isEmpty():
    print("Próxima Pessoa a ser atendida: ", pronto_socorro.dequeue())
    
