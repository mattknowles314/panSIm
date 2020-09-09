from tkinter import *
import sirSolve

root=Tk()

#Window attributes
root.title("SIR Grapher")
#root.geometry("500x500") #Set the size of the window
root.resizable(0,0) #Dont want the window to be resizable

#winTitle = Label(root, text="Welcome to SIR Grapher, a project by Matthew Knowles and Ben Apperley").grid(row = 0)

popLabel = Label(root, text="Population Size").grid(row=1)
infLabel = Label(root, text="Virus Infection Rate").grid(row = 2)
remLabel = Label(root, text="Recovery Rate").grid(row =3)
timeLabel = Label(root, text = "Time Period").grid(row=4)
ininfLabel = Label(root, text = "Initial Infections").grid(row=5)

popEnt = Entry(root)
popEnt.grid(row =1, column=1)
infEnt = Entry(root)
infEnt.grid(row=2, column=1)
remEnt = Entry(root)
remEnt.grid(row=3, column=1)
timeEnt = Entry(root)
timeEnt.grid(row=4, column=1)
i0Ent = Entry(root)
i0Ent.grid(row=5, column=1)

def getVals():
    N = popEnt.get()
    b = infEnt.get()
    c = remEnt.get()
    per = timeEnt.get()
    I0 = i0Ent.get()

    global values
    values = [N,b,c,per,I0]

subButton = Button(root, text= "Generate", command=getVals).grid(row=6, column=1, sticky=W)

sirSolve.sireqs


root.mainloop()
