import math;
def factorial (n):
    if n==0:
        return 1;
    else:
        return n * factorial(n-1);  

#Definimos la funcion cos que recibira como parametros: num=el numero a evaluar, parada: que sera la tolerancia porcentual prefijada,y valor real

def cos(num,parada,valorReal):
     valoreRelativo = 1; #Tomando en cuenta que este es el primer valor inicial en la serie de taylor:
     errorAproximado =  abs(((valorReal-valoreRelativo)/valorReal) * 100); #Se calcula el primer error aproximado para poder entrar al while
     print("Primer valor aproximado:" + str(errorAproximado));     
     signo=0; #Utilizo el signo como si fuera la iteracion ej: i,j,k, lo nombro asi ya que sera el que determinara el signo de la operación.
     i=2; #Inicio i en 2 ya que se supone que ya se hizo la iteracion 0 que el valorRelativo es igual a 1, este sera el encargado de determinar el exponente y el factorial.

     while(errorAproximado>parada):
        signo = signo+1; #Aumento el signo de a 1 nada mas entrar al ciclo ya que signo=0 ya fue evaluado antes de entrar al while.
        print("Iteracion:" + str(signo))

        if(signo%2!=0): #Compruebo si el signo es par o impar, en caso de que sea par se sumara,sino se restara.
            valoreRelativo-= (num**i)/factorial(i); #valorRelativo+= es equivalente a tener valorRelativo = valorRelativo + ...
        else:
            valoreRelativo+=(num**i)/factorial(i);

        i = i+2; #Al finalizar las operacione se aumenta i en 2 ya que asi es como lo indica el patrón de la serie de taylor de cos;
        print("Valor relativo:"+str(valoreRelativo));
        errorAproximado =abs( ((valorReal-valoreRelativo)/valorReal) * 100); #Se calcula el error aproximado, se pone en valor absoluto ya que  la condicion a cumplir en el while es que el errorAproximado debe ser mayor al punto de parada, entonces ciertos valores haian que este errorAproximado fuera negativo y por ende se saliera del while;
        print("Error aproximado:")
        print(errorAproximado);

     print("numero iteraciones: "+ str(signo));

cos(math.pi,0.005,-1); #Se invoca la funcion dando los argumentos, pi, la parada 


#Definicion de cos sin tener un valor real:
def cosWhitoutRealValue(num,parada):
    valoresObtenidos = [1]; #Se inicializa el arreglo donde iran los valores que se obtendran en el ciclo, el 1 es el valor inical para poder operar.
    errorAproximado = 100; #Se inicializa el error en 100% para poder entrar al ciclo, no se hace mediante la formula ya que de momento solo tenemos un valor en el arreglo.
    valorRelativo=1;
    i=2
    signo=0

    while(errorAproximado>parada):
         signo = signo+1; #Aumento el signo de a 1 nada mas entrar al ciclo ya que signo=0 ya fue evaluado antes de entrar al while.
         print("Iteracion:" + str(signo))

         if(signo%2!=0): #Compruebo si el signo es par o impar, en caso de que sea par se sumara,sino se restara.
            valorRelativo-= (num**i)/factorial(i); #valorRelativo+= es equivalente a tener valorRelativo = valorRelativo + ...
         else:
            valorRelativo+=(num**i)/factorial(i);

         i = i+2; #Al finalizar las operacione se aumenta i en 2 ya que asi es como lo indica el patrón de la serie de taylor de cos;
         valoresObtenidos.append(valorRelativo);
         print("Valor actual: " + str(valoresObtenidos[signo]));
         errorAproximado = abs( ((valoresObtenidos[signo]-valoresObtenidos[signo-1])/valoresObtenidos[signo])*100); #Tomar signo-1 como la posicion anterior en el arreglo, y signo como la actual.

         print("Error aproximado:" + str(errorAproximado));
    print("TOTAL ITERACIONES:" + str(signo));    

cosWhitoutRealValue(math.pi,0.005) #Se invoca la funcion.