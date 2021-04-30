# This is a sample Python script.
import instaloader
import requests
from instaloader import Instaloader, Profile
from Constants import Constants
import os
import datetime
from pathlib import Path
import uuid

from ImageDownloader import ImageDownloader
from Login import LoginInstagram
from UserNameHandling import UserNameClass

def main_function(name):
    UserNames = UserNameClass()

    Loader = LoginInstagram.Login()

    Downloader = ImageDownloader

    Downloader.downloadForAllUser(Downloader, UserNames.Usernames, Loader)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_function('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
