README

    This is my solution for the CERN reqruitement exercise. The GUI framework used in this project is PyQt5. The code is organised in a package  and allows the user to select a country from a list of countries obtained from https://www.apicountries.com/countries. In addition, the user can preselect their country in the command line. 

How to use:

    To use this package, navigate to the directory containing the country_picker directory and input into the command line:

    python -m country_picker

    If you wish to preselect your country, the command line input changes to:

    python -m country_picker --select <Your Country>

    For example, if you wish to preselect switzerland, the input is:

    python -m country_picker --select Switzerland

Testing:

    The testing file contains a test case for the JSON parsing logic using unittest. 

    To be honest I am unsure about the purpose of this test? The parsing logic used is all contained in 1 line of code:

    countries_data = response.json() (line 23 in utils.py)

    Our test mocks the response, meaning we replace what this line in the function does with our own results. I am not sure if this is what is being asked of me. 
