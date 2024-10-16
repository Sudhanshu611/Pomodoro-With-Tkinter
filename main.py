import tkinter as tk
import time
from tkinter import messagebox

class pomodoro():
    
    def __init__(self, root):
        self.root = root
        
    def working_time(self, timer):
        
        minutes, seconds = divmod(timer, 60)  # this will give you tuple of quotient and remainder (quotient = minutes, remainder = seconds)
        self.min.set(f'{minutes:02d}')
        self.sec.set(f'{seconds:02d}')
        self.root.update()
        time.sleep(1) # 1 SECOND
    
    def work_(self):
        self.work_label.set('~Work~')
        timer = 25*60
        while timer >= 0:
            pomo.working_time(timer)
            if timer == 0:
                messagebox.showinfo('Work time is over\nClick on break button to start your 5 min break')
            timer -= 1
            
            
    def break_(self):
        self.work_label.set('~Break~')
        timer = 5*60
        while timer >= 0:
            pomo.working_time(timer)
            if timer == 0:
                messagebox.showinfo('Break time is over\nClick on Work button to start your 25 min work')
            timer -= 1
            
    def main(self):
        
        # canvas
        self.root.geometry("380x300")
        self.root.title('Pomodoro')
        tk.Label(self.root, text = 'Welcome!',font=("arial", 28, "bold")).pack()
        self.work_label = tk.StringVar(self.root)
        self.work_label.set('~Work~')
        work_label = tk.Label(self.root, textvariable=self.work_label, font = ('arial', 15, 'bold'))
        work_label.pack()
        
        #Working Area
        self.min = tk.StringVar(self.root)
        self.min.set('25')
        
        self.sec = tk.StringVar(self.root)
        self.sec.set('00')
        
        minutes = tk.Label(self.root, textvariable = self.min, font=('arial',22,'bold'))
        minutes.pack()
        
        seconds = tk.Label(self.root, textvariable = self.sec, font=('arial',22,'bold'))
        seconds.pack()
        
        start_btn = tk.Button(self.root, text='Start', bd=5, command=self.work_, font=('arial', 18, 'bold')).place(x=90, y=220)
        break_btn = tk.Button(self.root, text='Break', bd=5, command=self.break_, font=('arial', 18, 'bold')).place(x=190, y=220)
        
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    pomo = pomodoro(root)
    pomo.main()