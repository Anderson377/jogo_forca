
#importacao da biblioteca random para gerar as palavras de ordem aleatoria
import random

#palavras a serem escolhidas pelo sistema
palavras = ["computador", "cachorro", "mulher", "brasil", "teclado", "carriola","casa"]

#selecao da palavra em ordem aleatoria
palavra = random.choice(palavras)

print (palavra)

#numeros de tentativas geradas pelo usuario
tentativas = 0

#numero maximo de tentativas
chances = 4

#variavel temporaria
letras_escolhidas = []

#variavel a ser preenchida pelas palavras acertadas
estado_atual = ["_"] * len(palavra)

#Trofeu de vencedor
def msg_vencedor():
    print("\n\nParabéns, você ganhou! a palavra era: ", palavra)
    print("       ___________      ")
    print("       **       **      ")
    print("       **       **      ")
    print("        **     **       ")
    print("         **___**        ")
    print("           ||           ")
    print("         __||__         ")
    print("        |______|        ")


def msg_perdeu():
	print("\n\n Você PERDEU! a palavra sorteada era: ", palavra)
	print("       ___________      ")
	print("      **          **    ")
	print("      **   *   *  **    ")
	print("      **          **    ")
	print("      **     |    **    ")
	print("      **  ______  **    ")
	print("      ** |      | **    ")
	print("      **__________**    ")


#mensagens de boas vindas e uma previa explicacao sobre o jogo
print("="*28)
print ("Bem vindo ao jogo da forca")
print("="*28)
print ("Vamos adivinhar a palavra secreta?")
print ("Caso voce erre,  perdera uma chance, você tem no máximo", chances, "tentativas")

# condicional para as palavras inseridas pelo usuario
while tentativas < chances and ''.join(estado_atual) != palavra:
	letra = input("\n\nQual letra você quer tentar? ")

	while letra in letras_escolhidas:
		print ("Esta letra ja so digitada, por favor escolha outra letra!")
		letra = input("\nDigite uma letra ")
	letras_escolhidas.append(letra)

	if letra in palavra:
		print ("Parabéns, você acertou a letra!\n")
		for i in range(len(palavra)):
			if letra == palavra[i]:
				estado_atual[i] = letra
	else:
		print ("Que pena, você errou!\n")
		tentativas = tentativas + 1

	# quantas tentativas ainda faltam
	print ("Você ja efetuou", tentativas, "tentativas erradas e ainda tem", chances-tentativas, "tentativas" )

	# estado atual do jogo
	print ("Esse é o estado atual: ")
	print (estado_atual)

	#letras que ja foram tentadas
	print ("As letras que você já tentou são: ")
	for item in letras_escolhidas:
		print (item, end=" ")

# mensagens para finalizar o jogo
if tentativas == chances:
	msg_perdeu()	
else:	
	msg_vencedor()
	



