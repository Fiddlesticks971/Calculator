import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class Calculator(Gtk.Window):
    def __init__(self):
        
        Gtk.Window.__init__(self,title = "Calculator")
        
        self.grid = Gtk.Grid()
        
        self.button0 = Gtk.Button(label ="0")
        self.button0.connect("clicked", self.Button0_Click)
        self.button1 = Gtk.Button(label ="1")
        self.button1.connect("clicked", self.Button1_Click)
        self.button2 = Gtk.Button(label ="2")
        self.button2.connect("clicked", self.Button2_Click)
        self.button3 = Gtk.Button(label ="3")
        self.button3.connect("clicked", self.Button3_Click)
        self.button4 = Gtk.Button(label ="4")
        self.button4.connect("clicked", self.Button4_Click)
        self.button5 = Gtk.Button(label ="5")
        self.button5.connect("clicked", self.Button5_Click)
        self.button6 = Gtk.Button(label ="6")
        self.button6.connect("clicked", self.Button6_Click)
        self.button7 = Gtk.Button(label ="7")
        self.button7.connect("clicked", self.Button7_Click)
        self.button8 = Gtk.Button(label ="8")
        self.button8.connect("clicked", self.Button8_Click)
        self.button9 = Gtk.Button(label ="9")
        self.button9.connect("clicked", self.Button9_Click)
        self.buttonPlus = Gtk.Button(label ="+")
        self.buttonPlus.connect("clicked", self.ButtonPlus_Click)
        self.buttonMinus = Gtk.Button(label ="-")
        self.buttonMinus.connect("clicked", self.ButtonMinus_Click)
        self.buttonDivide = Gtk.Button(label ="/")
        self.buttonDivide.connect("clicked", self.ButtonDivide_Click)
        self.buttonMulti = Gtk.Button(label ="X")
        self.buttonMulti.connect("clicked", self.ButtonMulti_Click)
        self.buttonEqual = Gtk.Button(label ="=")
        self.buttonEqual.connect("clicked", self.ButtonEqual_Click)
        self.buttonClear = Gtk.Button(label ="C")
        self.buttonClear.connect("clicked", self.ButtonClear_Click)
        self.textBox = Gtk.Entry()
        
        self.grid.add(self.button7)
        self.grid.attach_next_to(self.button8,self.button7,Gtk.PositionType.RIGHT,1,1)
        self.grid.attach_next_to(self.button9,self.button8,Gtk.PositionType.RIGHT,1,1)
        self.grid.attach_next_to(self.buttonPlus,self.button9,Gtk.PositionType.RIGHT,1,1)
        self.grid.attach_next_to(self.button4,self.button7,Gtk.PositionType.BOTTOM,1,1)
        self.grid.attach_next_to(self.button5,self.button4,Gtk.PositionType.RIGHT,1,1)
        self.grid.attach_next_to(self.button6,self.button5,Gtk.PositionType.RIGHT,1,1)
        self.grid.attach_next_to(self.buttonMinus,self.button6,Gtk.PositionType.RIGHT,1,1)
        self.grid.attach_next_to(self.button1,self.button4,Gtk.PositionType.BOTTOM,1,1)
        self.grid.attach_next_to(self.button2,self.button1,Gtk.PositionType.RIGHT,1,1)
        self.grid.attach_next_to(self.button3,self.button2,Gtk.PositionType.RIGHT,1,1)
        self.grid.attach_next_to(self.buttonDivide,self.button3,Gtk.PositionType.RIGHT,1,1)
        self.grid.attach_next_to(self.button0,self.button2,Gtk.PositionType.BOTTOM,1,1)
        self.grid.attach_next_to(self.buttonEqual,self.button0,Gtk.PositionType.RIGHT,1,1)
        self.grid.attach_next_to(self.buttonMulti,self.buttonDivide,Gtk.PositionType.BOTTOM,1,1)
        self.grid.attach_next_to(self.buttonClear,self.button1,Gtk.PositionType.BOTTOM,1,1)
        self.grid.attach_next_to(self.textBox,self.button7,Gtk.PositionType.TOP,4,1)
        
        self.add(self.grid)
        
    def Button0_Click(self,widget):
        self.textBox.set_text(self.textBox.get_text() + '0' )
    def Button1_Click(self,widget):
        self.textBox.set_text(self.textBox.get_text() + '1' )
    def Button2_Click(self,widget):
        self.textBox.set_text(self.textBox.get_text() + '2' )
    def Button3_Click(self,widget):
        self.textBox.set_text(self.textBox.get_text() + '3' )
    def Button4_Click(self,widget):
        self.textBox.set_text(self.textBox.get_text() + '4' )
    def Button5_Click(self,widget):
        self.textBox.set_text(self.textBox.get_text() + '5' )
    def Button6_Click(self,widget):
        self.textBox.set_text(self.textBox.get_text() + '6' )
    def Button7_Click(self,widget):
        self.textBox.set_text(self.textBox.get_text() + '7' )
    def Button8_Click(self,widget):
        self.textBox.set_text(self.textBox.get_text() + '8' )
    def Button9_Click(self,widget):
        self.textBox.set_text(self.textBox.get_text() + '9' )
    def ButtonPlus_Click(self,widget):
        self.textBox.set_text(self.textBox.get_text() + ' + ' )
    def ButtonMinus_Click(self,widget):
        self.textBox.set_text(self.textBox.get_text() + ' - ' )
    def ButtonDivide_Click(self,widget):
        self.textBox.set_text(self.textBox.get_text() + ' / ' )
    def ButtonMulti_Click(self,widget):
        self.textBox.set_text(self.textBox.get_text() + ' * ' )
    def ButtonClear_Click(self,widget):
        self.textBox.set_text('')
    def ButtonEqual_Click(self,widget):
        try:
            self.textBox.set_text(str(eval(self.textBox.get_text())))
        except ZeroDivisionError:
            self.textBox.set_text("Divided by Zero!")
        
        
        
win = Calculator()
win.connect("delete-event",Gtk.main_quit)
win.show_all()
Gtk.main()
        
