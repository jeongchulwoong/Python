#상속(inheritance)
class Car :
    
    def __init__(self, make, model, color, price) :
        self.make = make
        self.model = model
        self.color = color
        self.price = price
        
    def set_make(self, make) :
        self.make = make
        
    def get_make(self) :
        return self.make
    
    def get_Desc(self) :
        return "차량 = (" + (self.make) +","+ \
            self.model + "," + \
            self.color + "," + \
            str(self.price)  + ")"
class ElectricCar(Car) :        #상속 받을 클래스 명
    
    def __init__(self, make, model, color, price, batterySize):     #상속을 받으면 받은 것의 책임을 져야한다
        super().__init__(make, model, color, price)             #__init__ : 생성자
        self.batterySize = batterySize
        
    def set_batterySize(self, batterySize) :
        self.batterySize = batterySize
        
    def get_batterySize(self) :
        return str(self.batterySize)
    
        

def main() :
    myCar = ElectricCar("Tisla", "Model S", "white", 10000, 0)
    myCar.set_make("Tesla")
    myCar.set_batterySize(60)
    print(myCar.get_Desc())
    print(myCar.get_batterySize())
    
main()   