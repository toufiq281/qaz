Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class student:
    def __init__(self):
        self.name=name
        self.rollno=rollno
    def show(self):
        print(self.name,self.rollno)
    class laptop:
        def __init__(self):
            self.brand='HP'
            self.cpu='i5'
            self.memory='1tb'
        def show(self):
            print(self.brand,self.cpu,self.memory)

            
s1=student('toufik',3)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s1=student('toufik',3)
TypeError: student.__init__() takes 1 positional argument but 3 were given
