"""
Shamus Murphy
Ewan Pedersen
Programming Final
"""

from tkinter import *
import pygame
import os

root = Tk()
root.title('MP3 Player')
root.geometry("600x400")

pygame.mixer.init()

menubar = Menu(root)
root.config(menu=menubar)

organize_menu = Menu(menubar)
organize_menu.add_command(label='Select Folder')

songlist = Listbox(root, bg="black", fg="white", width=100, height=15)
songlist.pack

play_button = PhotoImage(file='play.png')
pause_button = PhotoImage(file='pause.png')
next_button = PhotoImage(file='next.png')
back_button = PhotoImage(file='back.png')

control_frame = Frame(root)
control_frame.pack()

play_btn = Button(control_frame, image=play_button, borderwidth=0)
pause_btn = Button(control_frame, image=pause_button, borderwidth=0)
next_btn = Button(control_frame, image=next_button, borderwidth=0)
back_btn = Button(control_frame, image=back_button, borderwidth=0)

root.mainloop()