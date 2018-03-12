
# coding: utf-8

# # Turbopalindromos

# In[268]:

from time import time #modulos para 


# In[167]:

def int_to_list(x): #funcion para descomponer un numero en sus digitos y convertirlos a listas
    y=str(x) #Convierte el numero a cadena
    
    arreglo=[] #arreglo vacio
    
    for i in y: #selecciona los elementos de de la cadena
        num=int(i) #vuelve a convertir la cadena a entero
        arreglo.append(num) #introduce los numeros a la lista
    #print(arreglo)
    return(arreglo)


# In[168]:

def rot(x,α):
    tam=len(x)
    rotar=[] #arreglo vacio para introducir la nueva rotacion de numeros
    for j in range(0,tam):
        rotar.append(0) #agrega ceros a nuestra lista vacia de tal modo que contengan el mismo numero de elementos que el original
        #print(rotar)
    for i in range(0,tam): #algoritmo para rotar
        final=tam-(i+1)
        modulo=α%tam
        if modulo <= final:
            rotar[i+modulo]=x[i]
        else:
            rotar[modulo-final-1]=x[i]
           
    #print(rotar)
    return(rotar)
   


# In[219]:

def list_to_int(lista):#convierte las listas en enteros
    cadena=""
    for i in lista:
        cadena=cadena+str(i)
        
    numero=int(cadena)
    
    return (numero)
    


# In[251]:

def numero_r(x): #calcula el numero r
    lista=int_to_list(x)
    digitos=len(lista)
    suma=0
    for i in range(0,(digitos)):
        lista_rotacion=rot(lista,lista[i])
        #print(lista_rotacion)
        numero_rotacion=list_to_int(lista_rotacion)
        suma=numero_rotacion*(-1)**(i)+suma
        #print(numero_rotacion)
    r=x+suma
    #print(r)
    return(r)
    #print(suma)
    
    


# In[247]:

def palindromo(number): #funcion que verifica si un numero es palindromo o no
    lista_number=int_to_list(number)
    tamaño=len(lista_number)
    mitad_tamaño=tamaño/2
    leg=0
    if tamaño%2==0:
        for i in range(0,int(mitad_tamaño)):
            if lista_number[i]!= lista_number[tamaño-1-i]:
                leg=leg+1
        if leg>0:
            #print("no es palindromo")
            return(0)
        else:
            #print("es palindromo")
            return(1)
    if tamaño%2==1:
        for i in range(0,int((tamaño-1)/2)):
            if lista_number[i]!= lista_number[tamaño-1-i]:
                leg=leg+1
        if leg>0:
            #print("no es palindromo")
            return(0)
        else:
            #print("es palindromo")
            return(1)
    
        
            


# In[278]:

def turbopalindromo(inicio,final):
    tiempo_inicial=time()
    ntp=0 #numero de turbopalindromos
    print("tp","pal")
    for i in range(inicio,final):
        prueba=abs(numero_r(i))
        k=palindromo(prueba)
        if k==1:
            print(i,numero_r(i))
            ntp=ntp+1 #contador
    print("el numero de turbopalindromos entre ",inicio," y ",final," : ",ntp)
    tiempo_final=time()
    tiempo_ejec=tiempo_final-tiempo_inicial
    print("el tiempo de ejecucion fue de: ",tiempo_ejec," segundos")
        


# In[279]:

turbopalindromo(1,2000)


# In[ ]:



