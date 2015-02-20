#Conroy, Dylan, Egan, Ryan, Roberts, William
#CS110 A51 and A52 and A53
#Project Main

#Algorithm:
#1: Initialize the Pygame window.
#2: Create instances of sprite objects to be used in the Pygame screen.
#3: Run the main game loop.
#4: Update the location of the cursor based upon W, A, S, and D key inputs.
#5: When the spacebar is pressed, open a character window that allows
#   commands to be enacted on the chosed character.
#6: When a character has their current health value reduced to zero, remove
#   them from the game via lists.
#7. When backspace is pressed, change the turn of the players.
#8: When all of the movement options of the characters are also done, change
#   the players' turns.
#9. When one of the lists containing each players' characters is empty,
#   the other player wins and the game exits.

#Pygame Module is from Pygame.org.
#http://www.pygame.org/
import pygame
from Character import Character
from Cursor import Cursor
from Background import Background
from CharacterWindow import CharacterWindow
from NotificationBox import NotificationBox
from SettingsWindow import SettingsWindow

##Comments about what specific code does are not repeated in the same file
##when the code itself is repeated.

##Help for resolving code provided by users on Stack Overflow.com.
##http://stackoverflow.com/

#Sets a constant for the RGB Color values of the color white.
#http://thepythongamebook.com/
WHITE = (255, 255, 255)
#Sets the constant for the Pygame window and its size.
#http://thepythongamebook.com/
SCREEN = pygame.display.set_mode((900, 600))

#Narrative: Makes instances of all of the characters to be used in the game.
#PreConditions: The game is initialized,the function is called, and the
#               Character class is imported.
#PostConditions: A list containing every instance of the Character class is
#                returned.
def makeCharacters():
    #Each argument represents the Name, Max Health, Current Health, Strength,
    #Current Movement, Healing, Original Movement, Current X Value,
    #Current Y Value, IsEnemy(determines what team each character is on),
    #and Done(whether if character is active or not).
    #Character names are from The Fire Emblem Wiki.
    #http://fireemblem.wikia.com/wiki/Fire_Emblem_Wikia
    lonqu = Character("Lon'Qu", 30, 30, 15, 10, 12, 10, 150, 480, False, False)
    basilio = Character("Basilio", 60, 60, 20, 5, 8, 5, 180, 450, False, False)
    gregor = Character("Gregor", 45, 45, 18, 7, 5, 7, 330, 480, False, False)
    flavia = Character("Flavia", 40, 40, 12, 7, 15, 7, 360, 450, False, False)
    chrom = Character("Chrom", 40, 40, 15, 8, 10, 8, 510, 480, False, False)
    lucina = Character("Lucina", 40, 40, 12, 9, 5, 9, 540, 450, False, False)
    robin = Character("Robin", 35, 35, 10, 7, 20, 7, 690, 480, False, False)
    donnel = Character("Donnel", 50, 50, 18, 6, 8, 6, 720, 450, False, False)
    yenfay = Character("Yen'Fay", 50, 50, 18, 0, 8, 6, 150, 120, True, True)
    marth = Character("Marth", 35, 35, 10, 0, 20, 7, 180, 90, True, True)
    excellus = Character("Excellus", 40, 40, 12, 0, 5, 9, 330, 120, True, True)
    gangrel = Character("Gangrel", 40, 40, 15, 0, 10, 8, 360, 90, True, True)
    walhart = Character("Walhart", 40, 40, 12, 0, 15, 7, 510, 120, True, True)
    cervantes = Character("Cervantes", 45, 45, 18, 0, 5, 7, 540, 90, True, True)
    validar = Character("Validar", 60, 60, 20, 0, 8, 5, 690, 120, True, True)
    pheros = Character("Pheros", 30, 30, 15, 0, 12, 10, 720, 90, True, True)

    characterList = [lonqu, basilio, gregor, flavia, chrom, lucina, robin,
                     donnel, yenfay, marth, excellus, gangrel, walhart,
                     cervantes, validar, pheros]
    return characterList

