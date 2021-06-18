class Warehouse:
    purpose = "storage"
    region = "west"

w1 = Warehouse()
print(w1.purpose,w1.region)

class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)
    
    def addtwice(self,x):
        self.add(x)
        self.add(x)