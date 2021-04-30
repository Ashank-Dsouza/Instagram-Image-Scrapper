from Constants import Constants
from FolderManager import FolderManager
from instaloader import Instaloader, Profile
import datetime
import requests
from pathlib import Path
import uuid

class ImageDownloader:
    constants = Constants()

    def downloadForAllUser(self, UserNames, Loader):

        folderManager = FolderManager()
        folderManager.makeFolderIfNotExists(self.constants.IMAGE_FOLDER_NAME)

        for name in UserNames:
            folderPath = self.constants.IMAGE_FOLDER_NAME + '\\' + name
            print(folderPath)
            folderManager.makeFolderIfNotExists(folderPath, True)

            profile = Profile.from_username(Loader.context, name)

            postsList = list(profile.get_posts())

            postCount = len(postsList)
            maxPosts = self.constants.POST_LIMIT

            postCountToBeDownloaded = min(postCount, maxPosts)

            postsToBeDownloaded = postsList[:postCountToBeDownloaded]

            self.downloadImages(self, postsToBeDownloaded, folderPath, name)

    def isNewImagesAvailable(self, folderPath, Posts):

        if len(Posts) == 0:
            raise Exception("There are no posts available!")
        try:
            with open(folderPath + "\\" + self.constants.LATEST_POST_INFO_TXT, 'r') as file:
                date_time_str = file.read().replace('\n', '')

                if not date_time_str:
                    raise Exception("Could not find date of latest post")

                date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')

                if not date_time_obj:
                    raise Exception("Could not find date of latest post")

                latest_post = Posts[0]
                if date_time_obj < latest_post.date_utc:
                    return True
                else:
                    return False
        except OSError:
            raise Exception("Could not find txt file having latest post date")

    def downloadImages(self, Posts, folderPath, userName):

        if not self.isNewImagesAvailable(self, folderPath, Posts):
            print("download is not needed right now")
            return

        for post in Posts:
            print(post.caption)
            print(post.typename)
            print(post.url)
            if post.typename == "GraphImage":
                response = requests.get(post.url)

                date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M")
                date_string = date_string + userName
                data_folder = Path(folderPath)

                imageName = str(uuid.uuid4()) + ".png"

                print("the data this post was created is ")
                print(post.date_utc)

                file_to_open = data_folder / imageName

                file = open(file_to_open, "wb")

                file.write(response.content)
                file.close()

        self.updateLatestPostInfoTxt(self, folderPath, Posts)

    def updateLatestPostInfoTxt(self, folderPath, Posts):

        latest_post_date = Posts[0].date_utc
        time_str = latest_post_date.strftime("%Y-%m-%d %H:%M:%S.%f")
        with open(folderPath + "\\" + self.constants.LATEST_POST_INFO_TXT, "w") as file:
            file.write(time_str)


