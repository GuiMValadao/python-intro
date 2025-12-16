# Write a Python function to verify that a given string only contains letters (upper
# case or lower case) and numbers. Thus spaces and underbars (‘_’) are not allowed.
# An example of the use of this function might be:

# Write a function to verify a UK Postcode format (call it verify_postcode).
# The format of a Postcode is two letters followed by 1 or 2 numbers, followed by aThe format of a Postcode is two letters followed by 1 or 2 numbers, followed by a
# space, followed by one or two numbers and finally two letters. An Example of a
# postcode is SY23 4ZZ another postcode might be BB1 3PO and finally we might
# have AA1 56NN (note this is a simplification of the UK Postcode system but is
# suitable for our purposes).

# Write a function that will extract the value held between two strings or characters
# such as ‘<’ and ‘>’. The function should take three parameters, the start character,
# the end character and the string to process. For example, the following code snippet:
import re

PADRAO_NALFANUM = re.compile(r"_|\s|\W")


def verificador_alfanum(string: str) -> bool:
    """Verifica se a string fornecida possui caracteres que não são alfanuméricos
    e retorna True se não possuir ou False se possuir.
    """
    combinacao_false = PADRAO_NALFANUM.search(string)
    if not combinacao_false:
        return True
    else:
        return False


def verificador_postcodeENG(postcode: str) -> bool:
    """Verifica se o postcode fornecido é do tipo AA1(1) 1(1)AA"""
    padrao_postcode = re.compile(r"[A-Z]{2}[0-9]{1,2}?\s[0-9]{1,2}?[A-Z]{2}")
    combinacao_formato = padrao_postcode.search(postcode)

    if combinacao_formato:
        return True
    else:
        return False


def extrator_valores(inicio: str, fim: str, string: str) -> str:
    """Extrai todos os caracteres encontrados entre o caractere fornecido de
    inicio e fim todas as vezes que ocorrem na string fornecida."""

    #    valor = rf"{inicio}(\w+\s\w+|\w+){fim}"
    valor = rf"{inicio}.*?{fim}"  # .: Qualquer caractere exceto de nova linha; * Zero ou mais ocorrências do padrão precedente(nesse caso todos/.); ?Zero ou 1 ocorrência do padrão precedente('inicio .*')
    filtro = re.compile(valor, flags=re.VERBOSE)
    procurar = filtro.findall(string)
    resultado = []
    for palavra in procurar:
        resultado.append(palavra)
    return resultado


print(verificador_alfanum("John"))  # True
print(verificador_alfanum("John_Hunt"))  # False
print(verificador_alfanum("42"))  # True
print(verificador_alfanum("John42"))  # True
print(verificador_alfanum("John 42"))  # False
print(verificador_alfanum("abcdefghijklmnopqrstuvwxyz0123456789"))


# True
print("verificador_postcodeENG('SY23 3AA'):", verificador_postcodeENG("SY23 33AA"))
# True
print("verificador_postcodeENG('SY23 4ZZ'):", verificador_postcodeENG("SY23 4ZZ"))
# True
print("verificador_postcodeENG('BB1 3PO'):", verificador_postcodeENG("BB1 3PO"))
# False
print("verificador_postcodeENG('AA111 NN56'):", verificador_postcodeENG("AA111 NN56"))
# True
print("verificador_postcodeENG('AA1 56NN'):", verificador_postcodeENG("AA1 56NN"))
# False
print("verificador_postcodeENG('AA156NN'):", verificador_postcodeENG("AA156NN"))
# False
print("verificador_postcodeENG('AA NN'):", verificador_postcodeENG("AA NN"))

print(extrator_valores("<", ">", "<John><Wgar><asdf asdf><asd "))
print(extrator_valores("<", ">", "<42>"))
print(extrator_valores("<", ">", "<John 42>"))
print(extrator_valores("<", ">", "The <town> was <in> the <valley>"))
