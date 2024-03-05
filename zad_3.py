class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property: {self.address}\n" \
               f"Area: {self.area} sq. meters\n" \
               f"Number of rooms: {self.rooms}\n" \
               f"Price: ${self.price}"


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return super().__str__() + f"\nPlot size: {self.plot} sq. meters\n"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return super().__str__() + f"\nFloor: {self.floor}\n"


# Tworzenie instancji klasy House
house1 = House(area=150, rooms=4, price=300000, address="123 Main Street", plot=500)

# Tworzenie instancji klasy Flat
flat1 = Flat(area=80, rooms=2, price=150000, address="456 Side Street", floor=3)

# Wyświetlanie obiektów
print(house1)
print("\n-------------------------\n")
print(flat1)
