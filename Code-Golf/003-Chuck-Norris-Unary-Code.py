"""
Original Code:

message = ''.join([bin(ord(character))[2:].rjust(7, '0') for character in list(input())])

chuck_norris = ''
index = 0

while index < len(message):

    letter = message[index]

    chuck_norris += ' 0 ' if letter == '1' else ' 00 '

    for next_letter in message[index:]:
        if next_letter == letter:
            index += 1
            chuck_norris += '0'
        else:
            break

print(chuck_norris[1:])
"""
F='0'
C=''
B=C.join([bin(ord(A))[2:].rjust(7,F)for A in list(input())])
A=0
while A<len(B):
	D=B[A];C+=' 0 'if D=='1'else' 00 '
	for E in B[A:]:
		if E==D:A+=1;C+=F
		else:break
print(C[1:])
