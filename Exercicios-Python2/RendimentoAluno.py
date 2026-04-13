import os


#Criando uma opcao

#def exibir_resultado():
        #print ('Média final é {} \nSituação final: {}' .format(media,situacao) )
        #print ('media final é: {media}\nSituação final: {situacao})')
        #print ('media final é:{}\nSituação final: {}' .format(media,situacao))


while True:
    #bibleoteca
    os.system('cls')
    #Entrada de dados
    n1=float(input('digite a nota 1:'))
    n2=float(input('digite a nota 2:'))
    n3=float(input('digite a nota 3:'))
    #processamento
    media= round((n1+n2+n3)/3)
    #condicionais
    if (media < 4):
        situacao='Reprovado'
    elif (media >=4 and media <6):
        situacao='Recuperação'
    else:
        situacao='Aprovado'

    # Saída de dados
    print ("---------------------------------------------------------------")
    print ('Sua Media final é: {}\nSituação final: {}' .format (media,situacao))
    print ("---------------------------------------------------------------")


    continuar= input ('novo cálculo [S/N]: ')
    if (continuar == 'N' or continuar == 'n'):
        break
