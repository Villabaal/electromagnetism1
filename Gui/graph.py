from ttkbootstrap import Frame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class graphFrame(Frame):
    def __init__(self,master, **kwargs) -> None:
        super().__init__(master,**kwargs)
        self.master = master
        self._create()
    
    def _create(self):
        # Crear el lienzo de la figura para incrustarlo en el Frame
        color = self.master['bg']
        canvas = FigureCanvasTkAgg(master=self)
        canvas.figure.set_facecolor(color)
        canvas.get_tk_widget().place(relheight=0.95,relwidth=0.65,relx=0.175,rely=0.025)