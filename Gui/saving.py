from ttkbootstrap import Frame,Entry,Button

class saveFrame(Frame):
    def __init__(self,master, **kwargs) -> None:
        super().__init__(master,**kwargs)
        self.master = master
        self._create()
        
    def _create(self)-> None:
        self.division = Frame(self)
        self.entry = Entry(self.division,bootstyle = 'primary',state='disabled',justify='center')
        self.saveButton = Button(self.division, text='guardar como', state='disabled')
        
        self.division.place(relx=0.5,rely=0.5,anchor='center')
        self.entry.pack(ipadx=40)
        self.saveButton.pack(pady=20,ipadx=40,ipady=10)
