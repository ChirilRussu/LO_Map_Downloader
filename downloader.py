import os
import urllib.request

# stores current directory
path = os.getcwd()
print ("The current working directory is %s" % path)

# adds the names of the new directory to be created
path += "/tiles/"

# defines the access rights
access_rights = 0o755

# creates the tiles directory
try:
    os.mkdir(path, access_rights)
except OSError:
    print ("Creation of the tiles directory {} failed".format(path))
else:
    print ("Successfully created the tiles directory {}".format(path))

# main itteration variable
var_iteration = 0
# number of x subfolders
x_array = [8]
# array to be used in loops
ar_loop = [1,5,9,17,33,65,129]
# arry to be used for number of tiles
ar_tiles = [0,4,8,16,32,64,128]

# main loop 
# creates the x directories
for x in range(x_array[0]):
    try:
        os.mkdir("{}/{}".format(path,x), access_rights)
    except OSError:
        print ("Creation of the X directoriy {} failed".format(x))
    except:
        print("Something else went wrong")
    else:
        print ("Successfully created the X directoriy {}".format(x))
   
        # creates the y directories
    for y in range(ar_loop[var_iteration]):
        try:
            os.mkdir("{}/{}".format(path,x), access_rights)
        except OSError:
            print ("Creation of the X directoriy {} failed".format(x))
        except:
            print("Something else went wrong")
        else:
            print ("Successfully created the X directoriy {}".format(x))
        
       # for y in range(ar_loop[var_iteration]):
            #urllib.request.urlretrieve("https://www.shiftingsands.gg//img/Leaflet/Maps/Canyon/{}/{}/{}.png" \
            #.format(var_iteration,x,y), "{}/{}/{}.png".format(path,x,y))
            
    #print(var_iteration)
    #var_iteration += 1
    
    
    
    
    