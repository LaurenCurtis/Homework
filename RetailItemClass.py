class RetailItem:
    def __init__(self, desc, inven, price):
        self.__description = desc 
        self.__units_in_inventory = inven
        self.__price = price

    def get_description(self):
        return self.__description

    def get_inventory(self):
        return self.__units_in_inventory

    def get_price(self):
        return self.__price

    def set_description(self, desc):
        self.__description = desc

    def set_inventory(self, inven):
        self.__units_in_inventory = inven

    def set_price(self, price):
        self.__price = price