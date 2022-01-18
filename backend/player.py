import random
import requests
import sys

class Player:
    def __init__(self, name,id, pos, money, props):
        self.name = name
        self.id = id
        self.pos = pos
        self.money = money
        self.props = props
        self.jail = False


class property:
    def __init__(self,name, posx,posy, type, price, house_price, rent, houses, owner):
        self.name = name
        self.type = type
        self.price = price
        self.house_price = house_price
        self.rent = rent
        self.houses = houses
        self.owner = owner
    
    def __str__(self):
        return "Name: "+self.name+", Owner: "+str(self.owner)+", Rent: "+str(self.rent) 



properties= []
playerOne = Player("Human",1,0,1500,[]) #human player
playerTwo = Player("Markov AI",2,0,1500,[]) #AI player
landing_probs = [0.022,0.023,0.023,0.023,0.023,0.022,0.022,
0.022,0.022,0.023,0.073,0.023,0.023,0.024,0.025,0.025,0.026,
0.027,0.027,0.027,0.026,0.026,0.026,0.026,0.026,0.026,0.026,
0.026,0.026,0.026,0,0.026,0.025,0.025,0.024,0.023,0.022,0.021,0.022,0.022]

def roll():
    return random.randint(1,6)+random.randint(1,6)

def reset():
    global playerOne
    global playerTwo
    global properties
    playerOne = Player("Human",1,0,1500,[]) 
    playerTwo = Player("Markov AI",2,0,1500,[])
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
    property("Boardwalk", 650, 560, "Reg", 400, 200,[50,200,600,1400,1700,2000],0,0)]

    

def calculateChange(pos,type,roll,oppID):
    global properties
    change = 0
    if(properties[pos].owner == oppID and properties[pos].type in ["Reg","Util","Rail"]):
        print(pos)
        change-=properties[pos].rent[0]
    
    if(pos-roll<=0):change+=200
    
    if(type=="CH" or type=="CC"):
        if(random.randint(0,100)<=50):change-=50
        else: change+=50
    
    if(type=="Tax"):
        if(pos==4): change-=200
        elif(pos==38): change-=100
    
    return change

def buyProperty(pos):
    global playerOne
    global playerTwo
    global properties
    print(pos,properties[pos].owner)
    if (properties[pos].owner>0):
        return False
    return True

def buyPropertyMarkov(pos,playerMoney):
    if (properties[pos].owner>0):
        return -1
    min_turns =  sys.maxsize
    index = -1
    for i in range(0,len(properties[pos].rent)):
        x1 = landing_probs[pos]*properties[pos].rent[i]
        if(x1<min_turns):
            min_turns = x1
            index = i
    if index!=-1:
        price = (properties[pos].price+(properties[pos].house_price*index))
        cutoff = 0.02*(playerMoney-price)-10
        if(min_turns<=cutoff):
            return index
        else: 
            return -1


def buyHousesMarkov(playerID):    
    min_turns = sys.maxsize
    index = -1
    houses =0
    for i in range (0,40):
        if (properties[i].owner != playerID): continue
        for j in range(properties[i].houses,len(properties[i].rent)):
            x1 = landing_probs[i]*(properties[i].rent[j]-properties[i].rent[0])
            if(x1<min_turns):
                min_turns = x1
                index = i
                houses = (j-properties[i].houses)
    
    cutoff =0
    if(min_turns<=cutoff):
        return [index,houses]
    else: return [-1,0]

def play(oppPos,oppMoney,oppPropertyBought,oppPropertyExpanded,oppHousesBought):
    global playerOne
    global playerTwo
    global properties

    oppPos = int(oppPos)
    oppPropertyBought = int(oppPropertyBought)
    oppPropertyExpanded = int(oppPropertyExpanded)
    oppHousesBought = int(oppHousesBought)

    print(oppPos,oppPropertyBought,oppPropertyExpanded,oppHousesBought)
    print("Called")
    playerOne.pos = oppPos #update postion
    playerOne.money = oppMoney #update money
    if (oppPropertyBought != -1):  #if player got a property, update prop list, prop owner
        playerOne.props.append(oppPropertyBought)
        properties[oppPropertyBought].owner = 1
        print("Bought by you: ",properties[oppPropertyBought].owner)
        

    if (oppPropertyExpanded != -1): #if player got houses, update no of houses, and rent
        properties[oppPropertyExpanded].houses += oppHousesBought
        houses = properties[oppPropertyExpanded].houses
        properties[oppPropertyExpanded].rent[0] = properties[oppPropertyExpanded].rent[houses] #update rent

    dice_roll =0
    if (playerTwo.jail == True):
        if(random.random()<0.333):
            playerTwo.jail = False
    else:
        dice_roll = roll()
        playerTwo.pos = (playerTwo.pos + dice_roll)%40
    
    newProp = -1
    invtypes = ["Tax","CH","CC","Jail","GO","Park","GoJail"]
    bought_property = False
    [newPropertyExpanded,newHousesBought]= [-1,0]

    if (playerTwo.pos == 30):
        playerTwo.pos =10
        playerTwo.jail = True
    #buy new prop with or without houses
    elif ((properties[playerTwo.pos].type not in invtypes)):
        buy_index = buyPropertyMarkov(playerTwo.pos,playerTwo.money)
        print("Buy Index:",buy_index)
        if (buy_index != -1):
            if(buy_index>0):
                newPropertyExpanded = playerTwo.pos
                newHousesBought = buy_index
            bought_property = True
            newProp = playerTwo.pos
            playerTwo.money -= (properties[playerTwo.pos].price + properties[playerTwo.pos].house_price*buy_index)
            properties[playerTwo.pos].owner = 2
            properties[playerTwo.pos].rent[0] = properties[playerTwo.pos].rent[buy_index]
            properties[playerTwo.pos].houses = buy_index
            

    if (bought_property == False):
        [newPropertyExpanded,newHousesBought]= buyHousesMarkov(playerTwo.id)
        if(newHousesBought>0):
            playerTwo.money-= properties[newPropertyExpanded].house_price*newHousesBought
            properties[newPropertyExpanded].houses+=newHousesBought
            num_houses =  properties[newPropertyExpanded].houses
            properties[newPropertyExpanded].rent[0] = properties[newPropertyExpanded].rent[num_houses]

    playerTwo.money+= calculateChange(playerTwo.pos,properties[playerTwo.pos].type,dice_roll,1)

    #print(playerTwo.pos,playerTwo.money,newProp)
    payload = {"pos":playerTwo.pos,"money":playerTwo.money,"propertyBought":newProp,"propertyExpanded":newPropertyExpanded,"housesBought":newHousesBought}
    res = requests.put('http://127.0.0.1:8000/api/interactions/6/',data=payload)


    


    