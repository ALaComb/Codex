import os, shutil

print('start')
path = r'E:\E-DnD\MapsAndTokens'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for filen in f:
        files.append(os.path.join(r, filen))
    break

badfilefound = False
for fil in files:
    if fil.find(' ') != -1:
        print(f'Bad Name: {fil}')
        newfil = ''.join(fil.split(' '))
        shutil.move(fil, newfil)
        fil = newfil
        d = input('Press any key to continue...')
        badfilefound = True

if not badfilefound:
    print('No files renamed.\n')


print('looking through files')
for filename in files:

    os.system('start "' + filename + '"')
    print("Original Name: " + filename)
    name = input('NAME: ')
    size = input('SIZE: ')
    tags = input('TAGS: ')
    newfilename = name + '_' + size + '_[' + '-'.join(tags.split()) + ']' + filename[filename.find('.'):]
    print(newfilename)
    n = input('Press any key to continue...')
    newdestination = r'E:\E-DnD\MapsAndTokens\Tagged\' + newfilename
    shutil.move(filename, newdestination)
    print('Moved to ' + newdestination)
    print()