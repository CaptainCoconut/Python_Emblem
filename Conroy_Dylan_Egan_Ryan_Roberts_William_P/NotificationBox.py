#Conroy, Dylan, Egan, Ryan, Roberts, William
#CS110 A51 and A52 and A53
#Project Notification Box

from tkinter import *

##Comments about what specific code does are not repeated in the same file
##when the code itself is repeated.

##Help for resolving code provided by users on Stack Overflow.com.
##http://stackoverflow.com/

#This is the class for a Notification Box GUI, which displays a customized
#notification box based upon passed title and description arguments.
class NotificationBox(Frame):
    def __init__(self, title, description):
        Frame.__init__(self)
        #Sets the title of the window to be a predetermined title string.
        self.master.title(title)
        self.master.resizable(0, 0)
        self.grid()
        #Creates a label of a predetermined text to be displayed
        #in the notification box.
        words = Label(self.master, text=description)
        words.grid()
        #Creates a button that exits upon pressing.
        self.__buttonFinish = Button(self.master, text="Exit",
                                     command=self.master.destroy, height=2)
        self.__buttonFinish.grid()
        mainloop()