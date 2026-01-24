from timeit import default_timer


def timer(func):
    def interna():
        start = default_timer()
        result = func()
        end = default_timer()
        print(end - start)
        return result

    return interna


def timer2(func):
    def interna(arr):
        start = default_timer()
        result = func(arr)
        end = default_timer()
        print(end - start)
        return result

    return interna


@timer
def selection_sort():
    """Selection sort written without searching the web"""
    lista = [64, 34, 25, 5, 22, 11, 90, 12]
    tamanho = len(lista)
    for i in range(tamanho):
        for j in range(tamanho):
            if i == j:
                continue
            elif lista[i] < lista[j]:
                temp = lista[i]
                lista[i] = lista[j]
                lista[j] = temp
    return lista


@timer
def selection_sort2():
    """Selection sort written based on the web"""
    mylist = [64, 34, 25, 5, 22, 11, 90, 12]
    n = len(mylist)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if mylist[j] < mylist[min_index]:
                min_index = j
        min_value = mylist.pop(min_index)
        mylist.insert(i, min_value)
    return mylist


# @timer2
def merge_sort(arr):
    """Merge sort written based on the web"""
    if len(arr) > 1:
        meio = len(arr) // 2

        esq = arr[:meio]
        dir = arr[meio:]

        merge_sort(esq)
        merge_sort(dir)

        i = j = k = 0
        while i < len(esq) and j < len(dir):
            if esq[i] < dir[j]:
                arr[k] = esq[i]
                i += 1
            else:
                arr[k] = dir[j]
                j += 1
            k += 1

        while i < len(esq):
            arr[k] = esq[i]
            i += 1
            k += 1

        while j < len(dir):
            arr[k] = dir[j]
            j += 1
            k += 1
    return arr


merge_list = [64, 34, 25, 5, 22, 11, 90, 12]

# start = default_timer()
# print("Selection sort 1", selection_sort())
# end = default_timer()
# print(end - start)

# start = default_timer()
# print("Selection sort 2", selection_sort2())
# end = default_timer()
# print(end - start)

# start = default_timer()
# print("Merge sort", merge_sort(arr=merge_list))
# end = default_timer()
# print(end - start)

merge_sort(merge_list)
