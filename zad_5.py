def sprawdz_czy_wartosc_w_liscie(lista, szukana_wartosc):
    return szukana_wartosc in lista

# Przykład użycia
moja_lista = [1, 3, 7, 9]
szukana_wartosc = 5

czy_wartosc_w_liscie = sprawdz_czy_wartosc_w_liscie(moja_lista, szukana_wartosc)

print(czy_wartosc_w_liscie)
