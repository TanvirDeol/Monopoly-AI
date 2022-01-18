import winreg
from player import property,Player,roll,landing_probs
import random,math,sys,copy
from collections import deque
import time
import threading

playerAI = Player("Markov AI",1,0,1500,[]) #human player
playerRandom = Player("Randomized",2,0,1500,[]) #AI player
properties =[]
max_risk = 300
scoreboard = [0,0]
game_log = ""
moves = 0

itr = 2
MAX = 10
wins = [0,0]
q = deque()
def reset():
    global playerAI
    global playerRandom
    global properties
    playerAI = Player(playerAI.name,1,0,1500,[]) 
    playerRandom = Player(playerRandom.name,2,0,1500,[])
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

def mcts(player,opp,props,turn):
    global itr
    global wins
    if len(q)>=MAX: itr=1
    if (turn == 'P'):
        for i in range(0,itr):
            props_copy = copy.deepcopy(props)
            opp_copy = copy.deepcopy(opp)
            player_copy = copy.deepcopy(player)
            [opp_copy,player_copy,winner] = play(opp_copy,player_copy,props_copy,False)
            if (winner!=-1):
                wins[winner-1]+=1
            else: q.append([opp_copy,player_copy,props_copy,'O'])
    elif (turn == 'O'):
        for i in range(0,itr):
            props_copy = copy.deepcopy(props)
            opp_copy = copy.deepcopy(opp)
            player_copy = copy.deepcopy(player)
            [player_copy,opp_copy,winner] = play(player_copy,opp_copy,props_copy,False)
            if (winner!=-1):
                wins[winner-1]+=1
            else: q.append([player_copy,opp_copy,props_copy,'P'])

def mcts_sim(player,opp,props):
    global itr
    global wins
    for i in range(0,1):
        itr = 2
        q.append([copy.deepcopy(opp),copy.deepcopy(player),props,'O'])
        while (len(q)>0):       
            player_copy,opp_copy,props_copy,turn = q.pop()
            mcts(player_copy,opp_copy,props_copy,turn)
    win_rate = (wins[player.id-1]/(wins[0]+wins[1]))*100
    wins = [0,0]
    print(win_rate)
    return win_rate

def simulate(runs):
    global scoreboard
    global moves
    global properties
    global game_log
    for i in range(0,runs):
        reset()
        game_log=""
        moves =0
        playerOne = playerAI
        playerTwo = playerRandom
        winner = -1
        while(1):
            [b1,b,winner] = play(playerOne,playerTwo,properties,True)
            if(winner!=-1):break
            [b2,b3,winner] = play(playerTwo,playerOne,properties,True)
            if(winner!=-1):break
        #print("WINNER: ",winner)
        scoreboard[winner-1]+=1
        f = open("log.txt", "a")
        f.write(game_log+"\n") 
        prop_str = ""
        for i in range(0,len(properties)):
            prop_str+="ID: "+str(i)+" "+str(properties[i])+"\n"
        f.write(prop_str+"\n----------------------------------------------------------------------------\n")
        f.close()
    print(scoreboard)

def calculateChange(pos,type,roll,oppID,props):
    change = 0
    reason = ""
    if(props[pos].owner == oppID and (props[pos].type in ["Reg","Util","Rail"])):
        change-=props[pos].rent[0]
        reason = "Rent Owned on "+str(pos)
    
    if(pos-roll<=0):
        change+=200
        reason = "Crossed GO"
    
    if(type=="CH" or type=="CC"):
        if(random.randint(0,100)<=50):change-=50
        else: change+=50
        reason = "Change or Chest"
    
    if(type=="Tax"):
        if(pos==4): change-=200
        elif(pos==38): change-=100
        reason = "Tax Paid"
    
    return [change,reason]

def buyPropertyRandom(pos,playerMoney,props):
    if (random.random()<0.5): return -1
    index = random.randint(0,len(props[pos].rent)-1)
    price = props[pos].price+(props[pos].house_price*index)
    if(playerMoney-price<max_risk):return -1
    else: return index

def buyPropertyRandom1(pos, playerMoney,props):
    prob = (2.11*pos)+7.89
    if ((random.random()*100)>prob): return -1
    index = random.randint(0,len(props[pos].rent)-1)
    price = props[pos].price+(props[pos].house_price*index)
    if(playerMoney-price<max_risk):return -1
    else: return index

def buyHousesRandom(playerMoney,playerID,props):
    if(random.random()>0.1): return [-1,0]
    props = []
    for i in range(len(props)):
        if(props[i].owner == playerID and props[i].houses<(len(props[i].rent)-1)): 
            props.append(i)
    if(len(props)==0): return [-1,0]
    pick = props[random.randint(0,len(props)-1)]
    
    if(playerMoney- props[pick].house_price < max_risk): return [-1,0]
    return [pick,1]
    
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
        cutoff = 300
        if(min_turns<=cutoff and playerMoney-price>=max_risk):
            return index
        else: 
            return -1


def buyHousesMarkov(playerMoney,playerID):    
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
    
    price = properties[index].price+ (properties[index].house_price*houses)
    cutoff =300
    if(min_turns<=cutoff and playerMoney-price>=max_risk):
        return [index,houses]
    else: return [-1,0]

