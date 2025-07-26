import PyQt5.QtWidgets as qtw

#changes import method so main can be ran inside and outside of country_picker
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

    Methods
    --------
    update_label(text)
        updates the label to read what has been selected in the combobox
    fill_out_combobox(url)
        requests the list of countries from countries.api, and collects the
        names of all the countries. This list is sorted then added to the
        combobox. 
    set_selected_country(selected_country)
        Sets the selected country of the combobox to the one
        specified by the user in the command line if there is one.
    """

    def __init__(self, selected_country=None):
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

        #add initial value for combobox
        self.country_combobox.addItem('None Selected')

        #connect combobox to label
        self.country_combobox.currentTextChanged.connect(self.update_label)
    
        #show app
        self.show()

        #request countries data from api
        url = "https://www.apicountries.com/countries"
        self.fill_out_combobox(url)

        #set combobox to preselected country if there is one
        if selected_country != None:
            self.set_selected_country(selected_country)


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
        """
        requests the list of countries from countries.api, and collects the
        names of all the countries. This list is sorted then added to the
        combobox. 

        Parameters:
        ------------
        url: str
            the String format of the url for the api used for the countries data
        
        Returns:
        ---------
        None
        """
        
        countries_data = get_countries_data(url)
        country_list = get_list_of_countries(countries_data)
        self.country_combobox.addItems(country_list)
    
    def set_selected_country(self, selected_country):
        """
        Sets the selected country of the combobox to the one
        specified by the user in the command line if there is one.

        Parameters:
        ------------
        selected_country: str
            Country selected by the user if any

        Returns:
            None
        """

        self.country_combobox.setCurrentText(selected_country)