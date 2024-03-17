from ttkbootstrap import Window
from Gui.graph import graphFrame
from Gui.saving import saveFrame
from Gui.mode import modeFrame
from utils import randomPoint
from random import uniform, randint
from electric_mass import electricCurrent,electricCharge
from Questions import currentSystem,chargeSystem
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg




class App(Window):
    
    massTypes = [electricCharge,electricCurrent]
    systemTypes = [chargeSystem,currentSystem]
    nMasses = 4
    sigma = 2
    scale: list[float] = [1e-8,1]
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self._questions = [self._fieldQuestions,self._forceQuestions]
        self._create()
    
    def _fieldQuestions(self, Space:currentSystem|chargeSystem) -> None:
        ## punto en cuestión para pregunta de campo
        P = randomPoint(scale=App.sigma)            
        self.Answer = Space.fieldQuestion(P)     

    def _forceQuestions(self, Space:currentSystem|chargeSystem) -> None:
        ## punto en cuestión para pregunta de campo
        id = randint(1,App.nMasses)            
        self.Answer = Space.forceQuestion(id)        
    
    def makeQuestion(self) -> None:
        App.nMasses = randint(2,4)
        subject = self.controls.subject_state
        question = self.controls.question_state
        #cargas electricas o corrientes electricas
        massType = App.massTypes[subject]
        #electrostatica o magnetostatica
        systemType = App.systemTypes[subject]
        masses = [ massType( App.scale[subject]*round( uniform(-200,200), 2), randomPoint(scale=App.sigma) ) for _ in range(App.nMasses)]
        Space = systemType( masses )
        self._questions[ question ]( Space )
        canvas = FigureCanvasTkAgg(master=self.graph,figure=self.Answer.fig)
        canvas.get_tk_widget().place(relheight=0.95,relwidth=0.65,relx=0.5,rely=0.5,anchor='center')
        self.save.entry['state'],self.save.saveButton['state'] = 'active','active'
        
    def disableSaveFrame(self,e)->None:
        self.controls.subjectSelection()        
        self.save.entry['state'],self.save.saveButton['state'] = 'disabled','disabled'  
                
    def saveAnswer(self)->None:
        name = self.save.entry.get()
        self.Answer.fig.savefig( f'{ name }.jpg',dpi = 1080 )
        with open(f'{ name }.txt','w') as file:
            file.write( self.Answer.__str__() )        
        
    def _create(self) -> None:
        #crea los frames
        self.graph = graphFrame(self)
        self.controls = modeFrame(self)
        self.save = saveFrame(self)
        #posicionalos
        self.graph.place( relwidth=1, relheight=0.75 )
        self.controls.place(relwidth=0.5,relheight=0.2,rely=0.75)
        self.save.place(relwidth=0.5,relheight=0.2,relx=0.5,rely=0.75)
        #configuralos
        self.protocol("WM_DELETE_WINDOW", self._closing_cbk)
        self.controls.subject.bind('<<ComboboxSelected>>',self.disableSaveFrame)
        self.controls.generateButton['command'] = self.makeQuestion
        self.save.saveButton['command'] = self.saveAnswer
        
    def _closing_cbk(self) -> None:
        #cerrado seguro
        self.quit()
        self.destroy()