class Car : 
    def __init__(self, speed, color, model) :
        self.speed = speed
        self.color = color
        self.model = model
        
    def drive(self) :
        self.speed = 60
        
myCar = Car(0, "blue", "E-calss")

print("자동차 객체를 생성 했습니다.")
print("자동차의 속도는 : ", myCar.speed)
print("자동차의 색상 : ", myCar.color)
print("자동차의 모델 : ", myCar.model)