#Narrative: Initializes and runs the game. Controls the mainloop that keeps
#           the game running, such as updating sprites, managing remaining
#           character lists, playing music, opening message boxes, etc.
#PreConditions: The function is called, with the Character, Cursor, Background,
#               CharacterWindow, NotificationBox, and Settings Window imported.
#PostConditions: The game is completed when either the list goodList or
#                evilList is empty.
def runGame():
    #Initializes a Pygame window.
    #http://thepythongamebook.com/
    pygame.init()
    #Sets the caption for the Pygame window.
    #http://thepythongamebook.com/
    pygame.display.set_caption("Python Emblem")
    #Fills the Pygame screen to be white.
    #http://thepythongamebook.com/
    SCREEN.fill(WHITE)
    #Updates the Pygame screen with the current display changes.
    #http://thepythongamebook.com/
    pygame.display.update()
    #Sets a variable for the Pygame clock.
    #http://thepythongamebook.com/
    clock = pygame.time.Clock()

    #Creates an instance of the Background Sprite Class using default values.
    background = Background()
    #Updates the Pygame screen with the current state of the background image.
    #http://programarcadegames.com/
    background.update(SCREEN)

    #Creates a new GUI of the game settings window, providing background and
    #music choice for the players to decide.
    SettingsWindow(background)

    #Sets the volume of the music played back through Pygame, on a scale from
    #0.0 to 1.0.
    #http://www.pygame.org/
    pygame.mixer.music.set_volume(.27)
    #Plays what music files are currently in the Pygame sound mixer.
    #An argument of -1 makes the current track loop indefinitely.
    #http://www.pygame.org/
    pygame.mixer.music.play(-1)

    characterList = makeCharacters()
    goodList = []
    evilList = []
    #This loop updates the current image status of every element in the
    #characterList on the Pygame screen.
    for item in characterList:
        item.update(SCREEN)
        isenemy = item.getIsEnemy()
        if isenemy == False:
            #Creates a list of every game character whose isenemy attribute
            #equals False.
            goodList.append(item)
        else:
            #Creates a list of every game character whose isenemy attribute
            #equals True.
            evilList.append(item)

    #Creates an instance of the Cursor class using default values.
    cursor = Cursor()
    #Updates the current image status of the game cursor on the Pygame screen.
    cursor.update(SCREEN)
    pygame.display.update()

    #This is the mainloop of the game, continues until done equals True.
    done = False
    #When turn equals 1, if it Player 1's turn.
    turn = 1
    while not done:
        #Gets events that occur in the Pygame window.
        #http://programarcadegames.com/
        for event in pygame.event.get():
            #Sets the done variable to be True if the 'X' exit button is
            #pressed on the Pygame window.
            #http://programarcadegames.com/
            if event.type == pygame.QUIT:
                done = True
        #Sets a variable whose value is what key is being pressed.
        #http://programarcadegames.com/
        key = pygame.key.get_pressed()
        #Executes statements when the spacebar is pressed.
        if key[pygame.K_SPACE]:
            #Sets variables for the current X and Y values of the cursor on the
            #Pygame screen.
            cursorX = cursor.getCurrentX()
            cursorY = cursor.getCurrentY()
            for item in characterList:
                #Sets variables for the current X and Y values of the current
                #item from the characterList.
                characterX = item.getCurrentX()
                characterY = item.getCurrentY()
                #Checks if the position of the cursor and the current item
                #are the same.
                if characterX == cursorX and characterY == cursorY:
                    #Sets the character that is in the same position as the
                    #cursor to a new variable and passes that variable and
                    #the whole characterList the CharacterWindow GUI class.
                    #Opens up a CharacterWindow GUI for user interaction.
                    character = item
                    CharacterWindow(character, characterList)
        #Executes statements when the backspace is pressed.
        elif key[pygame.K_BACKSPACE]:
            if turn == 1:
                for item in goodList:
                    item.setMovement(0)
                    item.setDone(True)
            else:
                for item in evilList:
                    item.setMovement(0)
                    item.setDone(True)
        else:
            #Controls the activity of the cursor based upon key inputs.
            cursor.keyInput()
        SCREEN.fill(WHITE)
        background.update(SCREEN)

        #This loop checks the current health values for each of the elements in
        #the characterList, and deletes the element from the list if their
        #current health value equals 0, which removes the sprite from the game.
        index = len(characterList)-1
        while index >= 0:
            #Gets the current health value of the element in the characterList
            #at the current index.
            health = characterList[index].getCurrentHealth()
            if health <= 0:
                del characterList[index]
            index -= 1
        #This loop checks the current health values for each of the elements in
        #the goodList, and deletes the element from the list if their
        #current health value equals 0, which removes the sprite from the game.
        index = len(goodList)-1
        while index >= 0:
            #Gets the current health value of the element in the goodList
            #at the current index.
            health = goodList[index].getCurrentHealth()
            if health <= 0:
                del goodList[index]
            index -= 1
        #This loop checks the current health values for each of the elements in
        #the evilList, and deletes the element from the list if their
        #current health value equals 0, which removes the sprite from the game.
        index = len(evilList)-1
        while index >= 0:
            #Gets the current health value of the element in the evilList
            #at the current index.
            health = evilList[index].getCurrentHealth()
            if health <= 0:
                del evilList[index]
            index -= 1

        for item in characterList:
            item.update(SCREEN)

        #This decision structure decides which player's turn it is, based upon
        #the current movement values of each character in the current player's
        #team.
        if turn == 1:
            #Determines if the Player's turn should change from Player 1 to
            #Player 2.
            goodChange = False
            finish = False
            for item in goodList:
                #Gets the done value of the current element in goodList.
                goodDone = item.getDone()
                if goodDone == True and finish == False:
                    #If goodChange is True, then the player's turn will change.
                    goodChange = True
                else:
                    goodChange = False
                    #If finish becomes True, the loop will stop checking
                    #the elements in the list and continue with the
                    #current player's turn.
                    finish = True
            if goodChange == True:
                #Sets the title and description for a message box notifying
                #a change from Player 1's turn to Player 2's turn.
                title = "Player 2"
                description = "It's Player 2's turn."
                #Brings up a message box notifying
                #a change from Player 1's turn to Player 2's turn.
                NotificationBox(title, description)
                #If turn equals 2, it is player 2's turn.
                turn = 2
                for item in evilList:
                    #Gets the original movement value for the current element.
                    movement = item.getOriginalMovement()
                    #Sets the current movement value for the current element
                    #to be what the movement value was originally, effectively
                    #resetting the element for the new turn.
                    item.setMovement(movement)
                    #Sets the value of the done attribute of the current
                    #element to be False.
                    item.setDone(False)
        else:
            #Determines if the Player's turn should change from Player 2 to
            #Player 1.
            evilChange = False
            finish = False
            for item in evilList:
                #Gets the done value of the current element in evilList.
                evilDone = item.getDone()
                if evilDone == True and finish == False:
                    #If evilChange is True, then the player's turn will change.
                    evilChange = True
                else:
                    evilChange = False
                    finish = True
            if evilChange == True:
                #Sets the title and description for a message box notifying
                #a change from Player 2's turn to Player 1's turn.
                title = "Player 1"
                description = "It's Player 1's turn."
                NotificationBox(title, description)
                turn = 1
                for item in goodList:
                    movement = item.getOriginalMovement()
                    item.setMovement(movement)
                    item.setDone(False)
        #This decision structure checks if the goodList or evilList is empty,
        #causing the game to end.
        if goodList == [] or evilList == []:
            if goodList == []:
                #Sets the title and description for a notification box
                #notifying that Player 2 wins the game.
                title = "Player 2 Wins!"
                description = "Player 2 Wins! Please exit the game."
                NotificationBox(title, description)
            else:
                #Sets the title and description for a notification box
                #notifying that Player 1 wins the game.
                title = "Player 1 Wins!"
                description = "Player 1 Wins! Please exit the game."
                NotificationBox(title, description)
            #When this done is True, the game exits.
            done = True
        #Updates the Pygame screen with the current state of the cursor image.
        cursor.update(SCREEN)
        pygame.display.update()
        #Sets the frame rate for the game. The argument is 11, so the screen
        #updates 11 times per second.
        #http://thepythongamebook.com/
        clock.tick(11)
    #Closes the Pygame window.
    #http://thepythongamebook.com/
    pygame.quit()

def main():
    runGame()

main()