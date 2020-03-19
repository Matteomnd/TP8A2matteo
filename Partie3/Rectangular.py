class Rectangle :
    def __init__(self,x,y,width,height):
        self.__x=x
        self.__y=y
        self.__height=height
        self.__width=width

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getHeight(self):
        return self.__height

    def getWidth(self):
        return self.__width

    def setX(self,x):
        self.__x=x

    def setY(self,y):
        self.__y=y

    def setHeight(self, height):
        self.__height=height

    def setWidth(self,width):
        self.__width=width

