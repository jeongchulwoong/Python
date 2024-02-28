class Address : 
    def __init__(self, street, city) :
        self.street = street
        self.city = city
        
class Person :
    def __init__(self, name, email) :
        self.name = name
        self.email = email
        
class Contact() :
    def __init__(self, name, email, street, city):  
        Address.__init__(self,street, city)         #클래스 호출 개념
        Person.__init__(self,name, email)
        
# class Contact(Address, Person) :                  #상속개념
#     def __init__(self, name, email, street, city):
#         Address.__init__(self,street, city)
#         Person.__init__(self,name, email)
        
    def __str__(self) :
        return "\nname : {} \nemail : {} \nstreet : {} \ncity : {}".format(self.name, self.email, self.street, self.city)
    
c = Contact("kim", "kim@gmail", "gozan", "Ansan")
print(c)
    