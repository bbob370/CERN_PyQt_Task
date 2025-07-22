import json
import requests

def get_countries_data(url):
    response = requests.get(url)

    if response.status_code == 200:
        countries_data = response.json()
        return countries_data
    else:
        print(f'Failed to retrieve data {response.status_code}')


def get_list_of_countries(countries_data):
    country_list = []

    for country_dict in countries_data:
        country_list.append(country_dict["name"])
        
    #sort list:
    country_list.sort()

    return country_list
