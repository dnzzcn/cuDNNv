#!/usr/bin/env python

import os.path
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

    master.minsize(width=280, height=40)

  def cuDNN5(self):
    v5 = os.path.isfile("packages/cudnn-8.0-linux-x64-v5.1.tgz")
    if v5:
        switchText = "Switching.."
        switch.config(text = switchText)
        switch.pack()

        subprocess.call(['mkdir', 'packages/cudnn'])
        subprocess.call(['tar', 'xf', 'packages/cudnn-8.0-linux-x64-v5.1.tgz', 
                         '-C', 'packages/cudnn', '--strip-components', '1'])
        subprocess.call(['./switch.sh'])

        switchText = "Successfully switched to v5.1"
        switch.config(text = switchText)
        switch.pack()
    else:
        switchText = "Please download the package for v5.1"
        switch.config(text = switchText)
        switch.pack()

  def cuDNN6(self):
    v6 = os.path.isfile("packages/cudnn-8.0-linux-x64-v6.0.tgz")
    if v6:
        switchText = "Switching.."
        switch.config(text = switchText)
        switch.pack()

        subprocess.call(['mkdir', 'packages/cudnn'])
        subprocess.call(['tar', 'xf', 'packages/cudnn-8.0-linux-x64-v6.0.tgz', 
                         '-C', 'packages/cudnn', '--strip-components', '1'])
        subprocess.call(['./switch.sh'])

        switchText = "Successfully switched to v6.0"
        switch.config(text = switchText)
        switch.pack()
    else:
        switchText = "Please download the package for v6.0"
        switch.config(text = switchText)
        switch.pack()

  def cuDNN7(self):
    v7 = os.path.isfile("packages/cudnn-8.0-linux-x64-v7.tgz")
    if v7:
        switchText = "Switching.."
        switch.config(text = switchText)
        switch.pack()

        subprocess.call(['mkdir', 'packages/cudnn'])
        subprocess.call(['tar', 'xf', 'packages/cudnn-8.0-linux-x64-v7.tgz', 
                         '-C', 'packages/cudnn', '--strip-components', '1'])
        subprocess.call(['./switch.sh'])

        switchText = "Successfully switched to v7.0"
        switch.config(text = switchText)
        switch.pack()
    else:
        switchText = "Please download the package for v7.0"
        switch.config(text = switchText)
        switch.pack()

root = Tk()
root.wm_title("cuDNN Version Switcher")
root.resizable(width=False, height=False)
app = App(root)

switchText = ""
switch = Label(root, text=switchText)
switch.pack()

devnoteMessage = "\ncuDNNv v0.2"
devnote = Label(root, text=devnoteMessage)
devnote.pack()

root.mainloop()

