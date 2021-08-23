import tkinter


import tkinter as tk 
root=tk.Tk()
root.geometry("300x400")
root.title("LOGIN PORTAL")
namel=tk.Label(text="Name").grid(row=1)
namee=tk.Entry().grid(row=1,column=1)
passl=tk.Label(text="Password").grid(row=2)
passe=tk.Entry().grid(row=2,column=1)
cpassl=tk.Label(text="Confirm Password").grid(row=3)
cpasse=tk.Entry().grid(row=3,column=1)
submit=tk.Button(text="Submit").grid(row=4, column=2)
name=namee.__getattribute__ 
print(name)
root.mainloop()