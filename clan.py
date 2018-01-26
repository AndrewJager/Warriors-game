from Namegen import *
from random import randint
from cat import Cat

class Clan():
    def __init__(self,name,warriors):
        self.name = name
        self.allCats = []

        self.leader = Cat(randint(30,120),"Leader")#create leader
        self.leader.NPCSetup(RandomName(True) + "star")
        self.allCats.append(self.leader)

        self.deputy = Cat(randint(25,120),"Deputy")#create deputy
        self.deputy.NPCSetup(GenerateName())
        self.allCats.append(self.deputy)                  

        I = 0
        while I < warriors:#create warriors
            self.tempname = GenerateName()
            if SearchName(self.tempname,self.allCats) == True or AvoidName(self.tempname) == True:
                I = I - 1 #skip this iteneration
                print ("caught bad name " + self.tempname)
            self.warrior = Cat(randint(25,120),"Warrior")
            self.warrior.NPCSetup(self.tempname)
            self.allCats.append(self.warrior)
            I = I + 1
        I = 0
        
        while I < warriors * 0.15: #create apprentices
            self.tempname = RandomName(True) + "paw"
            if SearchName(self.tempname,self.allCats) == True or AvoidName(self.tempname) == True:
                I = I - 1 #skip this iteneration
                print ("caught bad name " + self.tempname)
            self.apprentice = Cat(randint(6,25),"Apprentice")
            self.apprentice.NPCSetup(self.tempname)
            self.allCats.append(self.apprentice)
            I = I + 1
        I = 0
        while I < warriors * 0.2: #create elders
            self.tempname = GenerateName()
            if SearchName(self.tempname,self.allCats) == True or AvoidName(self.tempname) == True:
                I = I - 1 #skip this iteneration
                print ("caught bad name " + self.tempname)
            self.elder = Cat(randint(120,150),"Elder")
            self.elder.NPCSetup(self.tempname)
            self.allCats.append(self.elder)
            I = I + 1
       
    def SayCats(self):
        print(self.name + "!")
        I = 0
        while I < len(self.allCats):
            print(self.allCats[I].SayRank() + ": " + self.allCats[I].SayName())
            I = I + 1
    def AddCat(self,newcat):
        self.allCats.append(newcat)
