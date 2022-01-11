//import board_img from "./board.png"
var myGamePiece;
let turn = false;
let p1Skips = 0;
let p2Skips = 0;
let p1NewProperty = -1;
let p1NewPropertyExpanded = -1;
let p1NewHouses = 0;

// List of all properties in monopoly
const properties = [
    new property("GO", 650, 650, "GO", 0, 0,[],0,0),
    new property("Mediteranean Avenue", 570, 650, "Reg", 60, 50,[2,10,30,90,160,250],0,0),
    new property("CC1", 515, 650, "CC", 0, 0,[],0,0),
    new property("Baltic Avenue", 460, 650, "Reg", 60, 50,[4,20,60,180,320,450],0,0),
    new property("Income Tax", 405, 650, "Tax", 0, 0,[200],0,0),
    new property("Reading Railroad", 350, 650, "Rail", 200, 0,[25,50,100,200],0,0),
    new property("Oriental Avenue", 295, 650, "Reg", 100, 50,[6,30,90,270,400,550],0,0),
    new property("CH1", 240, 650, "CH", 0, 0,[],0,0),
    new property("Vermont Avenue", 185, 650, "Reg", 100, 50,[6,30,90,270,400,550],0,0),
    new property("Connecticut Avenue", 130, 650, "Reg", 120, 50,[8,40,100,300,450,600],0,0),
    new property("Jail", 50, 650, "Jail", 120, 50,[],0,0),
    new property("St. Charles Place", 25, 550, "Reg", 140, 100,[10,50,150,450,625,750],0,0),
    new property("Electric Company", 25, 495, "Util", 150, 35,[30],0,0),
    new property("States Avenue", 25, 440, "Reg", 140, 100,[10,50,150,450,625,750],0,0),
    new property("Virginia Avenue", 25, 385, "Reg", 160, 100,[12,60,180,500,700,900],0,0),
    new property("Pennsylvania Railroad", 25, 330, "Rail", 200, 0,[25,50,100,200],0,0),
    new property("St. James Place", 25, 275, "Reg", 180, 100,[14,70,200,550,750,950],0,0),
    new property("CC2", 25, 220, "CC", 0, 0,[],0,0),
    new property("Tennessee Avenue", 25, 165, "Reg", 180, 100,[14,70,200,550,750,950],0,0),
    new property("New York Avenue", 25, 115, "Reg", 200, 100,[16,80,220,600,800,1000],0,0),
    new property("Free Parking",50, 50, "Park", 0, 0,[],0,0),
    new property("Kentucky Avenue", 130, 50, "Reg", 220, 150,[18,90,250,700,875,1050],0,0),
    new property("CH2", 185, 50, "CH", 0, 0,[],0,0),
    new property("Indiana Avenue", 240, 50, "Reg", 220, 150,[18,90,250,700,875,1050],0,0),
    new property("Illinois Avenue", 295, 50, "Reg", 240, 150,[20,100,300,750,925,1100],0,0),
    new property("B&O Railroad", 350, 50, "Rail", 200, 0,[25,50,100,200],0,0),
    new property("Atlantic Avenue", 405, 50, "Reg", 260, 150,[22,110,330,800,975,1150],0,0),
    new property("Ventnor Avenue", 460, 50, "Reg", 260, 150,[22,110,330,800,975,1150],0,0),
    new property("Water Works", 515, 50, "Util", 150, 0,[30],0,0),
    new property("Marvin Gardens", 570, 50, "Reg", 280, 150,[24,120,360,850,1025,1200],0,0),
    new property("Go To Jail", 650, 50, "GoJail", 0, 0,[],0,0),
    new property("Pacific Avenue", 650, 120, "Reg", 300, 200,[26,130,390,900,1100,1275],0,0),
    new property("North Carolina Avenue", 650, 175, "Reg", 300, 200,[26,130,390,900,1100,1275],0,0),
    new property("CC3", 650, 230, "CC", 0, 0,[],0,0),
    new property("Pennsylvania Avenue", 650, 285, "Reg", 320, 200,[28,150,450,1000,1200,1400],0,0),
    new property("Short Line", 650, 340, "Rail", 200, 0,[25,50,100,200],0,0),
    new property("CH3", 650, 395, "CH", 0, 0,[],0,0),
    new property("Park Place", 650, 450, "Reg", 350, 200,[35,175,500,1100,1300,1500],0,0),
    new property("Luxury Tax", 650, 505, "Tax", 0, 0,[100],0,0),
    new property("Boardwalk", 650, 560, "Reg", 400, 200,[50,200,600,1400,1700,2000],0,0),
]


function startGame() {
    myBoard = new img_component(700,700,"board.png",0,0);
    playerOne = new player(50, 50, "you.png", properties[0].posx, properties[0].posy);
    playerTwo = new player(50, 50, "opp.png", properties[0].posx, properties[0].posy);
    myGameArea.start();

}

