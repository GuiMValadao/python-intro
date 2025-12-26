from multiprocessing import Pool
import time


def fatorial(x):
    resultado = 1
    if x < 0:
        return "Fatorial de números negativos não é definido"
    elif x == 0:
        return 1
    else:
        while x > 0:
            resultado = resultado * (x)
            x -= 1
    return resultado


def main():
    dados = (5, 8, 10, 15, 3, 6, 4)
    inicio = time.perf_counter()
    with Pool(processes=4) as pool:
        print(pool.map(fatorial, (5, 8, 10, 15, 3, 6, 4)))
    final = time.perf_counter()
    print(f"Tempo de execução foi de:{final-inicio} segundos")


if __name__ == "__main__":
    main()
    # inicio = time.perf_counter()
    # valores = [5, 8, 10, 15, 3, 6, 4]
    # resultado = []
    # for item in valores:
    #     resultado.append(fatorial(item))
    # print(resultado)
    # final = time.perf_counter()
    # print(f"Tempo de execução foi de:{final-inicio} segundos")
