# changes import method so main can be ran inside and outside of country_picker
try:
    from .CountryPickerClass import countryPickerWindow
except ImportError:
    from CountryPickerClass import countryPickerWindow

import PyQt5.QtWidgets as qtw
import sys


def main():
    args = sys.argv
    app = qtw.QApplication([])

    if len(args) >= 2 and args[1] == '--select':
        selected_country = ' '.join(args[2:])
        mw = countryPickerWindow(selected_country='xxx')
    else:
        mw = countryPickerWindow()

    app.exec_()

#ensures this won't run if main is imported
if __name__ == '__main__':

    main()