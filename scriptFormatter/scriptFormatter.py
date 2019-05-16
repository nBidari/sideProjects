import tkinter as tk

class ScriptFormatter:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Premity Chat Rooms: #3429")  # Change title here
        self.root.configure(background="#DADFDF")

        self.paddingX = 15
        self.paddingY = 5

        self.userFrame = tk.LabelFrame(self.root, text="Users")
        self.userFrame.config(background="#DADFDF", relief="sunken")
        self.userFrame.grid(row=0, column=0, sticky='W', padx = self.paddingX, pady = self.paddingY)

        self.userName = tk.Text(self.userFrame, background="black", foreground="lime", height=20, width=11)
        self.userName.config(highlightbackground = "#074C0A")
        self.userName.grid(row=0, column=0, sticky='NESW',padx = self.paddingX,pady=self.paddingY)

        self.textFrame = tk.LabelFrame(self.root, text="Chat")
        self.textFrame.config(background="#DADFDF", relief="sunken")
        self.textFrame.grid(row=0, column=1, sticky='NESW', padx=self.paddingX, pady=self.paddingY)

        self.textName = tk.Text(self.textFrame, background="black", foreground="lime", height=20, width=100)
        self.textName.config(highlightbackground="#074C0A")
        self.textName.grid(row=0, column=0, sticky='NESW', padx=self.paddingX, pady=self.paddingY)



        self.root.mainloop()



mainPage = ScriptFormatter()