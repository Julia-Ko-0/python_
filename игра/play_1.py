import pygame,os,wx
from random import randint
from sys import exit
from pygame.locals import *
pygame.init()

def main():
	# Получить размер экрана
	app=wx.App()
	WHFRAMES=wx.DisplaySize()
	WIDTH=int(WHFRAMES[0]*0.7)
	HEIGHT=int(WHFRAMES[1]*0.8)
	Timers = 0 # Игровой таймер
	TimersSec = 0 # второй
	tim_psd = 0
	# Получить размер экрана
	screen=pygame.display.set_mode((WIDTH,HEIGHT),0,32)
	caption=pygame.display.set_caption("Супер Марио")
	screen.fill([255,255,255])
	mariofont = pygame.font.Font('fonts/poster.ttf',22)
	mario_name = mariofont.render("MARIO",True,(84,65,190),None)
	#Game_world = mariofont.render("WORLD",True,(84,65,190),None)
	Game_moneyX = mariofont.render("X",True,(255,255,128),None)
	Game_time = mariofont.render("TIME",True,(84,65,190),None)

	money_ic5 = pygame.image.load('images/PTModelSprite_ID21675.png')
	money_ic5 = pygame.transform.scale(money_ic5, (25, 25))
	money_ic6 = pygame.image.load('images/PTModelSprite_ID21676.png')
	money_ic6 = pygame.transform.scale(money_ic6, (10, 25))
	money_ic7 = pygame.image.load('images/PTModelSprite_ID21677.png')
	money_ic7 = pygame.transform.scale(money_ic7, (25, 25))
	money_ic8 = pygame.image.load('images/PTModelSprite_ID21678.png')
	money_ic8 = pygame.transform.scale(money_ic8, (25, 25))
	money_timers = 0 # Картинка Таймер карусели
	
	Game_world = pygame.image.load('images/PTModelSprite_ID2478.png')

	background = pygame.image.load('images/PTModelSprite_ID35342.png').convert_alpha()
	background = pygame.transform.scale(background, (WIDTH, HEIGHT))

	Roads = pygame.image.load('images/PTModelSprite_ID3790.png').convert_alpha()
	Roads2 = pygame.image.load('images/PTModelSprite_ID4224.png').convert_alpha()
	
	hero = pygame.image.load('images/PTModelSprite_ID34297.png').convert_alpha()
	x,y = 15,HEIGHT-200
	inp_flag = -2    #(stop:-1 left drection ,-2 right drection) ,(walk:1 right drection ,2 left drection)
	times,times2 = 0,0  # Таймер действия персонажа
	move_values,jump_values,jump_values2,jump_values3 = 12,0,0,0  # Расстояние в один шаг и значение прыжка 1,2
	jump_adder,jump_max_point = 0,50 #Аккумулятор #Jump используется для суммирования длины клавиш, а затем определения высоты прыжка, наивысшей точки начального значения прыжка. 
	jump_flag = 0
	bg_w_1,bg_w_2 = 0,WIDTH-2 # Два обоев Переменные, которые циклически перетаскиваются одна за другой

	# Играть фон
	
	# Играть фон



	# Описание данных об игре
	score = 0
	money = 0
	world = 11
	time = 400
	Gdata = [score,money,world,time]
	# Описание данных об игре

	# Функция инициализации
	def game_initializaion(score,money,world,time,Gdata,TimersSec,Timers,x,y,inp_flag,times,times2,move_values,jump_values,jump_values2,jump_values3,jump_adder,jump_max_point,jump_flag,bg_w_1,bg_w_2,tim_psd):# Инициализация данных
		# Данные инициализации игры
		inp_flag = -2   #(stop:-1 left drection ,-2 right drection) ,(walk:1 right drection ,2 left drection)
		x,y = 15,HEIGHT-200 # Марио координаты
		times,times2 = 0,0  # Таймер действия персонажа
		move_values,jump_values,jump_values2,jump_values3 = 12,0,0,0  # Расстояние в один шаг и значение прыжка 1,2
		jump_adder,jump_max_point = 0,50 #Аккумулятор #Jump используется для суммирования длины клавиш, а затем определения высоты прыжка, наивысшей точки начального значения прыжка.
		jump_flag = 0
		tim_psd = 0
		bg_w_1,bg_w_2 = 0,WIDTH-2 # Два обоев Переменные, которые циклически перетаскиваются одна за другой
		Timers = 0  # Игровой таймер
		score = 0 	# Начать счет
		money = 0 	# Стартовые деньги
		world = 11 	# Мировой уровень Первый уровень 1–1 = 11
		time = 400	# Общее время игры
		TimersSec = 0 # Игра за секунды
		Gdata = [score,money,world,time]
		# Данные инициализации игры
		return score,money,world,time,Gdata,TimersSec,Timers,x,y,inp_flag,times,times2,move_values,jump_values,jump_values2,jump_values3,jump_adder,jump_max_point,jump_flag,bg_w_1,bg_w_2,tim_psd
	# Функция инициализации

	score,money,world,time,Gdata,TimersSec,Timers,x,y,inp_flag,times,times2,move_values,jump_values,jump_values2,jump_values3,jump_adder,jump_max_point,jump_flag,bg_w_1,bg_w_2,tim_psd = \
	game_initializaion(score,money,world,time,Gdata,TimersSec,Timers,x,y,inp_flag,times,times2,move_values,jump_values,jump_values2,jump_values3,jump_adder,jump_max_point,jump_flag,bg_w_1,bg_w_2,tim_psd)# Функция ключа инициализации данных

	clock = pygame.time.Clock()
	pygame.key.set_repeat(55)
	pygame.display.flip()

	def WalkAction(times,times2,inp_flag,hero):
		#walk action
		if y < HEIGHT -200: # Если в воздухе для прыжков картинки
			if inp_flag == 1: #right
				hero = pygame.image.load('images/PTModelSprite_ID34259.png').convert_alpha()
			if inp_flag == 2: #left
				hero = pygame.image.load('images/PTModelSprite_ID34259.png').convert_alpha()
				hero = pygame.transform.flip(hero, True, False)
		else:
			if inp_flag == 1: #right
				times += 2
				if times < 20:
					hero = pygame.image.load('images/PTModelSprite_ID34256.png').convert_alpha()
				elif times < 20:
					hero = pygame.image.load('images/PTModelSprite_ID34257..png').convert_alpha()
				elif times < 40:
					hero = pygame.image.load('images/PTModelSprite_ID34258.png').convert_alpha()	
				elif times < 60:
					hero = pygame.image.load('images/PTModelSprite_ID34259.png').convert_alpha()
				elif times < 80:
					hero = pygame.image.load('images/PTModelSprite_ID34260.png').convert_alpha()
				elif times < 100:
					hero = pygame.image.load('images/PTModelSprite_ID34261.png').convert_alpha()	
				elif times < 120:
					hero = pygame.image.load('images/PTModelSprite_ID34297.png').convert_alpha()
				elif times < 140:
					times = 0
			if inp_flag == 2: #left 
				times2 += 2
				if times2 < 20:
					hero = pygame.image.load('images/PTModelSprite_ID34256.png').convert_alpha()
					hero = pygame.transform.flip(hero, True, False)
				elif times2 < 20:
					hero = pygame.image.load('images/PTModelSprite_ID34257..png').convert_alpha()
					hero = pygame.transform.flip(hero, True, False)
				elif times2 < 40:
					hero = pygame.image.load('images/PTModelSprite_ID34258.png').convert_alpha()	
					hero = pygame.transform.flip(hero, True, False)
				elif times2 < 60:
					hero = pygame.image.load('images/PTModelSprite_ID34259.png').convert_alpha()
					hero = pygame.transform.flip(hero, True, False)
				elif times2 < 80:
					hero = pygame.image.load('images/PTModelSprite_ID34260.png').convert_alpha()
					hero = pygame.transform.flip(hero, True, False)
				elif times2 < 100:
					hero = pygame.image.load('images/PTModelSprite_ID34261.png').convert_alpha()	
					hero = pygame.transform.flip(hero, True, False)
				elif times2 < 120:
					hero = pygame.image.load('images/PTModelSprite_ID34297.png').convert_alpha()
					hero = pygame.transform.flip(hero, True, False)
				elif times2 < 140:
					times2 = 0
			elif inp_flag == -1:
				hero = pygame.image.load('images/PTModelSprite_ID34297.png').convert_alpha()
				hero = pygame.transform.flip(hero, True, False)	
				times2 = 0
			elif inp_flag == -2:
				hero = pygame.image.load('images/PTModelSprite_ID34297.png').convert_alpha()
				times2 = 0

		return times,times2,inp_flag,hero


	def HeroHeightIs(): # Определить, находится ли персонаж на земле по оси Y
		if y >= HEIGHT-200:
			return False
		else:	# Это под контролем
			return True 


	def Reset_max_point(jump_max_point):	# Сбросить наивысшую точку стандартного прыжка на землю (восстановить)
		if y >= (HEIGHT-200):
			jump_max_point = 50 # Наивысшая точка по умолчанию - 50 
		return jump_max_point



	def jump_leftScreenBgnotMove(x): 
		if x<(WIDTH/4):
			if jump_max_point == 50 :
					if inp_flag == 1:
						x+=(2.7)
					if inp_flag == 2:
						x-=(2.7)
			elif jump_max_point == 100 :
					if inp_flag == 1:
						x+=(0.27)
					if inp_flag == 2:
						x-=(0.27)
		return x

	def Screen_MoneyIc(screen,money_ic5,money_ic6,money_ic7,money_ic8,money_timers) : # Нарисуйте второй предмет Значок денег

		money_timers += 1
		if money_timers < 15 :
			screen.blit(money_ic5,(WIDTH*0.24,25)) # Нарисуйте второй предмет Money icon 1
		elif money_timers < 40 :
			screen.blit(money_ic6,(WIDTH*0.24+7.5,25)) # Нарисуйте второй предмет Money icon 2
		elif money_timers < 55 :
			screen.blit(money_ic7,(WIDTH*0.24,25)) # Нарисуйте второй предмет Money icon 3
		elif money_timers < 80 :
			screen.blit(money_ic8,(WIDTH*0.24,25)) # Нарисуйте второй предмет Money icon 4
		else:
			money_timers = 0
		return screen,money_ic5,money_ic6,money_ic7,money_ic8,money_timers


	def  Game_Timers(TimersSec,Gdata,time_passed,tim_psd) : # Игровой таймер

		tim_psd += time_passed
		if tim_psd >= 1000 : # На 1 секунду
			TimersSec += 1 
			tim_psd = 0
		Gdata[3] = 400 - TimersSec # Игровое время осталось
		
		return TimersSec,Gdata,time_passed,tim_psd


	while True: 
		
		# Обнаружение событий  
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: 
				exit()

			if event.type == KEYDOWN:
				keys=pygame.key.get_pressed()
				if keys[pygame.K_a]:
						if event.key == K_w and inp_flag == 0:
							if y <= HEIGHT-200:  # Посмотрите на координату y, которая должна быть в начальной точке
								jump_flag = 3 # Нажал вверх и вперед
						if y >= HEIGHT-200:# Если персонаж идет по ровной поверхности, вернитесь назад и влево
							#if bg_w_1==0:
								#x-=5
							x-=(move_values+3.5)
							inp_flag = 2
					
				if keys[pygame.K_d]:
						if event.key == K_w and inp_flag == 0:
							if y <= HEIGHT-200:  # Посмотрите на координату y, которая должна быть в начальной точке
								jump_flag = 2 # Нажал вверх и вперед
						if y >= HEIGHT-200:# Если персонаж идет по ровной поверхности, передний план справа
							if x<(WIDTH/4): # Роль по-прежнему находится в левой части экрана, подвижная
								x+=(move_values+3.5)
							inp_flag = 1
					
				if keys[pygame.K_w]: #jump
						jump_flag = 1 # Просто нажал, чтобы прыгнуть
						jump_adder += 1 # Перейти аккумулятор
						if event.key == pygame.K_d and (jump_flag == 1):
							if y == HEIGHT-200:  # Посмотрите на координату y, которая должна быть в начальной точке
								jump_flag = 2 # Нажал вверх и вперед
						if event.key == pygame.K_a and (jump_flag == 1):
							if y == HEIGHT-200:  # Посмотрите на координату y, которая должна быть в начальной точке
								jump_flag = 3 # Нажал вверх и назад

				if keys[pygame.K_p]: #Рестарт
					score,money,world,time,Gdata,TimersSec,Timers,x,y,inp_flag,times,times2,move_values,\
					jump_values,jump_values2,jump_values3,jump_adder,jump_max_point,jump_flag,bg_w_1,bg_w_2,tim_psd = \
					game_initializaion(score,money,world,time,Gdata,TimersSec,Timers,x,y,inp_flag,times,times2,\
					move_values,jump_values,jump_values2,jump_values3,jump_adder,jump_max_point,jump_flag,bg_w_1,\
					bg_w_2,tim_psd)
						

			if event.type == KEYUP:
				if keys[pygame.K_a]:
					inp_flag = -1
				if keys[pygame.K_d]:
					inp_flag = -2
				if keys[pygame.K_w]:
					if jump_adder < 4 : # Если отпускание кнопки не доходит до значения jump_adder jump аккумулятор (тогда установите их в ноль)
						jump_adder = 0

		## На земле сбросить наивысшую точку прыжка по умолчанию (восстановить)
		jump_max_point = Reset_max_point(jump_max_point)

		#jump action 1
		if jump_flag == 1: # Только прыгать
			# Пусть в другую сторону прыгнет значение 0
			jump_values2 = 0
			jump_values3 = 0
			#------
			# Непрерывная структура перехода клавиш
			if jump_adder >=4 :
				jump_max_point = 100	# Второй прыжок максимум
				jump_adder = 0
			#------
			jump_values+=1.25
			if jump_values <= jump_max_point:
				y -= 5

				x = jump_leftScreenBgnotMove(x)

				if jump_max_point == 100:# Высота прыжка другая, скорость по координате y тоже должна быть меньше
					y += 1.5
					x = jump_leftScreenBgnotMove(x)

			elif jump_values <= jump_max_point+8:
				pass
			elif jump_values <=jump_max_point*2+8:
				if HeroHeightIs(): # Если персонаж находится под контролем, продолжаем добавлять значение оси Y 1
					y += 5
					
					x = jump_leftScreenBgnotMove(x)

					if jump_max_point == 100:# Высота прыжка другая, скорость по координате y тоже должна быть меньше
						y -= 1.5
						x = jump_leftScreenBgnotMove(x)

			else:
				y = HEIGHT-200
				jump_flag = 0
				jump_values = 0

	
		#wall detection
		if x<=0:
			x=0
		if x+hero.get_width()>WIDTH:
			x=WIDTH-hero.get_width()
			

		# Функция действия роли	
		times,times2,inp_flag,hero = WalkAction(times,times2,inp_flag,hero)

		#1 .bg move---blit
		screen.blit(background,(bg_w_2,0))
		screen.blit(background,(bg_w_1,0))

		# Информация для рисования
		
		screen.blit(mario_name,(WIDTH*0.03,3))# Нарисуйте имя первого предмета

		screen,money_ic5,money_ic6,money_ic7,money_ic8,money_timers = \
		Screen_MoneyIc(screen,money_ic5,money_ic6,money_ic7,money_ic8,money_timers) # Нарисуйте второй предмет Значок денег

		screen.blit(Game_moneyX,(WIDTH*0.28,24))# Нарисуйте второй предмет x
		screen.blit(Game_world,(WIDTH*0.5-Game_world.get_width()/2,3))# Нарисуйте третий предмет Карта мира
		screen.blit(Game_time,(WIDTH*0.84,3))# Нарисуй четвертый предмет Игровое время

		for DATAi in range(4):
			Game_data = mariofont.render("%s"% Gdata[DATAi],True,(255,255,128),None) # Всесторонний рисунок: набери золотую монету, время игры
			if DATAi != 2:
				screen.blit(Game_data,(WIDTH*(0.03+DATAi*0.27),24))
			elif DATAi == 2:
				Game_data = mariofont.render("%s-%s"% (Gdata[DATAi]/10,Gdata[DATAi]%10),True,(255,255,128),None) # Всесторонний рисунок: набери золотую монету, время игры
				screen.blit(Game_data,(WIDTH*0.5-Game_data.get_width()/2,15))
		
		# Информация для рисования

		#2 .bg move--panel
		#if inp_flag == 2: # Идите влево и перетащите обои вправо
		#	bg_w_1+=move_values/4
		#	bg_w_2+=move_values/4
		if inp_flag == 1 and x>=(WIDTH/4):# Иди вправо, перетащи обои влево
			bg_w_1-=(move_values/4-0.5)
			bg_w_2-=(move_values/4-0.5)

		if bg_w_1>=0:
			bg_w_1,bg_w_2 = 0,WIDTH-2
		if bg_w_1<-WIDTH:
			bg_w_1,bg_w_2 = 0,WIDTH-2

		screen.blit(hero,(x,y))
		pygame.time.delay(2) # миллисекунда

		time_passed = clock.tick()
		TimersSec,Gdata,time_passed,tim_psd = Game_Timers(TimersSec,Gdata,time_passed,tim_psd) # Время игры
		
		pygame.display.update()
		
if __name__ == '__main__':
	main()