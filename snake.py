# Snake Game
#our game imports
import pygame, sys, random, time


# returns (success,faliure)//in numbers
check_errors = pygame.init()
if check_errors[1]>0:
	print("(!) Had {0} initializing errors ,exiting.....".format(check_errors[1]))
	sys.exit(-1)
else:
	print("(+)Pygame successfully initialized!")


#play surface
playSurface = pygame.display.set_mode((720,460))
pygame.display.set_caption('BubbunS')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
#music 
game_music = pygame.mixer.music.load("music.mp3")
game_sound = pygame.mixer.Sound('beep-3.wav')
game_end = pygame.mixer.Sound('end.wav')
#Colors
red   = pygame.Color(187, 10, 30)#gameover
green = pygame.Color(61,216,44)#snake
black = pygame.Color(47,79,79)#score
white = pygame.Color(255,255,255)#background
brown = pygame.Color(165,42,42)#food
#Frames per second
fpsController = pygame.time.Clock()

#Important variables

def button_create(text,x,y,w,h,ac,ic,txtclr,funct):
	loc = pygame.mouse.get_pos()
	press = pygame.mouse.get_pressed()
	if x<loc[0]<x+w and y<loc[1]<y+h:
		pygame.draw.rect(playSurface,ac,(x,y,w,h))
		if press[0]==1:
			funct()
	else:
		pygame.draw.rect(playSurface,ic,(x,y,w,h))
	font = pygame.font.SysFont("impact",18)
	syst = font.render(text,True,txtclr)
	rect = syst.get_rect()
	rect.center=(x+w/2,y+h/2)
	playSurface.blit(syst,rect)

def exit():
	pygame.quit()
	sys.exit()

def showScore(choice,score):
	myFont = pygame.font.SysFont('Segoe Script',24)
	GOsurf = myFont.render('Score  :{0}'.format(score),True,black)
	GOrect = GOsurf.get_rect()
	if choice==1:
		GOrect.midtop =(80,10)
	else:
		GOrect.midtop =(360,120)
	playSurface.blit(GOsurf,GOrect)
	pygame.display.flip()
	

#Game Over Function
def gameOver(score):
	pygame.mixer.music.stop()
	pygame.mixer.Sound.play(game_end)
	myFont = pygame.font.SysFont('Segoe Script',72)
	GOsurf = myFont.render('Game Over!',True,red)
	GOrect = GOsurf.get_rect()
	GOrect.midtop =(360,15)
	playSurface.blit(GOsurf,GOrect)
	pygame.display.flip()
	showScore(2,score)
	time.sleep(2)
	game_initial()
	

####defining initial interface
def game_initial():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		playSurface.fill((0,0,0))
		logo=pygame.image.load('back.png')
		playSurface.blit(logo,(280,0))
		font = pygame.font.SysFont("segoe script",66)
		syst = font.render("sNaKeMaNiAc",True,(200,0,0))
		rect = syst.get_rect()
		rect.center=(360,460/2)
		playSurface.blit(syst,rect)
		button_create("play",100,400,80,50,(0,255,0),(0,200,0),(200,0,0),game_loop)
		button_create("quit",540,400,80,50,(255,0,0),(200,0,0),(0,200,0),exit)
		pygame.display.update()
		# time.sleep(2)
		# game_loop()
# Main logic of the game
def game_loop():
	pygame.mixer.music.play(-1)
	snakePos = [100,50]
	snakeBody =[[100,50],[90,50],[80,50]]
	foodPos = [random.randrange(1,69)*10,random.randrange(1,43)*10]
	foodSpawn = True
	direction = "RIGHT"
	changeto = direction
	score = 0
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT or event.key ==ord('d'):
					changeto = 'RIGHT'
				if event.key == pygame.K_LEFT or event.key ==ord('a'):
					changeto = 'LEFT'
				if event.key == pygame.K_UP or event.key ==ord('w'):
					changeto = 'UP'
				if event.key == pygame.K_DOWN or event.key ==ord('s'):
					changeto = 'DOWN'
				if event.key == pygame.K_ESCAPE :
					pygame.event.post(pygame.event.Event(QUIT))

	# validation of direction
		if changeto=="RIGHT" and not direction =='LEFT':
			direction='RIGHT'
		if changeto=="LEFT" and not direction =='RIGHT':
			direction='LEFT'
		if changeto=="UP" and not direction =='DOWN':
			direction='UP'
		if changeto=="DOWN" and not direction =='UP':
			direction='DOWN'
				#value updation with direction
		if direction == 'RIGHT':
			snakePos[0]+=10
		if direction == 'LEFT':
			snakePos[0]-=10
		if direction == 'UP':
			snakePos[1]-=10
		if direction == 'DOWN':
			snakePos[1]+=10
		#snake body mechanism
		snakeBody.insert(0,list(snakePos))
		if snakePos[0]==foodPos[0] and  snakePos[1]==foodPos[1]:
			pygame.mixer.Sound.play(game_sound)
			foodSpawn=False
			score+=1
		else:
			snakeBody.pop()
		if foodSpawn==False:
			foodPos = [random.randrange(1,69)*10,random.randrange(1,43)*10]
			foodSpawn=True
			#background
		playSurface.fill(white)
		pygame.draw.rect(playSurface,brown,pygame.Rect(0,0,720,10))
		pygame.draw.rect(playSurface,brown,pygame.Rect(0,450,720,10))
		pygame.draw.rect(playSurface,brown,pygame.Rect(0,0,10,460))
		pygame.draw.rect(playSurface,brown,pygame.Rect(710,0,10,460))



		#deaw snake
		for pos in snakeBody:
			pygame.draw.rect(playSurface,green,pygame.Rect(pos[0],pos[1],10,10))
		#draw food
		pygame.draw.rect(playSurface,brown,pygame.Rect(foodPos[0],foodPos[1],10,10))
		#snakePos
		if snakePos[0]>=702 or snakePos[0]<=9:
			gameOver(score)
		if snakePos[1] >=441 or snakePos[1]<=9:
			gameOver(score)
		for block in snakeBody[1:]:
			if  snakePos[0]==block[0] and snakePos[1]==block[1]:
				gameOver(score)

		#display speed
		pygame.display.flip()
		showScore(1,score)
		if len(snakeBody)>=3 and len(snakeBody)<10:
			fpsController.tick(8)
		elif len(snakeBody)>=10 and len(snakeBody)<15:
			fpsController.tick(10)
		elif len(snakeBody)>=15 and len(snakeBody)<20:
			fpsController.tick(12)
		elif len(snakeBody)>=20 and len(snakeBody)<25:
			fpsController.tick(14)
		elif len(snakeBody)>=25 and len(snakeBody)<30:
			fpsController.tick(16)
		else:
			fpsController.tick(18)

game_initial()
pygame.quit()
sys.exit()








