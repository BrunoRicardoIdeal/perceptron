import random, copy

class Perceptron:

	def __init__(self, amostras, saidas, taxa_aprendizado=0.1, epocas=1000, limiar=-1):

		self.amostras = amostras 
		self.saidas = saidas 
		self.taxa_aprendizado = taxa_aprendizado
		self.epocas = epocas 
		self.limiar = limiar 
		self.num_amostras = len(amostras) 
		self.num_amostra = len(amostras[0])
		self.pesos = []
	
	def treinar(self):
		
		# adiciona -1 para cada uma das amostras
		for amostra in self.amostras:
			amostra.insert(0, -1)

		# inicia o vetor de pesos com valores aleatórios
		for i in range(self.num_amostra):
			self.pesos.append(random.random())

		# insere o limiar no vetor de pesos
		self.pesos.insert(0, self.limiar)
	
		num_epocas = 0

		while True:

			# sem erro
			erro = False 

			# para todas as amostras de treinamento
			for i in range(self.num_amostras):

				u = 0

				'''
					realiza o somatório, o limite (self.amostra + 1)
					é porque foi inserido o -1 para cada amostra
				'''
				for j in range(self.num_amostra + 1):
					u += self.pesos[j] * self.amostras[i][j]

				# sáida pela função de ativação
				y = self.sinal(u)

				# compara com a saída desejada
				if y != self.saidas[i]:

					# calcula o erro
					erro_aux = self.saidas[i] - y

					# faz o ajuste dos pesos para cada elemento da amostra
					for j in range(self.num_amostra + 1):
						self.pesos[j] = self.pesos[j] + self.taxa_aprendizado * erro_aux * self.amostras[i][j]

					erro = True # ainda existe erro

			# incrementa o número de épocas
			num_epocas += 1

			# critério de parada é pelo número de épocas ou se não existir erro
			if num_epocas > self.epocas or not erro:
				break
	
	# perceber de qual classe é a mostra
	def testar(self, amostra, classe1, classe2):

		# iniciar com -1
		amostra.insert(0, -1)

		# usar os pesos que foi ajustado na fase de treinamento
		u = 0
		for i in range(self.num_amostra + 1):
			u += self.pesos[i] * amostra[i]

		# obter a saída
		y = self.sinal(u)

		# conferir a classe
		if y == -1:
			print('A amostra pertence a classe %s' % classe1)
		else:
			print('A amostra pertence a classe %s' % classe2)


	# aplicar o degrau bipolar
	def sinal(self, u):
		return 1 if u >= 0 else -1


print('\nA ou B?\n')

# amostras: um total de 4 amostras
amostras = [[0.1, 0.4, 0.7], [0.3, 0.7, 0.2], 
				[0.6, 0.9, 0.8], [0.5, 0.7, 0.1]]

print("Amostras:", amostras)				

# saídas desejadas de cada amostra
saidas = [1, -1, -1, 1]

print("Desejado:", saidas)				

# conjunto de amostras de testes
testes = copy.deepcopy(amostras)

# criar o Perceptron
rede = Perceptron(amostras=amostras, saidas=saidas,	
						taxa_aprendizado=0.1, epocas=1000)

# treina a rede
rede.treinar()

# testando a rede
for teste in testes:
	rede.testar(teste, 'A', 'B')