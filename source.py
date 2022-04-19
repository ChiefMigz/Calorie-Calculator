from ctypes import alignment
import tkinter

class CalorieCalulator:
    def __init__(self):
        self.mainWindow = tkinter.Tk()
        self.mainWindow.geometry("280x360")
        self.mainWindow.title("Calorie Calculator")
        
        self.topWindow = tkinter.Frame(self.mainWindow)
        self.middleWindow = tkinter.Frame(self.mainWindow)
        self.bottomWindow = tkinter.Frame(self.mainWindow)
        self.buttonWindow = tkinter.Frame(self.mainWindow)
        
        #Entry Weight Entry
        self.startingWeightLabel = tkinter.Label(self.topWindow, text="Starting weight: ")
        self.startingWeightEntry = tkinter.Entry(self.topWindow)
        
        #Calorie Cut/Gain
        self.calorieCutLabel = tkinter.Label(self.topWindow, text="Calorie Cut/Gain:")
        self.calorieCutEntry= tkinter.Entry(self.topWindow)
        
        #Target Month (int)
        self.targetMonthLabel = tkinter.Label(self.topWindow, text="Enter no. of month/s: ")
        self.targetMonthEntry = tkinter.Entry(self.topWindow)
        
        #Lose weight or gain weight radio button
        self.userWeightPlanChoice = tkinter.IntVar()
        self.userWeightPlanChoice.set(1)
        self.gainWeightRb = tkinter.Radiobutton(self.middleWindow, text="Gain Weight", value=1, variable=self.userWeightPlanChoice)
        self.loseWeightRb = tkinter.Radiobutton(self.middleWindow, text="Lose Weight", value=2, variable=self.userWeightPlanChoice)
        
        #Checkboxes
        self.inKiloVar = tkinter.IntVar()
        self.inKiloVar.set(1)
        self.inPoundVar = tkinter.IntVar()
        self.inKiloCb = tkinter.Checkbutton(self.bottomWindow, onvalue=1, variable=self.inKiloVar, text="Show weight in Kg")
        self.inPoundCb = tkinter.Checkbutton(self.bottomWindow, onvalue=1, variable=self.inPoundVar, text="Show weight in Lb")
        
        #Buttons
        self.applyBtn = tkinter.Button(self.buttonWindow, text="Apply", relief = 'ridge', command=self.apply)
        self.calculateBtn = tkinter.Button(self.buttonWindow, relief = 'ridge', text="Calculate")
        
        #Packing windows
        self.topWindow.pack(pady=10, padx=10, anchor="w")
        self.middleWindow.pack(anchor="w", padx=10, pady=10)
        self.bottomWindow.pack(anchor="w", padx=10, pady=10)
        self.buttonWindow.pack(anchor="w", padx=80, pady=10)
        
        #Placing top window items
        self.startingWeightLabel.grid(row=1, column=1, pady=10)
        self.startingWeightEntry.grid(row=1, column=2, pady=10)
        self.calorieCutLabel.grid(row=2, column=1, pady=10)
        self.calorieCutEntry.grid(row=2, column=2, pady=10)
        self.targetMonthLabel.grid(row=3, column=1, pady=10)
        self.targetMonthEntry.grid(row=3, column=2, pady=10)
        
        #Placing middle window items
        self.gainWeightRb.pack()
        self.loseWeightRb.pack()
        
        #Placing bottom window items
        self.inKiloCb.pack()
        self.inPoundCb.pack(pady=10)
        
        #Placing button window items
        self.applyBtn.pack(side="left")
        self.calculateBtn.pack(side="right", padx=10)
        
        self.weightProgress = list()
        
        tkinter.mainloop()
    
    def apply(self):
        calorieCutPerDay = 500
        weightChangePerMonth = 4
        initialWeight = float(self.startingWeightEntry.get())
        self.weightProgress.append(initialWeight)
        for i in range(int(self.targetMonthEntry.get())):
            if self.userWeightPlanChoice.get() == 1:
                initialWeight += (float(self.calorieCutEntry.get()) / calorieCutPerDay) * weightChangePerMonth
            elif self.userWeightPlanChoice.get() == 2:
                initialWeight -= (float(self.calorieCutEntry.get()) / calorieCutPerDay) * weightChangePerMonth
            self.weightProgress.append(initialWeight)
        print(self.weightProgress)
    
    def calculate(self):
        pass


if __name__ == '__main__':
    CalorieCalulator()