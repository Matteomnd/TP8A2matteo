from Cercle import Circle
from Rectangular import Rectangle
import turtle as T


class Shape:

    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self,x):
        self.__x = x

    def sety(self,y):
        self.__y = y

    class Circle(Shape):

        def __init__(self,radius):
            self.__radius = radius

        def getRadius(self):
            return self.__radius

        def setRadius(self,radius):
            self.__radius = radius

        def draw(self,turtle):
            turtle.circle(self.__radius)



    class Rectangle(Shape) :

        def __init__(self,width,height) :
            self.__width = width
            self.__height = height

        def getWidth(self):
             return self.__width

        def getHeight(self):
            return self.__height

        def setWidth(self,width):
            self.__width = width

        def setHeight(self,height):
            self.__height = height

        def draw(self,turtle):
            turtle.goto(0,0)
            turtle.right(90)
            turtle.forward(self.__width)
            turtle.right(90)
            turtle.forward(self.__height)
            turtle.right(90)
            turtle.forward(self.__width)
            turtle.right(90)
            turtle.forward(self.__height)
            turtle.exitonclick()

objet = Shape(3,4)

objrect= Rectangle(100,178)
objcircle = Circle(100)
objcircle.draw(T)
objrect.draw(T)



