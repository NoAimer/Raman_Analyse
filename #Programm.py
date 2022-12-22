from subprocess import Popen, PIPE
import os

s_in = b'something to say\nright here\non three lines'
p = Popen(['python', str(os.getcwd()+"\\Startseite_GUI.py")], stdin=PIPE, stdout=PIPE)
s_out = p.communicate(s_in)

p = Popen(['python', str(os.getcwd()+"\\Datenlese_GUI.py")], stdin=PIPE, stdout=PIPE)
s_out2, _ = p.communicate(s_in)

