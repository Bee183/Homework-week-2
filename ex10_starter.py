import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

print(sys.platform)
print(hdir)

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')
print(pattern)

# TODO: Use the glob.glob() function to obtain the list of filenames
for name in glob.glob('*'):
    print(name)

# TODO: use os.path.getsize to find each file's size
#each file in directory
#get size of each file
# print size of each file
directory = glob.glob('*')
print(directory)
for name in directory:
    print('Size of', name, 'is', os.path.getsize(name), 'bytes')

# TODO: Add a test to only display files that are not zero length
for name in directory:
    if not os.path.getsize(name)==0:
        print('Size of', name, 'is', os.path.getsize(name), 'bytes')

# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename()
#think ours is showing without the directory name
