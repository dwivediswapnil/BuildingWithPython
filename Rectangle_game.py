import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def falls_in_rectangle(self,lowleft,upright):
            if (lowleft[0]<self.x<upright[0]) and (lowleft[1]<self.y<upright[1]):
                 return True
            else:
                 return False
    def distance_from_coordinates(self,x,y):
         return math.sqrt((self.x-x)**2+(self.y-y)**2 )   

            
point = Point(4,5)
print(point.falls_in_rectangle((1,3),(8,9)))   
print(point.distance_from_coordinates(4,9))         
