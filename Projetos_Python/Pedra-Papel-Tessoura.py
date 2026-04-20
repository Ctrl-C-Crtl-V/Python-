import random

user_points = 0
computer_points = 0

options = ["r","p","t"]

while True:
    print("-----------------------------------------------------------------------------------------")
    user_choise = input("\nEscolha -R- para pedra, -P- para papel, -T- para tesoura ou -Q- para sair\n" + "\n--->  ").lower()
    print("-----------------------------------------------------------------------------------------")

    if user_choise == "q":
        print("Até Mais!")
        break

    if user_choise not in options:
        print("\nDigite alguma escolha Válida. ")
        continue

    computer_choise = random.randint(0, 2)
    # 0  : R, 1 : P, 2 : T
    computer_option = options[computer_choise]

    print("O computador Escolheu: " + computer_option)

    if computer_option == user_choise:
        print("Empate!")
    elif user_choise == "r" and computer_option == "t":
        print("Você Ganhou!")
        user_points = user_points + 1

    elif user_choise == "t" and computer_option == "p":
        print("Você Ganhou!")
        user_points = user_points + 1

    elif user_choise == "p" and computer_option == "r":
        print("Você Ganhou!")
        user_points = user_points + 1

    else:
        print("Você Perdeu.. :(")
        computer_points = computer_points + 1


print("A SUA pontuação foi : " + str(user_points))
print("E o seu rival: " + str(computer_points))

if computer_points > user_points:
    print("Você foi Derrotado(a)!")

elif computer_points == user_choise:
    print("Empate para ambos lados")

else:
    print("Você foi Vitorioso(a)!")
