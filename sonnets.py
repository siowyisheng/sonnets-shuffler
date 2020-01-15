import tkinter as tk
import tkinter.ttk as ttk
import requests
import random
import urllib.request
from PIL import Image, ImageTk
import io

from LabelLink import LabelLink


class App(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

        self.sonnets = self.get_sonnets()

        self.sonnet_number_category_frame = ttk.Frame(self)
        self.sonnet_number_category_frame.pack(anchor='w')
        self.sonnet_number = tk.StringVar()
        self.sonnet_number_label = ttk.Label(self.sonnet_number_category_frame,
                                             textvariable=self.sonnet_number)
        self.sonnet_number_label.pack(side=tk.LEFT)
        self.sonnet_category = tk.StringVar()
        self.sonnet_category_label = LabelLink(
            self.sonnet_number_category_frame,
            textvariable=self.sonnet_category)
        self.sonnet_category_label.pack(side=tk.LEFT)

        self.sonnet_title_frame = ttk.Frame(self, padding=(0, 0, 0, 20))
        self.sonnet_title_frame.pack()
        self.sonnet_title = tk.Text(self.sonnet_title_frame,
                                    width=50,
                                    height=1)
        self.sonnet_title.pack()
        self.sonnet_title.configure(font=("Helvetica", 12, 'bold'))

        self.text = tk.Text(self, width=50, height=14)
        self.text.pack()
        self.text.configure(font=("Helvetica", 12))

        self.show_new_sonnet()

        self.button_frame = ttk.Frame(self, padding=(0, 20, 0, 0))
        self.button_frame.pack()
        self.button = ttk.Button(self.button_frame,
                                 text='Shuffle',
                                 command=self.show_new_sonnet,
                                 padding='20 10')
        self.button.pack()

    def show_new_sonnet(self):
        chosen_sonnet = random.choice(self.sonnets)

        self.text.config(state=tk.NORMAL)
        self.text.delete(1.0, tk.END)
        for line in chosen_sonnet['lines']:
            self.text.insert(
                'end',
                line + '\n',
            )
        self.text.config(state=tk.DISABLED)

        full_title = chosen_sonnet['title']
        sonnet_number, *title_parts = full_title.split(': ')
        title = ''.join(title_parts)
        self.sonnet_number.set(sonnet_number)

        self.sonnet_title.config(state=tk.NORMAL)
        self.sonnet_title.delete(1.0, tk.END)
        self.sonnet_title.insert(
            'end',
            title,
        )
        self.sonnet_title.config(state=tk.DISABLED)

        sonnet_int = int(sonnet_number[7:])
        category, url = self.get_sonnet_category_and_url(sonnet_int)
        self.sonnet_category_label.update_url(url)
        self.sonnet_category.set(category)

    def get_sonnet_category_and_url(self, sonnet_num):
        if sonnet_num <= 17:
            return 'A Procreation sonnet', 'https://en.wikipedia.org/wiki/Procreation_sonnets'
        if sonnet_num <= 77:
            return 'A sonnet addressed to the Fair Youth', 'https://en.wikipedia.org/wiki/Shakespeare%27s_sonnets#Fair_Youth'
        if sonnet_num <= 86:
            return 'A Rival Poet sonnet', 'https://en.wikipedia.org/wiki/Shakespeare%27s_sonnets#The_Rival_Poet'
        if sonnet_num <= 125:
            return 'A sonnet addressed to the Fair Youth', 'https://en.wikipedia.org/wiki/Shakespeare%27s_sonnets#Fair_Youth'
        if sonnet_num == 126:
            return 'An Envoi to the Fair Youth', 'https://en.wikipedia.org/wiki/Sonnet_126#Envoi'
        if sonnet_num <= 152:
            return 'A sonnet addressed to the Dark Lady', 'https://en.wikipedia.org/wiki/Shakespeare%27s_sonnets#The_Dark_Lady'
        return 'An Anacreontic', 'https://en.wikipedia.org/wiki/Sonnet_153#Analysis'

    def get_sonnets(self):
        url = 'http://poetrydb.org/author,title/Shakespeare;Sonnet'
        r = requests.get(url)
        result = r.json()
        return result


def main():
    root = tk.Tk()
    root.title('Sonnet Shuffler')
    App(root, padding=20, width=800, height=500).pack()
    root.mainloop()


if __name__ == '__main__':
    main()