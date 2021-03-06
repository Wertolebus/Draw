import pygame as pg
from os import system as sys
import os
import datetime
import ctypes
import pygame_widgets
from pygame_widgets.slider import Slider


pg.init()

HEIGHT = 1280											# SCREEN HEIGHT
WIDTH = 880												# SCREEN WIDTH

white = (249, 255, 199)									# not totally a white
black = (0, 0, 0) 										# okay its really black

mouse = pg.mouse.get_pos()								# get mouse pos for idk

screen = pg.display.set_mode((HEIGHT, WIDTH))			# toggle window

pg.display.set_caption("Draw!")							# set caption

screen.fill(white)										# fill screen with not totally a white

FPS = 999999999999										# I DONT KNOW ALRIGHT

size = 10 												# brush size

size_font = pg.font.SysFont("consolas", 30)				# size font/text set

mode_font = pg.font.SysFont("consolas", 30)				# NOT USING (OLDER)

rgb_font = pg.font.SysFont("consolas", 20)				# rgb text font

# -- Sliders
Rslider = Slider(screen, 170, 780, 255, 15, min=0, max=255, step=1, colour=(255, 0, 0), initial = 0, curved = False)
Gslider = Slider(screen, 170, 810, 255, 15, min=0, max=255, step=1, colour=(0, 255, 0), initial = 0, curved = False)
Bslider = Slider(screen, 170, 840, 255, 15, min=0, max=255, step=1, colour=(0, 0, 255), initial = 0, curved = False)
# -- end of sliders
mode = 1 												# Brush mode

def help_win():											# help window
		MessageBox = ctypes.windll.user32.MessageBoxW
		MessageBox(None, 'F1 - Show this window\nF2 - take screenshot (in /Pictures folder)\n1 or Pencil button - set pencil mode\n2 or Eraser button - set eraser mode\nmwheelup/down - resize brush\nbackspace - erase all', 'Help window', 0)

help_win()												# call help window

