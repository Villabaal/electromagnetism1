from ttkbootstrap import Button,Frame,Combobox

class modeFrame(Frame):
    _defaultFldMsg = 'Elige el campo'
    def __init__(self,master, **kwargs) -> None:
        super().__init__(master,**kwargs)
        self.master = master
        self._create()
    
    def subjectSelection(self)-> None:
        state = self.subject.get()
        self.question.set( modeFrame._defaultFldMsg )
        self.generateButton['state'] = 'disabled'
        if state == 'Electrostática':
            self.subject_state = False #false si es electrostática
            self.question['values'] = ['Campo Eléctrico','Fuerza Electrostática']
        else:
            self.subject_state = True #true si es magnetostática
            self.question['values'] = ['Campo Magnético','Fuerza Magnetostática']
        self.question['state'] = 'readonly'
    
    def questionSelection(self,e) -> None:
        self.generateButton['state'] = 'active'
        if self.question.get().split()[0] == 'Campo':
            self.question_state = False #false si es pregunta de campo
            return
        self.question_state = True #false si es pregunta de Fuerza

    def _create(self) -> None:
        #creación de elementos
        self.division = Frame(self)
        self.subject = Combobox(self.division,bootstyle='primary',state='readonly',justify='center')
        self.question = Combobox(self.division,bootstyle='primary' ,state='disabled',justify='center')
        self.generateButton = Button(self.division, text='generar', state='disabled')
        #posicionamiento y tamaño
        self.division.place(anchor='center',relx=0.5,rely=0.5)
        self.subject.pack(ipadx=10)
        self.question.pack(ipadx=10, pady=20)
        self.generateButton.pack(ipadx=40, ipady=10)
        #configuración
        self.subject['values'] = ['Electrostática','Magnetostática']
        self.subject.set('Elige el tema')
        self.subject_state = None
        self.question.bind('<<ComboboxSelected>>',self.questionSelection)
        self.question.set( modeFrame._defaultFldMsg )
        self.question_state = None
        