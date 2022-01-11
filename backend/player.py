import random
import requests

class Player:
    def __init__(self, pos, money, props):
        self.pos = pos
        self.money = money
        self.props = props


class property:
    def __init__(self,name, posx,posy, type, price, house_price, rent, houses, owner):
        self.name = name
        self.type = type
        self.price = price
        self.house_price = house_price
        self.rent = rent
        self.houses = houses
        self.owner = owner

properties = [
    property("GO", 650, 650, "GO", 0, 0,[],0,0),
    property("Mediteranean Avenue", 570, 650, "Reg", 60, 50,[2,10,30,90,160,250],0,0),
    property("CC1", 515, 650, "CC", 0, 0,[],0,0),
    property("Baltic Avenue", 460, 650, "Reg", 60, 50,[4,20,60,180,320,450],0,0),
    property("Income Tax", 405, 650, "Tax", 0, 0,[200],0,0),
    property("Reading Railroad", 350, 650, "Rail", 200, 0,[25,50,100,200],0,0),
    property("Oriental Avenue", 295, 650, "Reg", 100, 50,[6,30,90,270,400,550],0,0),
    property("CH1", 240, 650, "CH", 0, 0,[],0,0),
    property("Vermont Avenue", 185, 650, "Reg", 100, 50,[6,30,90,270,400,550],0,0),
    property("Connecticut Avenue", 130, 650, "Reg", 120, 50,[8,40,100,300,450,600],0,0),
    property("Jail", 50, 650, "Jail", 120, 50,[],0,0),
    property("St. Charles Place", 25, 550, "Reg", 140, 100,[10,50,150,450,625,750],0,0),
    property("Electric Company", 25, 495, "Util", 150, 35,[30],0,0),
    property("States Avenue", 25, 440, "Reg", 140, 100,[10,50,150,450,625,750],0,0),
    property("Virginia Avenue", 25, 385, "Reg", 160, 100,[12,60,180,500,700,900],0,0),
    property("Pennsylvania Railroad", 25, 330, "Rail", 200, 0,[25,50,100,200],0,0),
    property("St. James Place", 25, 275, "Reg", 180, 100,[14,70,200,550,750,950],0,0),
    property("CC2", 25, 220, "CC", 0, 0,[],0,0),
    property("Tennessee Avenue", 25, 165, "Reg", 180, 100,[14,70,200,550,750,950],0,0),
    property("New York Avenue", 25, 115, "Reg", 200, 100,[16,80,220,600,800,1000],0,0),
    property("Free Parking",50, 50, "Park", 0, 0,[],0,0),
    property("Kentucky Avenue", 130, 50, "Reg", 220, 150,[18,90,250,700,875,1050],0,0),
    property("CH2", 185, 50, "CH", 0, 0,[],0,0),
    property("Indiana Avenue", 240, 50, "Reg", 220, 150,[18,90,250,700,875,1050],0,0),
    property("Illinois Avenue", 295, 50, "Reg", 240, 150,[20,100,300,750,925,1100],0,0),
    property("B&O Railroad", 350, 50, "Rail", 200, 0,[25,50,100,200],0,0),
    property("Atlantic Avenue", 405, 50, "Reg", 260, 150,[22,110,330,800,975,1150],0,0),
    property("Ventnor Avenue", 460, 50, "Reg", 260, 150,[22,110,330,800,975,1150],0,0),
    property("Water Works", 515, 50, "Util", 150, 0,[30],0,0),
    property("Marvin Gardens", 570, 50, "Reg", 280, 150,[24,120,360,850,1025,1200],0,0),
    property("Go To Jail", 650, 50, "GoJail", 0, 0,[],0,0),
    property("Pacific Avenue", 650, 120, "Reg", 300, 200,[26,130,390,900,1100,1275],0,0),
    property("North Carolina Avenue", 650, 175, "Reg", 300, 200,[26,130,390,900,1100,1275],0,0),
    property("CC3", 650, 230, "CC", 0, 0,[],0,0),
    property("Pennsylvania Avenue", 650, 285, "Reg", 320, 200,[28,150,450,1000,1200,1400],0,0),
    property("Short Line", 650, 340, "Rail", 200, 0,[25,50,100,200],0,0),
    property("CH3", 650, 395, "CH", 0, 0,[],0,0),
    property("Park Place", 650, 450, "Reg", 350, 200,[35,175,500,1100,1300,1500],0,0),
    property("Luxury Tax", 650, 505, "Tax", 0, 0,[100],0,0),
    property("Boardwalk", 650, 560, "Reg", 400, 200,[50,200,600,1400,1700,2000],0,0)
]

playerOne = Player(0,1500,[]) #human player
playerTwo = Player(0,1500,[]) #AI player

def roll():
    return random.randint(1,12)

def buyProperty(pos):
    return True

def buyHouses():
    return [-1,0]

def play(oppPos,oppMoney,oppPropertyBought,oppPropertyExpanded,oppHousesBought):
    playerOne.pos = oppPos 
    playerOne.money = oppMoney
    if (oppPropertyBought!= -1): 
        playerOne.props.append(oppPropertyBought)
        properties[oppHousesBought].owner = 1
    if (oppPropertyExpanded!= -1):
        properties[oppPropertyExpanded].houses += oppHousesBought
        houses = properties[oppPropertyExpanded].houses
        properties[oppPropertyExpanded].rent[0] = properties[oppPropertyExpanded].rent[houses]

    playerTwo.pos = (playerTwo.pos + roll())%40
    newProp = -1
    if (buyProperty(playerTwo.pos) == True):
        newProp = playerTwo.pos
        playerTwo.money -= properties[playerTwo.pos].price
        properties[playerTwo.pos].owner = 2

    payload = {"pos":playerTwo.pos,"money":2000,"propertyBought":newProp,"propertyExpanded":-1,"housesBought":0}
    res = requests.put('http://127.0.0.1:8000/api/interactions/6/',data=payload)
    return



    


    