coord = raw_input().split()
xy = []
for b in coord:
    xy.append(float(b))
if xy[0] == 0 and xy[0] == xy[1]:
    print("Origem")
elif xy[0] == 0:
    print("Eixo Y")
elif xy[1] == 0:
    print("Eixo X")
elif xy[0]>0 and xy[1]>0:
    print("Q1")
elif xy[0]>0 and xy[1]<0:
    print("Q4")
elif xy[0]<0 and xy[1]>0:
    print("Q2")
else:
    print("Q3")
    
