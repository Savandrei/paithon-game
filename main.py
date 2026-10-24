import sys
import pygame
from src.game import Game

""" basically run all the python files"""
def main():
	pygame.init()
	pygame.mixer.init()

	game = Game()
	game.run()

	pygame.quit()
	sys.exit()


if __name__ == "__main__":
	main()
