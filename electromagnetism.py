# -*- coding: utf-8 -*-
from Gui import App
from ttkbootstrap import PhotoImage

app = App(themename='darkly')
app.title('Electromágnetismo')
app.geometry('800x720')
icon = PhotoImage(file='images/icon.png')   
app.tk.call('wm', 'iconphoto', app._w, icon)
app.resizable(False,False)
app.mainloop()
