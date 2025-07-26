import unittest
from unittest.mock import patch, Mock
from country_picker.utils import get_countries_data




class TestGetListOfCountries(unittest.TestCase):

    @patch('requests.get') #anytime this is called, it gets mocked
    def test_countries_extraction(self, mock_get):
        """
        Test of JSON parsing logic to ensure the url is called
        correctly, and that we get the right response. 
        """

        #set up mock
        mock_response = Mock()
        mock_response.status_code = 200

        #set up the response of the mock object
        response_obj = [
            {
                "name": "Switzerland", 
                "population": 1000, 
                "gini": 47.8 
            },

            {
                "name": "United Kingdom",
                "population": 2000,
                "gini": 60
            },

            {
                "name": "United States",
                "population": 300,
                "gini": 80
            }

        ]

        mock_response.json.return_value = response_obj
        mock_get.return_value  = mock_response
        
        #run tests
        test_url = "https://test_api.com"
        countries_data = get_countries_data(test_url)

        #test the url is called correctly
        mock_get.assert_called_with("https://test_api.com")

        #test the output is as expected
        self.assertEqual(countries_data, response_obj)