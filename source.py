from ctypes import alignment
import tkinter

class CalorieCalulator:
    def __init__(self):
        self.mainWindow = tkinter.Tk()
        self.mainWindow.geometry("400x400")
        self.mainWindow.title("Calorie Calculator")
        
        self.topWindow = tkinter.Frame(self.mainWindow)
        self.middleWindow = tkinter.Frame(self.mainWindow)
        self.bottomWindow = tkinter.Frame(self.mainWindow)
        
        #Entry Weight Entry
        self.startingWeightLabel = tkinter.Label(self.topWindow, text="Starting weight: ", type="int")
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
        
        
        self.topWindow.pack(side="top", pady=10, padx=10, anchor="w")
        self.middleWindow.pack(anchor="w", padx=10, pady=10)
        self.bottomWindow.pack(side="bottom")
        
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
        
        tkinter.mainloop()


if __name__ == '__main__':
    CalorieCalulator()