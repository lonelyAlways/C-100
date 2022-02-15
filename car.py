from bdb import GENERATOR_AND_COROUTINE_FLAGS


class Car(object):
    def __init__(self,model,colour,company,speed):
        self.model = model
        self.company = company
        self.colour = colour
        self.speed = speed

o1 = Car("desire","black","Maruti",180)
o2 = Car("Audi","Baingani","AUdi",240)

print(o1.model)
print(o2.colour)

         