#Conroy, Dylan, Egan, Ryan, Roberts, William
#CS110 A51 and A52 and A53
#Project Character Window

#Pygame Module is from Pygame.org.
#http://www.pygame.org/
import pygame
from tkinter import *
from tkinter import messagebox

##Comments about what specific code does are not repeated in the same file
##when the code itself is repeated.

##Help for resolving code provided by users on Stack Overflow.com.
##http://stackoverflow.com/

#Sets the constant for the Pygame window and its size.
#http://thepythongamebook.com/
SCREEN = pygame.display.set_mode((900,600))

#This is a class for a Character Window GUI, which displays character
#statistics and provides buttons for players to input game commands.
class CharacterWindow(Frame):
    def __init__(self, character, characterList):

        #Gets the attributes from the passed character that are necessary for
        #label creation.
        movement = character.getMovement()
        name = character.getName()
        maxhealth = character.getMaxHealth()
        currenthealth = character.getCurrentHealth()
        strength = character.getStrength()
        healing = character.getHealing()

        #Defines attributes for the class equal to the passed character and
        #characterList for ease of access in button commands.
        self.__character = character
        self.__characterList = characterList

        #Initializes the GUI frame.
        Frame.__init__(self)
        #Sets the title of the GUI to be the name of the passed character.
        self.master.title(str(name))
        self.master.resizable(0, 0)
        self.grid()
        #Creates separate columns for the placement of widgets in the GUI.
        self.__portraitColumn = Frame(self)
        self.__firstColumn = Frame(self)
        self.__secondColumn = Frame(self)
        self.__portraitColumn.grid(row=0, column=0)
        self.__firstColumn.grid(row=0, column=1)
        self.__secondColumn.grid(row=0, column=2)

        #Decides what image to be uploaded as a character portrait in the
        #charatcer GUI based upon the character's name.
        #Character images are from the Fire Emblem Wiki.
        #http://fireemblem.wikia.com/wiki/Fire_Emblem_Wikia
        #Images converted to .gif using Online convert.com.
        #http://image.online-convert.com/convert-to-gif
        if name == "Lon'Qu":
            self.__image = PhotoImage(file="lonqu.gif")
        elif name == "Basilio":
            self.__image = PhotoImage(file="basilio.gif")
        elif name == "Gregor":
            self.__image = PhotoImage(file="gregor.gif")
        elif name == "Flavia":
            self.__image = PhotoImage(file="flavia.gif")
        elif name == "Chrom":
            self.__image = PhotoImage(file="chrom.gif")
        elif name == "Lucina":
            self.__image = PhotoImage(file="lucina.gif")
        elif name == "Robin":
            self.__image = PhotoImage(file="robin.gif")
        elif name == "Donnel":
            self.__image = PhotoImage(file="donnel.gif")
        elif name == "Yen'Fay":
            self.__image = PhotoImage(file="yenfay.gif")
        elif name == "Marth":
            self.__image = PhotoImage(file="marth.gif")
        elif name == "Excellus":
            self.__image = PhotoImage(file="excellus.gif")
        elif name == "Gangrel":
            self.__image = PhotoImage(file="gangrel.gif")
        elif name == "Walhart":
            self.__image = PhotoImage(file="walhart.gif")
        elif name == "Cervantes":
            self.__image = PhotoImage(file="cervantes.gif")
        elif name == "Validar":
            self.__image = PhotoImage(file="validar.gif")
        else:
            self.__image = PhotoImage(file="pheros.gif")

        #Creates labels of the character portrait image and statistics
        #and grids them to one fo the redefined columns.
        self.__imageLabel = Label(self.__portraitColumn, image=self.__image)
        self.__labelName = Label(self.__firstColumn, text="Name: "+str(name))
        self.__labelMaxHealth = Label(self.__firstColumn,
                                      text="Max Health: "+str(maxhealth))
        self.__labelCurrentHealth = Label(self.__firstColumn,
                                          text="Current Health: "
                                               +str(currenthealth))
        self.__labelStrength = Label(self.__firstColumn,
                                     text="Strength: "+str(strength))
        self.__labelHealing = Label(self.__firstColumn,
                                    text="Healing: "+str(healing))
        self.__labelMovement = Label(self.__firstColumn,
                                     text="Movement: "+str(movement))
        self.__imageLabel.grid(row=0, column=0)
        self.__labelName.grid(row=0, column=1)
        self.__labelMaxHealth.grid(row=1, column=1)
        self.__labelCurrentHealth.grid(row=2, column=1)
        self.__labelStrength.grid(row=3, column=1)
        self.__labelHealing.grid(row=4, column=1)
        self.__labelMovement.grid(row=5, column=1)

        #Creates buttons with different commands and labels and grids them to
        #one of the predefined columns.
        self.__buttonWait = Button(self.__secondColumn, text="Wait",
                                   command=self.__wait, height=2, width=12)
        self.__buttonMoveUp = Button(self.__secondColumn, text="Move Up",
                                     command=self.__moveUp, height=2, width=12)
        self.__buttonMoveDown = Button(self.__secondColumn, text="Move Down",
                                       command=self.__moveDown,
                                       height=2, width=12)
        self.__buttonMoveLeft = Button(self.__secondColumn, text="Move Left",
                                       command=self.__moveLeft,
                                       height=2, width=12)
        self.__buttonMoveRight = Button(self.__secondColumn, text="Move Right",
                                        command=self.__moveRight,
                                        height=2, width=12)
        self.__buttonHeal = Button(self.__secondColumn, text="Heal",
                                   command=self.__heal, height=2, width=12)
        self.__buttonAttackUp = Button(self.__secondColumn, text="Attack Up",
                                       command=self.__attackUp,
                                       height=2, width=12)
        self.__buttonAttackDown = Button(self.__secondColumn,
                                         text="Attack Down",
                                         command=self.__attackDown,
                                         height=2, width=12)
        self.__buttonAttackLeft = Button(self.__secondColumn,
                                         text="Attack Left",
                                         command=self.__attackLeft,
                                         height=2, width=12)
        self.__buttonAttackRight = Button(self.__secondColumn,
                                          text="Attack Right",
                                          command=self.__attackRight,
                                          height=2, width=12)
        self.__buttonFinish = Button(self.__secondColumn,
                                     text="Finish Commands",
                                     command=self.master.destroy, height=2)
        self.__buttonWait.grid(row=2, column=2)
        self.__buttonMoveUp.grid(row=1, column=2)
        self.__buttonMoveDown.grid(row=3, column=2)
        self.__buttonMoveLeft.grid(row=2, column=1)
        self.__buttonMoveRight.grid(row=2, column=3)
        self.__buttonHeal.grid(row=1, column=7)
        self.__buttonAttackUp.grid(row=1, column=5)
        self.__buttonAttackDown.grid(row=3, column=5)
        self.__buttonAttackLeft.grid(row=2, column=4)
        self.__buttonAttackRight.grid(row=2, column=6)
        self.__buttonFinish.grid(row=4, column=7)
        mainloop()

    #Narrative: Defines the command for the Wait button in the Character Window
    #           GUI. Sets the passed character's movement value to zero
    #           and ends their command opportunities.
    #PreConditions: The game is initialized, the characterList is created,
    #               a character and the characterList are passes, the
    #               Character Window GUI is initialized, and the Wait button is
    #               pressed by the user.
    #PostConditions: The character on screen does not move, their current
    #                movement value is set to zero, and the window closes.
    def __wait(self):
        #Defines a variable as the value of the character attribute
        #of the class.
        character = self.__character
        #Movement is set to zero and is set as the character's current movement.
        character.setMovement(0)
        #The current position of the character is updated on the screen.
        character.update(SCREEN)
        #Sets the value of the character's done value to be True.
        character.setDone(True)
        #Closes the Character Window GUI after everything else is executed.
        self.master.destroy()

    #Narrative: Defines the command for the Move Up button in the Character
    #           Window GUI. Moves the character by one space(30 pixels) unless
    #           the characters have no more movement options.
    #PreConditions: The game is initialized, the characterList is created,
    #               a character and the characterList are passes, the
    #               Character Window GUI is initialized, and the Move Up button
    #               is pressed by the user.
    #PostConditions: The character on screen moves up by one space(30 pixels)
    #                and their current movement value is reduced by 1, or the
    #                GUI window is closed.
    def __moveUp(self):
        character = self.__character
        movement = character.getMovement()
        currentX = character.getCurrentX()
        currentY = character.getCurrentY()
        #Defines a variable as the value of the characterList attribute
        #of the class.
        characterList = self.__characterList
        #This decision structure determines if the current character is
        #eligible for movement.
        if movement <= 0:
            #Displays a message that the character cannot move any more
            messagebox.showinfo("No more movement",
                                "You have run out of movement actions.")
            self.master.destroy()
        else:
            #This loop prevents the character from moving if there is another
            #character in an adjacent square in the Pygame screen, to avoid
            #sprites overlapping.
            stop = False
            for item in characterList:
                #Gets the X and Y values of each of the other characters
                #remaining in the game.
                otherY = item.getCurrentY()
                otherX = item.getCurrentX()
                #Checks if the difference between the current Y values of the
                #chosen character and the other character is 30 and if
                #their current X values are the same.
                if currentY - otherY == 30 and currentX == otherX:
                    stop = True
            #If stop is True, then the button does nothing when pressed.
            if stop == True:
                #Pass makes the program do nothing.
                #https://docs.python.org/2/tutorial/controlflow.html
                pass
            #Checks if the current Y value of the character is 0. If this is
            #True, then the character won't move.
            elif currentY == 0:
                pass
            else:
                #Changes the Current Y value of the character's image by -30,
                #and then sets it.
                currentY -= 30
                character.setCurrentY(currentY)
                character.update(SCREEN)
                #This decision structure reduces the character's movement
                #value by 1, and if the movement value becomes 0, then
                #a message box is displayed indicating that the character
                #has no more movement options. The character's done value
                #is also set to be True.
                movement -= 1
                character.setMovement(movement)
                if movement == 0:
                    messagebox.showinfo("No more movement",
                                        "You have run out of movement actions.")
                    character.setDone(True)
                    self.master.destroy()

    #Narrative: Defines the command for the Move Down button in the Character
    #           Window GUI. Moves the character by one space(30 pixels) unless
    #           the characters have no more movement options.
    #PreConditions: The game is initialized, the characterList is created,
    #               a character and the characterList are passes, the
    #               Character Window GUI is initialized, and the Move Down
    #               button is pressed by the user.
    #PostConditions: The character on screen moves down by one space(30 pixels)
    #                and their current movement value is reduced by 1, or the
    #                GUI window is closed.
    def __moveDown(self):
        character = self.__character
        movement = character.getMovement()
        currentX = character.getCurrentX()
        currentY = character.getCurrentY()
        characterList = self.__characterList
        if movement <= 0:
            messagebox.showinfo("No more movement",
                                "You have run out of movement actions.")
            self.master.destroy()
        else:
            stop = False
            for item in characterList:
                otherY = item.getCurrentY()
                otherX = item.getCurrentX()
                #Checks if the difference between the current Y values of the
                #chosen character and the other character is -30 and if their
                #current X values are the same.
                if currentY - otherY == -30 and currentX == otherX:
                    stop = True
            if stop == True:
                pass
            #Checks if the current Y value of the character is 570. If this is
            #True, then the character won't move.
            elif currentY == 570:
                pass
            else:
                #Changes the Current Y value of the character's image by -30,
                #and then sets it.
                currentY += 30
                character.setCurrentY(currentY)
                character.update(SCREEN)
                movement -= 1
                character.setMovement(movement)
                if movement == 0:
                    messagebox.showinfo("No more movement",
                                        "You have run out of movement actions.")
                    character.setDone(True)
                    self.master.destroy()

    #Narrative: Defines the command for the Move Left button in the Character
    #           Window GUI. Moves the character by one space(30 pixels) unless
    #           the characters have no more movement options.
    #PreConditions: The game is initialized, the characterList is created,
    #               a character and the characterList are passes, the
    #               Character Window GUI is initialized, and the Move Left
    #               button is pressed by the user.
    #PostConditions: The character on screen moves left by one space(30 pixels)
    #                and their current movement value is reduced by 1, or the
    #                GUI window is closed.
    def __moveLeft(self):
        character = self.__character
        movement = character.getMovement()
        currentX = character.getCurrentX()
        currentY = character.getCurrentY()
        characterList = self.__characterList
        if movement <= 0:
            messagebox.showinfo("No more movement",
                                "You have run out of movement actions.")
            self.master.destroy()
        else:
            stop = False
            for item in characterList:
                otherX = item.getCurrentX()
                otherY = item.getCurrentY()
                #Checks if the difference between the current X values of the
                #chosen character and the other character is 30 and if their
                #current Y values are the same.
                if currentX - otherX == 30 and currentY == otherY:
                    stop = True
            if stop == True:
                pass
            #Checks if the current X value of the character is 0. If this is
            #True, then the character won't move.
            elif currentX == 0:
                pass
            else:
                #Changes the Current X value of the character's image by -30,
                #and then sets it.
                currentX -= 30
                character.setCurrentX(currentX)
                character.update(SCREEN)
                movement -= 1
                character.setMovement(movement)
                if movement == 0:
                    messagebox.showinfo("No more movement",
                                        "You have run out of movement actions.")
                    self.master.destroy()
                    character.setDone(True)

    #Narrative: Defines the command for the Move Right button in the Character
    #           Window GUI. Moves the character by one space(30 pixels) unless
    #           the characters have no more movement options.
    #PreConditions: The game is initialized, the characterList is created,
    #               a character and the characterList are passes, the
    #               Character Window GUI is initialized, and the Move Right
    #               button is pressed by the user.
    #PostConditions: The character on screen moves right by one space(30 pixels)
    #                and their current movement value is reduced by 1, or the
    #                GUI window is closed.
    def __moveRight(self):
        character = self.__character
        movement = character.getMovement()
        currentX = character.getCurrentX()
        currentY = character.getCurrentY()
        characterList = self.__characterList
        if movement <= 0:
            messagebox.showinfo("No more movement",
                                "You have run out of movement actions.")
            self.master.destroy()
        else:
            stop = False
            for item in characterList:
                otherX = item.getCurrentX()
                otherY = item.getCurrentY()
                #Checks if the difference between the current X values of the
                #chosen character and the other character is -30 and if their
                #current Y values are the same.
                if currentX - otherX == -30 and currentY == otherY:
                    stop = True
            if stop == True:
                pass
            #Checks if the current X value of the character is 870. If this is
            #True, then the character won't move.
            elif currentX == 870:
                pass
            else:
                #Changes the Current X value of the character's image by 30,
                #and then sets it.
                currentX += 30
                character.setCurrentX(currentX)
                character.update(SCREEN)
                movement -= 1
                character.setMovement(movement)
                if movement == 0:
                    messagebox.showinfo("No more movement",
                                        "You have run out of movement actions.")
                    character.setDone(True)
                    self.master.destroy()

    #Narrative: Defines the command for the Heal button in the Character Window
    #           GUI alters the value of the character's health stat based upon
    #           the value of the character's healing stat.
    #PreConditions: The game is initialized, the characterList is created,
    #               a character and the characterList are passes, the
    #               Character Window GUI is initialized, and the Heal
    #               button is pressed by the user.
    #PostConditions: The character has their current health value increased by
    #                the amount specified by their healing value, or set equal
    #                to the value of their max health stat if their current
    #                health exceeds their max health, the character's current
    #                movement value is set to 0, and the Character Window GUI
    #                is closed.
    def __heal(self):
        character = self.__character
        #Gets the values of the character's current health, max health,
        #healing, and movement.
        currenthealth = character.getCurrentHealth()
        maxhealth = character.getMaxHealth()
        healing = character.getHealing()
        movement = character.getMovement()
        if movement <= 0:
            messagebox.showinfo("No more movement",
                                "You have run out of movement actions.")
            self.master.destroy()
        #Does nothing if the current health value is already equal to the
        #max health value.
        elif currenthealth == maxhealth:
            pass
        else:
            #Adds the healing value to the current health value.
            currenthealth += healing
            #If current health value becomes greater than the max health value,
            #then the current health value becomes equal to the max
            #health value.
            if currenthealth > maxhealth:
                currenthealth = maxhealth
            #Sets the current health value of the character.
            character.setCurrentHealth(currenthealth)
            character.setMovement(0)
            character.setDone(True)
            self.master.destroy()

    #Narrative: Defines the command for the Attack button in the Character
    #           Window GUI. Takes the characters strength value and reduces
    #           the upwards adjacent enemy's current health value. Exits the
    #           window after execution.
    #PreConditions: The game is initialized, the characterList is created,
    #               a character and the characterList are passes, the
    #               Character Window GUI is initialized, and the Attack
    #               button is pressed by the user.
    #PostConditions: An enemy unit has the value of their current health
    #                reduced by the value of the chosen character's strength
    #                and set. If the chosen character is next to no other
    #                character, then nothing happens. The chosen character's
    #                current movement value is set to 0 if the attack occurs,
    #                as well as the window closing if the attack occurs.
    def __attackUp(self):
        character = self.__character
        #Gets the values of the chosen character's strength, isenemy, movement,
        #currentX, and currentY attributes.
        characterStrength = character.getStrength()
        characterSide = character.getIsEnemy()
        movement = character.getMovement()
        currentX = character.getCurrentX()
        currentY = character.getCurrentY()
        characterList = self.__characterList
        #This loop finds a character in characterList that is both adjacent
        #and has an opposite isenemy value from the chosen character. If one is
        #found, then stay equals True.
        stay = False
        for item in characterList:
            #Gets the values of the current X and Y values and isenemy of the
            #other elements in the characterList.
            otherX = item.getCurrentX()
            otherY = item.getCurrentY()
            otherSide = item.getIsEnemy()
            #If the difference between Y values is 30 with the X
            #values being equal, and the isenemy values are opposite, then
            #stay equals True.
            if (currentY - otherY == 30 and currentX == otherX)\
                    and((characterSide == True and otherSide == False)
                    or (characterSide == False and otherSide == True)):
                stay = True
                otherCharacter = item
        if movement == 0:
            messagebox.showinfo("No more movement",
                                "You have run out of movement actions.")
            self.master.destroy()
        elif stay == True:
            #Gets the current health value of the character being attacked by
            #the chosen character.
            otherHealth = otherCharacter.getCurrentHealth()
            #Reduces the value of the current health stat of the character
            #being attacked by the value of the chosen character's
            #strength value.
            otherHealth -= characterStrength
            otherCharacter.setCurrentHealth(otherHealth)
            character.setMovement(0)
            self.master.destroy()
            character.setDone(True)
        #The button does nothing if neither of those above conditions are met.
        else:
            pass

    #Narrative: Defines the command for the Attack button in the Character
    #           Window GUI. Takes the characters strength value and reduces
    #           the downwards adjacent enemy's current health value. Exits the
    #           window after execution.
    #PreConditions: The game is initialized, the characterList is created,
    #               a character and the characterList are passes, the
    #               Character Window GUI is initialized, and the Attack
    #               button is pressed by the user.
    #PostConditions: An enemy unit has the value of their current health
    #                reduced by the value of the chosen character's strength
    #                and set. If the chosen character is next to no other
    #                character, then nothing happens. The chosen character's
    #                current movement value is set to 0 if the attack occurs,
    #                as well as the window closing if the attack occurs.
    def __attackDown(self):
        character = self.__character
        #Gets the values of the chosen character's strength, isenemy, movement,
        #currentX, and currentY attributes.
        characterStrength = character.getStrength()
        characterSide = character.getIsEnemy()
        movement = character.getMovement()
        currentX = character.getCurrentX()
        currentY = character.getCurrentY()
        characterList = self.__characterList
        stay = False
        for item in characterList:
            otherX = item.getCurrentX()
            otherY = item.getCurrentY()
            otherSide = item.getIsEnemy()
            #If the difference between Y values is -30 with the X
            #values being equal, and the isenemy values are opposite, then
            #stay equals True.
            if (currentY - otherY == -30 and currentX == otherX)\
                    and((characterSide == True and otherSide == False)
                    or (characterSide == False and otherSide == True)):
                stay = True
                otherCharacter = item
        if movement == 0:
            messagebox.showinfo("No more movement",
                                "You have run out of movement actions.")
            self.master.destroy()
        elif stay == True:
            otherHealth = otherCharacter.getCurrentHealth()
            otherHealth -= characterStrength
            otherCharacter.setCurrentHealth(otherHealth)
            character.setMovement(0)
            self.master.destroy()
            character.setDone(True)
        else:
            pass

    #Narrative: Defines the command for the Attack button in the Character
    #           Window GUI. Takes the characters strength value and reduces
    #           the left adjacent enemy's current health value. Exits the
    #           window after execution.
    #PreConditions: The game is initialized, the characterList is created,
    #               a character and the characterList are passes, the
    #               Character Window GUI is initialized, and the Attack
    #               button is pressed by the user.
    #PostConditions: An enemy unit has the value of their current health
    #                reduced by the value of the chosen character's strength
    #                and set. If the chosen character is next to no other
    #                character, then nothing happens. The chosen character's
    #                current movement value is set to 0 if the attack occurs,
    #                as well as the window closing if the attack occurs.
    def __attackLeft(self):
        character = self.__character
        characterStrength = character.getStrength()
        characterSide = character.getIsEnemy()
        movement = character.getMovement()
        currentX = character.getCurrentX()
        currentY = character.getCurrentY()
        characterList = self.__characterList
        stay = False
        for item in characterList:
            otherX = item.getCurrentX()
            otherY = item.getCurrentY()
            otherSide = item.getIsEnemy()
            #If the difference between X values is 30 with the Y
            #values being equal, and the isenemy values are opposite, then
            #stay equals True.
            if (currentX - otherX == 30 and currentY == otherY)\
                    and((characterSide == True and otherSide == False)
                    or (characterSide == False and otherSide == True)):
                stay = True
                otherCharacter = item
        if movement == 0:
            messagebox.showinfo("No more movement",
                                "You have run out of movement actions.")
            self.master.destroy()
        elif stay == True:
            otherHealth = otherCharacter.getCurrentHealth()
            otherHealth -= characterStrength
            otherCharacter.setCurrentHealth(otherHealth)
            character.setMovement(0)
            self.master.destroy()
            character.setDone(True)
        else:
            pass

    #Narrative: Defines the command for the Attack button in the Character
    #           Window GUI. Takes the characters strength value and reduces
    #           the right adjacent enemy's current health value. Exits the
    #           window after execution.
    #PreConditions: The game is initialized, the characterList is created,
    #               a character and the characterList are passes, the
    #               Character Window GUI is initialized, and the Attack
    #               button is pressed by the user.
    #PostConditions: An enemy unit has the value of their current health
    #                reduced by the value of the chosen character's strength
    #                and set. If the chosen character is next to no other
    #                character, then nothing happens. The chosen character's
    #                current movement value is set to 0 if the attack occurs,
    #                as well as the window closing if the attack occurs.
    def __attackRight(self):
        character = self.__character
        characterStrength = character.getStrength()
        characterSide = character.getIsEnemy()
        movement = character.getMovement()
        currentX = character.getCurrentX()
        currentY = character.getCurrentY()
        characterList = self.__characterList
        stay = False
        for item in characterList:
            otherX = item.getCurrentX()
            otherY = item.getCurrentY()
            otherSide = item.getIsEnemy()
            #If the difference between X values is -30 with the Y
            #values being equal, and the isenemy values are opposite, then
            #stay equals True.
            if (currentX - otherX == -30 and currentY == otherY)\
                    and((characterSide == True and otherSide == False)
                    or (characterSide == False and otherSide == True)):
                stay = True
                otherCharacter = item
        if movement == 0:
            messagebox.showinfo("No more movement",
                                "You have run out of movement actions.")
            self.master.destroy()
        elif stay == True:
            otherHealth = otherCharacter.getCurrentHealth()
            otherHealth -= characterStrength
            otherCharacter.setCurrentHealth(otherHealth)
            character.setMovement(0)
            self.master.destroy()
            character.setDone(True)
        else:
            pass