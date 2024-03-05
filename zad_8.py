import requests
import argparse


class Brewery:
    def __init__(self, brewery_data):
        self.id = brewery_data.get('id', 'N/A')
        self.name = brewery_data.get('name', 'N/A')
        self.brewery_type = brewery_data.get('brewery_type', 'N/A')
        self.address_1 = brewery_data.get('address_1', 'N/A')
        self.address_2 = brewery_data.get('address_2', 'N/A')
        self.address_3 = brewery_data.get('address_3', 'N/A')
        self.city = brewery_data.get('city', 'N/A')
        self.state_province = brewery_data.get('state_province', 'N/A')
        self.postal_code = brewery_data.get('postal_code', 'N/A')
        self.country = brewery_data.get('country', 'N/A')
        self.longitude = brewery_data.get('longitude', 'N/A')
        self.latitude = brewery_data.get('latitude', 'N/A')
        self.phone = brewery_data.get('phone', 'N/A')
        self.website_url = brewery_data.get('website_url', 'N/A')
        self.state = brewery_data.get('state', 'N/A')
        self.street = brewery_data.get('street', 'N/A')

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Brewery Type: {self.brewery_type}\n"
            f"Address 1: {self.address_1}\n"
            f"Address 2: {self.address_2}\n"
            f"Address 3: {self.address_3}\n"
            f"City: {self.city}\n"
            f"State/Province: {self.state_province}\n"
            f"Postal Code: {self.postal_code}\n"
            f"Country: {self.country}\n"
            f"Longitude: {self.longitude}\n"
            f"Latitude: {self.latitude}\n"
            f"Phone: {self.phone}\n"
            f"Website URL: {self.website_url}\n"
            f"State: {self.state}\n"
            f"Street: {self.street}\n"
        )


def get_breweries(api_url, city=None):
    params = {"per_page": 20, "by_city": city} if city else {"per_page": 20}
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        breweries_data = response.json()
        return [Brewery(data) for data in breweries_data]
    else:
        print(f"Failed to fetch data. Status Code: {response.status_code}")
        return []


def main():
    parser = argparse.ArgumentParser(description="Fetch and display brewery information.")
    parser.add_argument("--city", help="Filter breweries by city", default=None)
    args = parser.parse_args()

    api_url = "https://api.openbrewerydb.org/breweries"
    breweries_list = get_breweries(api_url, city=args.city)

    # Display each brewery object separately
    for brewery in breweries_list:
        print(brewery)


if __name__ == "__main__":
    main()
