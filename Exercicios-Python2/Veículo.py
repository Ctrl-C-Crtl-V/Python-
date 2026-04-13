while True:
    #variaveis
    
    Valor=float()
    
    #Entrada
    
    ValorF=float(input('Digite o valor Financeiro do seu Veículo: '))
    Entrada=float(input('Digite a Entrada do seu Veículo: '))
    Ano=float(input('Digite o Ano do seu Veículo: '))
    PlanoPag=float(input('Quantos meses vai financiar seu Veículo: '))
    
    
    
    
    #Condicionais
    
    if (PlanoPag <= 12):
        print ('Seus juros serão de 20%')
        porcentagem=(ValorF * 20/100)
        Valor= ( ValorF + porcentagem)
    
    elif (PlanoPag <= 24):
        print ('será de 35%')
        porcentagem=(ValorF * 20/100)
        Valor= ( ValorF + porcentagem)
        #Valor= (ValorF * 35/100 and Valor + PlanoPag)
        
    
    elif (PlanoPag <= 36):
        print ('sera 47%')
        porcentagem=(ValorF * 20/100)
        Valor= ( ValorF + porcentagem)
        #Valor= (ValorF * 47/100 and Valor + PlanoPag)
    
    else:
        print ('48 meses')
        porcentagem=(ValorF * 20/100)
        Valor= ( ValorF + porcentagem)
        #Valor= (ValorF * 63/100 and Valor + PlanoPag)
    
    #---------------------------------------------------------------------------
    
    if (Ano >=  2006 ):
        print('Aliquota de py4%')
        IPVA=round((ValorF*4/100))
    
    
    else:
        print('Isenção de imposto')
        IPVA = (0)
    
    
    #Processo
        Parcela=round((Valor/PlanoPag))



    #saída
    print ("---------------------------------------------------------------")
    print ('Valor Total: {}\nPlano de Pagamento: {}' .format (Valor,PlanoPag,))
    print ('Valor financeiro {}\nParcela {}'.format (ValorF,Parcela))
    print ('IPVA {}' .format (IPVA))
    print ("---------------------------------------------------------------")

    #laço
    continuar= input ('novo cálculo [S/N]: ')
    if (continuar == 'N' or continuar == 'n'):
        break