import os
import urllib.request

path = os.getcwd()
print ("The current working directory is %s" % path)

# define the name of the directory to be created
path += "/test"

# define the access rights
access_rights = 0o755

try:
    os.mkdir(path, access_rights)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s" % path)

for x in range(1):
    print(x)
    urllib.request.urlretrieve("https://www.shiftingsands.gg//img/Leaflet/Maps/Canyon/{}/0/0.png".format(x), "map.png")