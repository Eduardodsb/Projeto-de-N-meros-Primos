# -*- coding: cp1252 -*-
import random
import math

#INÍCIO DA FUNÇÃO MDC

def mdc(a,b):
    R = 1
    while (R!=0): #Enquanto o resto for diferente de 0, será realizado a divisão entre "a" e "b".
        R = a % b #O resto da divisão é guardado.
        a = b #O "b" passa a ser o novo "a"
        b = R #O "b" passa a ser o resto
    if(a == 1): #Caso o "a" seja 1, então o mdc é 1 e é retornado 1.
        return 1
    else: #Caso contrário o mdc é diferente de 1 e é retornado 0.
        return 0
    
#FIM DA FUNÇÃO MDC
    

#INÍCIO DA FUNÇÃO FATORES(tal função é responsável por achar todos diferentes fatores de um número. obs: sem repetição de fatores)

def Fatores(a): # A função Fatores, fatora o N-1 do teste de lucas. a recebe n-1.
    print ("//Inciando a Busca de Fatores de N-1 para o teste de Lucas...//")
    b = int(a) # Faço uma copia de "a" para "b".
    fatores = [] #Criei o vetor fatores para guardar os fatores de n-1.
    conf = 1 #conf serve para verificar se a multiplicação dos fatores bate com o valor de "a" que é o "n-1"
    arq = open('BasedePrimos.txt', 'r') #acesso a base de primos.
    for linha in arq: #O for pecorre linha a linha.
        j=0
        if int(linha) <= int(b):#Só vou tentar fatorar pelo valores menores que n-1.
            while(int(b) % int(linha) == 0):#enquanto n-1 for divisível por determinado fator, ele vai ficar fatorando.
                conf = conf * int(linha)#vou multiplicando os fatores.
                if(j == 0):#Faço isso para não pegar fatores repitidos.
                    fatores.append(int(linha))#guardo os fatores de n-1.
                b = b//int(linha)#pego o novo valor de b, após a divisão pelo fator.
                j = j + 1#Faço para não pegar fator repido.
        if int(linha) > int(b): #Caso o valor de linha supere n, o for será quebra. se não ele ficaria comparando (if int(linha) <= int(n):) e perderia desempenho.
            break
    arq.close()#fecho o arquivo
    if(conf == a):# Confiro se a multiplicação dos fatores encontrados bate como valor de n-1. caso sim eu retorno os fatores e o valor 1.
        return fatores,1
    if(conf != a):#Caso os valores não bata, tento descobrir se o fator que não consta na lista é um primo (Início de uma recursão).
        print ("Tentativa de descobrir se o fator de n-1 é primo - ", b)
        RespMiller = TesteMiller(b)
        if RespMiller == 0:
            RespLucas = TesteLucas(b)
            if RespLucas == 0:
                conf = conf*b
                if(conf == a):# Confiro se a multiplicação dos fatores encontrados bate como valor de n-1. caso sim eu retorno os fatores e o valor 1.
                    return fatores,1
                else:
                    print("Fatoração de n-1 não achou todos os fatores")
                    return fatores,0    
            else:
                print("Fatoração de n-1 não achou todos os fatores")
                return fatores,0
        else:
            print("Fatoração de n-1 não achou todos os fatores")
            return fatores,0
        
#FIM DA FUNÇÃO FATORES

#INÍCIO DA FUNÇÃO FATPRIMOS(Tal função, é responsável por fazer a primeira etapa do processo. É feita a fatoração ingênua até os primeiros 1 milhão de primos).

