# zad 2A
def wyswietl_imiona(imiona):
    for imie in imiona:
            print(imie)


# zad 2Bi
def pomnoz_przez_dwa_for(lista_liczb):
    wynik = []
    for liczba in lista_liczb:
        wynik.append(liczba * 2)
    return wynik


# zad 2Bii
def pomnoz_przez_dwa_lista_skladana(lista_liczb):
    return [liczba * 2 for liczba in lista_liczb]


# zad 2C
def wyswietl_parzyste_elementy(lista_liczb):
    for liczba in lista_liczb:
        if liczba % 2 == 0:
            print(liczba)


# zad 2D
def wyswietl_co_drugi_element(lista_liczb):
    [print(lista_liczb[i]) for i in range(0, len(lista_liczb), 2)]





