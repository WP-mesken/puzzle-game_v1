from tkinter import *

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
    # 2 уровень
    if value == "88888888":
        for widget in root.winfo_children():
            if isinstance(widget, Frame):
                widget.pack_forget()
        #
        next_frame = Frame(root, bg=bg_color)
        next_frame.pack(fill="both", expand=True)

        img = PhotoImage(file='Images/1_level.png') #FIXME: Там пока лежит просто рандомная фотка. Надо будет поменять
        flag = True

    #TODO: Сделать уровни



    if flag:
        img_label = Label(next_frame, image=img, bg=bg_color)
        img_label.image = img
        img_label.pack(pady=20)

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


