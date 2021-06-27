class Stack():
    def __init__ (self):
        self.items = []
    def isempty (self):
        return self.items == []
    def push (self,item):
        self.items.append(item)
    def pop (self):
        return self.items.pop()
    def peek (self):
        return self.items[len(self.items)-1]
    def size (self):
        return len(self.items)
s1=Stack()
s2=Stack()
tag=str(input("Masukkan kode html: ")).split()
balance=True
for i in tag:
     if i[0]=="<" and i[-1]==">":
          if i[1]=="/":
               s1.pop()
               if s2.pop() != i[2:-1]:
                    balance=False
          else:
               s1.push(tag)
               s2.push(i[1:-1])
if s1.isempty() and s2.isempty() and balance==True:
     print(True)
else:
     print(False)

print('Program selesai!')
