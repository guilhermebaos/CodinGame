'''
Original code, before getting minified:

lx, ly, tx, ty = [int(i) for i in input().split()]
while True:
    _ = int(input())
    dx = lx - tx
    dy = ly - ty
    m = [0, 0, 0]
    m[0] = 1 if dx > 0 else -1 if dx < 0 else 0
    m[1] = 1 if dy > 0 else -1 if dy < 0 else 0
    if dx > 0:
        m[2] = 'SE' if dy > 0 else 'NE' if dy < 0 else 'E'
    elif dx == 0:
        m[2] = 'S' if dy > 0 else 'N'
    else:
        m[2] = 'SW' if dy > 0 else 'NW' if dy < 0 else 'W'
    tx += m[0]
    ty += m[1]
    print(m[2])
'''
I=input
H=int
F,G,D,E=[H(A)for A in I().split()]
while True:
	J=H(I());C=F-D;B=G-E;A=[0,0,0];A[0]=1 if C>0 else-1 if C<0 else 0;A[1]=1 if B>0 else-1 if B<0 else 0
	if C>0:A[2]='SE'if B>0 else'NE'if B<0 else'E'
	elif C==0:A[2]='S'if B>0 else'N'
	else:A[2]='SW'if B>0 else'NW'if B<0 else'W'
	D+=A[0];E+=A[1];print(A[2])