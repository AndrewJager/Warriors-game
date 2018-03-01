from Namegen import *
from random import randint
from cat import Cat
from gameentity import GameEntity

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
                self.leader = GameEntity(randint(30,120),"Leader",RandomFur())#create leader
                self.leader.NPCSetup(tempname,self.name)
                self.leader.CreateSprite()
                self.allCats.append(self.leader)
                self.leadership.append(self.leader)
                worldcats.append(self.leader)
        elif rank == "Deputy":
            tempname = GenerateName()
            if SearchName(tempname,worldcats) == True or AvoidName(tempname) == True:
                self.CreateCat("Leader",worldcats)#try again
            else:
                self.deputy = GameEntity(randint(25,120),"Deputy",RandomFur())
                self.deputy.NPCSetup(tempname,self.name)
                self.deputy.CreateSprite()
                self.allCats.append(self.deputy)
                self.leadership.append(self.deputy)
                worldcats.append(self.deputy)
        elif rank == "Medicine Cat":
            tempname = GenerateName()
            if SearchName(tempname,worldcats) == True or AvoidName(tempname) == True:
                self.CreateCat("Leader",worldcats)#try again
            else:
                self.medCat = GameEntity(randint(35,120),"Medicine Cat",RandomFur())
                self.medCat.NPCSetup(tempname,self.name)
                self.medCat.CreateSprite()
                self.allCats.append(self.medCat)
                self.leadership.append(self.medCat)
                worldcats.append(self.medCat)
        elif rank == "Warrior":
            tempname = GenerateName()
            if SearchName(tempname,worldcats) == True or AvoidName(tempname) == True:
                self.CreateCat("Leader",worldcats)#try again
            else:
                self.newwarrior = GameEntity(randint(20,120),"Warrior",RandomFur())
                self.newwarrior.NPCSetup(tempname,self.name)
                self.newwarrior.CreateSprite()
                self.allCats.append(self.newwarrior)
                self.warriors.append(self.newwarrior)
                worldcats.append(self.newwarrior)
        elif rank == "Apprentice":
            tempname = RandomName(True) + 'paw'
            if SearchName(tempname,worldcats) == True or AvoidName(tempname) == True:
                self.CreateCat("Leader",worldcats)#try again
            else:
                self.newbie = GameEntity(randint(6,22),"Apprentice",RandomFur())
                self.newbie.NPCSetup(tempname,self.name)
                self.newbie.CreateSprite()
                self.allCats.append(self.newbie)
                self.apprentices.append(self.newbie)
                worldcats.append(self.newbie)
        elif rank == "Elder":
            tempname = GenerateName()
            if SearchName(tempname,worldcats) == True or AvoidName(tempname) == True:
                self.CreateCat("Leader",worldcats)#try again
            else:
                self.elder = GameEntity(randint(105,140),"Elder",RandomFur())
                self.elder.NPCSetup(tempname,self.name)
                self.elder.CreateSprite()
                self.allCats.append(self.elder)
                self.elders.append(self.elder)
                worldcats.append(self.elder)
        
    def AddCat(self,newcat,rank,worldcats):#adds an existing cat to the clan
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
        self.newmentor = (self.warriors[randint(0,len(self.warriors) - 1)])
        apprentice.MakeApprentice(self.newmentor)
        self.newmentor.MakeMentor(apprentice)
    def SayLeader(self):
        return self.leader

