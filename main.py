from tkinter import *

root = Tk()

#Название
root.title('Puzzle-game')

#Размеры окна
root.geometry('1200x1500')
root.resizable(width = False, height = False)

#Иконка
icon = PhotoImage(file='icon for puzzle-game.png')
root.iconphoto(True, icon)


root.mainloop()
