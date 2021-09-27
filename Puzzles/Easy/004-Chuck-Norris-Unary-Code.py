# Translate the message to binary
message = ''.join([bin(ord(character))[2:].rjust(7, '0') for character in list(input())])

chuck_norris = ''
index = 0
while index < len(message):

    letter = message[index]

    # Add the start of a block
    chuck_norris += '0 ' if letter == '1' else '00 '

    # Add the number of bits in that block
    num = 0
    for next_letter in message[index:]:
        if next_letter == letter:
            index += 1
            num += 1
        else:
            break
    chuck_norris += '0' * num + ' '

print(chuck_norris[:-1])
