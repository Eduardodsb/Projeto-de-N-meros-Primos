# -*- coding: cp1252 -*-
import random
import math

#IN�CIO DA FUN��O MDC

def mdc(a,b):
    R = 1
    while (R!=0): #Enquanto o resto for diferente de 0, ser� realizado a divis�o entre "a" e "b".
        R = a % b #O resto da divis�o � guardado.
        a = b #O "b" passa a ser o novo "a"
        b = R #O "b" passa a ser o resto
    if(a == 1): #Caso o "a" seja 1, ent�o o mdc � 1 e � retornado 1.
        return 1
    else: #Caso contr�rio o mdc � diferente de 1 e � retornado 0.
        return 0
    
#FIM DA FUN��O MDC
    

#IN�CIO DA FUN��O FATORES(tal fun��o � respons�vel por achar todos diferentes fatores de um n�mero. obs: sem repeti��o de fatores)

def Fatores(a): # A fun��o Fatores, fatora o N-1 do teste de lucas. a recebe n-1.
    print ("//Inciando a Busca de Fatores de N-1 para o teste de Lucas...//")
    b = int(a) # Fa�o uma copia de "a" para "b".
    fatores = [] #Criei o vetor fatores para guardar os fatores de n-1.
    conf = 1 #conf serve para verificar se a multiplica��o dos fatores bate com o valor de "a" que � o "n-1"
    arq = open('BasedePrimos.txt', 'r') #acesso a base de primos.
    for linha in arq: #O for pecorre linha a linha.
        j=0
        if int(linha) <= int(b):#S� vou tentar fatorar pelo valores menores que n-1.
            while(int(b) % int(linha) == 0):#enquanto n-1 for divis�vel por determinado fator, ele vai ficar fatorando.
                conf = conf * int(linha)#vou multiplicando os fatores.
                if(j == 0):#Fa�o isso para n�o pegar fatores repitidos.
                    fatores.append(int(linha))#guardo os fatores de n-1.
                b = b//int(linha)#pego o novo valor de b, ap�s a divis�o pelo fator.
                j = j + 1#Fa�o para n�o pegar fator repido.
        if int(linha) > int(b): #Caso o valor de linha supere n, o for ser� quebra. se n�o ele ficaria comparando (if int(linha) <= int(n):) e perderia desempenho.
            break
    arq.close()#fecho o arquivo
    if(conf == a):# Confiro se a multiplica��o dos fatores encontrados bate como valor de n-1. caso sim eu retorno os fatores e o valor 1.
        return fatores,1
    if(conf != a):#Caso os valores n�o bata, tento descobrir se o fator que n�o consta na lista � um primo (In�cio de uma recurs�o).
        print ("Tentativa de descobrir se o fator de n-1 � primo - ", b)
        RespMiller = TesteMiller(b)
        if RespMiller == 0:
            RespLucas = TesteLucas(b)
            if RespLucas == 0:
                conf = conf*b
                if(conf == a):# Confiro se a multiplica��o dos fatores encontrados bate como valor de n-1. caso sim eu retorno os fatores e o valor 1.
                    return fatores,1
                else:
                    print("Fatora��o de n-1 n�o achou todos os fatores")
                    return fatores,0    
            else:
                print("Fatora��o de n-1 n�o achou todos os fatores")
                return fatores,0
        else:
            print("Fatora��o de n-1 n�o achou todos os fatores")
            return fatores,0
        
#FIM DA FUN��O FATORES

#IN�CIO DA FUN��O FATPRIMOS(Tal fun��o, � respons�vel por fazer a primeira etapa do processo. � feita a fatora��o ing�nua at� os primeiros 1 milh�o de primos).

