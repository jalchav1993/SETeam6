class User:
    def __init__(self,configurations):
        print("Admin Created")
        self.__fn = configurations['firstname']
        self.__ln = configurations['lastname']
        self.__org = configurations['organization']
        self.__email = configurations['email']
        self.__password = configurations['password']
        self.__sklLevel = configurations['skillLevel']
        self.__wsHistory = configurations['wsHistory']
        
    def __eq__(self,other):
        return self.__email == other.getEmail()
    
    def __hash__(self):
        return hash(self.__email)
    
    def getFN(self):
        return self.__fn
    
    def getLN(self):
        return self.__ln
    
    def getOrg(self):
        return self.__org
    
    def getEmail(self):
        return self.__email
    
    def getPassword(self):
        return self.__password
    
    def getSkillLevel(self):
        return self.__sklLevel
    
    def getwshistory(self):
        return self.__wsHistory
