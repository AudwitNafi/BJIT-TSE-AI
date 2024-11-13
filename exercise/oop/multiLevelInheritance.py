class A():
    def showMessage(self):
        print("I am in A")
        
class B(A):
    def showMessage(self):
        print("I am in B")
        
class C(B):
    def showMessage(self):
        print("I am in Class C")
        