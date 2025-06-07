import threading

def coder(row,col):
    print(f'Coder ID: ({row},{col})')

threads = []
rows,cols=4,4
for i in range(rows):
    for j in range(cols):
        t = threading.Thread(target=coder, args=(i,j))
        threads.append(t)
        t.start()

for t in threads:
    t.join()






