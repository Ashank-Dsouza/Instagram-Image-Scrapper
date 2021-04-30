import os


class UserNameClass:
    Usernames = list()

    def __init__(self):
        self.Usernames = self.filter( self.getUserNamesFromTxtFile() )

    def filter(self, Usernames):
        ValidUsername = list()
        for name in Usernames:
            if name and isinstance(name, str):
                CandidateName = name.strip()
                if CandidateName:
                    ValidUsername.append(CandidateName)

        final_set = set(ValidUsername)

        final_list = list(final_set)
        self.printList(final_list)
        return final_list

    def getUserNamesFromTxtFile(self):
        UserNames = list()
        if not os.path.exists("user_names.txt"):
            raise Exception("user_names.txt file does not exist in root folder!!")
        with open("user_names.txt", 'r') as file:
            name = file.readline()
            while name:
                UserNames.append(name)
                name = file.readline()

        return UserNames

    def printList(self, UserNames):
        for x in range(len(UserNames)):
            print(UserNames[x])