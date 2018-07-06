def pri_x(directx,directy,vaux):
    xy = (vaux[0],vaux[1])
    casas = 0
    while not meta(vaux):
        if vaux[1] != vaux[3]:
            if diagonal(vaux) == True:
                casas = casas + 1
                break
            else:
                xy = move_coord(directx,'x',xy)
                vaux[0],vaux[1] = xy[0],xy[1]
                casas = casas + 1
            
        else:        
            if diagonal(vaux) == True:
                casas = casas + 1
                break
            else:
                xy = move_coord(directy,'y',xy)
                vaux[0],vaux[1] = xy[0],xy[1]
                casas = casas + 1
    return casas

def pri_y(directx,directy,vaux):
    xy = (vaux[0],vaux[1])
    casas = 0
    while not meta(vaux):
        if vaux[0]!=vaux[2]:
            if diagonal(vaux) == True:
                    casas = casas + 1
                    break
            else:
                xy = move_coord(directy,'y',xy)
                vaux[0],vaux[1] = xy[0],xy[1]
                casas = casas + 1
        else:
            if diagonal(vaux) == True:
                    casas = casas + 1
                    break
            else:
                xy = move_coord(directx,'x',xy)
                v[0],v[1] = xy[0],xy[1]
                casas = casas + 1
    return casas

def meta(v):
    if v[0]==v[2] and v[1]==v[3]:
        return True
    else:
        return False
def diagonal(v):
    altura = abs(v[0]-v[2])
    largura = abs(v[1]-v[3])
    if altura == largura:
        return True
    else:
        return False
def move_coord(sinal,orient,xy):
    if orient != 'x':
        xy = (xy[0] + sinal,xy[1])
        return xy
    else:
        xy = (xy[0],xy[1] + sinal)
        return xy
    

def dist(v):
    return abs(v[0]-v[2])


while True:
    
    coord = raw_input().split()
    xy =  (int(coord[0]),int(coord[1]))
    metaxy   =  (int(coord[2]),int(coord[3]))
    v = []
    for b in coord:
        v.append(int(b))
    directx = 1
    directy = 1
    if sum(v) == 0:
        break
    if xy[0]==metaxy[0] and xy[1]-metaxy[1]<0:
        directx = 1
    elif xy[0]==metaxy[0] and xy[1]-metaxy[1]>0:
        directx = -1
    elif xy[0]-metaxy[0]<0 and xy[1]==metaxy[1]:
        directy = 1
    elif xy[0]-metaxy[0]>0 and xy[1]==metaxy[1]:
        directy = -1
    elif xy[0]-metaxy[0]<0 and xy[1]-metaxy[1]<0:
        directx = 1
        directy = 1
    elif xy[0]-metaxy[0]>0 and xy[1]-metaxy[1]>0:
        directx = -1
        directy = -1
    elif xy[0]-metaxy[0]>0 and xy[1]-metaxy[1]<0:
        directx = 1
        directy = -1
    else:
        directx = -1
        directy = 1



    ax = pri_x(directx,directy,v)
    v = []
    for b in coord:
        v.append(int(b))

    ay = pri_y(directx,directy,v)

    print(min(ax,ay))








