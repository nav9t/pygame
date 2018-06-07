import pygame,sys,random,time
initial = pygame.init()

if initial[1]>0:
	print('erros {0}'.format(initial[1]))
else:
	scaleX = float(input("1 unit on x axis"))
	scaleY = float(input("1 unit on y  axis"))
	a = float(input('enter the coefficient of x2'))
	b = float(input('enter the coefficient of x'))
	con = float(input('enter the constant'))
	display_width = 800
	display_height = 600
	gameDisplay = pygame.display.set_mode((display_width,display_height))
	gameDisplay.fill((0,0,0))
	pixAr = pygame.PixelArray(gameDisplay)
	
#function
	def message_display(data,x,y):
		largeText = pygame.font.SysFont('segoe script',14)
		text_Surf = largeText.render("{0}".format(data),True,(0,255,0))
		gameDisplay.blit(text_Surf,(x,y))
		pygame.display.flip()
	#defining graph
	pygame.draw.line(gameDisplay,(255,255,255),(0,display_height/2),(display_width,display_height/2),2);
	pygame.draw.line(gameDisplay,(255,255,255),(display_width/2,0),(display_width/2,display_height),2);
	x=0
	y=0
	while x<display_width:
		pygame.draw.rect(gameDisplay,(0,255,0),((x-2),int(display_height/2)-3,4,6))
		data = -8*scaleX
		#message_display(data,x,int(display_height/2)+5)
		x+=50
	while y<display_height:
		pygame.draw.rect(gameDisplay,(0,255,0),(int(display_width/2)-2,y-2,6,4))
		y+=50

	x=0
	c=-8*scaleX
	while x<800:
		y = a*c*c + b*c +con
		y= ((display_height/2) - (50*y)/scaleY)
		if y>0 and y<display_height:
			pixAr[int(x)][int(y)] = (100,100,100)
		c += scaleX/50.0
		x=x+1
	#defining numbers
	del pixAr
	x=0
	y=0
	c=-8
	while x<display_width:
		data = c*scaleX
		message_display(data,x-2,int(display_height/2)+10)
		c=c+1
		x+=50
	c=-6
	while y<display_height:
		data = c*scaleY
		message_display(data,int(display_width/2)-40,y)
		c=c+1
		y+=50

	#defining game loop
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		pygame.display.update();



	pygame.quit()
	sys.exit()

