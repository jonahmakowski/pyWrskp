import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.active = False
        self.pas = '4412342132'
        self.create_widgets()
        self.code = ''
    
    def create_widgets(self):
        self.btnFrame = tk.Frame(self)
        
        self.btn1 = tk.Button(self.btnFrame, text='1', command=self.one)
        self.btn2 = tk.Button(self.btnFrame, text='2', command=self.two)
        self.btn3 = tk.Button(self.btnFrame, text='3', command=self.three)
        self.btn4 = tk.Button(self.btnFrame, text='4', command=self.four)
        self.btnsend = tk.Button(self.btnFrame, text='send', command=self.send)
        self.btndel = tk.Button(self.btnFrame, text='del', command=self.d)
        self.btns = [self.btn1, self.btn2, self.btn3, self.btn4, self.btnsend, self.btndel]
        
        self.btnFrame.grid(row = 0, column=0, sticky='ns')
        r, c = 0, 0
        for item in self.btns:
            item.grid(row=r, column=c, sticky='ew')
            r += 1
    def one(self):
        if self.active == False:
            print('Enter the code')
            self.active = True
        else:
            print('1')
            self.code += '1'
    
    def two(self):
        if self.active == True:
            print('2')
            self.code += '2'
        else:
            print('Error Wrong Button')
    
    def three(self):
        if self.active == True:
            print('3')
            self.code += '3'
        else:
            print('Error Wrong Button')
        
    def four(self):
        if self.active == True:
            print('4')
            self.code += '4'
        else:
            print('Error Wrong Button')
    
    def d(self):
        if self.active == True:
            self.code = self.code[:len(self.code)-1]
            print(self.code)
            print('del')
        else:
            print('Error Wrong Button')
    
    def send(self):
        if self.code == self.pas:
            self.master.destroy()
        else:
            print('FAIL, SYSTEM SHUTTING DOWN')
            exit()
