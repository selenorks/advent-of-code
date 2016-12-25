import llist
k = 3001330
b = llist.dllist(range(1, k + 1))
p = b.first
step = len(b)/2
for _ in range(0, step-1):
    p = p.next and p.next or b.first

step1 = True
s = 0
while len(b) > 1:

    if step1:
        p = p.next and p.next or b.first
    step1 = not step1

    p2 = p.next and p.next or b.first
    b.remove(p)
    p = p2
    s = s+1.0

print(b[0])