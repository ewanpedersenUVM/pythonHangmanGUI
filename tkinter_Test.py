import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pygame

class MP3PlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MP3 Player")

        # Title
        title_label = tk.Label(root, text="Title: Test")
        title_label.pack()

        # Author
        author_label = tk.Label(root, text="Author: Test")
        author_label.pack()

        # Album Cover
        album_cover_label = tk.Label(root, text="Album Cover:")
        album_cover_label.pack()

        # Placeholder for album cover image (replace 'test' with actual image link)
        album_cover_image = tk.PhotoImage(file="test")
        album_cover_label = tk.Label(root, image=album_cover_image)
        album_cover_label.pack()

        # Buttons
        button_frame = ttk.Frame(root)
        button_frame.pack(side=tk.RIGHT, padx=10)

        play_button = ttk.Button(button_frame, text="Play", command=self.play)
        play_button.pack(pady=10)

        pause_button = ttk.Button(button_frame, text="Pause", command=self.pause)
        pause_button.pack(pady=10)

        stop_button = ttk.Button(button_frame, text="Stop", command=self.stop)
        stop_button.pack(pady=10)

        browse_button = ttk.Button(button_frame, text="Browse", command=self.browse_folder)
        browse_button.pack(pady=10)

        self.playlist = []  # Store the list of MP3 files
        self.current_index = 0  # Index of the currently playing MP3 file

        root.mainloop()

    def play(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_index])
            pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def stop(self):
        pygame.mixer.music.stop()

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.playlist = [os.path.join(folder_selected, file) for file in os.listdir(folder_selected) if file.endswith(".mp3")]
            if self.playlist:
                # Update title and author labels with the first file in the playlist
                self.update_metadata(self.playlist[0])
                self.current_index = 0

    def update_metadata(self, file_path):
        # This is a placeholder function. You may want to use a library like mutagen to extract metadata from the MP3 files.
        title_label.config(text=f"Title: {os.path.basename(file_path)}")
        author_label.config(text="Author: Test")  # You can replace this with actual author information.

if __name__ == "__main__":
    pygame.init()
    root = tk.Tk()
    app = MP3PlayerApp(root)