def FatPrimos (n):# Recebe "n" como argumento.
    cont = 0
    arq = open('BasedePrimos.txt', 'r')#Acesso a base de primos.
    for linha in arq:#O for pecorre linha a linha.
        if int(linha) < int(n):#Só vou tentar fatorar pelo valores menores que n-1.
            cont = cont + 1 #Varável de controle
            if(cont == 1000000): #Caso pecorra o primeiro milhão de primo e não ache um fator, será considerado inconclusivo. Pois o miller testa mais rápido.
                print("Fatoração Ingênua muito lenta, será considerado inconclusivo para que o miller possa testar...")
                RespFatP = 0# É retornado 0 para dar inconclusivo e ir pro miller.
                arq.close()#fechei o arquivo.
                return RespFatP
                
            if int(n) % int(linha) == 0:#É verificado de algum primo do arquivo é fator de n. Caso seja, é retornado 1(composto).
                RespFatP = 1
                arq.close()
                return RespFatP
        if int(linha) > int(n):#Caso o valor de linha supere n, o for será quebra. se não ele ficaria comparando (if int(linha) < int(n):) e perderia desempenho.
            break #Sai do for.
    RespFatP = 0# caso não ache um fator primo ele retorna 0(Inconclusivo)
    arq.close()#fechei o arquivo.
    return RespFatP

#FIM DA FUNÇÃO FATPRIMOS

#INÍCIO DA FUNÇÃO TESTEMILLER (Na função TesteMiller executo o teste para os números que deram inconclusivo na FatPrimos).

def TesteMiller (n):
    print ("//Inciando Miller...//")
    auxx = 0 #variável de controle
    arq = open('BasedePrimos.txt', 'r')#Acesso a base de primos.
    for i in range(0, 15):#Testo 15 bases aletórias.
        b = int(arq.readline())#b recebe linhas por linha(dá linha 0 até 15).
        denominador = 1
        cont = cont1 = aux = 0
        if(mdc(b,n) == 1):#Caso o mdc entre n e b seja 1 ele continuará
            while((n-1)%denominador == 0):#Enquanto for possivel dividir os expoêntes da tabela de miller.
                expo = (n-1)//denominador
                RES = pow(b,expo,n)#faço b elevado a expo em mod n
                
                if(RES == (n-1)): #Caso a tabela de -1
                    aux = aux + 1 #variável de controle

                if(RES == 1): #Caso a tabela de completamente 1
                    cont = cont + 1 #variável de controle

                denominador = denominador*2
                cont1 = cont1 + 1 #variável de controle

            if(aux == 0) and (cont != cont1):# se não caiu no caso do -1 e não caiu no caso do tudo 1 ele é composto e é retornado 0. Caso cai em um dos casos, ele não entra no if e segue para a poróxima base.
                RespTesM = 1
                return RespTesM
            
        auxx = auxx +1 #variável de controle
    if(auxx == 15):#Caso auxx seja 15, siginifica que ele caiu em algum caso de -1 ou da tabela completamente 1.  
        RespTesM = 0
        return RespTesM
    
#FIM DA FUNÇÃO FATPRIMOS

#INÍCIO DA FUNÇÃO TESTELUCAS (Na função TesteLucas, testo os números que deram inconclusivo tanto no FatPrimos quanto no TesteMiller, para ter certeza que tal número é primo).

def TesteLucas (n):
    cont = 0
    print ("//Inciando Lucas...//")
    Fatoress = [] #É criado o vetor "Fatoress" para receber os fatores retornado pela função fatores.
    Fatoress,z = Fatores(n-1)# chamo a função Fatores para fatorar n-1
    if(z == 0):#caso a função Fatores retorne 0, significa que não foi possivel fatorar o n-1. Desta forma é retornado para a principal o valor 2.
        RespTesL = 2
        return RespTesL
    for i in range(0, 15):#Testo em 15 bases diferentes.
        b = random.randint(2,n-1)#sorteio das bases.
        if(mdc(b,n) == 1):#Caso o mdc entre n e b seja 1 ele continuará
            if(pow(b,n-1,n) == 1): #verifico se quando o expoênte é n-1 será realmente. Caso seja o processo continua.
                for j in range(0,len(Fatoress)):#corro o vetor. Para dividir o n-1 pelos seus fatores e achar os expôentes.
                    expo = (n-1)//Fatoress[j] #Descubro o novo expoente.
                    RES = pow(b,expo,n)
                    #print (b," ", expo," ", n) # <- utilizei apenas para controle do processo. 
                    #print (RES) #<- utilizei apenas para controle do porcesso.
                    if(RES != 1):#caso o resultado seja diferente de 1 ele ira somar um ao cont. siginifica que em determinado expoente deu diferente de 1 barra, desta forma uso a variável cont para contar em quantos expoentes abaixo de n-1 vai dar diferente de 1
                        cont = cont + 1
                if(cont == len(Fatoress)): #caso a quantidade de cont seja igual as dos expoentes testado(fatoress), quer dizer que apenas n-1 deu 1 barra, e logo é retornado 0(confirmação que é primo).
                        RespTesL = 0 #retorna 0
                        return RespTesL
        #print ("---------------------") # <- utilizei apenas para controle do processo. 
        cont = 0
    RespTesL = 1#caso não caia na condição que confirma que é primo, siginifica que é inconclusivo.
    return RespTesL#é retornado 1.

