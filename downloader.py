import os
import urllib.request
import ctypes

print ("This script will download map tiles from https://www.shiftingsands.gg.")
print ("The further it gets the more time it will take to fill the current folder.")
print ("Because the number of images increases exponentially.")
print ("You can check the progress by going into the latest folder.")
print ("When it is done the taskbar icon will flash and promt you to close it.")

# stores current directory
path = os.getcwd()
print ("The current working directory is {}.".format(path) + "\n")

# adds the names of the new directory to be created
path += "/Tiles/"

# defines the access rights
access_rights = 0o755

# creates the tiles directory
try:
    os.mkdir(path, access_rights)
except OSError:
    print ("Creation of the tiles directory {} failed.".format(path))
else:
    print ("All files will be downloaded to {}.".format(path))
    # for testing:
    # print ("Successfully created the tiles directory {}".format(path))

# number of x subfolders
x_folders = [8]
# number of y subfolders and z images - different folders have a different number of subfolders amd images
yz_array = [2**0, 2**1, 2**2, 2**3, 2**4, 2**5, 2**6, 2**7]

# main loop 
# creates the x directories
for x in range(x_folders[0]):
    try:
        os.mkdir("{}/{}".format(path,x), access_rights)
    except OSError:
        print ("Failed to create the X directory - {}.".format(x))
        break
    except:
        print("Something went wrong creating X folders.")
        break
    else:
        print("Downloading images to {}{}.".format(path,x))
    
        # creates the y directories
        for y in range(yz_array[x]):
            try:
                os.mkdir("{}/{}/{}".format(path,x,y), access_rights)
            except OSError:
                print ("Failed to create the Y directory - {}.".format(y))
                break
            except:
                print("Something went wrong creating Y folders.")
                break
            else:
                pass
            
            # downloads z images
            for z in range(yz_array[x]):
                try:
                    urllib.request.urlretrieve("https://www.shiftingsands.gg//img/Leaflet/Maps/Canyon/{}/{}/{}.png" \
                    .format(x,y,z), "{}/{}/{}/{}.png".format(path,x,y,z))
                except: 
                    print("Something went wrong downloading Z images.")
                    break
                else:
                    pass
    
    print("Successfully filled folder {}{}.".format(path,x) + "\n")
                    
print("Finished running.")
ctypes.windll.user32.FlashWindow(ctypes.windll.kernel32.GetConsoleWindow(), True) # flashes the taskbar icon
print("Press Enter to close")
input("\n")
            
    
    
    
    
    