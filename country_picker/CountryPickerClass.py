import PyQt5.QtWidgets as qtw
import PyQt5.QtNetwork as qtn
from PyQt5.QtCore import QUrl
import json


def a():
    pass

class countryPickerWindow(qtw.QWidget):
    """
    A class containing the frontend and backend logic of the country selecting window. #

    ...

    Attributes
    ----------
    country_label: obj
        A widget object which is the text label
    country_combobox: obj
        A widget object which is the combobox in the window
    network_manager: obj
        A network object that handles requests to external apis. 

    Methods
    --------
    access_data()
        sends a network request for the JSON data from apicountries
    update_label(text)
        updates the label to read what has been selected in the combobox
    handle_response(reply)
        Processes and extracts the list of countries from the data 
        and adds it to the combobox.
    """

    def __init__(self):
        """
        Initialises the fronted layout and connections between user
        interactions with the GUI and the backend methods. 

        Parameters:
        -----------
        None
        """
        super().__init__()

        #set window size
        self.resize(400,200)

        #set layout
        self.setLayout(qtw.QVBoxLayout())
        self.setWindowTitle('Country Picker')

        #create widgets
        self.country_label = qtw.QLabel()
        self.country_combobox = qtw.QComboBox(self)

        #add widgets
        self.layout().addWidget(self.country_label)
        self.layout().addWidget(self.country_combobox)

        #initialise and connect network manager
        self.network_manager = qtn.QNetworkAccessManager()
        self.network_manager.finished.connect(self.handle_response)
    
        #show app
        self.show()

        #request from api
        self.access_data()

    def access_data(self):
        """
        sends a network request for the JSON data from apicountries

        Parameters:
        -----------
        None

        Returns:
        ---------
        None
        """

        url = QUrl("https://www.apicountries.com/countries")
        request = qtn.QNetworkRequest(url)
        self.network_manager.get(request)
        
    
    def update_label(self, text):
        """
        updates the label to read what has been selected in the combobox

        Parameters:
        ----------
        text: obj
            A pyqt object containing the current text in the combobox
        
        Returns:
        ---------
        None
        """
        
        self.country_label.setText(f'Selected: {text}')

    def handle_response(self, reply):
        """
        Processes and extracts the list of countries from the data 
        and adds it to the combobox.

        Parameters:
        ------------
        reply: obj
            pyqt object containing the data recieved from the api.

        Returns:
        --------
        None
        """
        
        #handle errors
        if reply.error():
            print("Failed to fetch data.")
            return

        data = reply.readAll().data()
        
        #extract json data
        try:
            json_data = json.loads(data)
        except Exception as e:
            print(f"Error parsing data: {e}")
        

        #get list of countries
        country_list = []

        for country_dict in json_data:
            country_list.append(country_dict["name"])
        
        #sort list:
        country_list.sort()

        #add countries, then connect combobox to label
        self.country_combobox.addItems(country_list)
        self.country_combobox.currentTextChanged.connect(self.update_label)