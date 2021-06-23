class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()
    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)
    def show(self):
        return self.items
q=Queue()
cek='y'
while cek=='y':
    a=[]
    jumlah=int(input("Masukkan Proses dalam CPU: "))
    for i in range(jumlah):
        nama=str(input("Nama Proses ke-"+str(i+1)+": "))
        waktu=int(input("Waktu Proses: "))
        a.append(nama)
        a.append(waktu)
        q.enqueue(a)
        a=[]
    print()
    waktu_proses=int(input("Waktu proses CPU: "))
    print(q.show())
    i=1
    while not q.isEmpty():
        print("Iterasi ke-"+str(i))
        i+=1
        b=[]
        item=q.dequeue()
        sisa=item[1]-waktu_proses
        b.append(item[0])
        b.append(sisa)
        if b[1]>0 and b[1]!=0:
            q.enqueue(b)
            print("     Proses " + item[0] +" sedang Diproses,dan sisa prosess "+item[0]+"= ",sisa)
        elif b[1]==0:
            print("     Proses "+str(item[0])+" selesai")
        print("     Data proses yang tersisa="+str(q.show()))
        b=[]
    cek=str(input("Coba lagi? (y/n)"))
    cek=cek.lower()
