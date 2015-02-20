#Conroy, Dylan, Egan, Ryan, Roberts, William
#CS110 A51 and A52 and A53
#Project Cursor Class

#Pygame Module is from Pygame.org.
#http://www.pygame.org/
import pygame

##Comments about what specific code does are not repeated in the same file
##when the code itself is repeated.

##Help for resolving code provided by users on Stack Overflow.com.
##http://stackoverflow.com/

#Sets the constants for the RGB Color values of red and black.
#http://thepythongamebook.com/
RED = (255, 0, 0)
BLACK = (0, 0, 0)

#This is a class for creating cursor objects to be used in the game.
#This class is a subclass for the Pygame Sprite Class.
#http://programarcadegames.com/
class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        #Initializes the Sprite super class.
        #http://programarcadegames.com/
        pygame.sprite.Sprite.__init__(self)
        #self.__image is a pygame Sprite class attribute.
        #Creates a new image surface of a specified pixel size.
        #http://programarcadegames.com/
        self.__image = pygame.Surface((30, 30))
        #Sets the color key of the image to be black, creating a transparent
        #background for the surface.
        #http://programarcadegames.com/
        self.__image.set_colorkey(BLACK)
        #Draws a line on the self.__image surface, of a certain color, from
        #one point to another, and with a certain width.
        #http://programarcadegames.com/
        pygame.draw.line(self.__image, RED, [0, 0], [10, 0], 2)
        pygame.draw.line(self.__image, RED, [0, 0], [0, 10], 2)
        pygame.draw.line(self.__image, RED, [20, 0], [28, 0], 2)
        pygame.draw.line(self.__image, RED, [28, 0], [28, 10], 2)
        pygame.draw.line(self.__image, RED, [0, 20],[0, 28], 2)
        pygame.draw.line(self.__image, RED, [0, 28],[10, 28], 2)
        pygame.draw.line(self.__image, RED, [20, 28],[28, 28], 2)
        pygame.draw.line(self.__image, RED, [28, 28],[28, 20], 2)
        #Sets the default attributes of currentX and currentY. This sets the
        #default position of the cursor in game.
        self.__currentX = 450
        self.__currentY = 300

    #Narrative: Receives an argument for the cursor's current X position and
    #           sets the attribute's value.
    #PreConditions: The game is initialized, an instance of the cursor
    #               class is created, and the currentX variable
    #               is passed to the function.
    #PostConditions: The currentX attribute of the instance is set with
    #                a new value.
    def setCurrentX(self, currentX):
        self.__currentX = currentX

     #Narrative: Receives an argument for the cursor's current Y position and
    #           sets the attribute's value.
    #PreConditions: The game is initialized, an instance of the cursor
    #               class is created, and the currentY variable
    #               is passed to the function.
    #PostConditions: The currentY attribute of the instance is set with
    #                a new value.
    def setCurrentY(self, currentY):
        self.__currentY = currentY

    #Narrative: Returns the value for the current X position attribute of the
    #           selected Cursor class instance.
    #PreConditions: An instance of the Cursor class is created, and the
    #               function is called.
    #PostConditions: The value for the current X position attribute is returned.
    def getCurrentX(self):
        return(self.__currentX)

    #Narrative: Returns the value for the current Y position attribute of the
    #           selected Cursor class instance.
    #PreConditions: An instance of the Cursor class is created, and the
    #               function is called.
    #PostConditions: The value for the current Y position attribute is returned.
    def getCurrentY(self):
        return(self.__currentY)

    def keyInput(self):
        #Sets a variable for what key is being pressed.
        key = pygame.key.get_pressed()
        #This decision structure determines what attribute should be changed
        #for updating the character on screen.
        if key[pygame.K_a]:
            #If the current X value for the character is already 0, then
            #the function will do nothing.
            if self.__currentX == 0:
                #Pass makes the program do nothing.
                pass
            else:
                #Reduces the current X attribute by 30, which will move the
                #character image by 30 pixels to the left, or one in game space.
                self.__currentX -= 30
        elif key[pygame.K_w]:
            #If the current Y value for the character is already 0, then
            #the function will do nothing.
            if self.__currentY == 0:
                pass
            else:
                #Reduces the current Y attribute by 30, which will move the
                #character image by 30 pixels up, or one in game space.
                self.__currentY -= 30
        elif key[pygame.K_d]:
            #If the current X value for the character is already 870, then
            #the function will do nothing.
            if self.__currentX == 870:
                pass
            else:
                #Increases the current X attribute by 30, which will move the
                #character image by 30 pixels to the right,
                #or one in game space.
                self.__currentX += 30
        elif key[pygame.K_s]:
            #If the current Y value for the character is already 870, then
            #the function will do nothing.
            if self.__currentY == 570:
                pass
            else:
                #Increases the current Y attribute by 30, which will move the
                #character image by 30 pixels down, or one in game space.
                self.__currentY += 30
        else:
            pass

    #Narrative: Updates the cursor sprite on the Pygame screen to
    #           the coordinates indicated by the instance's
    #           currentX and currentY values.
    #PreConditions: An instance of the Cursor class is created, and the
    #               function is called.
    #PostConditions: The cursord sprite image is updated to its
    #                coordinates on the Pygame screen.
    def update(self, surface):
        #Blitting transfers the sprite from one location to the one specified
        #as an argument.
        #http://programarcadegames.com/
        surface.blit(self.__image, [self.__currentX, self.__currentY])







