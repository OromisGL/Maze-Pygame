# Roboter II
 
# In dieser Aufgabe geht wieder um eine Roboterklasse.
# Uns interessiert nicht das Aussehen und die Beschaffenheit eines Roboters,
# sondern nur seine Position in einer imaginären „Landschaft”,
# die zweidimensional sein soll
# und durch ein Koordinatensystem beschrieben werden kann.
# Ein Roboter hat also zwei Attribute für die x- und die y-Koordinate.
# Es empfiehlt sich, diese Informationen in einer 2er-Liste zusammenzufassen,
# also beispielsweise position = [3, 4],
# wobei dann 3 der x-Position und 4 der y-Position entspricht.
# Der Roboter ist in eine der vier Richtungen „west”, „south”, „east”
# oder „north” orientiert, was wir in einem Attribut speichern wollen.
# Außerdem sollten unsere Roboter auch Namen haben.
# Allerdings dürfen die Namen nicht länger als 10 Zeichen sein.
# Sollte jemand versuchen,
# dem Roboter einen längeren Namen zuzuweisen,
# soll der Name auf 10 Zeichen abgeschnitten werden.
# Um die Roboter im Koordinatensystem bewegen zu können,
# benötigen wir eine move()-Methode.
# Die Methode erwartet einen Parameter „distance”,
# der angibt, um welchem Betrag sich der Roboter in Richtung
# der eingestellten Orientierung bewegen soll.
# Wird ein Roboter x beispielsweise mit x.move(10) aufgerufen
# und ist dieser Roboter östlich orientiert,
# also x.orientation == "east", und ist [3, 7] die aktuelle Position des
# Roboters, dann bewegt er sich 10 Felder östlich
# und befindet sich anschließend in Position [13, 7].

""" from math import sqrt

class Roboter:
    def __init__(self, name, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.name = name

        @property
        def x(self, x):
            return self.__x
        
        @x.setter
        def x(self, x):
            pass

        @property
        def y(self, y):
            return self.__y
        
        @y.setter
        def y(self, y):
            pass

        @property
        def direction(self, direction):
            return self.__direction
        
        @direction.setter
        def direction(self, direction):
            pass

        @property
        def name(self, name):
            return self.__name
        
        @name.setter
        def name(self, name):
            pass

class Move:
    def __init__(self, distance):
        self.distance = distance """
""" 
# Example file showing a circle moving on screen
import pygame
from pygame.locals import *
from sys import exit



# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
player = pygame.image.load('Cartoon_Robot.svg.png').convert()

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    screen.blit(pygame.transform.scale_by(player, 0.2), (player_pos.x, player_pos.y))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit() """

import pygame

class Player:
	def __init__(self, x, y):
		self.x = int(x)
		self.y = int(y)
		self.player_size = 10
		self.rect = pygame.Rect(self.x, self.y, self.player_size, self.player_size)
		self.color = (250, 120, 60)
		self.velX = 0
		self.velY = 0
		self.left_pressed = False
		self.right_pressed = False
		self.up_pressed = False
		self.down_pressed = False
		self.speed = 4

	# get current cell position of the player
	def get_current_cell(self, x, y, grid_cells):
		for cell in grid_cells:
			if cell.x == x and cell.y == y:
				return cell

	# stops player to pass through walls
	def check_move(self, tile, grid_cells, thickness):
		current_cell_x, current_cell_y = self.x // tile, self.y // tile
		current_cell = self.get_current_cell(current_cell_x, current_cell_y, grid_cells)
		current_cell_abs_x, current_cell_abs_y = current_cell_x * tile, current_cell_y * tile
		if self.left_pressed:
			if current_cell.walls['left']:
				if self.x <= current_cell_abs_x + thickness:
					self.left_pressed = False
		if self.right_pressed:
			if current_cell.walls['right']:
				if self.x >= current_cell_abs_x + tile - (self.player_size + thickness):
					self.right_pressed = False
		if self.up_pressed:
			if current_cell.walls['top']:
				if self.y <= current_cell_abs_y + thickness:
					self.up_pressed = False
		if self.down_pressed:
			if current_cell.walls['bottom']:
				if self.y >= current_cell_abs_y + tile - (self.player_size + thickness):
					self.down_pressed = False

	# drawing player to the screen
	def draw(self, screen):
		pygame.draw.rect(screen, self.color, self.rect)

	# updates player position while moving
	def update(self):
		self.velX = 0
		self.velY = 0
		if self.left_pressed and not self.right_pressed:
			self.velX = -self.speed
		if self.right_pressed and not self.left_pressed:
			self.velX = self.speed
		if self.up_pressed and not self.down_pressed:
			self.velY = -self.speed
		if self.down_pressed and not self.up_pressed:
			self.velY = self.speed

		self.x += self.velX
		self.y += self.velY

		self.rect = pygame.Rect(int(self.x), int(self.y), self.player_size, self.player_size)