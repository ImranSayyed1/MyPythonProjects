from tkinter import *
from tkinter import filedialog

import pygame
import os


root = Tk()
root.title('Music Player')
root.geometry('700x500')

pygame.mixer.init()

menubar = Menu(root)
root.config(menu=menubar)

songs = []
curr_song = ""
paused = False


def select_music():
    global curr_song
    root.directory = filedialog.askdirectory()

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == '.mp3':
            songs.append(song)

    for song in songs:
        songlist.insert("end", song)

    songlist.selection_set(0)
    curr_song = songs[songlist.curselection()[0]]


def play_music():
    global curr_song, paused

    if not paused:
        pygame.mixer_music.load(os.path.join(root.directory, curr_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False



def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused = True


def next_music():
    global curr_song, paused

    try:
        songlist.select_clear(0, END)
        songlist.selection_set(songs.index(curr_song) + 1)
        curr_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass


def prev_music():
    global curr_song, paused

    try:
        songlist.select_clear(0, END)
        songlist.selection_set(songs.index(curr_song) - 1)
        curr_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass


def increaseVolume():
    global a
    a = pygame.mixer.music.get_volume()
    a += 0.1
    pygame.mixer.music.set_volume(a)


def decreaseVolume():
    global b
    b = pygame.mixer.music.get_volume()
    b -= 0.1
    pygame.mixer.music.set_volume(b)


Song = Menu(menubar, tearoff=False)
Song.add_command(label="Select Folder", command=select_music)
menubar.add_cascade(label="Songs", menu=Song)

songlist = Listbox(root, bg="violet", fg="black", width=100, height=20)
songlist.pack()

play_image = PhotoImage(file='play.png')
pause_image = PhotoImage(file='pause.png')
next_image = PhotoImage(file='next.png')
prev_image = PhotoImage(file='prev.png')
inc_image= PhotoImage(file = 'inc.png')
dec_image = PhotoImage(file = 'dec.png')

controls = Frame(root)
controls.pack()

play_btn = Button(controls, image=play_image, borderwidth=0, command=play_music)
pause_btn = Button(controls, image=pause_image, borderwidth=0, command=pause_music)
next_btn = Button(controls, image=next_image, borderwidth=0, command=next_music)
prev_btn = Button(controls, image=prev_image, borderwidth=0, command=prev_music)
increase_btn = Button(controls, image=inc_image,borderwidth=0,command=increaseVolume)
decrease_btn = Button(controls, image=dec_image,borderwidth=0,command=decreaseVolume)

play_btn.grid(row=0, column=1, padx=20, pady=50)
pause_btn.grid(row=0, column=2, padx=20, pady=50)
next_btn.grid(row=0, column=3, padx=20, pady=50)
prev_btn.grid(row=0, column=0, padx=20, pady=50)
increase_btn.grid(row=0, column=4, padx=20, pady=50)
decrease_btn.grid(row=0, column=5, padx=20, pady=50)

root.mainloop()


