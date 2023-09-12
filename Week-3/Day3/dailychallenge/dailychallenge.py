import math

class Circle():
  def __init__(self,radius):
    self.radius = radius
    self.diameter = radius*2

  def area_circle(self):
    circle_area = math.pi*(self.radius**2)
    return f"The circle area is {circle_area}"
  
  def __str__(self):
    return f"The circle attributes are: radius = {self.radius}cm  and diameter = {self.diameter}cm "
  
  def __add__(self,other_circle):
    new_circle = self.radius + other_circle.radius
    return f"{Circle(new_circle)}"
  
  def __gt__(self,other_cicle):
    try: 
      return self.radius > other_cicle.radius
    except:
      return self.radius < other_cicle.radius
    
  def __gt__(self,other_cicle):
    if self.radius == other_cicle.radius:
      return True
    else:
      return False
    

circle1 = Circle(5)
circle2 = Circle(6)
circle3 = Circle(8)

print(circle1.area_circle())

print(circle1 + circle2)









    
 
  







  


    


   

    

  


