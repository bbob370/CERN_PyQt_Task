# changes import method so main can be ran inside and outside of country_picker
try:
    from .CountryPickerClass import countryPickerWindow
except ImportError:
    from CountryPickerClass import countryPickerWindow

import PyQt5.QtWidgets as qtw

#ensures this won't run if main is imported
if __name__ == '__main__':
    app = qtw.QApplication([])
    mw = countryPickerWindow()

    app.exec_()