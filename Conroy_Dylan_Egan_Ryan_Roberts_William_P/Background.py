#Conroy, Dylan, Egan, Ryan, Roberts, William
#CS110 A51 and A52 and A53
#Project Background Class

#Pygame Module is from Pygame.org.
#http://www.pygame.org/
import pygame

##Comments about what specific code does are not repeated in the same file
##when the code itself is repeated.

##Help for resolving code provided by users on Stack Overflow.com.
##http://stackoverflow.com/

#Sets the constant for the RGB Color value of black.
#http://thepythongamebook.com/
BLACK = (0, 0, 0)

#This is a class for creating background objects to be used in the game.
#This class is a subclass for the Pygame Sprite Class.
#http://programarcadegames.com/
class Background(pygame.sprite.Sprite):
    def __init__(self):
        #Initializes the Sprite super class.
        #http://programarcadegames.com/
        pygame.sprite.Sprite.__init__(self)
        #Opens the image to be the sprite's default image before the
        #player's decide their preferred settings.
        #http://www.pygame.org/
        #Default map image is from the Fire Emblem wiki.
        #http://fireemblem.wikia.com/wiki/Fire_Emblem_Wikia
        self.__image = pygame.image.load("grass_map.png")
        #Tranforms the image to be of a certain resolution.
        self.__image = pygame.transform.scale(self.__image, (900,600))

        #This loop draws horizontal lines on the screen 30 pixels away
        #from each other.
        y_offset = 0
        while y_offset <= 600:
            #Draws a line on the self.__image surface, of a certain color, from
            #one point to another, and with a certain width.
            #http://programarcadegames.com/
            pygame.draw.line(self.__image, BLACK, [0,0+y_offset],
                             [900, 0+y_offset], 1)
            y_offset += 30
            #Updates the Pygame screen with the current display changes.
            #http://thepythongamebook.com/
            pygame.display.update()
        x_offset = 0
        while x_offset <= 900:
            pygame.draw.line(self.__image, BLACK, [0+x_offset, 600],
                             [0+x_offset,0], 1)
            x_offset += 30
            pygame.display.update()

    #Narrative: Receives an argument from Settings Window that determines which
    #           image to load as the background sprite image. Then it draws
    #           lines on the image to create a grid made of squares.
    #PreConditions: An instance of the background class has been created
    #               and the function is called.
    #PostConditions: The sprite to be displayed in the Pygame screen is
    #                created and drawn on.
    def setImage(self, choice):
        #This decision structure chooses what image to load as the background
        #sprite, based upon the choice made in Settings Window.
        #Additional map image choices are from the Fire Emblem Wiki.
        if choice == 1:
            self.__image = pygame.image.load("grass_map.png")
        elif choice == 2:
            self.__image = pygame.image.load("desert_map.png")
        else:
            self.__image = pygame.image.load("temple_map.png")
        self.__image = pygame.transform.scale(self.__image, (900,600))

        y_offset = 0
        while y_offset <= 600:
            pygame.draw.line(self.__image, BLACK, [0,0+y_offset],
                             [900, 0+y_offset], 1)
            y_offset += 30
            pygame.display.update()
        x_offset = 0
        while x_offset <= 900:
            pygame.draw.line(self.__image, BLACK, [0+x_offset, 600],
                             [0+x_offset,0], 1)
            x_offset += 30
            pygame.display.update()

    #Narrative: Updates the background sprite on the Pygame screen to
    #           the coordinates indicated by the instance's
    #           currentX and currentY values.
    #PreConditions: An instance of the Background class is created, and the
    #               function is called.
    #PostConditions: The background sprite image is updated to its
    #                coordinates on the Pygame screen.
    def update(self, surface):
        #Blitting transfers the sprite from one location to the one specified
        #as an argument.
        #http://programarcadegames.com/
        surface.blit(self.__image, [0,0])
