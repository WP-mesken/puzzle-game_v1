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
menu_frame = Frame(root, bg='#D6C1A6') #Создаем контейнер внутри окна, чтобы потом внутри него были кнопки
menu_frame.pack(expand=True)

## кнопка играть в меню
def open_game():
    menu_frame.pack_forget()
    game_frame.pack(expand=True)

game_frame = Frame(root, bg="red")

play_btn = Button(menu_frame, text="Play", command=open_game,
       font=('Comic Sans MS',  20, 'bold'), width='20',height='2',
       bg='beige', activebackground='maroon', activeforeground='white', fg='brown', )
play_btn.pack(pady=10)

# Кнопка меню

def open_settings():
       menu_frame.pack_forget()
       settings_frame.pack(expand=True)

settings_frame = Frame(root, bg='red')

settings_btn = Button(menu_frame, text="Settings", command=open_settings,
                  font=('Comic Sans MS',  20, 'bold'), width='20', height='2',
                  bg='beige', activebackground='maroon', activeforeground='white', fg='brown')
settings_btn.pack(pady=10)


#Выход из игры

quit_btn = Button(menu_frame, text="Quit", command=root.destroy,
       font=('Comic Sans MS',  20, 'bold'), width='20', height='2',
       bg='beige', activebackground='maroon', activeforeground='white', fg='brown')
quit_btn.pack(pady=10)





#Настройки TODO: После создания игры этим заняться

def back_to_menu_from_settings():
       settings_frame.pack_forget()
       menu_frame.pack(expand=True)

settings = Button(settings_frame, text="Menu", command=back_to_menu_from_settings,
       font=('Comic Sans MS',  20, 'bold'), width='20', height='2',
       bg='beige', activebackground='maroon', activeforeground='white', fg='brown')
settings.pack(pady=10)







#сама игра:

def add_digit(): #TODO Сделать строку с добавлением цифр
    pass

def back_to_menu_from_game():
       game_frame.pack_forget()
       menu_frame.pack(expand=True)


Button(game_frame, text="Menu",command=back_to_menu_from_game, #TODO Переписать эту кнопку в строке с кнопками цифр
       font=('Comic Sans MS',  20, 'bold'), width='20', height='2',
       bg='beige', activebackground='maroon', activeforeground='white', fg='brown').pack(pady=10)


root.mainloop()
