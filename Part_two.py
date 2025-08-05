class Product:
    def __init__(self, name, quantity):
        self.name = str(name)
        self.quantity = int(quantity)

class Store:
    def __init__(self):
        self.__products = []

    def add_product(self, name, quantity):
        obj = Product(name, quantity)
        self.__products.append(obj)

    def show_products(self):    
        for obj in self.__products:
            print(obj.name + " : " + str(obj.quantity))

my_store = Store()
my_store.add_product("Laptop", 15)
my_store.add_product("Mouse", 50)
my_store.add_product("Mouse", 50)
my_store.show_products()