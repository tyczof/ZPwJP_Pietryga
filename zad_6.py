def operacje_na_listach(lista1, lista2):
    polaczona_lista = list(set(lista1 + lista2))
    wynikowa_lista = [x ** 3 for x in polaczona_lista]
    return wynikowa_lista


# Przykład użycia
lista_a = [1, 2, 3]
lista_b = [3, 4, 5]

wynikowa_lista = operacje_na_listach(lista_a, lista_b)
print(wynikowa_lista)
