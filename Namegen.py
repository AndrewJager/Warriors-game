import random

FirstNames = ["Shade","Feather","Bramble","Fire","Red","Blue",
		"Silver","Dusk","Dust","Sand","Gray","Silver","Dark","Long","Bracken","Fern","Duck",
		"Cinder","Ash","Jay","Holly","Lion","Tiger","Squrrel","Night","Willow","Flame","Hawk"
		,"Raven","Black","Gorse","Torn","Thorn","Mouse","Spider","Sorrel","Cloud","White",
		"Shrew","Bright","Rain","Soot","Golden","Frost","Dapple","Speckle","Russet","Little",
		"Oak","Smoke","Tawny","Cedar","Rowan","Talon","Tall","Poppy","Running","Mud","Crow",
		"Bark","One","Web","Morning","Leopard","Misty","Moth","Heavy","Storm","Moss","Dawn",
		"Loud","Barley","Stumpy","Jagged","Rat","Fox","Deer","Bird","Berry","Sparrow","Cherry"
		,"Birch","Maple","Snow","Honey","Ice","Owl","Olive","Toad","Snake","Scorch","Water",
		"Breeze"]
LastNames = ["claw","pelt","fur","face","heart","stripe","foot",
	    "spirit","whisker","feather","tail","storm","leaf","blaze","pool","wing","sky",
	    "berry","nose","ear","eye","flight","flower","cloud","poppy","step","frost","belly",
	    "tooth","eyes","shade","fern","leg","scar","water"]

def RandomName(first):
    if first == True:
        index = random.randint(0,len(FirstNames)-1)
        return FirstNames[index]
    else:
        index = random.randint(0,len(LastNames)-1)
        return LastNames[index]

def GenerateName():
    return RandomName(True) + RandomName(False)

def SearchName(target,cats):
    I = 0
    while I < len(cats):
        if cats[I].SayName() == target: return True
        I = I + 1
    return False

def AvoidName(target):
    BadNames = ["Featherfeather","Berryberry","Shadeshade","Poppypoppy",
		"Fernfern","Cloudcloud","Waterwater"]
    I = 0
    while I < len(BadNames):
        if target == BadNames[I]: return True
        I = I + 1
    return False
