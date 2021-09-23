"""
Original code, before getting minified:

lx, ly, tx, ty = [int(i) for i in input().split()]
moves = [['', 'S', 'N'], ['E', 'SE', 'NE'], ['W', 'SW', 'NE']]
while True:
    _ = int(input())
    mx = 1 if lx > tx else -1 if lx < tx else 0
    my = 1 if ly > ty else -1 if ly < ty else 0
    tx += mx
    ty += my
    print(moves[mx][my])
"""
I=input
H=int
C,D,A,B=[H(A)for A in I().split()]
G=[['','S','N'],['E','SE','NE'],['W','SW','NW']]
while True:K=H(I());E=1 if C>A else-1 if C<A else 0;F=1 if D>B else-1 if D<B else 0;A+=E;B+=F;print(G[E][F])