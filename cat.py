class Cat():

    def __init__(self,age,rank):
        self.age = age
        self.rank = rank
        self.name = None
        self.mentor = None
        self.apprentice = None
        self.clan = None
        self.firstname = None
    def Setup(self):
        self.firstname = input ("Enter your name: ")
        self.firstnaem = self.firstname.capitalize()
        self.name = self.firstname + "paw"
        self.rank = "Apprentice"
        print ("Welcome " + self.name + "!")
    def NPCSetup(self,name,clan):
        self.name = name
        self.clan = clan

    def SayName(self):
        return self.name
    def SayRank(self):
        return self.rank
    def MakeApprentice(self,mentor):
        self.mentor = mentor
        self.rank = "Apprentice"
        print  (self.name + ", your mentor is " + self.mentor.SayName() + "!")
    def MakeMentor(self,apprentice):
        self.apprentice = apprentice
    def MakeWarrior(self,newname):
        self.name = self.firstname + newname
        print ("welcome " + self.SayName())

