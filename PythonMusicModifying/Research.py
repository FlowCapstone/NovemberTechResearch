from pyo import *

s = Server(duplex=0)
s.setOutputDevice(4)
s.boot()
s.start()

a = Sine(mul=0.01).out()
print(a)
#savefile(a, './test.aif')