import PyQt5.QtWidgets as qtw
import PyQt5.QtNetwork as qtn

try:
    from .utils import get_countries_data, get_list_of_countries
except ImportError:
    from utils import get_countries_data, get_list_of_countries


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
        self.country_combobox.addItem('None Selected')

        #add widgets
        self.layout().addWidget(self.country_label)
        self.layout().addWidget(self.country_combobox)

        self.country_combobox.currentTextChanged.connect(self.update_label)
    
        #show app
        self.show()

        url = "https://www.apicountries.com/countries"
        self.fill_out_combobox(url)


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


    def fill_out_combobox(self, url):
        
        countries_data = get_countries_data(url)
        country_list = get_list_of_countries(countries_data)
        self.country_combobox.addItems(country_list)