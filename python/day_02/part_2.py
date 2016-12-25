#name = "test2_check.txt"
name = "task.txt"
data = open(name, "r").read()
stride = 3

def f(x):
    if x == 'R':
        return [1,0]
    if x == 'L':
        return [-1, 0]
    if x == 'D':
        return [0, 1]
    if x == 'U':
        return [0, -1]
    return [0,1,0]

data = data.split()
r = [-2,0]
result = []

map =[
['.', '.'  '1', '.', '.'],
['.', '2', '3', '4', '.'],
['5', '6', '7', '8','9' ],
['.', 'A', 'B', 'C', '.'],
['.', '.', 'D', '.', '.'],
    ]
#36629
for x in data:
    for s in x.strip():
        new_s = f(s)
        pos = [0,0]
        pos[0] = r[0] + new_s[0]
        pos[1] = r[1] + new_s[1]
        if abs(pos[0])<=(2-abs(pos[1])) and abs(pos[1])<=(2-abs(pos[0])):
            r = pos
        #else:
        #    print("skip",s,pos)

    #print(r)
    p = map[r[1]+2][r[0]+2]
    result += [str(p)]
print ("".join(result))
