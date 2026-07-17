#defining class to perform operations on retangle
class rectangle:
    #memeber variable
    length=0
    breath=0
    #method to initialize data
    def initialize(self,l,b):
        self.length=l
        self.breath=b
    #method to display data
    def displaydata(self):
        print("-----Rectangle------")
        print("length",self.length,"cm")
        print("breath",self.breath,"cm")
#----------main program------------
#object creation
rect=rectangle()
rect=initialize(20,50)
