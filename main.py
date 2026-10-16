from tkinter import *

root = Tk()

# Название
root.title('Puzzle-game')

# Размеры окна
root.geometry('1200x1500')
root.resizable(width=False, height=False)

# Иконка
icon = PhotoImage(file='icon for puzzle-game.png')
root.iconphoto(True, icon)


# Начальное окно

root['bg'] = '#D6C1A6'
menu_frame = Frame(root) #Создаем контейнер внутри окна, чтобы потом внутри него были кнопки
menu_frame.pack(expand=True)

## кнопка играть
def f_btn_play(): #TODO: открытие окна с игрой
    pass

btn_play = Button(menu_frame,
                  text="Play",                        #текст на кнопке
                  command=f_btn_play,                   #что происходит при нажатии
                  font=('Comic Sans MS',  20, 'bold'),  #размер шрифта
                  width='20',
                  height='2',
                  bg='beige',                           #цвет кнопки
                  activebackground='maroon',            #цвет кнопки при нажатии
                  activeforeground='white',             #цвет шрифта
                  fg='brown',
                  )

btn_play.pack(pady=10)


# Кнопка меню
def f_btn_menu(): #TODO: кнопка меню
    pass

Button(menu_frame,
                  text="Settings",                      #текст на кнопке
                  command=f_btn_menu,                   #что происходит при нажатии
                  font=('Comic Sans MS',  20, 'bold'),  #размер шрифта
                  width='20',
                  height='2',
                  bg='beige',                           #цвет кнопки
                  activebackground='maroon',            #цвет кнопки при нажатии
                  activeforeground='white',             #цвет шрифта
                  fg='brown',
                  )

btn_menu.pack(pady=10)

root.mainloop()
