import threading
from customtkinter import *
import tkinter as tk
from PIL import Image
from Functions import *
import pygame

class App():
    def __init__(self, root):
        root.title("Witam Pani Nejman!")
        root.iconbitmap("png/icon.ico")
        root.resizable(False, False)
        root.geometry("720x600")
        normalfont = CTkFont("Comic Sans MS", 25)
        bigfont = CTkFont("Comic Sans MS", 50)
        smallfont = CTkFont("Comis Sans MS", 12)
        smallbuttonfont = CTkFont("Comic Sans MS", 12)

        homeicon = Image.open("png/home.png")
        copyicon = Image.open("png/copy.png")
        spamicon = Image.open("png/spam.png")
        soundon  = Image.open("png/soundon.png")
        soundoff = Image.open("png/soundoff.png")
        goofygif = Image.open("png/goofy.gif")
        icon_size = (50, 50)
        homeImage =     CTkImage(dark_image=homeicon, size=icon_size)
        filecopyImage = CTkImage(dark_image=copyicon, size=icon_size)
        filespamImage = CTkImage(dark_image=spamicon, size=icon_size)
        soundonImage  = CTkImage(dark_image=soundon, size=icon_size)
        soundoffImage = CTkImage(dark_image=soundoff, size=icon_size)
        self.copyfrom = ""
        self.copyto = ""
        self.spamto = ""
        frames = goofygif.n_frames
        gifObject = [tk.PhotoImage(file=r"png/goofy.gif", format=f"gif -index {i}") for i in range(frames)]
        count = 0
        pygame.init()
        pygame.mixer.init()
        
        self.sound = pygame.mixer.Sound("png/goofysong.wav")
        self.isplaying = False
        self.sound.set_volume(0.5)

        def sound(self):
            if not self.isplaying:
                self.sidesoundButton.configure(image=soundonImage)
                self.sound.play()
                self.isplaying = True 
            else:
                self.sidesoundButton.configure(image=soundoffImage)
                self.sound.stop()
                self.isplaying = False
        def updatevolume(volume):
            self.sound.set_volume(volume)

        def gif(count, gifLabel: CTkLabel):
                newGif = gifObject[count]
                gifLabel.configure(image=newGif)
                count += 1
                if count == frames:
                    count = 0
                root.after(50, lambda: gif(count, gifLabel))

        def homePage():
            homeFrame = CTkFrame(mainFrame, fg_color="transparent")
            homeLabel = CTkLabel(homeFrame, 650, 80, font=bigfont, text="Witam na lekcji M3")
            gifLabel = CTkLabel(homeFrame, image="", text="")

            homeLabel.pack(side="top")
            gifLabel.pack(side="top", pady=10)
            homeFrame.pack()
            homeFrame.configure(width=570, height=480)

            gif(count, gifLabel)

        def filecopyPage():
            copyFrame1 = CTkFrame(mainFrame, fg_color="transparent")
            copyFrame2 = CTkFrame(mainFrame, fg_color="transparent")
            copyFrame3 = CTkFrame(mainFrame, fg_color="transparent")
            copyFrame4 = CTkFrame(mainFrame, fg_color="transparent")
            copyFrame5 = CTkFrame(mainFrame, fg_color="transparent")
            copyFrame6 = CTkFrame(mainFrame, fg_color="transparent")

            mainLabel = CTkLabel(copyFrame1, 540, 100, font=bigfont, text="File copy page")
            copyfromLabel = CTkLabel(copyFrame2, 270, 60, font=normalfont, text="Folder to copy from")
            self.copyfromButton = CTkButton(copyFrame2, 270, 60, font=normalfont, text="Pick folder", command=lambda: copyfromButton_command())
            copytoLabel = CTkLabel(copyFrame3, 270, 60, font=normalfont, text="Folder to copy to")
            self.copytoButton = CTkButton(copyFrame3, 270, 60, font=normalfont, text="Pick folder", command=lambda: copytoButton_command())
            copyextLabel = CTkLabel(copyFrame4, 270, 60, font=normalfont, text="Files with extension")
            copyextEntry = CTkEntry(copyFrame4, 270, 60, font=normalfont)
            copyButton = CTkButton(copyFrame5, 555, 60, font=normalfont, text="Start file copy", command=lambda: copyButton_command(self.copyfrom, self.copyto, copyextEntry.get()))

            mainLabel.pack(side="top", padx=5, pady=5)
            copyfromLabel.pack(side="left", padx=5, pady=5)
            self.copyfromButton.pack(side="left", padx=5, pady=5)
            copytoLabel.pack(side="left", padx=5, pady=5)
            self.copytoButton.pack(side="left", padx=5, pady=5)
            copyextLabel.pack(side="left", padx=5, pady=5)
            copyextEntry.pack(side="left", padx=5, pady=5)
            copyButton.pack(side="top", padx=5, pady=5)
            copyFrame1.pack(side="top")
            copyFrame2.pack(side="top")
            copyFrame3.pack(side="top")
            copyFrame4.pack(side="top")
            copyFrame5.pack(side="top")
            copyFrame6.pack(side="top", expand=True)

        def filespamPage():
            spamFrame1 = CTkFrame(mainFrame, fg_color="transparent")
            spamFrame2 = CTkFrame(mainFrame, fg_color="transparent")
            spamFrame3 = CTkFrame(mainFrame, fg_color="transparent")
            spamFrame3a = CTkFrame(spamFrame3, fg_color="transparent")
            spamFrame3b = CTkFrame(spamFrame3, fg_color="transparent")
            spamFrame4 = CTkFrame(mainFrame, fg_color="transparent")
            spamFrame5 = CTkFrame(mainFrame, fg_color="transparent")
            spamFrame6 = CTkFrame(mainFrame, fg_color="transparent")
            spamFrame7 = CTkFrame(mainFrame, fg_color="transparent")
            spamFrame8 = CTkFrame(mainFrame, fg_color="transparent")

            mainLabel = CTkLabel(spamFrame1, 540, 100, font=bigfont, text="File spam page")
            spamtoLabel = CTkLabel(spamFrame2, 270, 60, font=normalfont, text="Folder to spam to")
            self.spamtoButton = CTkButton(spamFrame2, 270, 60, font=normalfont, text="Pick folder", command=lambda: spamtoButton_command())
            spamnameLabel = CTkLabel(spamFrame3a, 270, 40, font=normalfont, text="Files name")
            spamnameRLabel = CTkLabel(spamFrame3a, 270, 20, font=smallfont, text="(random names if RANDOM)")
            spamnameEntry = CTkEntry(spamFrame3b, 270, 60, font=normalfont)
            spamextLabel = CTkLabel(spamFrame4, 270, 60, font=normalfont, text="Files extension")
            spamextEntry = CTkEntry(spamFrame4, 270, 60, font=normalfont)
            spamamountLabel = CTkLabel(spamFrame5, 270, 60, font=normalfont, text="Files number")
            spamamountEntry = CTkEntry(spamFrame5, 270, 60, font=normalfont)
            spamsizeLabel = CTkLabel(spamFrame6, 270, 60, font=normalfont, text="Single file size")
            spamsizeEntry = CTkEntry(spamFrame6, 135, 60, font=normalfont)
            spamsizeCombo = CTkComboBox(spamFrame6, 135, 60, font=normalfont, values=["B (Fast)", "KB", "MB", "GB (Slow)"], state="readonly")
            self.spamButton = CTkButton(spamFrame7, 555, 60, font=normalfont, text="Start file spam", command=lambda: spamButton_command(self.spamto, spamnameEntry.get(), spamextEntry.get(), int(spamamountEntry.get()), int(spamsizeEntry.get()), spamsizeCombo.get()))

            mainLabel.pack(side="top", padx=5, pady=5)
            spamtoLabel.pack(side="left", padx=5, pady=5)
            self.spamtoButton.pack(side="left", padx=5, pady=5)
            spamnameLabel.pack(side="top", padx=5, pady=5)
            spamnameRLabel.pack(side="top")
            spamnameEntry.pack(side="left", padx=5, pady=5)
            spamextLabel.pack(side="left", padx=5, pady=5)
            spamextEntry.pack(side="left", padx=5, pady=5)
            spamamountLabel.pack(side="left", padx=5, pady=5)
            spamamountEntry.pack(side="left", padx=5, pady=5)
            spamsizeLabel.pack(side="left", padx=5, pady=5)
            spamsizeEntry.pack(side="left")
            spamsizeCombo.pack(side="left")
            self.spamButton.pack(side="top", padx=5, pady=5)
            spamFrame1.pack(side="top")
            spamFrame2.pack(side="top")
            spamFrame3.pack(side="top")
            spamFrame3a.pack(side="left")
            spamFrame3b.pack(side="left")
            spamFrame4.pack(side="top")
            spamFrame5.pack(side="top")
            spamFrame6.pack(side="top")
            spamFrame7.pack(side="top")
            spamFrame8.pack(side="top", expand=True)

            spamnameEntry.insert(0, "file")
            spamextEntry.insert(0, "txt")
            spamamountEntry.insert(0, "10")
            spamsizeEntry.insert(0, "5")
            spamsizeCombo.set("KB")

        def openpage(page):
            delete()
            page()

        def copyfromButton_command():
            self.copyfrom = filedialog.askdirectory()
            text = str(self.copyfrom)
            if len(text) > 30:
                part1, part2 = text[:len(text)//2], text[len(text)//2:]
                textbutton = f"{part1}\n{part2}"
                fontbutton = smallbuttonfont
            else:
                textbutton = text
                fontbutton = normalfont
            self.copyfromButton.configure(text=textbutton, font=fontbutton)
        def copytoButton_command():
            self.copyto = filedialog.askdirectory()
            text = str(self.copyto)
            if len(text) > 30:
                part1, part2 = text[:len(text)//2], text[len(text)//2:]
                textbutton = f"{part1}\n{part2}"
                fontbutton = smallbuttonfont
            else:
                textbutton = text
                fontbutton = normalfont
            self.copytoButton.configure(text=textbutton, font=fontbutton)
        def copyButton_command(copyfrom, copyto, copyext):
            Functions.copy_files(copyfrom, copyto, copyext)

        def spamtoButton_command():
            self.spamto = filedialog.askdirectory()
            text = str(self.spamto)
            if len(text) > 30:
                part1, part2 = text[:len(text)//2], text[len(text)//2:]
                textbutton = f"{part1}\n{part2}"
                fontbutton = smallbuttonfont
            else:
                textbutton = text
                fontbutton = normalfont

            self.spamtoButton.configure(text=textbutton, font=fontbutton)
        def spamButton_command(spamto, filesname, spamext, amount, size, sizeunit):
            if sizeunit == "B (Fast)":
                size_multiplier = 1
            if sizeunit == "KB":
                size_multiplier = 1024
            elif sizeunit == "MB":
                size_multiplier = 1024 * 1024
            elif sizeunit == "GB (Slow)":
                size_multiplier = 1024 * 1024 * 1024

            filesize = size * size_multiplier
            Functions.create_files(spamto, filesname, spamext, amount, filesize)

        sidebarFrame = CTkFrame(root, fg_color="transparent")
        mainFrame = CTkFrame(root, fg_color="transparent")

        sidehomeButton =     CTkButton(sidebarFrame, 50, 50, 5, image=homeImage,     text="", command=lambda: openpage(homePage))
        sidefilecopyButton = CTkButton(sidebarFrame, 50, 50, 5, image=filecopyImage, text="", command=lambda: openpage(filecopyPage))
        sidefilespamButton = CTkButton(sidebarFrame, 50, 50, 5, image=filespamImage, text="", command=lambda: openpage(filespamPage))
        self.sidesoundButton = CTkButton(sidebarFrame, 50, 50, 0, image=soundoffImage, text="", command=lambda: threading.Thread(target=sound(self), daemon=True).start())
        self.sidesoundSlider = CTkSlider(sidebarFrame, 25, 150, 0, orientation="vertical", number_of_steps=100, command=updatevolume)

        sidehomeButton.pack(side="top", padx=5, pady=5)
        sidefilecopyButton.pack(side="top", padx=5, pady=5)
        sidefilespamButton.pack(side="top", padx=5, pady=5)
        self.sidesoundButton.pack(side="bottom", padx=5, pady=5)
        self.sidesoundSlider.pack(side="bottom", padx=5, pady=5)
        sidebarFrame.pack(side="left")
        sidebarFrame.pack_propagate(False)
        sidebarFrame.configure(width=70, height=600)
        mainFrame.pack(side="left", padx=5)
        mainFrame.configure(width=540, height=600)

        def delete():
            for frame in mainFrame.winfo_children():
                frame.destroy()

        openpage(homePage)

if __name__ == "__main__":
    root = CTk()
    app = App(root)
    root.mainloop()



# ZROBIC STOP