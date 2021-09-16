class Car:
    def __init__(self, year, make):
        self.__year_model = year
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -=5
    
    def getspeed(self):
        return self.__speed
    
    def getmake(self):
        return self.__make
    
    def getyear(self):
        return self.__year_model
    