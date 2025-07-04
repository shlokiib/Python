class Students:   
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Student name: {self.name}, Student Age: {self.age}"
    
S1 = Students("Abc",21)
S2 = Students("HELLO",32)

print(S1)
print(S2)
        
        
        