def FatPrimos (n):# Recebe "n" como argumento.
    cont = 0
    arq = open('BasedePrimos.txt', 'r')#Acesso a base de primos.
    for linha in arq:#O for pecorre linha a linha.
        if int(linha) < int(n):#S� vou tentar fatorar pelo valores menores que n-1.
            cont = cont + 1 #Var�vel de controle
            if(cont == 1000000): #Caso pecorra o primeiro milh�o de primo e n�o ache um fator, ser� considerado inconclusivo. Pois o miller testa mais r�pido.
                print("Fatora��o Ing�nua muito lenta, ser� considerado inconclusivo para que o miller possa testar...")
                RespFatP = 0# � retornado 0 para dar inconclusivo e ir pro miller.
                arq.close()#fechei o arquivo.
                return RespFatP
                
            if int(n) % int(linha) == 0:#� verificado de algum primo do arquivo � fator de n. Caso seja, � retornado 1(composto).
                RespFatP = 1
                arq.close()
                return RespFatP
        if int(linha) > int(n):#Caso o valor de linha supere n, o for ser� quebra. se n�o ele ficaria comparando (if int(linha) < int(n):) e perderia desempenho.
            break #Sai do for.
    RespFatP = 0# caso n�o ache um fator primo ele retorna 0(Inconclusivo)
    arq.close()#fechei o arquivo.
    return RespFatP

#FIM DA FUN��O FATPRIMOS

#IN�CIO DA FUN��O TESTEMILLER (Na fun��o TesteMiller executo o teste para os n�meros que deram inconclusivo na FatPrimos).

def TesteMiller (n):
    print ("//Inciando Miller...//")
    auxx = 0 #vari�vel de controle
    arq = open('BasedePrimos.txt', 'r')#Acesso a base de primos.
    for i in range(0, 15):#Testo 15 bases alet�rias.
        b = int(arq.readline())#b recebe linhas por linha(d� linha 0 at� 15).
        denominador = 1
        cont = cont1 = aux = 0
        if(mdc(b,n) == 1):#Caso o mdc entre n e b seja 1 ele continuar�
            while((n-1)%denominador == 0):#Enquanto for possivel dividir os expo�ntes da tabela de miller.
                expo = (n-1)//denominador
                RES = pow(b,expo,n)#fa�o b elevado a expo em mod n
                
                if(RES == (n-1)): #Caso a tabela de -1
                    aux = aux + 1 #vari�vel de controle

                if(RES == 1): #Caso a tabela de completamente 1
                    cont = cont + 1 #vari�vel de controle

                denominador = denominador*2
                cont1 = cont1 + 1 #vari�vel de controle

            if(aux == 0) and (cont != cont1):# se n�o caiu no caso do -1 e n�o caiu no caso do tudo 1 ele � composto e � retornado 0. Caso cai em um dos casos, ele n�o entra no if e segue para a por�xima base.
                RespTesM = 1
                return RespTesM
            
        auxx = auxx +1 #vari�vel de controle
    if(auxx == 15):#Caso auxx seja 15, siginifica que ele caiu em algum caso de -1 ou da tabela completamente 1.  
        RespTesM = 0
        return RespTesM
    
#FIM DA FUN��O FATPRIMOS

#IN�CIO DA FUN��O TESTELUCAS (Na fun��o TesteLucas, testo os n�meros que deram inconclusivo tanto no FatPrimos quanto no TesteMiller, para ter certeza que tal n�mero � primo).

def TesteLucas (n):
    cont = 0
    print ("//Inciando Lucas...//")
    Fatoress = [] #� criado o vetor "Fatoress" para receber os fatores retornado pela fun��o fatores.
    Fatoress,z = Fatores(n-1)# chamo a fun��o Fatores para fatorar n-1
    if(z == 0):#caso a fun��o Fatores retorne 0, significa que n�o foi possivel fatorar o n-1. Desta forma � retornado para a principal o valor 2.
        RespTesL = 2
        return RespTesL
    for i in range(0, 15):#Testo em 15 bases diferentes.
        b = random.randint(2,n-1)#sorteio das bases.
        if(mdc(b,n) == 1):#Caso o mdc entre n e b seja 1 ele continuar�
            if(pow(b,n-1,n) == 1): #verifico se quando o expo�nte � n-1 ser� realmente. Caso seja o processo continua.
                for j in range(0,len(Fatoress)):#corro o vetor. Para dividir o n-1 pelos seus fatores e achar os exp�entes.
                    expo = (n-1)//Fatoress[j] #Descubro o novo expoente.
                    RES = pow(b,expo,n)
                    #print (b," ", expo," ", n) # <- utilizei apenas para controle do processo. 
                    #print (RES) #<- utilizei apenas para controle do porcesso.
                    if(RES != 1):#caso o resultado seja diferente de 1 ele ira somar um ao cont. siginifica que em determinado expoente deu diferente de 1 barra, desta forma uso a vari�vel cont para contar em quantos expoentes abaixo de n-1 vai dar diferente de 1
                        cont = cont + 1
                if(cont == len(Fatoress)): #caso a quantidade de cont seja igual as dos expoentes testado(fatoress), quer dizer que apenas n-1 deu 1 barra, e logo � retornado 0(confirma��o que � primo).
                        RespTesL = 0 #retorna 0
                        return RespTesL
        #print ("---------------------") # <- utilizei apenas para controle do processo. 
        cont = 0
    RespTesL = 1#caso n�o caia na condi��o que confirma que � primo, siginifica que � inconclusivo.
    return RespTesL#� retornado 1.

