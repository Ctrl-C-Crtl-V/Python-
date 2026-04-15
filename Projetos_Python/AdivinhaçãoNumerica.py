import random

print("Seja muito bem-vindo(a) ao Guess do Adrian!\n")
choice_number = input("Digite um numero teto do desafio: ")

if choice_number.isdigit():
    choice_number = int(choice_number)
else:
    print("Algo está errado.. Tente digitar numeros!!")
    quit()

random_number = random.randint(0, choice_number)

n_choises = 0

while True:
    awser_user = input("Agora tente chutar o numero!\n ---> ")

    if awser_user.isdigit():
        awser_user = int(awser_user)
    else:
        awser_user = input("tente chutar um numero..\n ---> ")
        continue

    n_choises = n_choises + 1
    if awser_user == random_number:
        print("Parabéns! Você acertou!!")
        break
    elif awser_user > random_number:
        print("Chutou Alto!, talvez algo menor que isso...")
    else:
        print("Chutou Baixo!, talvez algo maior que isso...")

print("N° de tentativas: " + str(n_choises))