// Displays all fields of the property that the current player is on
function displayProperty(index){
    let disp = properties[index].name+"<br>";
    let owners = ["None","Player 1","Player 2"];
    if(properties[index].type === "Reg"){
        disp+= "Price: "+ properties[index].price+"<br>"+
                "House/Hotel Price: "+ properties[index].house_price+"<br>"+
                "Rent: "+ properties[index].rent[0]+"<br>"+
                "1 House Rent: "+ properties[index].rent[1]+"<br>"+
                "2 House Rent: "+ properties[index].rent[2]+"<br>"+
                "3 House Rent: "+ properties[index].rent[3]+"<br>"+
                "4 House Rent: "+ properties[index].rent[4]+"<br>"+
                "Hotel Rent: "+ properties[index].rent[5]+"<br>"+
                "Houses Built: "+ properties[index].houses+"<br>"+
                "Owner: "+ owners[properties[index].owner]+"<br>";

    }else if (properties[index].type === "Rail"){
        disp+= "Price: "+ properties[index].price+"<br>"+
                "1 Railroad Rent: "+ properties[index].rent[0]+"<br>"+
                "2 Railroad Rent: "+ properties[index].rent[1]+"<br>"+
                "3 Railroad Rent: "+ properties[index].rent[2]+"<br>"+
                "4 Railroad Rent: "+ properties[index].rent[3]+"<br>"+
                "Owner: "+ owners[properties[index].owner]+"<br>";
    }
    else if (properties[index].type === "Util"){
        disp+= "Price: "+ properties[index].price+"<br>"+
                "Rent: "+ properties[index].rent[0]+"<br>"+
                "Owner: "+ owners[properties[index].owner]+"<br>";
        
    }
    else if (properties[index].type === "Tax"){
        disp+= "Must Pay: "+ properties[index].rent[0]+"<br>";
    }
    else if(properties[index].type==="CC"){disp = "Community Chest";}
    else if(properties[index].type==="CH"){disp = "Chance";}
    
    return disp;
}

// Calculates Reward/Penalty for landing on certain properties
function calculateChange(prevPos,nextPos,type,playerId){
    var change = 0;
    if(properties[nextPos].owner>0 && properties[nextPos].owner!=playerId){
        change-=properties[nextPos].rent[0];
    }
    if(nextPos<prevPos)change+=200;
    if(type==="CH" || type==="CC"){
        if(Math.random()<=0.5)change-=50;
        else change+=50;
    }
    if(type==="Tax"){
        if(nextPos===4)change-=200;
        else if(nextPos===38)change-=100;
    }
    return change;
}

// Rolls the dice and moves the player to where it needs to be
function rollDice(){
    let moves = Math.floor(Math.random() * 12)+1;
    invtypes = ["Tax","CH","CC","Jail","GO","Park","GoJail"];
    if (turn === false){
        playerOne.next_pos = (playerOne.current_pos+moves)%40;
        document.getElementById("propinfo").innerHTML= displayProperty(playerOne.next_pos);
        //if property owned by another player, or its a property thats not a building...
        if(p1Skips>0){
            turn=true;
            p1Skips=0;
            rollDice();
        }
        else if(properties[playerOne.next_pos].owner> 0 || invtypes.includes(properties[playerOne.next_pos].type)){
            document.getElementById("buy_button").disabled = true;
            playerOne.money += calculateChange(playerOne.current_pos,playerOne.next_pos,properties[playerOne.next_pos].type,1);
            document.getElementById("p1_money").innerHTML = "Your Balance: $" + playerOne.money;
        }
        //if player lands in go to jail...
        else if(playerOne.next_pos===30){
            playerOne.next_pos = 10;
            p1Skips=1;
        }
        else{ document.getElementById("buy_button").disabled = false;}

    }else{
        playerTwo.next_pos = (playerTwo.current_pos+moves)%40;
        document.getElementById("propinfo").innerHTML= displayProperty(playerTwo.next_pos);
        if(p1Skips>0){
            turn=true;
            p1Skips=0;
            rollDice();
        }
        else if(properties[playerTwo.next_pos].owner> 0 || invtypes.includes(properties[playerTwo.next_pos].type)){
            document.getElementById("buy_button").disabled = true;
            playerTwo.money += calculateChange(playerTwo.current_pos,playerTwo.next_pos,properties[playerTwo.next_pos].type,2);
            document.getElementById("p2_money").innerHTML = "Opponent Balance: $" + playerTwo.money;
        }
        else if(playerTwo.next_pos===30){
            playerTwo.next_pos = 10;
            p2Skips=1;
        }
        else{ document.getElementById("buy_button").disabled = false;}
    }
    document.getElementById("roll_button").disabled=true;
}

// Switches turns from one player to another
function switchTurns(){
    if (turn === false){ //player 1
        turn = true;
        document.getElementById("playerturn").innerHTML= "Turn: Player 2";
        if(playerTwo.current_pos === 30){
            playerTwo.next_pos = 10;
            switchTurns();
        }
        let p1Data = {pos: playerOne.current_pos,
            money: playerOne.money,
            propertyBought: p1NewProperty,
            propertyExpanded: p1NewPropertyExpanded,
            housesBought: p1NewHouses};
        const res = axios.put('http://127.0.0.1:8000/api/interactions/5/',p1Data);
        const p2Data = await axios.get('http://127.0.0.1:8000/api/interactions/6/')
        .then(function(response){console.log(response)});
        console.log(p2Data);

    }else{ //player 2
        turn = false;
        document.getElementById("playerturn").innerHTML= "Turn: Player 1";
        if(playerOne.current_pos === 30){
            playerOne.next_pos = 10;
            switchTurns();
        }
    }
    document.getElementById("roll_button").disabled=false;
    document.getElementById("buy_button").disabled=true;
}

