#!/usr/bin/env python

import os.path
import subprocess
import glob
from Tkinter import *

class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()

    self.quit = Button(frame, 
                         text="QUIT", fg="red",
                         command=quit)
    self.quit.pack(side=RIGHT)

    self.v5 = Button(frame,
                         text="v5",
                         command=self.cuDNN5)
    self.v5.pack(side=LEFT)

    self.v6 = Button(frame,
                         text="v6",
                         command=self.cuDNN6)
    self.v6.pack(side=LEFT)

    self.v7 = Button(frame,
                         text="v7",
                         command=self.cuDNN7)
    self.v7.pack(side=LEFT)

    master.minsize(width=280, height=40)

  def cuDNN5(self):
    v5 = glob.glob("packages/*v5*tgz")
    c5 = len(v5)
    if c5:
        switchText = "Switching.."
        switch.config(text = switchText)
        switch.pack()

        subprocess.call(['mkdir', 'packages/cudnn'])
        subprocess.call(['tar', 'xf', v5[0], 
                         '-C', 'packages/cudnn', '--strip-components', '1'])
        subprocess.call(['./switch.sh'])

        switchText = "Successfully switched to v5"
        switch.config(text = switchText)
        switch.pack()
    else:
        switchText = "Please download the package for v5"
        switch.config(text = switchText)
        switch.pack()

  def cuDNN6(self):
    v6 = glob.glob("packages/*v6*tgz")
    c6 = len(v6)
    if c6:
        switchText = "Switching.."
        switch.config(text = switchText)
        switch.pack()

        subprocess.call(['mkdir', 'packages/cudnn'])
        subprocess.call(['tar', 'xf', v6[0], 
                         '-C', 'packages/cudnn', '--strip-components', '1'])
        subprocess.call(['./switch.sh'])

        switchText = "Successfully switched to v6"
        switch.config(text = switchText)
        switch.pack()
    else:
        switchText = "Please download the package for v6"
        switch.config(text = switchText)
        switch.pack()

  def cuDNN7(self):
    v7 = glob.glob("packages/*v7*tgz")
    c7 = len(v7)
    if c7:
        switchText = "Switching.."
        switch.config(text = switchText)
        switch.pack()

        subprocess.call(['mkdir', 'packages/cudnn'])
        subprocess.call(['tar', 'xf', v7[0], 
                         '-C', 'packages/cudnn', '--strip-components', '1'])
        subprocess.call(['./switch.sh'])

        switchText = "Successfully switched to v7"
        switch.config(text = switchText)
        switch.pack()
    else:
        switchText = "Please download the package for v7"
        switch.config(text = switchText)
        switch.pack()

root = Tk()
root.wm_title("cuDNN Version Switcher")
root.resizable(width=False, height=False)
app = App(root)

switchText = ""
switch = Label(root, text=switchText)
switch.pack()

devnoteMessage = "\ncuDNNv v0.3"
devnote = Label(root, text=devnoteMessage)
devnote.pack()

root.mainloop()
