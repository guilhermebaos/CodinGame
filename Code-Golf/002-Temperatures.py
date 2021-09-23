"""
Original code, before getting minified:

if int(input()) == 0:
    print('0')
else:
    temps = [int(i) for i in input().split()]
    print(max([t for t in temps if abs(t) == min([abs(t) for t in temps])]))
"""
E=abs
D=print
C=input
B=int
if B(C())==0:D('0')
else:A=[B(A)for A in C().split()];D(max([B for B in A if E(B)==min([E(B)for B in A])]))