from tkinter import font
import tkinter.ttk as ttk
import webbrowser


class LabelLink(ttk.Label):
    def __init__(self, parent, url='', *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.url = url
        self.bind("<Button-1>", lambda e: webbrowser.open_new(self.url))

        label_font = font.nametofont(ttk.Style().lookup('TLabel',
                                                        'font')).copy()
        label_font.configure(underline=True)
        ttk.Style().configure('link.TLabel',
                              foreground='blue',
                              font=label_font)
        self.configure(style='link.TLabel')

    def update_url(self, url):
        self.url = url
        self.bind("<Button-1>", lambda e: webbrowser.open_new(self.url))
