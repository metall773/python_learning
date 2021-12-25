import graphics as gr

window = gr.GraphWin("Jenkslex and Ganzz project", 900, 600)

def draw_background():
    land = gr.Rectangle(gr.Point(0,350), gr.Point(900,600))
    land.setFill('darkgray')
    land.draw(window)
    sky = gr.Rectangle(gr.Point(0,0), gr.Point(900,349))
    sky.setFill('blue')
    sky.draw(window)
    
def draw_house():
    house = gr.Rectangle(gr.Point(200,250), gr.Point(400,450))
    house.setFill('gray')
    house.draw(window)
    
    roof = gr.Polygon(gr.Point(200,250), gr.Point(400,250),  gr.Point(300,150))
    roof.setFill('red3')
    roof.draw(window)
    
    windows = gr.Rectangle(gr.Point(250,300), gr.Point(350,400))
    windows.setFill('yellow')
    
    windows2 = gr.Line(gr.Point(250,350), gr.Point(350,350))
    windows3 = gr.Line(gr.Point(300,300), gr.Point(300,400))
    windows.draw(window)
    windows2.draw(window)
    windows3.draw(window)

def draw_sun(): 
    sun = gr.Circle(gr.Point(650, 90), 70)
    sun.setFill('yellow')
    sun.draw(window)

def draw_clouds(x, y, radius):
    cloud1 = gr.Circle(gr.Point(x, y), radius)
    cloud1.setFill('darkgray')
    cloud2 = gr.Circle(gr.Point(x+30, y), radius)
    cloud2.setFill('darkgray')
    cloud3 = gr.Circle(gr.Point(x+70, y+20), radius)
    cloud3.setFill('darkgray')
    cloud4 = gr.Circle(gr.Point(x+30, y+30), radius)
    cloud4.setFill('darkgray')
    cloud5 = gr.Circle(gr.Point(x-15, y+30), radius)
    cloud5.setFill('darkgray')
    cloud6 = gr.Circle(gr.Point(x-50, y+30), radius)
    cloud6.setFill('darkgray')
    cloud1.draw(window)
    cloud2.draw(window)
    cloud3.draw(window)
    cloud4.draw(window)
    cloud5.draw(window)
    cloud6.draw(window)
    
def draw_tree():
    tree1 = gr.Rectangle(gr.Point(680,550), gr.Point(700,500))
    tree1.setFill('red4')
    tree2 = gr.Polygon(gr.Point(515,500), gr.Point(875,500),  gr.Point(690,370))
    tree2.setFill('green')
    tree3 = gr.Polygon(gr.Point(550,450), gr.Point(840,450),  gr.Point(690,350))
    tree3.setFill('green')
    tree4 = gr.Polygon(gr.Point(585,400), gr.Point(805,400),  gr.Point(690,300))
    tree4.setFill('green')
    tree5 = gr.Polygon(gr.Point(615,340), gr.Point(765,340), gr.Point(690,260))
    tree5.setFill('green')
    tree6 = gr.Polygon(gr.Point(680,265), gr.Point(690,240), gr.Point(700,265))
    tree6.setFill('red')
    tree1.draw(window)
    tree2.draw(window)
    tree3.draw(window)
    tree4.draw(window)
    tree5.draw(window)
    tree6.draw(window)

def draw_all():
    draw_background()
    draw_sun()
    draw_clouds(150, 100, 50)
    draw_clouds(550, 120, 30)
    draw_clouds(750, 100, 40)
    draw_house()
    draw_tree()

draw_all()

window.getMouse()

window.close()