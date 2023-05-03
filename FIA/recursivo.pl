%Factorial
factorial(0,1).
factorial(N,F):-
    N>0,
    N1 is N-1,
    factorial(N1,F1),
    F is N*F1.

%factorial(3,X). -> factorial(numero, resultado).

%Sumatoria
sumatoria(0,0).
sumatoria(A,B):- 
    C is A-1, 
    sumatoria(C, D),
    B is (A+D).

%sumatoria(4,X). -> sumatoria(sumatoria hasta n, resultado).

%Fibonacci
fibonacci(0,0).
fibonacci(1,1).
fibonacci(N,X):-
    N > 1,
    N1 is N-1,
    fibonacci(N1,X1),
    N2 is N-2,
    fibonacci(N2,X2),
    X is X1+X2.

%fibonacci(6,X). -> fibonacci(No. de secuencia, Valor).


hanoi(0,_,_,_).

hanoi(N,Origen,Auxiliar,Destino):- N1 is N-1,
    hanoi(N1,Origen,Destino,Auxiliar),
    def_pasos(Origen,Destino),
    hanoi(N1,Auxiliar,Origen,Destino).

def_pasos(Origen,Destino):-
    write(' desde '),
    write(Origen),
    write(' hasta '),
    write(Destino),
    write('\n'). 

%hanoi(5,1,2,3). -> hanoi(No. de discos, torre inicio, torre pivote, torre final)