class Board:
    def __init__(self):
        self.p1_pos = 0
        self.p2_pos = 0
        self.properties = []

    def start(self):
        print("Started")

    def create_properties(self):
        self.properties.append("Baltic Avenue","Brown",300,40)
        self.properties.append("Connecticut Avenue","Light Blue",600,80)
        self.properties.append("Virginia Avenue","Purple",800,120)
        self.properties.append("New York Avenue","Orange",1000,160)
        self.properties.append("Illinois Avenue","Red",1200,200)
        self.properties.append("B.&O. Railroad","Black",1000,250)
        self.properties.append("Marvin Gardens","Yellow",1400,240)
        self.properties.append("Pennsylvania Avenue","Green",1600,280)
        self.properties.append("Short Line","Black",1000,250)
        self.properties.append("Boardwalk","Blue",2000,500)


