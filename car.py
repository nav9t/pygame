import pygame,sys,time,random

##################checks for errors#########################
error_check = pygame.init()
if error_check[1]>0:
	print("can't initiate {0}, errors found".format(error_check[1]))
	sys.exit()
else:
	print("{0} process initiated successfully...".format(error_check[0]))

############################a general initiation concept####################

display_width= 800
display_height =600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('pygame module')
clock = pygame.time.Clock()

#######defining car #############
carImg = pygame.image.load('Car.png')
carImg1 = pygame.image.load('b.png')

####################defining color################################

black= pygame.Color(0,0,0)
white =pygame.Color(255,255,255)


#####defining car########
def score_display(score):
	 font = pygame.font.SysFont('segoe print',24);
	 surf = font.render('score : {0}'.format(score),True,white)
	 gameDisplay.blit(surf,(0,0))
	 pygame.display.update()


def object(color,x,y,size_x,size_y):
	pygame.draw.rect(gameDisplay,color,[x,y,size_x,size_y])
def car(x,y,carImg):
	gameDisplay.blit(carImg,(x,y))
#####defining game loop###

def crash():
	message_display('You Crashed')

def exit_game():
	pygame.quit()
	sys.exit()
def message_display(text):
	largeText = pygame.font.SysFont('segoe script',55)
	text_Surf = largeText.render(text,True,white)
	textRect = text_Surf.get_rect();
	textRect.midtop= ((display_width/2),(display_height/2))
	gameDisplay.blit(text_Surf,textRect)
	pygame.display.flip()
	time.sleep(2)
	game_loop()
###########defining buttons#################
def buttons(text,x,y,w,h,ac,ic,fun):
	pos = pygame.mouse.get_pos()
	click  = pygame.mouse.get_pressed()
	if x<pos[0]<x+w and y<pos[1]<y+h:
		pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
		if click[0]==1:
			fun()
	else:
		pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
	medium_text = pygame.font.SysFont("segoe script",18)
	surf = medium_text.render(text,True,white)
	rect = surf.get_rect()
	rect.center = (x+w/2,y+h/2)
	gameDisplay.blit(surf,rect)

###############defining the initial loop##############

def initial_loop():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit();
				exit();
		largeText = pygame.font.SysFont('segoe script',55)
		text_Surf = largeText.render("welcome",True,white)
		textRect = text_Surf.get_rect();
		textRect.center= ((display_width/2),(display_height/2))
		gameDisplay.blit(text_Surf,textRect)
		buttons("start",200,400,80,50,(0,200,0),(0,255,0),game_loop)
		buttons("exit",520,400,80,50,(200,0,0),(255,0,0),exit_game)

		pygame.display.update()

	##################loop for the main game#####################
def game_loop():
	object_startx = random.randrange(0,display_width-100)
	object_starty  = display_height+ 500
	y_increament = -6
	object_sizex = 80
	object_sizey = 161
	score = 0;

	gameExit=False
	x = (display_width * 0.40)
	y = (display_height*.1)
	x_change = 0
	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT or event.key == ord('a'):
					x_change = -5
				if event.key == pygame.K_RIGHT or event.key == ord('d'):
					x_change = 5
			if event.type == pygame.KEYUP:
					x_change = 0
		x=x+x_change
		gameDisplay.fill(black)
		car(object_startx,object_starty,carImg1)
		object_starty+=y_increament
		if(object_starty<0+y_increament):
			score+=1
			y_increament-=1
			object_starty = display_height
			object_startx = random.randrange(0,display_width-object_sizex)
		car(x,y,carImg)
		if x>=display_width-100 or x<=0:
			crash()
		if (y<object_starty+object_sizey and y+object_sizey>object_starty+object_sizey) or (y<object_starty and y+object_sizey>object_starty):
			if (x<object_startx+object_sizex and x+object_sizex>object_startx+object_sizex) or (x<object_startx and x+object_sizex>object_startx):
				crash()
		score_display(score)
		pygame.display.update()
		clock.tick(20)
initial_loop()
pygame.quit()
sys.exit()






