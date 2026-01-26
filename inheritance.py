class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage = mileage
        self.cost = cost

    def show_details(self):
        print("I am a Vehicle")
        print("Mileage of vehicle is ",self.mileage)
        print("Cost of Vehicle is ",self.cost)
v1 = Vehicle(500,500)
v1.show_details()

#inheritance example
class Car(Vehicle):
    def show_car(self):
        print("I am a Car")
c1=Car(200,1200)
c1.show_details()
c1.show_car()


#over-riding init method
class Car(Vehicle):
    def __init__(self,mileage,cost,tyres,hp):
        super().__init__(mileage,cost)
        self.tyres = tyres
        self.hp = hp
    def show_car_details(self):
        print("i am a car")
        print("number of tyres are",self.tyres)
        print("value of horse power is",self.hp)
c1 = Car(20,12000,4,300)
c1.show_details()
c1.show_car_details()

    
