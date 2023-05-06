class Car:
    wheel=4
    def __init__(self,make,model,color,speed=0):
        self.make=make
        self.model=model
        self.color=color
        self.speed=speed
    def hooting(self):
        return f"peep peep" 
    def get_model(self):
        return self.model
    def get_color(self):
        return self.color
car=Car("BMW","Toyota","Black",500)