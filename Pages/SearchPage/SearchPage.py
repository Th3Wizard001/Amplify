import tkinter as tk
from .Components.FilterFrame import FilterFrame
from Pages.MusicPage.Components.TitleFrame import TitleFrame
from .Components.MusicFrame import MusicFrame
from .Components.Content import Content

class SearchPage(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self['background'] = "yellow"

        self.titleFrame = tk.Frame(self,background="blue")
        self.contentFrame = tk.Frame(self,background="red")
        
        self.heading = tk.Label(self.titleFrame,text="Search",bg="#000000",foreground='white')

        self.filterFrame = FilterFrame(self.contentFrame,data=self.data())
        self.labelTitleFrame = TitleFrame(self.contentFrame)
        self.content = Content(self.contentFrame,data=self.data())


        self.titleFrame.grid(row=0, column=0 , sticky='nsew')
        self.heading.grid(row=0, column=0 , sticky='nsew')
        self.contentFrame.grid(row=1,column=0,sticky='nsew')
        self.filterFrame.grid(row=0,column=0,sticky='nsew')
        self.labelTitleFrame.grid(row=1,column=0,sticky='nsew')

        self.grid_rowconfigure(0,weight=3)
        self.grid_rowconfigure(1,weight=10)
        self.grid_columnconfigure(0,weight=1)
        self.contentFrame.grid_rowconfigure(0,weight=2)
        self.contentFrame.grid_rowconfigure(1,weight=1)
        self.contentFrame.grid_rowconfigure(2,weight=100)
        self.contentFrame.grid_columnconfigure(0,weight=1)
        # self.contentFrame.grid_columnconfigure(0,weight=1)

    def data(self):
        from Database.Database import all_songs
        # info = [
        #     {
        #         'genre': 'Workout',
        #         'location': 'https://firebasestorage.googleapis.com/v0/b/one-more-tk.appspot.com/o/tracks%2FThe%20Mission.mp3?alt=media&token=e549651c-c737-41d8-8eb5-9fd2fb06cc7e',
        #         'title': 'The Mission',
        #         'artist': 'Dread Pitt'
        #     },
        #     {
        #         'genre': 'WorkIn',
        #         'location': 'https://firebasestorage.googleapis.com/v0/b/one-more-tk.appspot.com/o/tracks%2FThe%20Mission.mp3?alt=media&token=e549651c-c737-41d8-8eb5-9fd2fb06cc7e',
        #         'title': 'The Kotkar',
        #         'artist': 'Dead Pitt'
        #     }

        # ]
        return all_songs
