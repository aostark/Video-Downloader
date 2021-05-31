from playsound import *
from pytube import YouTube
import tkinter as tk
from os import path

WINDOW_WIDTH = 550
WINDOW_HEIGHT = 150
WINDOW_TITLE = "YouTube Video Downloader"
BUTTON_CLICK_SOUND = r"D:\PyCharm Community Edition 2020.3.1\PycharmProjects\VideoDownloader\click.mp3"


class VideoDownloader:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.window.configure(bg="#990000")
        self.window.title(WINDOW_TITLE)

        # Entry Labels Names
        self.link_label = tk.Label(self.window, text="Download link", font='Times 14')
        self.link_label.grid(column=0, row=0)
        self.name_label = tk.Label(self.window, text="Save File As", font='Times 14')
        self.name_label.grid(column=0, row=1)
        self.path_label = tk.Label(self.window, text="Save File Path", font='Times 14')
        self.path_label.grid(column=0, row=2)
        self.extension_label = tk.Label(self.window, text="File Extension", font='Times 14')
        self.extension_label.grid(column=0, row=3)

        # Create Entry
        self.link_entry = tk.Entry(master=self.window, width=65)
        self.link_entry.grid(column=1, row=0)
        self.name_entry = tk.Entry(master=self.window, width=65)
        self.name_entry.grid(column=1, row=1)
        self.path_entry = tk.Entry(master=self.window, width=65)
        self.path_entry.grid(column=1, row=2)
        self.extension_entry = tk.Entry(master=self.window, width=65)
        self.extension_entry.grid(column=1, row=3)

        # Download button
        self.download_button = tk.Button(self.window, text="Download", command=self.__get_link)
        self.download_button.grid(column=1, row=4)

    def downloader(self, link, save_path="", save_name="", extension=".mp4"):
        playsound(BUTTON_CLICK_SOUND)
        yt = YouTube(link)
        yt_stream = yt.streams.filter(file_extension=extension).order_by("resolution").desc().first()
        yt_stream.download(output_path=save_path, filename=save_name)

    def __get_link(self):
        link = self.link_entry.get()
        name = self.name_entry.get()
        path = self.path_entry.get()
        extension = self.extension_entry.get()

        self.downloader(link, path, name, extension)

    def run_app(self):
        self.window.mainloop()
        return


if __name__ == "__main__":
    app = VideoDownloader()
    app.run_app()
