from Namegen import *
from random import randint
from cat import Cat

class Clan():
    def __init__(self,name,warriors,worldCats):
        self.name = name
        self.allCats = []
        self.warriors =[]
        self.apprentices = []
        self.elders = []
        self.leadership = []
        
        self.CreateCat("Leader",worldCats)#create leader
        self.CreateCat("Deputy",worldCats)#create deputy
        self.CreateCat("Medicine Cat",worldCats)#create medicine cat
        I = 0
        while I < warriors:#create warriors
            self.CreateCat("Warrior",worldCats)
            I = I + 1
        I = 0
        
        while I < warriors * 0.15: #create apprentices
            self.CreateCat("Apprentice",worldCats)
            I = I + 1
        I = 0
        while I < warriors * 0.2: #create elders
            self.CreateCat("Elder",worldCats)
            I = I + 1
       
    def SayCats(self):
        print(self.name + "!")
        I = 0
        while I < len(self.allCats):
            print(self.allCats[I].SayRank() + ": " + self.allCats[I].SayName())
            I = I + 1
            
    def CreateCat(self,rank,worldcats):
        if rank == "Leader":
            tempname = (RandomName(True) + "star")
            if SearchName(tempname,worldcats) == True or AvoidName(tempname) == True:
                self.CreateCat("Leader",worldcats)#try again
            else: #create cat
                self.leader = Cat(randint(30,120),"Leader")#create leader
                self.leader.NPCSetup(tempname,self.name)
                self.allCats.append(self.leader)
                self.leadership.append(self.leader)
                worldcats.append(self.leader)
        elif rank == "Deputy":
            tempname = GenerateName()
            if SearchName(tempname,worldcats) == True or AvoidName(tempname) == True:
                self.CreateCat("Leader",worldcats)#try again
            else:
                self.deputy = Cat(randint(25,120),"Deputy")
                self.deputy.NPCSetup(tempname,self.name)
                self.allCats.append(self.deputy)
                self.leadership.append(self.deputy)
                worldcats.append(self.deputy)
        elif rank == "Medicine Cat":
            tempname = GenerateName()
            if SearchName(tempname,worldcats) == True or AvoidName(tempname) == True:
                self.CreateCat("Leader",worldcats)#try again
            else:
                self.medCat = Cat(randint(35,120),"Medicine Cat")
                self.medCat.NPCSetup(tempname,self.name)
                self.allCats.append(self.medCat)
                self.leadership.append(self.medCat)
                worldcats.append(self.medCat)
        elif rank == "Warrior":
            tempname = GenerateName()
            if SearchName(tempname,worldcats) == True or AvoidName(tempname) == True:
                self.CreateCat("Leader",worldcats)#try again
            else:
                self.newwarrior = Cat(randint(20,120),"Warrior")
                self.newwarrior.NPCSetup(tempname,self.name)
                self.allCats.append(self.newwarrior)
                self.warriors.append(self.newwarrior)
                worldcats.append(self.newwarrior)
        elif rank == "Apprentice":
            tempname = RandomName(True) + 'paw'
            if SearchName(tempname,worldcats) == True or AvoidName(tempname) == True:
                self.CreateCat("Leader",worldcats)#try again
            else:
                self.newbie = Cat(randint(6,22),"Apprentice")
                self.newbie.NPCSetup(tempname,self.name)
                self.allCats.append(self.newbie)
                self.apprentices.append(self.newbie)
                worldcats.append(self.newbie)
        elif rank == "Elder":
            tempname = GenerateName()
            if SearchName(tempname,worldcats) == True or AvoidName(tempname) == True:
                self.CreateCat("Leader",worldcats)#try again
            else:
                self.elder =Cat(randint(105,140),"Elder")
                self.elder.NPCSetup(tempname,self.name)
                self.allCats.append(self.elder)
                self.elders.append(self.elder)
                worldcats.append(self.elder)
        
    def AddCat(self,newcat,rank,worldcats):
        self.allCats.append(newcat)
        worldcats.append(newcat)
        if newcat.SayRank() == "Leader" or newcat.SayRank() == "Deputy" or newcat.SayRank() == "Medicine Cat":
            self.leadership.append(newcat)
        elif newcat.SayRank() == "Warrior":
            self.warriors.append(newcat)
        elif newcat.SayRank() == "Apprentice":
            self.apprentices.append(newcat)
        elif newcat.SayRank() == "Elder":
            self.elders.append(newcat)
    def ChooseMentor(self,apprentice):
        self.newmentor = (self.warriors[randint(0,len(self.warriors) - 1)])#not sure if I need the -1
        apprentice.MakeApprentice(self.newmentor)

