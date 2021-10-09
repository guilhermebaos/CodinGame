n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
association = dict()
for i in range(n):
    extension, mime = input().split()
    association[extension.lower()] = mime
for i in range(q):
    fname = input().split('.')
    if len(fname) == 1:
        print('UNKNOWN')
        continue
    extension = fname[-1].lower()
    try:
        print(association[extension])
    except KeyError:
        print('UNKNOWN')
