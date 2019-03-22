from graphics import graphics
import random

def main():
    gui = graphics(400, 650, 'Rilakkuma')
    i = 0
    while True:
        gui.clear()
        gui.rectangle(0, 0, 400, 650, 'gray12')
        gui.ellipse(70, 400, 220, 200, 'orange')
        gui.ellipse(30, 400, 200, 130, 'yellow')
        gui.ellipse(330, 400, 220, 200, 'orange')
        gui.ellipse(370, 400, 200, 130, 'yellow')
        gui.ellipse(200, 600, 600, 500, 'orange')
        gui.ellipse(200, 600, 600, 500, 'orange')
        gui.ellipse(200, 620, 180, 150, 'white')
        gui.ellipse(200, 600, 40, 40, 'black')
        gui.line(200, 615, 160, 640, 'black', 8)
        gui.line(200, 615, 240, 640, 'black', 8)
        if i <= 30:
            gui.ellipse(70, 550, 45, 15+i, 'black')
            gui.ellipse(330, 550, 45, 15+i, 'black')
        else:
            gui.ellipse(70, 550, 45, 45-(i-30), 'black')
            gui.ellipse(330, 550, 45, 45-(i-30), 'black')
        i = i%60
        i += 10
        gui.update_frame(2)

main()

