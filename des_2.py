def fibonacci(n):
    sequencia = [0, 1]
    while sequencia[-1] < n:
        proximo = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo)
    return sequencia

def eFibonacci(num):
    sequencia = fibonacci(num)
    if num in sequencia:
        print(f"{num} faz parte da sequência de Fibonacci")
    else:
        print(f"{num} não faz parte da sequência de Fibonacci")

numConsulta = int(input("Qual número deseja consultar? digite: "))
eFibonacci(numConsulta)