def buyPropertyMCTS(player,opp,properties):
    mx_rate = 0
    mx_index =-1
    for index in range(0,len(properties[player.pos].rent)):
        player_copy = copy.deepcopy(player)
        props = copy.deepcopy(properties)
        player_copy.props.append(player_copy.pos) #upd prop list
        props[player_copy.pos].owner = player_copy.id # upd owner
        player_copy.money -= (props[player_copy.pos].price + (props[player_copy.pos].house_price*index)) #upd money
        props[player_copy.pos].houses = index #upd num houses
        props[player_copy.pos].rent[0] = props[player_copy.pos].rent[index] #upd rent
        win_rate = mcts_sim(player_copy,opp,props)
        if (win_rate>mx_rate):
            mx_rate = win_rate
            mx_index = index
    price = properties[player.pos].price+(properties[player.pos].house_price*mx_index)
    percent_nw = (price/player.money)*100
    threshold = (0.008)*(mx_rate*mx_rate)

    if(player.money-price<(max_risk) and percent_nw>threshold): return -1
    else: return mx_index

def buyHousesMCTS(player,opp,properties):
    index = -1
    houses =0
    mx_rate =0
    for i in range (0,40):
        if (properties[i].owner != player.id): continue
        for j in range(max(1,properties[i].houses),min(len(properties[i].rent),properties[i].houses+1)):
            player_copy = copy.deepcopy(player)
            props = copy.deepcopy(properties)
            tmp_houses = (j-properties[i].houses)
            player_copy.money -= (props[player_copy.pos].house_price*tmp_houses) #upd money
            props[i].houses = j #upd num houses
            props[i].rent[0] = props[i].rent[j] #upd rent
            win_rate = mcts_sim(player_copy,opp,props)
            if (win_rate>mx_rate):
                mx_rate = win_rate
                index = i
                houses = tmp_houses
            
    price = (properties[index].house_price*houses)
    percent_nw = (price/player.money)*100
    threshold = (0.008)*(mx_rate*mx_rate)
    if(player.money-price<(max_risk) or percent_nw>threshold): return [-1,0]
    else: return [index,houses]





def play(player,opp,props,sim):
    global game_log
    global moves
    dice_roll =0
    if (player.jail == True):
        if(random.random()<0.333):
            player.jail = False
    else:
        dice_roll = roll()
        player.pos = (player.pos + dice_roll)%40
    
    newProp = -1
    invtypes = ["Tax","CH","CC","Jail","GO","Park","GoJail"]
    bought_property = False
    [newPropertyExpanded,newHousesBought]= [-1,0]

    if (sim==True):
        print("Yes")

    if (player.pos == 30):
        player.pos =10
        player.jail = True
    #buy new prop with or without houses
    elif ((props[player.pos].type not in invtypes) and props[player.pos].owner==0):
        buy_index = -1
        #prop_copy = copy.deepcopy(props)
        if (player.id == 1):
            if (sim == True): buy_index = buyPropertyMCTS(player,opp,props)
            else : buy_index = buyPropertyRandom(player.pos,player.money,props)
        elif (player.id ==2): buy_index = buyPropertyRandom(player.pos,player.money,props)
        if (buy_index != -1):
            if(buy_index>0):
                #newPropertyExpanded = player.pos
                newHousesBought = buy_index
            bought_property = True
            newProp = player.pos
            player.props.append(player.pos) #append props
            player.money -= (props[player.pos].price + props[player.pos].house_price*buy_index) #update money
            props[player.pos].owner = player.id #update prop owner
            props[player.pos].rent[0] = props[player.pos].rent[buy_index] #update prop rent
            props[player.pos].houses = buy_index #update prop houses
            

    
    if (bought_property == False):
        #prop_copy = copy.deepcopy(props)
        if (player.id == 1): 
            if(sim == True): 
                [newPropertyExpanded,newHousesBought]= buyHousesMCTS(player,opp,props)
            else : [newPropertyExpanded,newHousesBought]= buyHousesRandom(player.money,player.id,props)
        elif (player.id == 2): [newPropertyExpanded,newHousesBought]= buyHousesRandom(player.money,player.id,props)

        if(newHousesBought>0):
            player.money-= props[newPropertyExpanded].house_price*newHousesBought #update money
            props[newPropertyExpanded].houses+=newHousesBought #update prop houses
            num_houses =  props[newPropertyExpanded].houses
            props[newPropertyExpanded].rent[0] = props[newPropertyExpanded].rent[num_houses] #update prop rent

    [change,reason]= calculateChange(player.pos,props[player.pos].type,dice_roll,opp.id,props)
    player.money+=change
    winner = -1
    if(player.money<=0): winner = opp.id

    if (sim==True): 
        game_log+="Player: "+str(player.id)+", Money:"+str(player.money)+", New Property: "+str(bought_property)+str(newProp)+", New Property Expanded: "+str(newPropertyExpanded)+", New Houses Bought: "+str(newHousesBought)+", Changes: "+str(change)+", Reason: "+reason+"\n"
        moves+=1
        print(moves)

    return [player,opp,winner]

def printit():
  threading.Timer(3.0, printit).start()
  print(scoreboard)



printit()
start = time.time()
simulate(20)
end = time.time()
print(end-start)


