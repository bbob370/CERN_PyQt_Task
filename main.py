import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtNetwork as qtn
from PyQt5.QtCore import QUrl
import json


class countrySelectWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        #set window size
        self.resize(400,200)

        #set layout
        self.setLayout(qtw.QVBoxLayout())
        self.setWindowTitle('CERN PyQt5 Task')

        #create widgets
        self.country_label = qtw.QLabel('Hello World!')
        self.country_combobox = qtw.QComboBox(self)

        #add widgets
        self.layout().addWidget(self.country_label)
        self.layout().addWidget(self.country_combobox)

        self.network_manager = qtn.QNetworkAccessManager()
        #network stuff
        self.network_manager.finished.connect(self.handle_response)

        #set connections
        #self.country_combobox.currentTextChanged.connect(self.update_label)
    
        #show app
        self.show()

        self.access_data()

    def access_data(self):
        print('fetching data')
        url = QUrl("https://www.apicountries.com/countries")
        request = qtn.QNetworkRequest(url)
        self.network_manager.get(request)
        
        print('data obtained')
    
    def update_label(self, text):
        self.country_label.setText(f'Selected: {text}')

    def handle_response(self, reply):
        print('handling response')

        if reply.error():
            print("Failed to fetch data.")
            return

        data = reply.readAll().data()
        
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

        self.country_combobox.addItems(country_list)

        self.country_combobox.currentTextChanged.connect(self.update_label)


app = qtw.QApplication([])
mw = countrySelectWindow()

app.exec_()