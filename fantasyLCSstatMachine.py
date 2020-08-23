week1 = r"C:\Users\hbker123\Desktop\FantasyLCSPlayerPoints Spring 2020 - Week1 Stats (1).csv"
week2 = r"C:\Users\hbker123\Desktop\FantasyLCSPlayerPoints Spring 2020 - Week2.csv"
userInput = input("Enter TOP JG MID BOT ADC or ALL: ")
class Player:
    name = ""
    totalScore = 0
    role = ""

    def __init__(self, var1, var2, var3):
        self.name = var1
        self.totalScore = var2
        self.role = var3

f = open(week1,"r", encoding='unicode_escape')
next(f)
f1 = f.readlines()
players = []
for x in f1:
    line = x.split(",")
    players.append(Player(line[0].lower(), float(line[3]), line[2]))
    #print(line[0],line[3], line[2])

otherFile = open(week2, "r", encoding = 'unicode_escape')
f2 = otherFile.readlines()
for x in f2:
    line = x.split(",")
    for player in players:
        if player.name == line[0].lower():
            player.totalScore += float(line[1])
            
if userInput == "TOP":
    returnList = []
    for player in players:
        if player.role =="Top":
            returnList.append(player)
    returnList.sort(key=lambda x: x.totalScore, reverse = True)   
    for i in returnList:
        print(i.name, i.totalScore, i.role) 

if userInput == "ADC":
    returnList = []
    for player in players:
        if player.role =="ADC":
            returnList.append(player)
    returnList.sort(key=lambda x: x.totalScore, reverse = True)   
    for i in returnList:
        print(i.name, i.totalScore, i.role) 

if userInput == "JG":
    returnList = []
    for player in players:
        if player.role =="Jungle":
            returnList.append(player)
    returnList.sort(key=lambda x: x.totalScore, reverse = True)   
    for i in returnList:
        print(i.name, i.totalScore, i.role) 

if userInput == "MID":
    returnList = []
    for player in players:
        if player.role =="Mid":
            returnList.append(player)
    returnList.sort(key=lambda x: x.totalScore, reverse = True)   
    for i in returnList:
        print(i.name, i.totalScore, i.role) 

if userInput == "SUPP":
    returnList = []
    for player in players:
        if player.role =="Support":
            returnList.append(player)
    returnList.sort(key=lambda x: x.totalScore, reverse = True)   
    for i in returnList:
        print(i.name, i.totalScore, i.role) 

if userInput == "ALL":
    players.sort(key=lambda x: x.totalScore, reverse = True)
    for i in players:
        print(i.name, i.totalScore, i.role)