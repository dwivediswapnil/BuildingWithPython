# import math
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

#     def falls_in_rectangle(self,lowleft,upright):
#             if (lowleft[0]<self.x<upright[0]) and (lowleft[1]<self.y<upright[1]):
#                  return True
#             else:
#                  return False
#     def distance_from_coordinates(self,x,y):
#          return math.sqrt((self.x-x)**2+(self.y-y)**2 )   

            
# point = Point(4,5)
# print(point.falls_in_rectangle((1,3),(8,9)))   
# print(point.distance_from_coordinates(4,9))    

from random import randint
class Point:
     def __init__(self,x,y):
          self.x = x
          self.y = y

     def falls_in_rectangle(self, rectangle):
          if (rectangle.lowleft.x < self.x < rectangle.upright.x) and (rectangle.lowleft.y < self.y < rectangle.upright.y):
               return True
          else:
               return False
          
class Rectangle:
     def __init__(self,lowleft,upright):
          self.lowleft = lowleft
          self.upright = upright

     def area(self):
          return (self.upright.x - self.lowleft.x) * (self.upright.y - self.lowleft.y)     

# rectanglex = Rectangle(Point(5,6),Point(7,9))
rectangle = Rectangle(Point(randint(0,9), randint(0,9)),
                      Point(randint(10,19),randint(10,19)))

print("Rectangle coordinates: ", rectangle.lowleft.x,",",rectangle.lowleft.y,"and",rectangle.upright.x,",",rectangle.upright.y)

user_point = Point(float(input("Guess x:")),float(input("Guess y:")))
user_area = float(input("Guess the area: "))

print("Your point was in rectangle: ",user_point.falls_in_rectangle(rectangle))
print("Your area was off by: ",rectangle.area() - user_area)

