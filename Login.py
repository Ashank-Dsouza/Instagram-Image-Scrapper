import instaloader

from Constants import Constants

class LoginInstagram:
    def __init__(self):
        pass

    def Login():

        constants = Constants

        L = instaloader.Instaloader()

        L.login(constants.USER, constants.PASSWORD)

        return L