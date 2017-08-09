#!/usr/bin/env python

import subprocess
from tkinter import *

class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()

    self.quit = Button(frame, 
                         text="QUIT", fg="red",
                         command=quit)
    self.quit.pack(side=RIGHT)

    self.v5 = Button(frame,
                         text="v5.1",
                         command=self.cuDNN5)
    self.v5.pack(side=LEFT)

    self.v6 = Button(frame,
                         text="v6.0",
                         command=self.cuDNN6)
    self.v6.pack(side=LEFT)

    self.v7 = Button(frame,
                         text="v7.0",
                         command=self.cuDNN7)
    self.v7.pack(side=LEFT)

    master.minsize(width=240, height=25)

  def cuDNN5(self):
    subprocess.call(['./cuDNN5.sh'])

  def cuDNN6(self):
    subprocess.call(['./cuDNN6.sh'])

  def cuDNN7(self):
    subprocess.call(['./cuDNN7.sh'])

root = Tk()
root.wm_title("cuDNN Version Switcher")
root.resizable(width=False, height=False)
app = App(root)
root.mainloop()
