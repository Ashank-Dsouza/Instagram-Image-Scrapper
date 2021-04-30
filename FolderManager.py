import datetime
import os

from Constants import Constants


class FolderManager:
    constants = Constants()

    def makeFolderIfNotExists(self, folderPath, CreateLatestImageInfoTxt=False):
        if not os.path.exists(folderPath):
            os.makedirs(folderPath)
            if CreateLatestImageInfoTxt:
                date_three_years_ago = datetime.datetime.now() - datetime.timedelta(days=3 * 365)
                time_str = date_three_years_ago.strftime("%Y-%m-%d %H:%M:%S.%f")
                with open(folderPath + "\\" + self.constants.LATEST_POST_INFO_TXT, "w") as file:
                    file.write(time_str)
