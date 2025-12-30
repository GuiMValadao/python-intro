import asyncio


async def calcular_fatorial(x):
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
        await asyncio.sleep(0.1)
    return resultado


async def calculos(valores):
    for async_func in asyncio.as_completed(
        (calcular_fatorial(numero) for numero in valores)
    ):
        resultado = await async_func
        print("O fatorial calculado é:", resultado)


def main():
    print("Main - Starting")
    asyncio.run(calculos([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print("Main - Done")


if __name__ == "__main__":
    main()
