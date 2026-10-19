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


def check_level_value(value, root, current_frame, bg_color):
    flag = False
    # 1 уровень
    if value == "88888888":
        for widget in root.winfo_children():
            if isinstance(widget, Frame):
                widget.pack_forget()
        #
        next_frame = Frame(root, bg=bg_color)
        next_frame.pack( expand=True)

        heading_label = Label(
            next_frame,
            text='Several pairs of digits \n have stuck together. \n Separate them',
            font=('Comic Sans MS', 20, 'bold'),
            width=35,
            height=4,
            bg=BTN_BG,
            fg=BTN_FG
        )
        heading_label.pack(pady=40)

        original_image = Image.open("Images/level_1.png")
        resized_image = original_image.resize((1024, 440))
        tk_image = ImageTk.PhotoImage(resized_image)
        image_label = Label(next_frame, image=tk_image)
        image_label.image = tk_image
        image_label.pack()

        flag = True

    # 2 уровень
    elif value == "23652273":
        for widget in root.winfo_children():
            if isinstance(widget, Frame):
                widget.pack_forget()
        #
        next_frame = Frame(root, bg=bg_color)
        next_frame.pack(expand=True)

        heading_label = Label(
            next_frame,
            text='Solve the Sudoku\n and find the numbers \n in the red squares.',
            font=('Comic Sans MS', 20, 'bold'),
            width=35,
            height=4,
            bg=BTN_BG,
            fg=BTN_FG
        )
        heading_label.pack(pady=40)

        original_image = Image.open("Images/level_2.jpg")
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
            text='Move one match \n to make a true equation',
            font=('Comic Sans MS', 20, 'bold'),
            width=35,
            height=3,
            bg=BTN_BG,
            fg=BTN_FG
        )
        heading_label.pack(pady=40)

        original_image = Image.open("Images/level_3.jpg") #TODO Добавить игру со спичками
        resized_image = original_image.resize((1024, 988))
        tk_image = ImageTk.PhotoImage(resized_image)
        image_label = Label(next_frame, image=tk_image)
        image_label.image = tk_image
        image_label.pack()

        flag = True

    # 8 уровень
    elif value == "99":
        for widget in root.winfo_children():
            if isinstance(widget, Frame):
                widget.pack_forget()
        #
        next_frame = Frame(root, bg=bg_color)
        next_frame.pack(fill="both", expand=True)

        heading_label = Label(
            next_frame,
            text='Solve the towers and find \n the numbers on the main diagonal',
            font=('Comic Sans MS', 20, 'bold'),
            width=35,
            height=2,
            bg=BTN_BG,
            fg=BTN_FG
        )
        heading_label.pack(pady=40)

        original_image = Image.open("Images/level_2.png")
        resized_image = original_image.resize((1024, 988))
        tk_image = ImageTk.PhotoImage(resized_image)
        image_label = Label(next_frame, image=tk_image)
        image_label.image = tk_image
        image_label.pack()

        flag = True

    if flag:
        btn_back = Button(
            next_frame,
            text="Back",
            font=("Comic Sans MS", 16),
            command=lambda: back_to_game_frame(next_frame, current_frame),
            width = 20,
            height = 2,
            bg = BTN_BG,
            activebackground = ACTIVE_BG,
            activeforeground = ACTIVE_FG,
            fg = BTN_FG
        )
        btn_back.pack(pady=20)

