import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

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
        
        #add items to combobox
        country_list = ['China', 'France', 'Switzerland', 'US', 'UK']
        self.country_combobox.addItems(country_list)

        #add widgets
        self.layout().addWidget(self.country_label)
        self.layout().addWidget(self.country_combobox)

        #set connections
        self.country_combobox.currentTextChanged.connect(self.update_label)
    
        #show app
        self.show()

        #network stuff


    def update_label(self, text):
        self.country_label.setText(f'Selected: {text}')



app = qtw.QApplication([])
mw = countrySelectWindow()

app.exec_()