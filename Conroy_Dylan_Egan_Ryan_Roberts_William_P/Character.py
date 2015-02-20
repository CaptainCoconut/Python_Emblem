#Conroy, Dylan, Egan, Ryan, Roberts, William
#CS110 A51 and A52 and A53
#Project Character Class

#Pygame Module is from Pygame.org.
#http://www.pygame.org/
import pygame

##Comments about what specific code does are not repeated in the same file
##when the code itself is repeated.

##Help for resolving code provided by users on Stack Overflow.com.
##http://stackoverflow.com/

#Sets constants for the RGB Color values of red, blue, and white.
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

#This is a class for creating character objects to be used in the game.
#This class is a subclass for the Pygame Sprite Class.
#http://programarcadegames.com/
class Character(pygame.sprite.Sprite):
    def __init__(self, name, maxhealth, currenthealth, strength, movement,
                 healing, originalMovement, currentX, currentY, isenemy, done):
        #Initializes the Sprite super class.
        #http://programarcadegames.com/
        pygame.sprite.Sprite.__init__(self)

        #This decision structure determines which color to make the lines
        #for the character sprite.
        if isenemy == True:
            color = RED
        else:
            color = BLUE
        #Creates a new image surface of a specified pixel size.
        #http://programarcadegames.com/
        self.__image = pygame.Surface((30, 30))
        #Sets the color key of the image to be black, creating a transparent
        #background for the surface.
        #http://programarcadegames.com/
        self.__image.set_colorkey(BLACK)
        #Draws an ellipse on the self.__image surface, of a certain color,
        #with dimensions for what space it takes up, and its width. If width
        #equals 0 or no argument is given, then the ellipse is filled.
        #http://programarcadegames.com/
        pygame.draw.ellipse(self.__image, color, [10, 0, 10, 10])
        #Draws a line on the self.__image surface, of a certain color, from
        #one point to another, and with a certain width.
        #http://programarcadegames.com/
        pygame.draw.line(self.__image, color,
                         [14, 10], [14, 20], 2)
        pygame.draw.line(self.__image, color,
                         [5, 12], [25, 12], 2)
        pygame.draw.line(self.__image, color,
                         [14, 20], [5, 29], 3)
        pygame.draw.line(self.__image, color,
                         [14, 20], [25, 29], 3)
        #Sets the attributes for the class, with attributes being character
        #name, max health, current health, strength, movement, healing,
        #original movement, current X value, current Y value, isenemy(whether
        #the character is an enemy or not), and done(if the character is done
        #operating or not.
        self.__name = name
        self.__maxhealth = maxhealth
        self.__currenthealth = currenthealth
        self.__strength = strength
        self.__movement = movement
        self.__healing = healing
        self.__originalMovement = originalMovement
        self.__currentX = currentX
        self.__currentY = currentY
        self.__isenemy = isenemy
        self.__done = done

    #Narrative: Receives an argument for the character's name and sets the
    #           attribute's value.
    #PreConditions: The game is initialized, an instance of the character
    #               class is created, and the name variable is passed to the
    #               function.
    #PostConditions: The name attribute of the instance is set with a new value.
    def setName(self, name):
        self.__name = name

    #Narrative: Receives an argument for the character's max health and sets the
    #           attribute's value.
    #PreConditions: The game is initialized, an instance of the character
    #               class is created, and the maxhealth variable is passed to
    #               the function.
    #PostConditions: The max health attribute of the instance is set with
    #                a new value.
    def setMaxHealth(self, maxhealth):
        self.__maxhealth = maxhealth

    #Narrative: Receives an argument for the character's current health and
    #           sets the attribute's value.
    #PreConditions: The game is initialized, an instance of the character
    #               class is created, and the currenthealth variable
    #               is passed to the function.
    #PostConditions: The current health attribute of the instance is set with
    #                a new value.
    def setCurrentHealth(self, currenthealth):
        self.__currenthealth = currenthealth

    #Narrative: Receives an argument for the character's strength and
    #           sets the attribute's value.
    #PreConditions: The game is initialized, an instance of the character
    #               class is created, and the strength variable
    #               is passed to the function.
    #PostConditions: The strength attribute of the instance is set with
    #                a new value.
    def setStrength(self, strength):
        self.__strength = strength

    #Narrative: Receives an argument for the character's current movement and
    #           sets the attribute's value.
    #PreConditions: The game is initialized, an instance of the character
    #               class is created, and the movement variable
    #               is passed to the function.
    #PostConditions: The movement attribute of the instance is set with
    #                a new value.
    def setMovement(self, movement):
        self.__movement = movement

    #Narrative: Receives an argument for the character's healing and
    #           sets the attribute's value.
    #PreConditions: The game is initialized, an instance of the character
    #               class is created, and the healing variable
    #               is passed to the function.
    #PostConditions: The healing attribute of the instance is set with
    #                a new value.
    def setHealing(self, healing):
        self.__healing = healing

    #Narrative: Receives an argument for the character's original movement and
    #           sets the attribute's value.
    #PreConditions: The game is initialized, an instance of the character
    #               class is created, and the originalMovement variable
    #               is passed to the function.
    #PostConditions: The original movement attribute of the instance is set with
    #                a new value.
    def setOriginalMovement(self, originalMovement):
        self.__originalMovement = originalMovement

    #Narrative: Receives an argument for the character's current X position and
    #           sets the attribute's value.
    #PreConditions: The game is initialized, an instance of the character
    #               class is created, and the currentX variable
    #               is passed to the function.
    #PostConditions: The currentX attribute of the instance is set with
    #                a new value.
    def setCurrentX(self, currentX):
        self.__currentX = currentX

    #Narrative: Receives an argument for the character's current Y position and
    #           sets the attribute's value.
    #PreConditions: The game is initialized, an instance of the character
    #               class is created, and the currentY variable
    #               is passed to the function.
    #PostConditions: The currentY attribute of the instance is set with
    #                a new value.
    def setCurrentY(self, currentY):
        self.__currentY = currentY

    #Narrative: Receives an argument for the character's isenemy and
    #           sets the attribute's value.
    #PreConditions: The game is initialized, an instance of the character
    #               class is created, and the isenemy variable
    #               is passed to the function.
    #PostConditions: The isenemy attribute of the instance is set with
    #                a new value.
    def setIsEnemy(self, isenemy):
        self.__isenemy = isenemy

    #Narrative: Receives an argument for the character's done value and
    #           sets the attribute's value.
    #PreConditions: The game is initialized, an instance of the character
    #               class is created, and the done variable
    #               is passed to the function.
    #PostConditions: The done attribute of the instance is set with
    #                a new value.
    def setDone(self, done):
        self.__done = done

    #Narrative: Returns the value for the name attribute of the selected
    #           Character class instance.
    #PreConditions: An instance of the Character class is created, and the
    #               function is called.
    #PostConditions: The value for the name attribute is returned.
    def getName(self):
        return(self.__name)

    #Narrative: Returns the value for the max health attribute of the selected
    #           Character class instance.
    #PreConditions: An instance of the Character class is created, and the
    #               function is called.
    #PostConditions: The value for the max health attribute is returned.
    def getMaxHealth(self):
        return(self.__maxhealth)

    #Narrative: Returns the value for the current health attribute of the
    #           selected Character class instance.
    #PreConditions: An instance of the Character class is created, and the
    #               function is called.
    #PostConditions: The value for the current health attribute is returned.
    def getCurrentHealth(self):
        return(self.__currenthealth)

    #Narrative: Returns the value for the strength attribute of the selected
    #           Character class instance.
    #PreConditions: An instance of the Character class is created, and the
    #               function is called.
    #PostConditions: The value for the strength attribute is returned.
    def getStrength(self):
        return(self.__strength)

    #Narrative: Returns the value for the movement attribute of the selected
    #           Character class instance.
    #PreConditions: An instance of the Character class is created, and the
    #               function is called.
    #PostConditions: The value for the movement attribute is returned.
    def getMovement(self):
        return(self.__movement)

    #Narrative: Returns the value for the healing attribute of the selected
    #           Character class instance.
    #PreConditions: An instance of the Character class is created, and the
    #               function is called.
    #PostConditions: The value for the healing attribute is returned.
    def getHealing(self):
        return(self.__healing)

    #Narrative: Returns the value for the original movement attribute of the
    #           selected Character class instance.
    #PreConditions: An instance of the Character class is created, and the
    #               function is called.
    #PostConditions: The value for the original movement attribute is returned.
    def getOriginalMovement(self):
        return(self.__originalMovement)

    #Narrative: Returns the value for the current X position attribute of the
    #           selected Character class instance.
    #PreConditions: An instance of the Character class is created, and the
    #               function is called.
    #PostConditions: The value for the current X position attribute is returned.
    def getCurrentX(self):
        return(self.__currentX)

    #Narrative: Returns the value for the current Y position attribute of the
    #           selected Character class instance.
    #PreConditions: An instance of the Character class is created, and the
    #               function is called.
    #PostConditions: The value for the current Y position attribute is returned.
    def getCurrentY(self):
        return(self.__currentY)

    #Narrative: Returns the value for the isenemy attribute of the selected
    #           Character class instance.
    #PreConditions: An instance of the Character class is created, and the
    #               function is called.
    #PostConditions: The value for the isenemy attribute is returned.
    def getIsEnemy(self):
        return(self.__isenemy)

    #Narrative: Returns the value for the done attribute of the selected
    #           Character class instance.
    #PreConditions: An instance of the Character class is created, and the
    #               function is called.
    #PostConditions: The value for the done attribute is returned.
    def getDone(self):
        return(self.__done)

    #Narrative: Returns a string containing a description of every class
    #           attribute for the Character class.
    #PreConditions: An instance of the Character class is created, and the
    #               function is called.
    #PostConditions: The string is returned.
    def __str__(self):
        return("Name: "+str(self.__name)+"\n"
               +"Max Health: "+str(self.__maxhealth)+"\n"
               +"Current Health: "+str(self.__currenthealth)+"\n"
               +"Strength: "+str(self.__strength)+"\n"
               +"Movement: "+str(self.__movement)+"\n"
               +"Healing: "+str(self.__healing)+"\n"
               +"Original Movement: "+str(self.__originalMovement)+"\n"
               +"Current X Position: "+str(self.__currentX)+"\n"
               +"Current Y Position: "+str(self.__currentY)+"\n"
               +"Is an enemy: "+str(self.__isenemy)+"\n"
               +"Is done: "+str(self.__done))

    #Narrative: Updates the character sprite on the Pygame screen to
    #           the coordinates indicated by the instance's
    #           currentX and currentY values.
    #PreConditions: An instance of the Character class is created, and the
    #               function is called.
    #PostConditions: The character sprite image is updated to its
    #                coordinates on the Pygame screen.
    def update(self, surface):
        #Blitting transfers the sprite from one location to the one specified
        #as an argument.
        ##http://programarcadegames.com/
        surface.blit(self.__image, [self.__currentX, self.__currentY])