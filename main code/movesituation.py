import random as rd

x = input()
y = input()
class move:
    def __init__(self,x,y):
        self.x = int(x)
        self.y = int(y)
    def move1(self):
        x = self.x + 1
        y = self.y + 1
        return(x,y)

    def move2(self):
        x = self.x + 1
        y = self.y
        #print("test")
        return(x,y)

    def move3(self):
        x = self.x + 1
        y = self.y - 1
        return(x,y)

    def move4(self):
        x = self.x
        y = self.y - 1
        return(x,y)

    def move5(self):
        x = self.x - 1
        y = self.y - 1
        return(x,y)

    def move6(self):
        x = self.x - 1
        y = self.y
        return(x,y)

    def move7(self):
        x = self.x - 1
        y = self.y + 1
        return(x,y)

    def move8(self):
        x = self.x
        y = self.y + 1
        return(x,y)

k = rd.randint(1, 8)
method_name = 'move'+str(k)
a = move(x,y)
method = getattr(a,method_name)
print(method())