while True:

	colorR = Rslider.getValue()							# get value from RedSlider
	colorG = Gslider.getValue()							# get value from GreenSlider
	colorB = Bslider.getValue()							# get value from BlueSlider


	color = (colorR, colorG, colorB)					# set brush color

	#print(colorR, colorG, colorB)						# DEBUG DONT WATCH ON THIS

	now = datetime.datetime.now()						# take time
	screenshot_time = now.strftime("%Y-%m-%d---%H-%M-%S")# screenshot name obviously

	# -- brush color text things
	brush_color = rgb_font.render("Brush color", True, black, (255,255,255))
	brush_colorRect = brush_color.get_rect()
	brush_colorRect.center = (500, 770)
	# -- end of brush color things

	# -- size things
	size_text = size_font.render(f"Size: {size}", True, black, (255, 255, 255))
	size_rect = size_text.get_rect()
	size_rect.center = (900, 98)
	# -- end of bruh size things


	# -- rgb text okay?
	cR_text = rgb_font.render(f"R: {colorR}", True, black, (255, 255, 255))
	cR_textRect = cR_text.get_rect()
	cR_textRect.center = (110, 785)

	cG_text = rgb_font.render(f"G: {colorG}", True, black, (255, 255, 255))
	cG_textRect = cG_text.get_rect()
	cG_textRect.center = (110, 815)

	cB_text = rgb_font.render(f"B: {colorB}", True, black, (255, 255, 255))
	cB_textRect = cB_text.get_rect()
	cB_textRect.center = (110, 845)
	# -- end of rgb

	def draw():											# idk its just a draw func
		
		mouse_x, mouse_y = pg.mouse.get_pos()
		if mouse_x < 1280 and mouse_y > 200 and mouse_y < 750:
			if mode == 1:
				brush = pg.draw.circle(screen, color, (mouse_x, mouse_y), size)
			if mode == 2:
				brush = pg.draw.circle(screen, white, (mouse_x, mouse_y), size)
	def info_panel():									# info panel settings
		screen.fill((255, 255, 255), (0, 0, 1280, 200))
		screen.fill(black, (0, 195, 1280, 5))
		screen.blit(size_text, size_rect)
		size_brush = pg.draw.circle(screen, black, (1150, 98), size)
		# screen.blit(mode_text, mode_textRect)

	def create_screenshot():							# screenshots baby
		screenshot_rect = pg.Rect(0, 200, HEIGHT, 680)
		screenshot_surface = screen.subsurface(screenshot_rect)
		screenshot = pg.Surface((HEIGHT, 545))
		screenshot.blit(screenshot_surface, (0, 0))
		userprofile = os.environ['USERPROFILE']
		
		screenshot_path = f"{userprofile}\\Pictures\\Draw! Saves"
		isExist = os.path.exists(screenshot_path)

		try:

			os.makedirs(screenshot_path)
			pg.image.save(screenshot, f"{userprofile}\\Pictures\\Draw! Saves\\{screenshot_time}.jpg")
		
		except FileExistsError:
			
			pg.image.save(screenshot, f"{userprofile}\\Pictures\\Draw! Saves\\{screenshot_time}.jpg")

	def color_panel():									# color panel settings
		
		screen.fill((255, 255, 255), (0, 750, 1280, 880))
		screen.fill(black, (0, 745, 1280, 5))
		screen.fill(black, (445, 790, 110, 85))
		screen.fill(color, (450, 795, 100, 75))
		
		screen.blit(cR_text, cR_textRect)
		screen.blit(cG_text, cG_textRect)
		screen.blit(cB_text, cB_textRect)

		screen.blit(brush_color, brush_colorRect)

	def buttons():										# pencil/eraser buttons setting
		pencil_button_x = 25
		pencil_button_y = 25
		
		eraser_button_x = 200
		eraser_button_y = 25


		pencil_button_outline = pg.draw.rect(screen, black, pg.Rect(pencil_button_x, pencil_button_y, 125, 125))
		pencil_button = pg.draw.rect(screen, (255, 255, 255), pg.Rect(pencil_button_x+5, pencil_button_y+5, 115, 115))

		eraser_button_outline = pg.draw.rect(screen, black, pg.Rect(eraser_button_x, eraser_button_y, 125, 125))
		eraser_button = pg.draw.rect(screen, (255,255,255), pg.Rect(eraser_button_x+5, eraser_button_y+5, 115, 115))


		pencil_button_text = mode_font.render("Pencil", True, black, (255, 255 ,255))
		pencil_button_rect = pencil_button_text.get_rect()
		pencil_button_rect.center = (86, 90)

		eraser_button_text = mode_font.render("Eraser", True, black, (255, 255 ,255))
		eraser_button_rect = eraser_button_text.get_rect()
		eraser_button_rect.center = (263, 90)

		if mode == 1:
			pencil_button = pg.draw.rect(screen, black, pg.Rect(pencil_button_x+5, pencil_button_y+5, 115, 115))
			pencil_button_text = mode_font.render("Pencil", True, (255, 255, 255), black)

		if mode == 2:
			eraser_button = pg.draw.rect(screen, black, pg.Rect(eraser_button_x+5, eraser_button_y+5, 115, 115))
			eraser_button_text = mode_font.render("Eraser", True, (255, 255 ,255), black)

		screen.blit(pencil_button_text, pencil_button_rect)
		screen.blit(eraser_button_text, eraser_button_rect)


	# -- absolutely nothing interesting here
	ev = pg.event.get()

	for event in ev:

		if event.type == pg.QUIT:
			pg.quit()
			quit()

		if pg.mouse.get_pressed()[0]==True:
			draw()

		if event.type == pg.MOUSEBUTTONDOWN:
			if event.button == 4:
				if size < 95:
					size+=1
			if event.button == 5:
				if size > 1:
					size-=1
			if event.button == 1: # PENCIL BUTTON
				mouse_x, mouse_y = pg.mouse.get_pos()
				if mouse_x > 30 and mouse_x < 150 and mouse_y > 25 and mouse_y < 150 :
					# print("pencil")
					mode = 1

			if event.button == 1: # ERASER BUTTON
				mouse_x, mouse_y = pg.mouse.get_pos()
				if mouse_x > 200 and mouse_x < 325 and mouse_y > 25 and mouse_y < 150 :
					# print("eraser")
					mode = 2


		if event.type == pg.KEYDOWN:
			if event.key == pg.K_1:
				color = black
				mode = 1
			if event.key == pg.K_2:
				color = white
				mode = 2
			if event.key == pg.K_BACKSPACE:
				screen.fill(white, rect = (0, 100, HEIGHT, 668))

			if event.key == pg.K_F2:
				create_screenshot()

			if event.key == pg.K_F1:
				help_win()
							
	pygame_widgets.update(event)

	pg.display.update()
	
	pg.time.Clock().tick(FPS)

	color_panel()
	info_panel()
	buttons()
	# print(pg.mouse.get_pos())
	# -- lol end