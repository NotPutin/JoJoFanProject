import pygame 
pygame.init()

W=500
H=500

x=100
y=100

x1=500
y1=500
x2=1
y2=1
xx=25
yy=6
sc=pygame.display.set_mode((W, H))
def move():
    global xx
    xx += 1
    if xx == 500:
        xx -= 400
    
        
    
#def draw():
    #sc.fill ((100,120,50))
    #pygame.draw.rect(sc,((0,45,100)),(x,y,100,130))
    #pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    sc.fill ((100,120,50))
    pygame.draw.rect(sc,((0, 45, 100)),(x,y,100,130))
    pygame.draw.circle(sc,(120,200,0),(xx,yy), 5)
    pygame.draw.line(sc, ((6,0,50)),  (500,0), (0,500),10)
    pygame.draw.line(sc,((6,0,50)),  (x1,y1),(x2, y2),10)
    pygame.display.update()

    move()