#FIM DA FUNÇÃO TESTELUCAS
                
    
#INÍCIO DA FUNÇÃO PRINCIPAL,                

n = int(input('Acima de qual valor você deseja o primo?')) #Entrada do Usuário.  
parada = 0 #Utilizo a Variável "parada" como minha condição de parada para sair do while.
while(parada != 1): #Enquanto não achar um primo a Variável "parada" não recebe o valor 1.
    RespFatP = FatPrimos(n) #É chamada a função FatPrimos que é responsável pela primeira etapa do processo. Tal função faz fatoração ingênua, do valor de entrada, pelos primeiros 1 milhão primos.
    if(RespFatP == 1): #Caso FatPrimos retorne valor 1, significa que o teste de fatoração ingênua acusou o número como composto.
        print ("O teste de fatoração ingênua acusou composto para o: ",n)
        print ("_____________________________________________________________________________________")
        n = n+1 #Uma vez que o número é composto é somado uma unidade ao mesmo.
    if(RespFatP == 0): #Caso FatPrimos retorne valor 0, significa que o teste de fatoração ingênua foi inconclusivo.
        print ("O teste de fatoração ingênua acusou inconclusivo para o: ",n)
        print ("_____________________________________________________________________________________")
        RespTesM = TesteMiller(n) #Uma vez que, o teste da fatoração ingênua é inconclusivo é chamado o teste de Miller (2° etapa). 
        if(RespTesM == 1): #Caso Miller retorne 1, significa que o teste de miller deu composto.
            print ("O teste de Miller acusou composto para o: ",n)
            print ("_____________________________________________________________________________________")
            n = n+1 #Uma vez que o número é composto é somado uma unidade ao n.
        if(RespTesM == 0): #Caso o teste de miller retorne 0, significa que o teste deu inconclusivo.
            print ("O teste de Miller acusou inconclusivo para o: ",n)
            print ("_____________________________________________________________________________________")
            RespTesL = TesteLucas(n) #Uma vez que, o teste de Miller é inconclusivo é chamado o teste de Lucas. 
            if(RespTesL == 2): #Caso o teste de Lucas retorne 2, significa que não foi achado os fatores de n-1.
                print ("O teste de Lucas não pode ser concluido: ",n)
                print ("_____________________________________________________________________________________")
                n = n+1 #Logo, é somado novamente mais uma unidade ao n.
            if(RespTesL == 1): #Caso o teste de Lucas retorne 1, significa que o teste deu composto. 
                print ("O teste de Lucas acusou inconclusivo para o: ",n)
                print ("_____________________________________________________________________________________")
                n = n+1 #E novamente é somado uma unidade ao n.
            if(RespTesL == 0): #Caso o teste de Lucas retorne 0, significa que o teste de lucas confirmou que número é primo.
                print ("O teste de lucas confirmou que é primo o: ",n)
                print ("_____________________________________________________________________________________")
                parada = 1 #Uma vez que é achado um primo, a condição de parada recebe valor 1, para poder sair do while, e o algoritmo é encerrado.

#FIM DA FUNÇÃO PRINCIPAL,
