import threading
from tkinter import *
import tkinter
from PIL import Image as Pilimage
from PIL import ImageTk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import os
from multiprocessing import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from work_with_database import *
import sys
import configparser


ddd = 0
kh = 0
counter = 0
counter2 = 0

close = None
cpu_load = None
change_bg_en = None
fon1 = None
fon2 = None
quitButton = None
change_lang_UA = None
change_lang_EN = None
language_en = None

check = 0

config = configparser.ConfigParser()




class Window():
    def __init__(
        self,
        width,
        height,
        title="MyWindow",
        icon=None,
        resizable=(
            False,
            False)):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)

        config.read("parameters.ini", encoding='utf_8')
        img = Pilimage.open(os.path.join('images', "settings.png"))
        img = img.resize((80, 75), Pilimage.Resampling.LANCZOS)
        self.photo_image = ImageTk.PhotoImage(img)

        ccc = Pilimage.open(os.path.join('images', "child.jpg"))
        ccc = ccc.resize((505, 505), Pilimage.Resampling.LANCZOS)
        self.ccc = ImageTk.PhotoImage(ccc)

        bg = Pilimage.open(os.path.join('images', config["images"]["bg"]))
        bg = bg.resize((500, 500), Pilimage.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(bg)

        self.my_canvas1 = Canvas(
            self.root,
            width=500,
            height=500,
            highlightthickness=0)

        self.my_canvas1.pack(fill="both", expand=True)

        self.my_canvas = Canvas(
            self.root,
            width=500,
            height=500,
            highlightthickness=0,
            bg="grey")
        self.my_canvas.pack(fill="both", expand=True)
        self.my_canvas.create_image(0, 0, image=self.photo, anchor=NW)

        bg1 = Pilimage.open(os.path.join('images', "light_theme.png"))
        bg1 = bg1.resize((40, 40), Pilimage.Resampling.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(bg1)

        bg2 = Pilimage.open(os.path.join('images', "black_theme.png"))
        bg2 = bg2.resize((30, 30), Pilimage.Resampling.LANCZOS)
        self.photo2 = ImageTk.PhotoImage(bg2)

        start_scanning = Pilimage.open(
            os.path.join('images', "button_strt_scan.png"))
        start_scanning = start_scanning.resize(
            (215, 35), Pilimage.Resampling.LANCZOS)
        self.start_scanning = ImageTk.PhotoImage(start_scanning)

        non_recursive = Pilimage.open(
            os.path.join(
                'images',
                "button_strt_scan.png"))
        non_recursive = non_recursive.resize(
            (190, 30), Pilimage.Resampling.LANCZOS)
        self.not_recursive = ImageTk.PhotoImage(non_recursive)

        non_recursive_ua = Pilimage.open(
            os.path.join('images', "button_strt_scan.png"))
        non_recursive_ua = non_recursive_ua.resize(
            (210, 30), Pilimage.Resampling.LANCZOS)
        self.not_recursive_ua_210 = ImageTk.PhotoImage(non_recursive_ua)

        clear_scrollbar = Pilimage.open(
            os.path.join('images', "button_strt_scan.png"))
        clear_scrollbar = clear_scrollbar.resize(
            (100, 25), Pilimage.Resampling.LANCZOS)
        self.clear_scrollbar = ImageTk.PhotoImage(clear_scrollbar)

        scan_1_file = Pilimage.open(
            os.path.join(
                'images',
                "button_strt_scan.png"))
        scan_1_file = scan_1_file.resize(
            (190, 30), Pilimage.Resampling.LANCZOS)
        self.scan_1_file = ImageTk.PhotoImage(scan_1_file)

        scan_1_file_ua = Pilimage.open(
            os.path.join('images', "button_strt_scan.png"))
        scan_1_file_ua = scan_1_file_ua.resize(
            (210, 30), Pilimage.Resampling.LANCZOS)
        self.scan_1_file_ua_210 = ImageTk.PhotoImage(scan_1_file_ua)

        in_progress = Pilimage.open(os.path.join('images', "in_progress.png"))
        in_progress = in_progress.resize(
            (180, 35), Pilimage.Resampling.LANCZOS)
        self.in_progress = ImageTk.PhotoImage(in_progress)

        browse_dir = Pilimage.open(os.path.join('images', "browse_dir.png"))
        browse_dir = browse_dir.resize((30, 30), Pilimage.Resampling.LANCZOS)
        self.browse_dir = ImageTk.PhotoImage(browse_dir)

        browse_file = Pilimage.open(os.path.join('images', "browse_file.jpg"))
        browse_file = browse_file.resize((40, 30), Pilimage.Resampling.LANCZOS)
        self.browse_file1 = ImageTk.PhotoImage(browse_file)

        for_change_bg_en = Pilimage.open(
            os.path.join('images', "background_en.png"))
        for_change_bg_en = for_change_bg_en.resize(
            (140, 42), Pilimage.Resampling.LANCZOS)
        self.for_change_bg_en = ImageTk.PhotoImage(for_change_bg_en)

        for_change_bg_ua = Pilimage.open(
            os.path.join('images', "background_ua.png"))
        for_change_bg_ua = for_change_bg_ua.resize(
            (140, 40), Pilimage.Resampling.LANCZOS)
        self.for_change_bg_ua = ImageTk.PhotoImage(for_change_bg_ua)

        for_quit = Pilimage.open(os.path.join('images', "quit_en.png"))
        for_quit = for_quit.resize((100, 40), Pilimage.Resampling.LANCZOS)
        self.for_quit = ImageTk.PhotoImage(for_quit)

        for_quit_ua = Pilimage.open(os.path.join('images', "quit_ua.png"))
        for_quit_ua = for_quit_ua.resize(
            (100, 43), Pilimage.Resampling.LANCZOS)
        self.for_quit_ua = ImageTk.PhotoImage(for_quit_ua)

        flag_ua = Pilimage.open(os.path.join('images', "flag_ua.png"))
        flag_ua = flag_ua.resize((35, 25), Pilimage.Resampling.LANCZOS)
        self.flag_ua = ImageTk.PhotoImage(flag_ua)

        flag_en = Pilimage.open(os.path.join('images', "flag_en.png"))
        flag_en = flag_en.resize((35, 25), Pilimage.Resampling.LANCZOS)
        self.flag_en = ImageTk.PhotoImage(flag_en)

        language_label_ua = Pilimage.open(
            os.path.join('images', "language_ua_btn.png"))
        language_label_ua = language_label_ua.resize(
            (144, 40), Pilimage.Resampling.LANCZOS)
        self.language_label_ua = ImageTk.PhotoImage(language_label_ua)

        language_label_en = Pilimage.open(
            os.path.join('images', "language_en_btn.png"))
        language_label_en = language_label_en.resize(
            (144, 40), Pilimage.Resampling.LANCZOS)
        self.language_label_en = ImageTk.PhotoImage(language_label_en)


# ---------------------------------- Black theme -------------------------

        bg1_black = Pilimage.open(
            os.path.join(
                'images',
                "light_theme_black.png"))
        bg1_black = bg1_black.resize((30, 30), Pilimage.Resampling.LANCZOS)
        self.photo1_black = ImageTk.PhotoImage(bg1_black)

        bg2_black = Pilimage.open(
            os.path.join(
                'images',
                "black_theme_black.png"))
        bg2_black = bg2_black.resize((30, 30), Pilimage.Resampling.LANCZOS)
        self.photo2_black = ImageTk.PhotoImage(bg2_black)

        start_scanning_black = Pilimage.open(
            os.path.join('images', "button_strt_scan_black.png"))
        start_scanning_black = start_scanning_black.resize(
            (222, 35), Pilimage.Resampling.LANCZOS)
        self.start_scanning_black = ImageTk.PhotoImage(start_scanning_black)

        img_black = Pilimage.open(os.path.join('images', "settings_black.png"))
        img_black = img_black.resize((80, 75), Pilimage.Resampling.LANCZOS)
        self.photo_image_black = ImageTk.PhotoImage(img_black)

        non_recursive_black = Pilimage.open(
            os.path.join('images', "button_strt_scan_black.png"))
        non_recursive_black = non_recursive_black.resize(
            (190, 30), Pilimage.Resampling.LANCZOS)
        self.not_recursive_black = ImageTk.PhotoImage(non_recursive_black)

        non_recursive_ua_black = Pilimage.open(
            os.path.join('images', "button_strt_scan_black.png"))
        non_recursive_ua_black = non_recursive_ua_black.resize(
            (219, 30), Pilimage.Resampling.LANCZOS)
        self.not_recursive_ua_210_black = ImageTk.PhotoImage(
            non_recursive_ua_black)

        clear_scrollbar_black = Pilimage.open(
            os.path.join('images', "button_strt_scan_black.png"))
        clear_scrollbar_black = clear_scrollbar_black.resize(
            (100, 25), Pilimage.Resampling.LANCZOS)
        self.clear_scrollbar_black = ImageTk.PhotoImage(clear_scrollbar_black)

        scan_1_file_black = Pilimage.open(
            os.path.join('images', "button_strt_scan_black.png"))
        scan_1_file_black = scan_1_file_black.resize(
            (190, 30), Pilimage.Resampling.LANCZOS)
        self.scan_1_file_black = ImageTk.PhotoImage(scan_1_file_black)

        scan_1_file_ua_black = Pilimage.open(
            os.path.join('images', "button_strt_scan_black.png"))
        scan_1_file_ua_black = scan_1_file_ua_black.resize(
            (219, 30), Pilimage.Resampling.LANCZOS)
        self.scan_1_file_ua_210_black = ImageTk.PhotoImage(
            scan_1_file_ua_black)

        browse_dir_black = Pilimage.open(
            os.path.join('images', "browse_dir_black.png"))
        browse_dir_black = browse_dir_black.resize(
            (27, 27), Pilimage.Resampling.LANCZOS)
        self.browse_dir_black = ImageTk.PhotoImage(browse_dir_black)

        browse_file_black = Pilimage.open(
            os.path.join('images', "browse_file_black.png"))
        browse_file_black = browse_file_black.resize(
            (36, 27), Pilimage.Resampling.LANCZOS)
        self.browse_file1_black = ImageTk.PhotoImage(browse_file_black)

        for_change_bg_en_black = Pilimage.open(
            os.path.join('images', "background_en_black.png"))
        for_change_bg_en_black = for_change_bg_en_black.resize(
            (140, 35), Pilimage.Resampling.LANCZOS)
        self.for_change_bg_en_black = ImageTk.PhotoImage(
            for_change_bg_en_black)

        for_change_bg_ua_black = Pilimage.open(
            os.path.join('images', "background_ua_black.png"))
        for_change_bg_ua_black = for_change_bg_ua_black.resize(
            (113, 35), Pilimage.Resampling.LANCZOS)
        self.for_change_bg_ua_black = ImageTk.PhotoImage(
            for_change_bg_ua_black)

        for_quit_black = Pilimage.open(
            os.path.join('images', "quit_en_black.png"))
        for_quit_black = for_quit_black.resize(
            (100, 40), Pilimage.Resampling.LANCZOS)
        self.for_quit_black = ImageTk.PhotoImage(for_quit_black)

        for_quit_ua_black = Pilimage.open(
            os.path.join('images', "quit_ua_black.png"))
        for_quit_ua_black = for_quit_ua_black.resize(
            (100, 40), Pilimage.Resampling.LANCZOS)
        self.for_quit_ua_black = ImageTk.PhotoImage(for_quit_ua_black)

        language_label_ua_black = Pilimage.open(
            os.path.join('images', "language_ua_black.png"))
        language_label_ua_black = language_label_ua_black.resize(
            (117, 34), Pilimage.Resampling.LANCZOS)
        self.language_label_ua_black = ImageTk.PhotoImage(
            language_label_ua_black)

        language_label_en_black = Pilimage.open(
            os.path.join('images', "language_en_black.png"))
        language_label_en_black = language_label_en_black.resize(
            (144, 34), Pilimage.Resampling.LANCZOS)
        self.language_label_en_black = ImageTk.PhotoImage(
            language_label_en_black)




    def draw_widgets(self):

        config.read('parameters.ini', encoding='utf_8')
        self.for_canvas1 = Button(
            self.my_canvas1,
            width=500,
            height=500,
            bg="#141414",
            fg="#328bb8",
            activebackground="#141414",
            image=self.ccc,
            text=" i am here",
            font=(
                "Comic Sans MS",
                15),
            borderwidth=0,
            command=self.destr_canvas1,
            relief=SUNKEN)
        self.for_canvas1.place(x=0, y=0)
        self.my_canvas1_button = Button(
            self.my_canvas1,
            width=16,
            bg="#141414",
            fg="#76f589",
            text="#Protect yourself",
            borderwidth=0,
            font=(
                "Comic Sans MS",
                13))
        self.for_canvas1.place(x=0, y=0)

        self.mainButton = Button(
            self.my_canvas,
            width=215,
            height=35,
            image=self.start_scanning,
            text=config["text"]["recursive_scanning"],
            bg=config["images"]["color"],
            fg="white",
            activebackground=config["images"]["color"],
            borderwidth=0,
            border=0,
            font=(
                "Arya",
                14),
            command=self.main_func_to_be_threatened,
            compound=CENTER)

        self.mainButton.place(x=143, y=200)

        self.settingsButton = Button(
            self.my_canvas,
            image=self.photo_image,
            bg=config["images"]["color"],
            activebackground=config["images"]["color"],
            command=self.settings_func_to_be_threatened,
            borderwidth=0,
            border=0)
        self.settingsButton.place(x=410, y=8)

        self.choice_for_non_recursive = IntVar()

        self.choice_for_one_file = IntVar()

        self.non_recursive = Checkbutton(
            self.my_canvas,
            width=int(
                config["btn_settings"]["width"]),
            text=config["text"]["non-recursive"],
            justify=CENTER,
            compound=CENTER,
            height=25,
            bg=config["images"]["color"],
            fg="white",
            activebackground=config["images"]["color"],
            font=(
                "Arya",
                13),
            image=self.not_recursive,
            variable=self.choice_for_non_recursive,
            command=self.check,
            borderwidth=0,
            border=0)
        self.non_recursive.place(x=11, y=8)

        self.one_file = Checkbutton(
            self.my_canvas,
            width=int(
                config["btn_settings"]["width"]),
            height=25,
            image=self.scan_1_file,
            text=config["text"]["one_file_scanning"],
            justify=CENTER,
            compound=CENTER,
            font=(
                "Arya",
                13),
            bg=config["images"]["color"],
            fg="white",
            activebackground=config["images"]["color"],
            variable=self.choice_for_one_file,
            command=self.check2,
            borderwidth=0,
            border=0)
        self.one_file.place(x=11, y=50)

        self.entry = Entry(
            self.my_canvas,
            width=29,
            fg="#D64769",
            bg=config["images"]["color"],
            relief=GROOVE,
            bd=3,
            font=(
                "Arya",
                13,
                "bold"))
        self.entry.place(x=120, y=250)
        self.entry.insert(0, config["text"]["entered_path"])

        self.browse_directory = Button(
            self.my_canvas,
            width=30,
            height=30,
            image=self.browse_dir,
            bg=config["images"]["color"],
            fg=config["images"]["color"],
            activebackground=config["images"]["color"],
            border=0,
            borderwidth=0,
            command=self.choose_directory)
        if config["images"]["bg"] == "light_bg.jpg":
            self.browse_directory.place(x=400, y=245)
        elif config["images"]["bg"] == "black_bg.jpg":
            self.browse_directory.place(x=400, y=247)

        self.browse_file = Button(
            self.my_canvas,
            width=40,
            height=30,
            image=self.browse_file1,
            bg=config["images"]["color"],
            fg=config["images"]["color"],
            activebackground=config["images"]["color"],
            activeforeground=config["images"]["color"],
            border=0,
            borderwidth=0,
            command=self.choose_file)

        self.scroll_text = ScrolledText(
            self.my_canvas,
            width=51,
            height=6,
            bg="#FFFB97",
            font=(
                "Arya",
                12),
            wrap=WORD)
        self.del_scroll_text = Button(
            self.my_canvas,
            image=self.clear_scrollbar,
            width=100,
            height=25,
            text=config["text"]["clear"],
            font=(
                "Arya",
                12),
            bg=config["images"]["color"],
            fg="white",
            activebackground=config["images"]["color"],
            command=self.delete_scroll,
            compound=CENTER,
            justify=CENTER,
            borderwidth=0,
            border=0)


        if (config["images"]["bg"] ==
                "light_bg.jpg" and config["text"]["clear"] == "Clear all"):
            self.mainButton.configure(image=self.start_scanning)
            self.settingsButton.configure(image=self.photo_image)
            self.non_recursive.configure(image=self.not_recursive)
            self.one_file.configure(image=self.scan_1_file)
            self.browse_directory.configure(image=self.browse_dir)
            self.browse_file.configure(image=self.browse_file1)
            self.del_scroll_text.configure(image=self.clear_scrollbar)
            self.scroll_text.configure(bg="#FCF0F0")

        elif(config["images"]["bg"] == "light_bg.jpg" and config["text"]["clear"] == "Очистити"):
            self.mainButton.configure(image=self.start_scanning)
            self.settingsButton.configure(image=self.photo_image)
            self.non_recursive.configure(image=self.not_recursive_ua_210)
            self.one_file.configure(image=self.scan_1_file_ua_210)
            self.browse_directory.configure(image=self.browse_dir)
            self.browse_file.configure(image=self.browse_file1)
            self.del_scroll_text.configure(image=self.clear_scrollbar)
            self.scroll_text.configure(bg="#FCF0F0")


        if (config["images"]["bg"] ==
                "black_bg.jpg" and config["text"]["clear"] == "Clear all"):
            self.mainButton.configure(image=self.start_scanning_black)
            self.settingsButton.configure(image=self.photo_image_black)
            self.non_recursive.configure(image=self.not_recursive_black)
            self.one_file.configure(image=self.scan_1_file_black)
            self.browse_directory.configure(image=self.browse_dir_black)
            self.browse_file.configure(image=self.browse_file1_black)
            self.del_scroll_text.configure(image=self.clear_scrollbar_black)
            self.scroll_text.configure(bg="#FFFB97")

        elif(config["images"]["bg"] == "black_bg.jpg" and config["text"]["clear"] == "Очистити"):
            self.mainButton.configure(image=self.start_scanning_black)
            self.settingsButton.configure(image=self.photo_image_black)
            self.non_recursive.configure(image=self.not_recursive_ua_210_black)
            self.one_file.configure(image=self.scan_1_file_ua_210_black)
            self.browse_directory.configure(image=self.browse_dir_black)
            self.browse_file.configure(image=self.browse_file1_black)
            self.del_scroll_text.configure(image=self.clear_scrollbar_black)
            self.scroll_text.configure(bg="#FFFB97")




    def destr_canvas1(self):
        self.my_canvas1.destroy()




    def check(self):
        config.read('parameters.ini', encoding='utf_8')
        if self.choice_for_non_recursive.get():

            self.non_recursive.configure(fg="black")

            self.browse_file.configure(
                bg=config["images"]["color"],
                activebackground=config["images"]["color"])

            self.mainButton.configure(
                text=config["text"]["start_scanning"],
                command=self.non_recursive_threatened)

            self.one_file.place_forget()


        else:
            config.read('parameters.ini', encoding='utf_8')
            self.non_recursive.configure(fg="white")

            self.mainButton.configure(
                text=config["text"]["recursive_scanning"],
                command=self.main_func_to_be_threatened)
            self.one_file.place(x=11, y=50)




    def check2(self):

        config.read('parameters.ini', encoding='utf_8')

        if self.choice_for_one_file.get():
            self.one_file.configure(fg="black")
            self.non_recursive.place_forget()

            self.mainButton.configure(
                text=config["text"]["start_scanning"],
                command=self.one_file_threatened)

            self.browse_directory.place_forget()

            if config["images"]["bg"] == "light_bg.jpg":
                if counter2 > 0:
                    self.browse_file.place(x=400, y=309)
                else:
                    self.browse_file.place(x=400, y=245)


            elif config["images"]["bg"] == "black_bg.jpg":
                if counter2 > 0:
                    self.browse_file.place(x=400, y=311)
                else:
                    self.browse_file.place(x=400, y=247)


        else:
            config.read('parameters.ini', encoding='utf_8')
            self.one_file.configure(fg="white")

            self.mainButton.configure(
                text=config["text"]["recursive_scanning"],
                command=self.main_func_to_be_threatened)

            self.non_recursive.place(x=11, y=8)

            if config["images"]["bg"] == "light_bg.jpg":
                if counter2 > 0:
                    self.browse_directory.place(x=400, y=309)
                else:
                    self.browse_directory.place(x=400, y=245)
                self.browse_file.place_forget()


            if config["images"]["bg"] == "black_bg.jpg":
                if counter2 > 0:
                    self.browse_directory.place(x=400, y=311)
                else:
                    self.browse_directory.place(x=400, y=247)
                self.browse_file.place_forget()




    def quit_or_no(self):
        choice = messagebox.askyesno(
            config["btn_settings"]["quit_msg1"],
            config["btn_settings"]["quit_msg2"])
        if choice:
            self.root.quit()




    def recursive_scannig(self):
        config.read('parameters.ini', encoding='utf_8')
        config["text"]["entered_path"] = str(self.entry.get())
        with open('parameters.ini', 'w', encoding='utf_8') as configfile:
            config.write(configfile)

        if os.path.isdir(self.entry.get()):
            try:
                self.mainButton.configure(
                    text=config["btn_settings"]["in_progress"],
                    image=self.in_progress)

                find_malware_files(self)

                if (self.choice_for_non_recursive.get()
                        and config["images"]["bg"] == "light_bg.jpg"):
                    self.mainButton.configure(
                        image=self.start_scanning,
                        text=config["text"]["start_scanning"])

                elif (self.choice_for_one_file.get() and config["images"]["bg"] == "light_bg.jpg"):
                    self.mainButton.configure(
                        image=self.start_scanning,
                        text=config["text"]["start_scanning"])

                elif (self.one_file["state"] == tkinter.NORMAL and self.non_recursive["state"] == tkinter.NORMAL and config["images"]["bg"] == "light_bg.jpg"):
                    self.mainButton.configure(
                        image=self.start_scanning,
                        text=config["text"]["recursive_scanning"])


                if (self.choice_for_non_recursive.get()
                        and config["images"]["bg"] == "black_bg.jpg"):
                    self.mainButton.configure(
                        image=self.start_scanning_black,
                        text=config["text"]["start_scanning"])

                elif (self.choice_for_one_file.get() and config["images"]["bg"] == "black_bg.jpg"):
                    self.mainButton.configure(
                        image=self.start_scanning_black,
                        text=config["text"]["start_scanning"])

                elif (self.one_file["state"] == tkinter.NORMAL and self.non_recursive["state"] == tkinter.NORMAL and config["images"]["bg"] == "black_bg.jpg"):
                    self.mainButton.configure(
                        image=self.start_scanning_black,
                        text=config["text"]["recursive_scanning"])


            except BaseException:

                if (self.choice_for_non_recursive.get()
                        and config["images"]["bg"] == "light_bg.jpg"):
                    self.mainButton.configure(
                        image=self.start_scanning,
                        text=config["text"]["start_scanning"])

                elif (self.choice_for_one_file.get() and config["images"]["bg"] == "light_bg.jpg"):
                    self.mainButton.configure(
                        image=self.start_scanning,
                        text=config["text"]["start_scanning"])

                elif (self.one_file["state"] == tkinter.NORMAL and self.non_recursive["state"] == tkinter.NORMAL and config["images"]["bg"] == "light_bg.jpg"):
                    self.mainButton.configure(
                        image=self.start_scanning,
                        text=config["text"]["recursive_scanning"])


                if (self.choice_for_non_recursive.get()
                        and config["images"]["bg"] == "black_bg.jpg"):
                    self.mainButton.configure(
                        image=self.start_scanning_black,
                        text=config["text"]["start_scanning"])

                elif (self.choice_for_one_file.get() and config["images"]["bg"] == "black_bg.jpg"):
                    self.mainButton.configure(
                        image=self.start_scanning_black,
                        text=config["text"]["start_scanning"])

                elif (self.one_file["state"] == tkinter.NORMAL and self.non_recursive["state"] == tkinter.NORMAL and config["images"]["bg"] == "black_bg.jpg"):
                    self.mainButton.configure(
                        image=self.start_scanning_black,
                        text=config["text"]["recursive_scanning"])


                if config["btn_settings"]["width"] == "190":
                    messagebox.showerror(
                        "Error", str(
                            sys.exc_info()[1]) + "\n" + "Please, change permissions in the file explorer")

                elif config["btn_settings"]["width"] == "210":
                    messagebox.showerror(
                        "Помилка", str(
                            sys.exc_info()[1]) + "\n" + "Будь ласка, змініть дозволи у файловому провіднику")


        else:

            if config["btn_settings"]["width"] == "190":
                messagebox.showerror(
                    "Error", "Please, enter the path correctly")

            elif config["btn_settings"]["width"] == "210":
                messagebox.showerror(
                    "Помилка", "Будь ласка, вкажіть шлях коректно")




    def scan_one_file(self):

        if os.path.isfile(self.entry.get()):
            try:

                self.mainButton.configure(
                    text=config["btn_settings"]["in_progress"],
                    image=self.in_progress)

                check_one_file(self)

                if (self.choice_for_non_recursive.get()
                        and config["images"]["bg"] == "light_bg.jpg"):
                    self.mainButton.configure(
                        image=self.start_scanning,
                        text=config["text"]["start_scanning"])

                elif (self.choice_for_one_file.get() and config["images"]["bg"] == "light_bg.jpg"):
                    self.mainButton.configure(
                        image=self.start_scanning,
                        text=config["text"]["start_scanning"])

                elif (self.one_file["state"] == tkinter.NORMAL and self.non_recursive["state"] == tkinter.NORMAL and config["images"]["bg"] == "light_bg.jpg"):
                    self.mainButton.configure(
                        image=self.start_scanning,
                        text=config["text"]["recursive_scanning"])


                if (self.choice_for_non_recursive.get()
                        and config["images"]["bg"] == "black_bg.jpg"):
                    self.mainButton.configure(
                        image=self.start_scanning_black,
                        text=config["text"]["start_scanning"])

                elif (self.choice_for_one_file.get() and config["images"]["bg"] == "black_bg.jpg"):
                    self.mainButton.configure(
                        image=self.start_scanning_black,
                        text=config["text"]["start_scanning"])

                elif (self.one_file["state"] == tkinter.NORMAL and self.non_recursive["state"] == tkinter.NORMAL and config["images"]["bg"] == "black_bg.jpg"):
                    self.mainButton.configure(
                        image=self.start_scanning_black,
                        text=config["text"]["recursive_scanning"])


            except BaseException:

                if (self.choice_for_non_recursive.get()
                        and config["images"]["bg"] == "light_bg.jpg"):
                    self.mainButton.configure(
                        image=self.start_scanning,
                        text=config["text"]["start_scanning"])

                elif (self.choice_for_one_file.get() and config["images"]["bg"] == "light_bg.jpg"):
                    self.mainButton.configure(
                        image=self.start_scanning,
                        text=config["text"]["start_scanning"])

                elif (self.one_file["state"] == tkinter.NORMAL and self.non_recursive["state"] == tkinter.NORMAL and config["images"]["bg"] == "light_bg.jpg"):
                    self.mainButton.configure(
                        image=self.start_scanning,
                        text=config["text"]["recursive_scanning"])


                if (self.choice_for_non_recursive.get()
                        and config["images"]["bg"] == "black_bg.jpg"):
                    self.mainButton.configure(
                        image=self.start_scanning_black,
                        text=config["text"]["start_scanning"])

                elif (self.choice_for_one_file.get() and config["images"]["bg"] == "black_bg.jpg"):
                    self.mainButton.configure(
                        image=self.start_scanning_black,
                        text=config["text"]["start_scanning"])

                elif (self.one_file["state"] == tkinter.NORMAL and self.non_recursive["state"] == tkinter.NORMAL and config["images"]["bg"] == "black_bg.jpg"):
                    self.mainButton.configure(
                        image=self.start_scanning_black,
                        text=config["text"]["recursive_scanning"])


                if config["btn_settings"]["width"] == "190":
                    messagebox.showerror(
                        "Error", str(
                            sys.exc_info()[1]) + "\n" + "Please, change permissions in the file explorer")

                elif config["btn_settings"]["width"] == "210":
                    messagebox.showerror(
                        "Помилка", str(
                            sys.exc_info()[1]) + "\n" + "Будь ласка, змініть дозволи у файловому провіднику")


        else:

            if config["btn_settings"]["width"] == "190":
                messagebox.showerror(
                    "Error", "Please, enter the path correctly")

            elif config["btn_settings"]["width"] == "210":
                messagebox.showerror(
                    "Помилка", "Будь ласка, вкажіть шлях коректно")




    def main_func_to_be_threatened(self):
        t1 = threading.Thread(target=self.recursive_scannig, daemon=TRUE)
        t1.start()




    def non_recursive_threatened(self):
        t2 = threading.Thread(target=self.recursive_scannig, daemon=TRUE)
        t2.start()




    def one_file_threatened(self):
        t3 = threading.Thread(target=self.scan_one_file, daemon=TRUE)
        t3.start()




    def settings_func_to_be_threatened(self):
        threading.Thread(
            target=self.settings_button_action,
            daemon=TRUE).start()




    def choose_file(self):
        file = filedialog.askopenfile(mode='r')
        if file:
            filepath = os.path.abspath(file.name)
            self.entry.delete(0, END)
            self.entry.insert(0, str(filepath))




    def choose_directory(self):
        dii = filedialog.askdirectory(initialdir='r')
        if dii:
            diipath = os.path.abspath(dii)
            self.entry.delete(0, END)
            self.entry.insert(0, str(diipath))




    def settings_button_action(self):
        global kh, cpu_load, change_bg_en, fon1, fon2, quitButton, change_lang_UA, change_lang_EN, language_en, counter, counter2

        if fon1 is None:
            counter2 += 1
            config.read('parameters.ini', encoding='utf_8')
            change_bg_en = Button(
                self.my_canvas,
                width=140,
                height=40,
                bg=config["images"]["color"],
                fg=config["images"]["color"],
                activebackground=config["images"]["color"],
                activeforeground=config["images"]["color"],
                borderwidth=0,
                border=0,
                compound=CENTER,
                justify=CENTER,
                relief=SUNKEN)
            change_bg_en.place(x=347, y=167)

            language_en = Button(
                self.my_canvas,
                width=144,
                height=40,
                fg=config["images"]["color"],
                bg=config["images"]["color"],
                activeforeground=config["images"]["color"],
                activebackground=config["images"]["color"],
                borderwidth=0,
                border=0,
                compound=CENTER,
                justify=CENTER,
                relief=SUNKEN)
            language_en.place(x=345, y=95)

            fon1 = Button(
                self.my_canvas,
                image=self.photo1,
                bg=config["images"]["color"],
                width=40,
                height=30,
                activebackground=config["images"]["color"],
                borderwidth=0,
                border=0,
                command=lambda: self.changebg("light_bg.jpg"))
            fon1.place(x=370, y=212)

            fon2 = Button(
                self.my_canvas,
                image=self.photo2,
                bg=config["images"]["color"],
                width=30,
                height=30,
                activebackground=config["images"]["color"],
                borderwidth=0,
                border=0,
                command=lambda: self.changebg("black_bg.jpg"))
            fon2.place(x=420, y=212)

            change_lang_UA = Button(
                self.my_canvas,
                image=self.flag_ua,
                width=35,
                height=25,
                bg=config["images"]["color"],
                activebackground=config["images"]["color"],
                borderwidth=0,
                border=0,
                command=self.change_lang_ua)
            change_lang_UA.place(x=365, y=140)

            change_lang_EN = Button(
                self.my_canvas,
                image=self.flag_en,
                width=35,
                height=25,
                bg=config["images"]["color"],
                activebackground=config["images"]["color"],
                borderwidth=0,
                border=0,
                command=self.change_lang_en)
            change_lang_EN.place(x=435, y=140)

            quitButton = Button(
                self.my_canvas,
                width=100,
                height=40,
                fg=config["images"]["color"],
                bg=config["images"]["color"],
                activebackground=config["images"]["color"],
                activeforeground="black",
                borderwidth=0,
                border=0,
                command=self.quit_or_no,
                justify=CENTER,
                compound=CENTER)
            quitButton.place(x=385, y=249)

            self.mainButton.place(x=143, y=265)
            self.entry.place(x=120, y=314)

            if (self.choice_for_one_file.get()
                    and config["images"]["bg"] == "light_bg.jpg"):
                self.browse_file.place(x=400, y=309)

            elif (self.choice_for_one_file.get() == 0 and config["images"]["bg"] == "light_bg.jpg"):
                self.browse_directory.place(x=400, y=309)


            if (self.choice_for_one_file.get()
                    and config["images"]["bg"] == "black_bg.jpg"):
                self.browse_file.place(x=400, y=311)

            elif (self.choice_for_one_file.get() == 0 and config["images"]["bg"] == "black_bg.jpg"):
                self.browse_directory.place(x=400, y=311)


            if (config["images"]["bg"] ==
                    "light_bg.jpg" and config["text"]["clear"] == "Clear all"):
                change_bg_en.configure(image=self.for_change_bg_en)
                language_en.configure(image=self.language_label_en)
                quitButton.configure(image=self.for_quit)
                fon1.configure(image=self.photo1)
                fon2.configure(image=self.photo2)

            elif (config["images"]["bg"] == "light_bg.jpg" and config["text"]["clear"] == "Очистити"):
                change_bg_en.configure(image=self.for_change_bg_ua)
                language_en.configure(image=self.language_label_ua)
                quitButton.configure(image=self.for_quit_ua)
                fon1.configure(image=self.photo1)
                fon2.configure(image=self.photo2)


            if (config["images"]["bg"] ==
                    "black_bg.jpg" and config["text"]["clear"] == "Clear all"):
                change_bg_en.configure(image=self.for_change_bg_en_black)
                language_en.configure(image=self.language_label_en_black)
                quitButton.configure(image=self.for_quit_black)
                fon1.configure(image=self.photo1_black)
                fon2.configure(image=self.photo2_black)

            elif (config["images"]["bg"] == "black_bg.jpg" and config["text"]["clear"] == "Очистити"):
                change_bg_en.configure(image=self.for_change_bg_ua_black)
                language_en.configure(image=self.language_label_ua_black)
                quitButton.configure(image=self.for_quit_ua_black)
                fon1.configure(image=self.photo1_black)
                fon2.configure(image=self.photo2_black)


        if kh == 1:
            kh = 0

            if counter == 0:
                self.mainButton.place(x=143, y=200)
                self.entry.place(x=120, y=250)

                if (config["images"]["bg"] == "light_bg.jpg"):
                    if self.choice_for_one_file.get():
                        self.browse_file.place(x=400, y=245)
                    else:
                        self.browse_directory.place(x=400, y=245)


                if (config["images"]["bg"] == "black_bg.jpg"):
                    if self.choice_for_one_file.get():
                        self.browse_file.place(x=400, y=247)
                    else:
                        self.browse_directory.place(x=400, y=247)

            change_bg_en.place_forget()
            change_bg_en = None

            fon1.place_forget()
            fon1 = None

            fon2.place_forget()
            fon2 = None

            quitButton.place_forget()
            quitButton = None

            change_lang_UA.place_forget()
            change_lang_UA = None

            change_lang_EN.place_forget()
            change_lang_EN = None

            language_en.place_forget()
            language_en = None

            counter2 = 0


        else:
            kh += 1




    def delete_scroll(self):
        self.scroll_text.delete("1.0", END)
        self.scroll_text.place_forget()
        self.del_scroll_text.place_forget()




    def changebg(self, new_bg):
        global change_bg_en, fon1, fon2, change_lang_EN, change_lang_UA, language_en, quitButton
        config.read('parameters.ini', encoding='utf_8')
        bg = Pilimage.open(os.path.join('images', new_bg))
        bg = bg.resize((500, 500), Pilimage.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(bg)

        if new_bg == "light_bg.jpg":

            if self.choice_for_one_file.get():
                self.browse_file.place(x=400, y=309)

            else:
                self.browse_directory.place(x=400, y=309)
            config["images"]["color"] = "white"
            self.scroll_text.configure(bg="#FCF0F0")


            if config["text"]["clear"] == "Clear all":
                self.mainButton.configure(image=self.start_scanning)
                self.settingsButton.configure(image=self.photo_image)
                self.non_recursive.configure(image=self.not_recursive)
                self.one_file.configure(image=self.scan_1_file)
                self.browse_directory.configure(image=self.browse_dir)
                self.browse_file.configure(image=self.browse_file1)
                self.del_scroll_text.configure(image=self.clear_scrollbar)
                change_bg_en.configure(image=self.for_change_bg_en)
                language_en.configure(image=self.language_label_en)
                quitButton.configure(image=self.for_quit)
                fon1.configure(image=self.photo1)
                fon2.configure(image=self.photo2)

            elif config["text"]["clear"] == "Очистити":
                self.mainButton.configure(image=self.start_scanning)
                self.settingsButton.configure(image=self.photo_image)
                self.non_recursive.configure(image=self.not_recursive_ua_210)
                self.one_file.configure(image=self.scan_1_file_ua_210)
                self.browse_directory.configure(image=self.browse_dir)
                self.browse_file.configure(image=self.browse_file1)
                self.del_scroll_text.configure(image=self.clear_scrollbar)
                change_bg_en.configure(image=self.for_change_bg_ua)
                language_en.configure(image=self.language_label_ua)
                quitButton.configure(image=self.for_quit_ua)
                fon1.configure(image=self.photo1)
                fon2.configure(image=self.photo2)


        elif new_bg == "black_bg.jpg":

            if self.choice_for_one_file.get():
                self.browse_file.place(x=400, y=311)
            else:
                self.browse_directory.place(x=400, y=311)
            config["images"]["color"] = "#0a0217"
            self.scroll_text.configure(bg="#FFFB97")


            if config["text"]["clear"] == "Clear all":
                self.mainButton.configure(image=self.start_scanning_black)
                self.settingsButton.configure(image=self.photo_image_black)
                self.non_recursive.configure(image=self.not_recursive_black)
                self.one_file.configure(image=self.scan_1_file_black)
                self.browse_directory.configure(image=self.browse_dir_black)
                self.browse_file.configure(image=self.browse_file1_black)
                self.del_scroll_text.configure(
                    image=self.clear_scrollbar_black)
                change_bg_en.configure(image=self.for_change_bg_en_black)
                language_en.configure(image=self.language_label_en_black)
                quitButton.configure(image=self.for_quit_black)
                fon1.configure(image=self.photo1_black)
                fon2.configure(image=self.photo2_black)

            elif config["text"]["clear"] == "Очистити":
                self.mainButton.configure(image=self.start_scanning_black)
                self.settingsButton.configure(image=self.photo_image_black)
                self.non_recursive.configure(
                    image=self.not_recursive_ua_210_black)
                self.one_file.configure(image=self.scan_1_file_ua_210_black)
                self.browse_directory.configure(image=self.browse_dir_black)
                self.browse_file.configure(image=self.browse_file1_black)
                self.del_scroll_text.configure(
                    image=self.clear_scrollbar_black)
                change_bg_en.configure(image=self.for_change_bg_ua_black)
                language_en.configure(image=self.language_label_ua_black)
                quitButton.configure(image=self.for_quit_ua_black)
                fon1.configure(image=self.photo1_black)
                fon2.configure(image=self.photo2_black)


        config["images"]["bg"] = new_bg
        with open('parameters.ini', 'w', encoding='utf_8') as configfile:
            config.write(configfile)
        config.read('parameters.ini', encoding='utf_8')
        self.mainButton.configure(
            bg=config["images"]["color"],
            fg="white",
            activebackground=config["images"]["color"])

        self.settingsButton.configure(
            bg=config["images"]["color"],
            activebackground=config["images"]["color"])


        if self.choice_for_non_recursive.get():
            self.non_recursive.configure(
                bg=config["images"]["color"],
                fg="black",
                activebackground=config["images"]["color"])

        else:
            self.non_recursive.configure(
                bg=config["images"]["color"],
                fg="white",
                activebackground=config["images"]["color"],
                activeforeground="black")


        if self.choice_for_one_file.get():
            self.one_file.configure(
                bg=config["images"]["color"],
                fg="black",
                activebackground=config["images"]["color"])

        else:
            self.one_file.configure(
                bg=config["images"]["color"],
                fg="white",
                activebackground=config["images"]["color"])

        self.entry.configure(fg="#D64769", bg=config["images"]["color"])

        self.browse_directory.configure(
            bg=config["images"]["color"],
            fg=config["images"]["color"],
            activebackground=config["images"]["color"])

        self.browse_file.configure(
            bg=config["images"]["color"],
            activebackground=config["images"]["color"])

        self.del_scroll_text.configure(
            bg=config["images"]["color"],
            fg="white",
            activebackground=config["images"]["color"])

        change_bg_en.configure(
            bg=config["images"]["color"],
            fg="white",
            activebackground=config["images"]["color"],
            activeforeground=config["images"]["color"])

        language_en.configure(
            fg=config["images"]["color"],
            bg=config["images"]["color"],
            activeforeground=config["images"]["color"],
            activebackground=config["images"]["color"])

        fon1.configure(
            bg=config["images"]["color"],
            activebackground=config["images"]["color"])

        fon2.configure(
            bg=config["images"]["color"],
            activebackground=config["images"]["color"])

        change_lang_EN.configure(
            bg=config["images"]["color"],
            activebackground=config["images"]["color"])
        change_lang_UA.configure(
            bg=config["images"]["color"],
            activebackground=config["images"]["color"])

        quitButton.configure(
            bg=config["images"]["color"],
            fg="white",
            activebackground=config["images"]["color"],
            activeforeground=config["images"]["color"])

        self.my_canvas.create_image(0, 0, image=self.photo, anchor=NW)




    def change_lang_ua(self):
        config.read('parameters.ini', encoding='utf_8')
        config["text"]["non-recursive"] = "Нерекурсивне сканування"
        config["text"]["one_file_scanning"] = "Сканування одного файлу"
        config["text"]["recursive_scanning"] = "Рекурсивне сканування"
        config["text"]["start_scanning"] = "Розпочати сканування"
        config["text"]["clear"] = "Очистити"

        config["btn_settings"]["width"] = "210"

        config["btn_settings"]["quit_msg1"] = "Вихід"
        config["btn_settings"]["quit_msg2"] = "Впевнені, що бажаєте вийти?"

        config["btn_settings"]["in_progress"] = "У прогресі..."

        with open('parameters.ini', 'w', encoding='utf_8') as configfile:
            config.write(configfile)

        self.non_recursive.configure(
            text=config["text"]["non-recursive"],
            font=(
                "Arya",
                13))
        self.one_file.configure(
            text=config["text"]["one_file_scanning"], font=(
                "Arya", 13))

        self.del_scroll_text.configure(text=config["text"]["clear"])


        if config["images"]["bg"] == "light_bg.jpg":
            change_bg_en.configure(image=self.for_change_bg_ua)
            language_en.configure(image=self.language_label_ua)
            quitButton.configure(image=self.for_quit_ua)
            self.non_recursive.configure(
                width=config["btn_settings"]["width"],
                image=self.not_recursive_ua_210)
            self.one_file.configure(
                width=config["btn_settings"]["width"],
                image=self.scan_1_file_ua_210)


            if self.choice_for_non_recursive.get():
                self.mainButton.configure(
                    image=self.start_scanning,
                    text=config["text"]["start_scanning"])

            elif self.choice_for_one_file.get():
                self.mainButton.configure(
                    image=self.start_scanning,
                    text=config["text"]["start_scanning"])

            else:
                self.mainButton.configure(
                    image=self.start_scanning,
                    text=config["text"]["recursive_scanning"])


        if config["images"]["bg"] == "black_bg.jpg":
            change_bg_en.configure(image=self.for_change_bg_ua_black)
            language_en.configure(image=self.language_label_ua_black)
            quitButton.configure(image=self.for_quit_ua_black)
            self.non_recursive.configure(
                width=config["btn_settings"]["width"],
                image=self.not_recursive_ua_210_black)
            self.one_file.configure(
                width=config["btn_settings"]["width"],
                image=self.scan_1_file_ua_210_black)


            if self.choice_for_non_recursive.get():
                self.mainButton.configure(
                    image=self.start_scanning_black,
                    text=config["text"]["start_scanning"])

            elif self.choice_for_one_file.get():
                self.mainButton.configure(
                    image=self.start_scanning_black,
                    text=config["text"]["start_scanning"])

            else:
                self.mainButton.configure(
                    image=self.start_scanning_black,
                    text=config["text"]["recursive_scanning"])




    def change_lang_en(self):

        config.read('parameters.ini', encoding='utf_8')
        config["text"]["non-recursive"] = "Non-recursive scanning"
        config["text"]["one_file_scanning"] = "One file scanning"
        config["text"]["recursive_scanning"] = "Recursive scanning"
        config["text"]["start_scanning"] = "Start scanning"
        config["text"]["clear"] = "Clear all"

        config["btn_settings"]["width"] = "190"

        config["btn_settings"]["quit_msg1"] = "Quit"
        config["btn_settings"]["quit_msg2"] = "Are you sure you want to quit?"

        config["btn_settings"]["in_progress"] = "In progress..."

        with open('parameters.ini', 'w', encoding='utf_8') as configfile:
            config.write(configfile)

        self.non_recursive.configure(
            text=config["text"]["non-recursive"],
            font=(
                "Arya",
                13))
        self.one_file.configure(
            text=config["text"]["one_file_scanning"], font=(
                "Arya", 13))

        self.del_scroll_text.configure(text=config["text"]["clear"])


        if config["images"]["bg"] == "light_bg.jpg":
            change_bg_en.configure(image=self.for_change_bg_en)
            language_en.configure(image=self.language_label_en)
            quitButton.configure(image=self.for_quit)
            self.non_recursive.configure(width=190, image=self.not_recursive)
            self.one_file.configure(width=190, image=self.scan_1_file)


            if self.choice_for_non_recursive.get():
                self.mainButton.configure(
                    image=self.start_scanning, text="Start scanning")

            elif self.choice_for_one_file.get():
                self.mainButton.configure(
                    image=self.start_scanning, text="Start scanning")

            else:
                self.mainButton.configure(
                    image=self.start_scanning,
                    text=config["text"]["recursive_scanning"])


        if config["images"]["bg"] == "black_bg.jpg":
            change_bg_en.configure(image=self.for_change_bg_en_black)
            language_en.configure(image=self.language_label_en_black)
            quitButton.configure(image=self.for_quit_black)
            self.non_recursive.configure(
                width=190, image=self.not_recursive_black)
            self.one_file.configure(width=190, image=self.scan_1_file_black)


            if self.choice_for_non_recursive.get():
                self.mainButton.configure(
                    image=self.start_scanning_black,
                    text="Start scanning")

            elif self.choice_for_one_file.get():
                self.mainButton.configure(
                    image=self.start_scanning_black,
                    text="Start scanning")

            else:
                self.mainButton.configure(
                    image=self.start_scanning_black,
                    text=config["text"]["recursive_scanning"])




    def run(self):
        self.root.after(3000, self.destr_canvas1)
        self.draw_widgets()
        self.root.mainloop()




if __name__ == "__main__":
    window = Window(
        500,
        500,
        "Guard Lite",
        os.path.join(
            'images',
            "neapplogo.ico"))

    window.run()