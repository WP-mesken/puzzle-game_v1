from tkinter import *
from PIL import Image, ImageTk

BG = '#D6C1A6'
BTN_BG = 'beige'
BTN_FG = 'brown'
ACTIVE_BG = 'maroon'
ACTIVE_FG = 'white'



def back_to_game_frame(current_response_frame, game_frame):
    current_response_frame.pack_forget()
    game_frame.pack(fill="both", expand=True)


def check_level_value(value, root, current_frame, game_frame, bg_color):
    flag = False
    # 1 уровень (Слипшиеся цифры)
    if value == "88888888":
        for widget in root.winfo_children():
            if isinstance(widget, Frame):
                widget.pack_forget()
        #
        next_frame = Frame(root, bg=bg_color)
        next_frame.pack( expand=True)

        heading_label = Label(
            next_frame,
            text='Несколькопар\n цифрслиплись. \n Разделитеих',
            font=('Comic Sans MS', 20, 'bold'),
            width=35,
            height=4,
            bg=BTN_BG,
            fg=BTN_FG
        )
        heading_label.pack(pady=40)

        original_image = Image.open("Images/level_1_stuck‑together_digits.png")
        resized_image = original_image.resize((1024, 440))
        tk_image = ImageTk.PhotoImage(resized_image)
        image_label = Label(next_frame, image=tk_image)
        image_label.image = tk_image
        image_label.pack()

        flag = True

    # 2 уровень (Судоку)
    elif value == "23652273":
        for widget in root.winfo_children():
            if isinstance(widget, Frame):
                widget.pack_forget()
        #
        next_frame = Frame(root, bg=bg_color)
        next_frame.pack(expand=True)

        heading_label = Label(
            next_frame,
            text='Решите судоку\n и найдите все числа \n на красных квадратах.',
            font=('Comic Sans MS', 20, 'bold'),
            width=35,
            height=4,
            bg=BTN_BG,
            fg=BTN_FG
        )
        heading_label.pack(pady=40)

        original_image = Image.open("Images/level_2_sudoku.jpg")
        resized_image = original_image.resize((1024, 988))
        tk_image = ImageTk.PhotoImage(resized_image)
        image_label = Label(next_frame, image=tk_image)
        image_label.image = tk_image
        image_label.pack()

        flag = True

    # 3 уровень
    elif value == "28165569":
        for widget in root.winfo_children():
            if isinstance(widget, Frame):
                widget.pack_forget()
        #
        next_frame = Frame(root, bg=bg_color)
        next_frame.pack(expand=True)

        heading_label = Label(
            next_frame,
            text='Подвиньте одну спичку \n чтобы создать верное равенство',
            font=('Comic Sans MS', 20, 'bold'),
            width=35,
            height=3,
            bg=BTN_BG,
            fg=BTN_FG
        )
        heading_label.pack(pady=40)

        original_image = Image.open("Images/level_3_matches.png")
        resized_image = original_image.resize((1024, 988))
        tk_image = ImageTk.PhotoImage(resized_image)
        image_label = Label(next_frame, image=tk_image)
        image_label.image = tk_image
        image_label.pack()

        flag = True

    # 4 уровень
    elif value == "63513519":
        for widget in root.winfo_children():
            if isinstance(widget, Frame):
                widget.pack_forget()
        #
        next_frame = Frame(root, bg=bg_color)
        next_frame.pack(expand=True)

        heading_label = Label(
            next_frame,
            text='Составьте в правильном\nпорядке картинки\nи уберите из них 1, 3, 7',
            font=('Comic Sans MS', 20, 'bold'),
            width=35,
            height=3,
            bg=BTN_BG,
            fg=BTN_FG
        )
        heading_label.pack(pady=40)

        original_image = Image.open("Images/level_4_Bidstrup.jpg") #TODO: Разделить фото на части, составив пазл
        resized_image = original_image.resize((1024, 988))
        tk_image = ImageTk.PhotoImage(resized_image)
        image_label = Label(next_frame, image=tk_image)
        image_label.image = tk_image
        image_label.pack()

        flag = True

    # 5 уровень
    elif value == "65782915":
        for widget in root.winfo_children():
            if isinstance(widget, Frame):
                widget.pack_forget()
        #
        next_frame = Frame(root, bg=bg_color)
        next_frame.pack(expand=True)

        heading_label = Label(
            next_frame,
            text='Между цифрами получилась \n разная дистанция (｡•́-•̀｡)',
            font=('Comic Sans MS', 20, 'bold'),
            width=35,
            height=3,
            bg=BTN_BG,
            fg=BTN_FG
        )
        heading_label.pack(pady=40)

        original_image = Image.open("Images/level_5_strange distances.png")
        resized_image = original_image.resize((1024, 988))
        tk_image = ImageTk.PhotoImage(resized_image)
        image_label = Label(next_frame, image=tk_image)
        image_label.image = tk_image
        image_label.pack()

        flag = True

    # 6 уровень
    elif value == "52131376":
        for widget in root.winfo_children():
            if isinstance(widget, Frame):
                widget.pack_forget()
        #
        next_frame = Frame(root, bg=bg_color)
        next_frame.pack(expand=True)

        heading_label = Label(
            next_frame,
            text='', #TODO: Написать короткое описание для левела с наложенными цифрами
            font=('Comic Sans MS', 20, 'bold'),
            width=35,
            height=3,
            bg=BTN_BG,
            fg=BTN_FG
        )
        heading_label.pack(pady=40)

        original_image = Image.open("Images/level_6_superimposed_numbers.png")
        resized_image = original_image.resize((1024, 988))
        tk_image = ImageTk.PhotoImage(resized_image)
        image_label = Label(next_frame, image=tk_image)
        image_label.image = tk_image
        image_label.pack()

        flag = True

    # 7 уровень
    elif value == "72254317":
        for widget in root.winfo_children():
            if isinstance(widget, Frame):
                widget.pack_forget()
        #
        next_frame = Frame(root, bg=bg_color)
        next_frame.pack(expand=True)

        heading_label = Label(
            next_frame,
            text='Я вижу что ты пишешь!\nНе пиши при мне',
            font=('Comic Sans MS', 20, 'bold'),
            width=35,
            height=3,
            bg=BTN_BG,
            fg=BTN_FG
        )
        heading_label.pack(pady=40)

        original_image = Image.open("Images/level_7_menu_frame.jpg")
        resized_image = original_image.resize((1024, 988))
        tk_image = ImageTk.PhotoImage(resized_image)
        image_label = Label(next_frame, image=tk_image)
        image_label.image = tk_image
        image_label.pack()

        flag = True

    # 8 уровень
    elif value == "10372048" and current_frame.winfo_name() != "game_frame":
        for widget in root.winfo_children():
            if isinstance(widget, Frame):
                widget.pack_forget()
        #
        next_frame = Frame(root, bg=bg_color)
        next_frame.pack(fill="both", expand=True)

        heading_label = Label(
            next_frame,
            text='Решите towers и найдите \n числа на главной диагонали',
            font=('Comic Sans MS', 20, 'bold'),
            width=35,
            height=2,
            bg=BTN_BG,
            fg=BTN_FG
        )
        heading_label.pack(pady=40)

        original_image = Image.open("Images/level_8_towers.png")
        resized_image = original_image.resize((1024, 988))
        tk_image = ImageTk.PhotoImage(resized_image)
        image_label = Label(next_frame, image=tk_image)
        image_label.image = tk_image
        image_label.pack()

        flag = True

    # 9 уровень
    elif value == "84124382":
        for widget in root.winfo_children():
            if isinstance(widget, Frame):
                widget.pack_forget()
        #
        next_frame = Frame(root, bg=bg_color)
        next_frame.pack(fill="both", expand=True)

        heading_label = Label(
            next_frame,
            text='Присмотрись к кнопкам\nво вкладке информации',
            font=('Comic Sans MS', 20, 'bold'),
            width=35,
            height=2,
            bg=BTN_BG,
            fg=BTN_FG
        )
        heading_label.pack(pady=40)
        flag = True

    # 10 (конец)
    elif value == "84124382":
        for widget in root.winfo_children():
            if isinstance(widget, Frame):
                widget.pack_forget()
        #
        next_frame = Frame(root, bg=bg_color)
        next_frame.pack(fill="both", expand=True)

        heading_label = Label(
            next_frame,
            text='Поздравляю\nты прошел игру!',
            font=('Comic Sans MS', 20, 'bold'),
            width=35,
            height=2,
            bg=BTN_BG,
            fg=BTN_FG
        )
        heading_label.pack(pady=40)
        flag = True

    if flag:
        btn_back = Button(
            next_frame,
            text="Back",
            font=("Comic Sans MS", 16),
            command=lambda: back_to_game_frame(next_frame, game_frame),
            width = 20,
            height = 2,
            bg = BTN_BG,
            activebackground = ACTIVE_BG,
            activeforeground = ACTIVE_FG,
            fg = BTN_FG
        )
        btn_back.pack(pady=20)

