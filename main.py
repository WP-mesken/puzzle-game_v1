
from tkinter import *

root = Tk()

# Название окна
root.title('Puzzle-game')

# Размеры окна
root.geometry('1200x1500')
root.resizable(width=False, height=False)

# Иконка
icon = PhotoImage(file='Images/icon for puzzle-game.png')
root.iconphoto(True, icon)

# Цвета
BG = '#D6C1A6'
BTN_BG = 'beige'
BTN_FG = 'brown'
ACTIVE_BG = 'maroon'
ACTIVE_FG = 'white'

root.configure(bg=BG)


# =========================
# ГЛАВНОЕ МЕНЮ
# =========================

menu_frame = Frame(root, bg=BG)
menu_frame.pack(expand=True)


def open_game():
    menu_frame.pack_forget()
    settings_frame.pack_forget()
    game_frame.pack(expand=True)
    root.focus_set()


def open_settings():
    menu_frame.pack_forget()
    game_frame.pack_forget()
    settings_frame.pack(expand=True)


def back_to_menu():
    game_frame.pack_forget()
    settings_frame.pack_forget()
    menu_frame.pack(expand=True)


# Кнопка Play
play_btn = Button(
    menu_frame,
    text='Play',
    command=open_game,
    font=('Comic Sans MS', 20, 'bold'),
    width=20,
    height=2,
    bg=BTN_BG,
    activebackground=ACTIVE_BG,
    activeforeground=ACTIVE_FG,
    fg=BTN_FG
)
play_btn.pack(pady=10)


# Кнопка Settings
settings_btn = Button(
    menu_frame,
    text='Settings',
    command=open_settings,
    font=('Comic Sans MS', 20, 'bold'),
    width=20,
    height=2,
    bg=BTN_BG,
    activebackground=ACTIVE_BG,
    activeforeground=ACTIVE_FG,
    fg=BTN_FG
)
settings_btn.pack(pady=10)


# Кнопка Quit
quit_btn = Button(
    menu_frame,
    text='Quit',
    command=root.destroy,
    font=('Comic Sans MS', 20, 'bold'),
    width=20,
    height=2,
    bg=BTN_BG,
    activebackground=ACTIVE_BG,
    activeforeground=ACTIVE_FG,
    fg=BTN_FG
)
quit_btn.pack(pady=10)

text_widget = Text(
    menu_frame,
    bg=BG,
    fg=BG,
    font=("Arial", 12),
    bd=0,
    highlightthickness=0,
    wrap="word",
    width=30,
    height=2
)
text_widget.pack( pady=20, expand=True)

# Функция для безопасной вставки текста
def insert_readonly_text(widget, text):
    widget.config(state="normal")  # Разрешаем редактирование для вставки
    widget.insert("1.0", text)     # Вставляем текст
    widget.config(state="disabled")# Запрещаем редактирование, оставляя возможность копирования

# Пример текста для копирования
sample_text = "mskn"

insert_readonly_text(text_widget, sample_text)


# =========================
# НАСТРОЙКИ
# =========================

def open_info():
    settings_frame.pack_forget()
    info_frame.pack(expand=True)


settings_frame = Frame(root, bg=BG)

info_btn = Button(
    settings_frame,
    text='Info',
    command=open_info,
    font=('Comic Sans MS', 20, 'bold'),
    width=20,
    height=2,
    bg=BTN_BG,
    activebackground=ACTIVE_BG,
    activeforeground=ACTIVE_FG,
    fg=BTN_FG
)
info_btn.pack(pady=10)

back_to_settings_btn = Button(
    settings_frame,
    text='Back',
    command=back_to_menu,
    font=('Comic Sans MS', 20, 'bold'),
    width=20,
    height=2,
    bg=BTN_BG,
    activebackground=ACTIVE_BG,
    activeforeground=ACTIVE_FG,
    fg=BTN_FG
)
back_to_settings_btn.pack(pady=10)

#Информация

def close_info():
    info_frame.pack_forget()
    settings_frame.pack(expand=True)

def open_hints():
    info_frame.pack_forget()
    hints_frame.pack(expand=True)

info_frame = Frame(root, bg=BG)

back_to_settings_btn = Button(
    info_frame,
    text='Back',
    command=close_info,
    font=('Comic Sans MS', 20, 'bold'),
    width=20,
    height=2,
    bg=BTN_BG,
    activebackground=ACTIVE_BG,
    activeforeground=ACTIVE_FG,
    fg=BTN_FG
)
back_to_settings_btn.pack(pady=10)

hints_btn = Button(
    info_frame,
    text='Definitely not a hint for the 1st level.',
    command=open_hints,
    font=('Comic Sans MS', 20, 'bold'),
    width=32,
    height=2,
    bg=BG,
    activebackground=BG,
    activeforeground=BG,
    fg= '#cfbca3',
    relief='flat',
    borderwidth=0,
    highlightthickness=0)
