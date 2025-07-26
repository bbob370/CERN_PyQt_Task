# changes import method so main can be ran inside and outside of country_picker
try:
    from .CountryPickerClass import countryPickerWindow
except ImportError:
    from CountryPickerClass import countryPickerWindow

import PyQt5.QtWidgets as qtw
import sys


def main():
    """
    Executes the GUI. Inputs a country if the user has specified
    a country to be selected on startup

    Parameters:
    -----------
    None

    Returns:
    ---------
    None
    """
    args = sys.argv
    app = qtw.QApplication([])

    #check if the user has selected a country beforehand
    if len(args) >= 2 and args[1] == '--select':

        selected_country = ' '.join(args[2:])
        mw = countryPickerWindow(selected_country=selected_country)

    else:

        mw = countryPickerWindow()

    app.exec_()

#ensures this won't run if main is imported
if __name__ == '__main__':

    main()