import random
import vektory
import numpy as np


x = vektory.collect_color_elements()
def dobierzkolor(allreults,cycle):
    tablica = allreults
    red,green,blue =0,0,0 
    for i in range(cycle):
        vi = tablica[i]
        print (f"v{i+1}:", vi)
        dlugosc = np.linalg.norm(vi)
        #print(f"dlugosc v{i+1}:", dlugosc)
        red += int(vi[0])
        green += int(vi[1])
        blue += int(vi[2])
    return red,green,blue
#print (len(x))
y= dobierzkolor(x, len(x))
red, green, blue = zip(y)

red = abs(int(red[0]) * 20)
green = abs(int(green[0]) * 20)
blue = abs(int(blue[0]) * 20)

print(red, green, blue)
print(f"\033[38;2;{red};{green};{blue}m■ THIS TEXT IS RANDOMLY COLORED! \033[0m")