hints_btn.pack(pady=10)

# ПОДСКАЗКИ

def close_hints():
    hints_frame.pack_forget()
    menu_frame.pack(expand=True)

hints_frame = Frame(root, bg=BG)


first_hint_lbl = Label(
    hints_frame,
    text='A1, B2, C3, D4 ... \n Find smth on the menu',
    font=('Comic Sans MS', 20, 'bold'),
    width=30,
    height=4,
    bg=BTN_BG,
    fg=BTN_FG
)
first_hint_lbl.pack(pady=40)

back_to_info_btn = Button(
    hints_frame,
    text='Back to menu',
    command=close_hints,
    font=('Comic Sans MS', 20, 'bold'),
    width=20,
    height=2,
    bg=BTN_BG,
    activebackground=ACTIVE_BG,
    activeforeground=ACTIVE_FG,
    fg=BTN_FG
)
back_to_info_btn.pack(pady=10)

#Подсказка на первый уровень


# =========================
# ИГРА
# =========================

game_frame = Frame(root, bg=BG)

# Переменная для хранения введённых цифр
display_var = StringVar()


# Добавление цифры в строку
def add_digit(char):
    current_text = display_var.get()

    # Только цифры, максимум 8 символов
    if char.isdigit() and len(current_text) < 8:
        display_var.set(current_text + char)


# Очистка строки
def clear_display():
    display_var.set('')


# Отправка введённого значения
def enter_value(): #TODO: Levels
    value = display_var.get()
    clear_display()
    # Здесь будет твоя обработка введённого значения
    print('Введённое значение:', value)


# Обработка клавиатуры
def on_key_press(event):
    # Ввод цифр
    if event.char and event.char in '0123456789':
        add_digit(event.char)

    # Удаление последней цифры
    elif event.keysym == 'BackSpace':
        display_var.set(display_var.get()[:-1])

    # Отправка значения клавишей Enter
    elif event.keysym == 'Return':
        if game_frame.winfo_ismapped():
            enter_value()


# Контейнер игрового поля
game_board = Frame(game_frame, bg=BG)
game_board.pack(expand=True)


# Строка ввода
display = Entry(
    game_board,
    textvariable=display_var,
    font=('Comic Sans MS', 28, 'bold'),
    width=16,
    justify='center',
    state='readonly',
    readonlybackground='white',
    fg=BTN_FG,
    bd=3,
    relief='solid'
)
display.grid(
    row=0,
    column=0,
    columnspan=3,
    padx=10,
    pady=(10, 30),
    ipady=10
)


# Общий стиль кнопок цифр
button_style = {
    'font': ('Comic Sans MS', 24, 'bold'),
    'width': 5,
    'height': 2,
    'bg': BTN_BG,
    'fg': BTN_FG,
    'activebackground': ACTIVE_BG,
    'activeforeground': ACTIVE_FG,
    'relief': 'raised',
    'bd': 3
}


# Кнопки с цифрами от 1 до 9
number = 1

for row in range(1, 4):
    for column in range(3):
        digit = str(number)

        btn = Button(
            game_board,
            text=digit,
            command=lambda d=digit: add_digit(d),
            **button_style
        )

        btn.grid(
            row=row,
            column=column,
            padx=5,
            pady=5,
            sticky='nsew'
        )

        number += 1


# Кнопка C — очистить строку
clear_btn = Button(
    game_board,
    text='C',
    command=clear_display,
    **button_style
)
clear_btn.grid(
    row=4,
    column=0,
    padx=5,
    pady=5,
    sticky='nsew'
)


# Кнопка 0
zero_btn = Button(
    game_board,
    text='0',
    command=lambda: add_digit('0'),
    **button_style
)
zero_btn.grid(
    row=4,
    column=1,
    padx=5,
    pady=5,
    sticky='nsew'
)


# Кнопка Enter — отправить значение
enter_btn = Button(
    game_board,
    text='Enter',
    command=enter_value,
    **button_style
)
enter_btn.grid(
    row=4,
    column=2,
    padx=5,
    pady=5,
    sticky='nsew'
)


# Кнопка Back — под панелью цифр
back_btn = Button(
    game_board,
    text='Back',
    command=back_to_menu,
    font=('Comic Sans MS', 20, 'bold'),
    width=20,
    height=2,
    bg=BTN_BG,
    fg=BTN_FG,
    activebackground=ACTIVE_BG,
    activeforeground=ACTIVE_FG
)
back_btn.grid(
    row=5,
    column=0,
    columnspan=3,
    padx=5,
    pady=(15, 5),
    sticky='ew'
)


# Обработка нажатий клавиш
root.bind('<Key>', on_key_press)
#FIXME: Есть проблема, что печатать можно и не открывая окна. Но это забавно))) Поэтому можно оставить как головоломку


# Запуск программы
root.mainloop()
