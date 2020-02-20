import os
import urllib.request

# stores current directory
path = os.getcwd()
print ("The current working directory is %s" % path)

# adds the names of the new directory to be created
path += "/tiles/"

# define the access rights
access_rights = 0o755

# creates the tiles directory
try:
    os.mkdir(path, access_rights)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s" % path)

# number of main subfolders
var_folders = 8
# array to be used in loops
ar_loop = [1,5,9,17,33,65,129]
# arry to be used for number of tiles
ar_tiles = [0,4,8,16,32,64,128]
# itteration variable
i = 0

# creates directories 0-7 inside tiles
for x in range(var_folders):
    print(x)
    try:
        os.mkdir("{}/{}".format(path,x), access_rights)
    except OSError:
        print ("Creation of the directory %s failed" % x)
    else:
        print ("Successfully created the directory %s" % x)
   

for x in range(var_folders): # loops 8 times
    for y in range(ar_loop[i]):
        urllib.request.urlretrieve("https://www.shiftingsands.gg//img/Leaflet/Maps/Canyon/0/0/0.png" \
        , "{}/{}/{}.png".format(path,x,y))
    ++i
    
    
    
    