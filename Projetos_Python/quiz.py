#Cartão de Credito -Shopee, Shein-
#Caixa eletronica
#Supermercado -Ifood-

print("Seja muito bem-vindo ao quiz do Adrian! ")
awser_user = input("Quer começar? (S/N) : ").upper()
print(awser_user)

if awser_user != "S":
    quit()

score = 0

print("Começando....")
print("Quem criou a Saga Star Wars?\n (A) George Lucas\n (B) Walt Disney\n (C) Michael Dante\n (D) Neil Gaiman")
awser_1 = input("Resposta : ").upper()

print("Quem traiu os Jedi na ordem 66?\n (A) Mandalorianos \n (B) Clones\n (C) Droides\n (D) Governador")
awser_2 = input("Resposta : ").upper()


if awser_1 == "A":
    print("Correto!, Parabéns!!")
    score = score + 1
else:
    print("Errado! Dá pra melhorar..")

if awser_2 == "B":
    print("Correto!, Parabéns!!")
    score = score + 1
else:
    print("Errado dá pra melhorar..")

print(f"O quiz acabou.. Obrigado por participar!\nO seu score total foi: {score}")



