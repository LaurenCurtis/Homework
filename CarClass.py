class Car:
    def __init__(self, year, make):
        self.__year_model = year
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -=5
    
    def get_speed(self):
        return self.__speed
    
    def get_make(self):
        return self.__make
    
    def get_year(self):
        return self.__year_model

    def set_speed(self, speed):
        self.__speed = speed

    def set_make(self, make):
        self.__make = make

    def set_year(self, year):
        self.__year_model = year
    