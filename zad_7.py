import requests


class Brewery:
    def __init__(self, brewery_data):
        self.name = brewery_data.get('name', 'N/A')
        self.type = brewery_data.get('brewery_type', 'N/A')
        self.city = brewery_data.get('city', 'N/A')
        self.state = brewery_data.get('state', 'N/A')

    def __str__(self):
        return f"Name: {self.name}\nType: {self.type}\nCity: {self.city}\nState: {self.state}\n"


def main():
    api_url = "https://api.openbrewerydb.org/breweries"

    response = requests.get(api_url)

    if response.status_code == 200:
        breweries_data = response.json()
        breweries_list = [Brewery(data) for data in breweries_data[:20]]

        for brewery in breweries_list:
            print(brewery)
    else:
        print(f"Failed to fetch data. Status Code: {response.status_code}")


if __name__ == "__main__":
    main()