// Buys a property for a player, this property is the current property the player is on
function buyProperty(){
    if (turn === false){
        playerOne.money-=properties[playerOne.next_pos].price;
        playerOne.props.push(playerOne.next_pos);
        p1NewProperty = playerOne.next_pos;
        document.getElementById("p1_money").innerHTML = "Your Balance: $" + playerOne.money;
        properties[playerOne.next_pos].owner=1;
        document.getElementById("your_props").innerHTML += "ID:"+ playerOne.next_pos +". "+ properties[playerOne.next_pos].name+"<br>";

    }else{
        playerTwo.money-=properties[playerTwo.next_pos].price;
        playerTwo.props.push(playerTwo.next_pos);
        document.getElementById("p2_money").innerHTML = "Opponent Balance: $" + playerTwo.money;
        properties[playerTwo.next_pos].owner=2;
        document.getElementById("opp_props").innerHTML += "ID:"+ playerTwo.next_pos +". "+properties[playerTwo.next_pos].name+"<br>";
    }
    document.getElementById("buy_button").disabled=true;

}

function showPropList(){
    document.getElementById("house_id").innerHTML = "";
    if(turn===false){
        for(let i =0;i<playerOne.props.length;i++){
            let j = playerOne.props[i];
            document.getElementById("house_id").innerHTML += "<option value="+j+">"+j+"</option>\n";
        }
    }else{
        for(let i =0;i<playerTwo.props.length;i++){
            let j = playerTwo.props[i];
            document.getElementById("house_id").innerHTML += "<option value="+j+">"+j+"</option>\n";
        }
    }
}

function addHouse(){
    id = document.getElementById("house_id").value;
    if(properties[id].houses===5)return;
    properties[id].houses+=1;
    properties[id].rent[0] = properties[id].rent[properties[id].houses];
    p1NewPropertyExpanded =id;
    p1NewHouses+=1;
    if (turn===false){
        playerOne.money-=properties[id].house_price;
    }else{
        playerTwo.money-=properties[id].house_price;
    }
}

function distance(x1, y1, x2, y2){
    return Math.floor(Math.sqrt(Math.pow(x2-x1,2)+Math.pow(y2-y1,2)));
}

var myGameArea = {
    canvas : document.createElement("canvas"),
    start : function() {
        this.canvas.width = 700;
        this.canvas.height = 700;
        this.context = this.canvas.getContext("2d");
        document.getElementById("mb").insertBefore(this.canvas, document.getElementById("mb").childNodes[0]);
        for(let i=0;i<40;i++){
            document.getElementById("prop_id").innerHTML+="<option value="+i+">"+i+"</option>\n";
        }
        this.interval = setInterval(updateGameArea, 20);
    },
    clear : function() {
        this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);
    }
}


function player(width, height, src, x, y) {
    this.image = new Image();
    this.image.src = src;
    this.width = width;
    this.height = height;
    this.x = x;
    this.y = y;    
    this.money = 1500;
    this.props = [];
    this.current_pos = 0;
    this.next_pos =0;
    this.update = function(){
        ctx = myGameArea.context;
        ctx.drawImage(this.image,this.x,this.y,this.width,this.height)
    }
    this.updatePos = function(){
        if (distance(this.x,this.y,properties[this.next_pos].posx,properties[this.next_pos].posy)<=50){
            this.x = properties[this.next_pos].posx;
            this.y = properties[this.next_pos].posy;
            this.current_pos = this.next_pos;
        }
        else{
            this.x += Math.floor((properties[this.next_pos].posx - properties[this.current_pos].posx)/50);
            this.y += Math.floor((properties[this.next_pos].posy - properties[this.current_pos].posy)/50);
        }
    }
}
function img_component(width, height, src, x, y) {
    this.image = new Image();
    this.image.src = src;
    this.width = width;
    this.height = height;
    this.x = x;
    this.y = y;    
    this.update = function(){
        ctx = myGameArea.context;
        ctx.drawImage(this.image,this.x,this.y,this.width,this.height)
    }
}

function property(name, posx, posy, type, price, house_price, rent, houses, owner){
    this.name = name; 
    this.posx = posx;
    this.posy = posy;
    this.type = type;
    this.price = price;
    this.house_price = house_price;
    this.rent = rent;
    this.houses = houses;
    this.owner = owner;
}

function updateGameArea() {
    myGameArea.clear();
    //myGamePiece.x +=1;
    myBoard.update();
    if (playerOne.next_pos != playerOne.current_pos){playerOne.updatePos();}
    playerOne.update();
    if (playerTwo.next_pos != playerTwo.current_pos){playerTwo.updatePos();}
    playerTwo.update();
    if(playerOne.money<=0 || playerTwo.money<=0)alert("Game Over!");
    
}
