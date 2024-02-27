# Stworzyć funkcję, która będzie sprawdzała czy przekazana liczba w
# parametrze jest parzysta i zwróci tą informację jako typ logiczny bool
# ( True / False ). Należy uruchomić funkcję, wynik wykonania zapisać do
# zmiennej, a następnie wykorzystując warunek logiczny wyświetlić prawidłowy
# tekst "Liczba parzysta" / "Liczba nieparzysta"

def sprawdz_czy_parzysta(liczba):
    return liczba % 2 == 0

liczba = 7
czy_parzysta = sprawdz_czy_parzysta(liczba)
if czy_parzysta:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")