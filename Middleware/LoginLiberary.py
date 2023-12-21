class LoginLibs:
    def __init__(self, id=0, userName=None, password=None):
        self.id=id
        self.userName=userName
        self.password=password


    #Getter
    def getId(self):
        return self.id

    def getUserName(self):
        return self.userName

    def getPassword(self):
        return self.password

    #Setter
    def setId(self, id):
        self.id=id

    def setUserName(self, userName):
        self.userName=userName

    def setPassword(self, password):
        self.password=password

    def __str__(self):
        return (
            "{},{},{}".format(self.id, self.userName, self.password))



