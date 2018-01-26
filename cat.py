class Cat():

    def __init__(self,age,rank):
        self.age = age
        self.rank = rank
        self.name = None
    def Setup(self):
        inputname = raw_input ("Enter your name: ")
        self.name = inputname + "paw"
        self.rank = "Apprentice"
        print ("Welcome " + self.name + "!")
    def NPCSetup(self,name):
        self.name = name

    def SayName(self):
        return self.name
    def SayRank(self):
        return self.rank
    def Ceramony(self,newrank):
        self.rank = newrank
        print (self.SayName() + " is now a/an " + self.SayRank() + "!")


