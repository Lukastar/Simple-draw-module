import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from math import fabs
import copy

class draw:
    
    '''Klasa draw przyjmuje szerokosc, wysokosc oraz kolor wypelnienia przestrzeni na ktorej chcemy rysowac. Inicjalizuje macierz o podanych wymiarach
       zawierajaca informacje o kolorze i polozeniu pikseli, flage bledu oraz liste, ktora bedzie sluzyla do zapisu stworzonego obiektu.'''
    def __init__(self,c_width,c_height,c_color=1.0):
        self.c_width = c_width
        self.c_height = c_height
        self.c_color = c_color
        self.data=np.zeros((c_height,c_width, 3))
        self.data.fill(c_color)
        self.undo_list=[]
        self.flag=0
        
    '''Funkcja pozwala na reset kanwy oraz wypelnienie jej kolorem.'''
    def reset(self,color=1.0):
        self.data.fill(color)
        
    '''Funkcja tworzy kopie macierzy i zapisuje ja na liscie. Pozwala na zapis progresu.'''        
    def save(self):
        self.undo_list.append(copy.copy(self.data))
        
    '''Funkcja przywraca ostatnia zapisana zmiane.'''          
    def undo(self):
        self.data=self.undo_list.pop()
        
    '''Funkcja wyswietla obrazek jesli nie napotkala bledu.'''  
    def show(self):
        if self.flag==1:
            self.flag=0
            print(self.flag)
            return 'Figure out of bonds!'
        else:
            plt.imshow(self.data, interpolation='none')
            plt.show()
            
    '''Funkcja rysowania linii. Przyjmuje wspolrzedne poczatku, konca oraz kolor.'''             
    def line(self,x0, y0, x1, y1, r=1.0, g=0.0, b=0.0):
        inc_x = x1 - x0
        inc_y = y1 - y0

        if x1 >= self.c_width or y1 >= self.c_height or x0 < 0 or y0 < 0 or x0 >= self.c_height or y0 >= self.c_width or x1 < 0 or y1 < 0:
            self.flag=1
            return
        
        if inc_x == 0:
            if inc_y == 0:
                self.data[y0,x0, 0] = r
                self.data[y0,x0, 1] = g
                self.data[y0,x0, 2] = b
        
            else:
                for y in range(y0, y1):
                    self.data[y, x0, 0] = r
                    self.data[y, x0, 1] = g
                    self.data[y, x0, 2] = b
                
        else:
            a = inc_y / inc_x
            if inc_x > inc_y:
                for x in range (x0, x1):
                    y = round(a * (x - x0)) + y0
                    self.data[y, x, 0] = r
                    self.data[y, x, 1] = g
                    self.data[y, x, 2] = b               
                
            else:
                for y in range (y0, y1):
                    x = round(1/a * (y - y0)) + x0
                    self.data[y, x, 0] = r
                    self.data[y, x, 1] = g
                    self.data[y, x, 2] = b
                    
    '''Funkcja rysuje dowolny prostokat. Przyjmuje wspolrzedne lewego gornego wierzcholka, szerokosc, dlugosc, wypelnienie (0 -brak, 1-wypelniony) oraz kolor.'''                     
    def rectangle(self,x_0,y_0,width,height, full=1, r=1.0, g=0.0, b=0.0):
        
        if full==1:
            for i in range(0,height):
                self.line(x_0,y_0+i,x_0+width,y_0+i,r,g,b)
                
        else:
            self.line(x_0+width, y_0, x_0+width, y_0+height,r,g,b)
            self.line(x_0, y_0, x_0+width, y_0,r,g,b)
            self.line(x_0, y_0, x_0, y_0+height,r,g,b)
            self.line(x_0, y_0+height, x_0+width, y_0+height,r,g,b)
            
    '''Funkcja rysuje wypelnione kolo. Przyjmuje wspolrzedne srodka, promien oraz kolor.'''             
    def circle(self,x,y,rad,r=1.0,g=0.0,b=0.0):

        r2 = rad ** 2

        for dx in range(0,rad):
            dx2 = dx ** 2
        
            for dy in range(0,dx + 1):
                dy2 = dy ** 2
            
                if (dx2 + dy2 <= r2):
                    self.data[x+dx,y+dy,0]=r
                    self.data[x+dx,y+dy,1]=g
                    self.data[x+dx,y+dy,2]=b
                
                    self.data[x-dx,y+dy,0]=r
                    self.data[x-dx,y+dy,1]=g
                    self.data[x-dx,y+dy,2]=b
                
                    self.data[x+dx,y-dy,0]=r
                    self.data[x+dx,y-dy,1]=g
                    self.data[x+dx,y-dy,2]=b
                
                    self.data[x-dx,y-dy,0]=r
                    self.data[x-dx,y-dy,1]=g
                    self.data[x-dx,y-dy,2]=b
                
                    self.data[x+dy,y+dx,0]=r
                    self.data[x+dy,y+dx,1]=g
                    self.data[x+dy,y+dx,2]=b
                
                    self.data[x-dy,y+dx,0]=r
                    self.data[x-dy,y+dx,1]=g
                    self.data[x-dy,y+dx,2]=b
                
                    self.data[x+dy,y-dx,0]=r
                    self.data[x+dy,y-dx,1]=g
                    self.data[x+dy,y-dx,2]=b
                
                    self.data[x-dy,y-dx,0]=r
                    self.data[x-dy,y-dx,1]=g
                    self.data[x-dy,y-dx,2]=b