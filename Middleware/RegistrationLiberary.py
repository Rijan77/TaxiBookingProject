class CustomerLibs:
    def __init__(self, id=0, fullName=None, email=None, contactNumber=None, gender=None, country=None,
                 paymentMethod=None, userType=None, userName=None, password=None):
        self.id = id
        self.fullName = fullName
        self.email = email
        self.contactNumber = contactNumber
        self.gender = gender
        self.country = country
        self.paymentMethod = paymentMethod
        self.userType = userType
        self.userName = userName
        self.password = password

        # Getter

    def getId(self):
        return self.id

    def getFullName(self):
        return self.fullName

    def getEmail(self):
        return self.email

    def getContactNumber(self):
        return self.contactNumber

    def getGender(self):
        return self.gender

    def getCountry(self):
        return self.country

    def getPaymentMethod(self):
        return self.paymentMethod

    def getUserType(self):
        return self.userType

    def getUserName(self):
        return self.userName

    def getUserPassword(self):
        return self.password

    # Setter

    def setID(self, id):
        self.id = id

    def setFullName(self, fullName):
        self.fullName = fullName

    def setEmail(self, email):
        self.email = email

    def setContactNumber(self, contactNumber):
        self.contactNumber = contactNumber

    def setGender(self, gender):
        self.gender = gender

    def setCountry(self, country):
        self.country = country

    def setPaymentMethod(self, paymentMethod):
        self.paymentMethod = paymentMethod

    def setUserType(self, userType):
        self.userType = userType

    def setUserName(self, userName):
        self.userName = userName

    def setPassword(self, password):
        self.password = password

    def __str__(self):
        return ("{},{},{},{},{},{},{},{},{},{}".format(self.id, self.fullName, self.email, self.contactNumber, self.gender,
                                                 self.country, self.paymentMethod, self.userType, self.userName, self.password))