#FIM DA FUN��O TESTELUCAS
                
    
#IN�CIO DA FUN��O PRINCIPAL,                

n = int(input('Acima de qual valor voc� deseja o primo?')) #Entrada do Usu�rio.  
parada = 0 #Utilizo a Vari�vel "parada" como minha condi��o de parada para sair do while.
while(parada != 1): #Enquanto n�o achar um primo a Vari�vel "parada" n�o recebe o valor 1.
    RespFatP = FatPrimos(n) #� chamada a fun��o FatPrimos que � respons�vel pela primeira etapa do processo. Tal fun��o faz fatora��o ing�nua, do valor de entrada, pelos primeiros 1 milh�o primos.
    if(RespFatP == 1): #Caso FatPrimos retorne valor 1, significa que o teste de fatora��o ing�nua acusou o n�mero como composto.
        print ("O teste de fatora��o ing�nua acusou composto para o: ",n)
        print ("_____________________________________________________________________________________")
        n = n+1 #Uma vez que o n�mero � composto � somado uma unidade ao mesmo.
    if(RespFatP == 0): #Caso FatPrimos retorne valor 0, significa que o teste de fatora��o ing�nua foi inconclusivo.
        print ("O teste de fatora��o ing�nua acusou inconclusivo para o: ",n)
        print ("_____________________________________________________________________________________")
        RespTesM = TesteMiller(n) #Uma vez que, o teste da fatora��o ing�nua � inconclusivo � chamado o teste de Miller (2� etapa). 
        if(RespTesM == 1): #Caso Miller retorne 1, significa que o teste de miller deu composto.
            print ("O teste de Miller acusou composto para o: ",n)
            print ("_____________________________________________________________________________________")
            n = n+1 #Uma vez que o n�mero � composto � somado uma unidade ao n.
        if(RespTesM == 0): #Caso o teste de miller retorne 0, significa que o teste deu inconclusivo.
            print ("O teste de Miller acusou inconclusivo para o: ",n)
            print ("_____________________________________________________________________________________")
            RespTesL = TesteLucas(n) #Uma vez que, o teste de Miller � inconclusivo � chamado o teste de Lucas. 
            if(RespTesL == 2): #Caso o teste de Lucas retorne 2, significa que n�o foi achado os fatores de n-1.
                print ("O teste de Lucas n�o pode ser concluido: ",n)
                print ("_____________________________________________________________________________________")
                n = n+1 #Logo, � somado novamente mais uma unidade ao n.
            if(RespTesL == 1): #Caso o teste de Lucas retorne 1, significa que o teste deu composto. 
                print ("O teste de Lucas acusou inconclusivo para o: ",n)
                print ("_____________________________________________________________________________________")
                n = n+1 #E novamente � somado uma unidade ao n.
            if(RespTesL == 0): #Caso o teste de Lucas retorne 0, significa que o teste de lucas confirmou que n�mero � primo.
                print ("O teste de lucas confirmou que � primo o: ",n)
                print ("_____________________________________________________________________________________")
                parada = 1 #Uma vez que � achado um primo, a condi��o de parada recebe valor 1, para poder sair do while, e o algoritmo � encerrado.

#FIM DA FUN��O PRINCIPAL,
