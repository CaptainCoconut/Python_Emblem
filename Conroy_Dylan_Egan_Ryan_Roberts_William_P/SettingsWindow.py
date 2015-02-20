#Conroy, Dylan, Egan, Ryan, Roberts, William
#CS110 A51 and A52 and A53
#Project Settings Window

#Pygame Module is from Pygame.org.
#http://www.pygame.org/
import pygame
from tkinter import *

##Comments about what specific code does are not repeated in the same file
##when the code itself is repeated.

##Help for resolving code provided by users on Stack Overflow.com.
##http://stackoverflow.com/

#This class creates a Settings Window GUI where players can choose between
#background image choices for the game and three background music choices
#for the game.
class SettingsWindow(Frame):
    def __init__(self, background):
        #Creates a class attribute for the instance of the background class
        #passed as an argument.
        self.__background = background
        #Initializes the GUI frame.
        Frame.__init__(self)
        self.master.title("Settings")
        self.master.resizable(0, 0)
        self.grid()
        #Creates separate columns for the placement of widgets in the GUI.
        self.__firstColumn = Frame(self)
        self.__secondColumn = Frame(self)
        self.__thirdColumn = Frame(self)
        self.__firstColumn.grid(row=0, column=0)
        self.__secondColumn.grid(row=0, column=1)
        self.__thirdColumn.grid(row=0, column=2)
        #Creates integer variables for the two different sets of radio buttons,
        #along with their default values.
        self.__map_var = IntVar()
        self.__map_var.set(1)
        self.__music_var = IntVar()
        self.__music_var.set(1)
        #Creates radio buttons that choose different map and music choices
        #and packs them.
        self.__forest = Radiobutton(self.__firstColumn, text="Forest Map",
                                    variable=self.__map_var, value=1)
        self.__desert = Radiobutton(self.__firstColumn, text="Desert Map",
                                    variable=self.__map_var, value=2)
        self.__temple = Radiobutton(self.__firstColumn, text="Temple Map",
                                    variable=self.__map_var, value=3)
        self.__energetic = Radiobutton(self.__secondColumn,
                                       text="Energetic Music",
                                       variable=self.__music_var, value=1)
        self.__calm = Radiobutton(self.__secondColumn, text="Calm Music",
                                  variable=self.__music_var, value=2)
        self.__epic = Radiobutton(self.__secondColumn, text="Epic Music",
                                  variable=self.__music_var, value=3)
        self.__forest.pack()
        self.__desert.pack()
        self.__temple.pack()
        self.__energetic.pack()
        self.__calm.pack()
        self.__epic.pack()
        #Creates buttons for saving settings and exiting the window
        #and packs them.
        self.__save_settings = Button(self.__thirdColumn, text="Start Game",
                                      command=self.__save_settings)
        self.__save_settings.pack(side="right")
        mainloop()

    #Narrative: Takes the choices of the radio buttons and chooses music and
    #           map images based upon the choice values. Closes the window
    #           once done.
    #PreConditions: The game is initialized, the characterList is created,
    #               a character and the characterList are passes, the
    #               Settings Window GUI is initialized, and the Save Settings
    #               button is pressed by the user.
    #PostConditions: The character on screen does not move, their current
    #                movement value is set to zero, and the window closes.
    def __save_settings(self):
        background = self.__background
        #Gets values of the selected choices of the map and music radio buttons.
        map_choice = self.__map_var.get()
        music_choice = self.__music_var.get()
        #This decision structure decides which music file to be loaded into the
        #music mixer for playback.
        #Music is from the Fire Emblem wiki.
        #http://fireemblem.wikia.com/wiki/Fire_Emblem_Wikia
        if music_choice == 1:
            #Loads music into the Pygame sound mixer for playback.
            #http://www.pygame.org/
            pygame.mixer.music.load("fire_emblem.wav")
        elif music_choice == 2:
            pygame.mixer.music.load("conquest.wav")
        else:
            pygame.mixer.music.load("id_purpose.wav")
        #This decision structure decides which map image to be selected in the
        #Background class.
        if map_choice == 1:
            choice = 1
        elif map_choice == 2:
            choice = 2
        else:
            choice = 3
        #Passes the map variable value to the background Class to choose
        #the map image.
        background.setImage(choice)
        self.master.destroy()