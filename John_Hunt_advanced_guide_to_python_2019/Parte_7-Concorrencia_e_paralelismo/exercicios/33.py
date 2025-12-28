from concurrent.futures import ThreadPoolExecutor
from time import sleep


def calcular_fatorial(x):
    resultado = 1
    print(f"Calculando o fatorial de {x}")
    if x < 0:
        return "Fatorial de números negativos não é definido"
    elif x == 0:
        return 1
    else:
        while x > 1:
            resultado = resultado * (x)
            x -= 1
        sleep(0.1)
    return resultado


def callback_fat(future):
    print(future.result())


print("Iniciando")
dados = [2, 3, 4, 5, 6, 7, 8]
pool = ThreadPoolExecutor(3)

for v in dados:
    future = pool.submit(calcular_fatorial, v)
    future.add_done_callback(callback_fat)

print("Terminado")
