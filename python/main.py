from account import Account
from car import Car

def run():
    print("Hola mundo")
    carrito = Car("AMS123", Account("Andrés Herrera", "ANDA876"))
    print(vars(carrito))
    print(vars(carrito.driver))
    # print(vars(carrito.license))




if __name__== '__main__':
    run()