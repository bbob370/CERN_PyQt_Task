import requests

def get_countries_data(url):
    """
    Requests countries data from the specified url, and 
    returns it as a python object

    Parameters:
    -----------
    url: str
        the url of the api used for the countries data
    
    Returns:
    --------
    countries_data: obj
        An object which is a list of dictionaries taken from
        the json data from the api. 
    """

    response = requests.get(url)

    if response.status_code == 200: #No issues accessing api
        countries_data = response.json()
        return countries_data
    else:
        print(f'Failed to retrieve data {response.status_code}')


def get_list_of_countries(countries_data):
    """
    Extracts the list of country names and sorts it 
    alphabetically. 

    Parameters:
    -----------
    countries_data: obj
        An object containing information on all countries.
    
    Returns:
    ---------
    country_list: list
        An alphabetically sorted list of the names of all the 
        countries in the world. 
    """

    country_list = []

    for country_dict in countries_data:
        country_list.append(country_dict["name"])
        
    #sort list:
    country_list.sort()

    return country_list
