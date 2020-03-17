import os
import urllib.request
import ctypes

print ("This script will download map tiles from https://www.shiftingsands.gg.")
print ("The further it gets the more time it will take to fill the current folder.")
print ("Because the number of images increases exponentially.")
print ("You can check the progress by going into the latest folder.")
print ("When it is done the taskbar icon will flash and prompt you to close the window.")

# stores current folder
path = os.getcwd()

# adds the names of the new folder to be created
path += "/Tiles"

# defines the access rights
access_rights = 0o755

# creates the tiles folder
try:
    os.mkdir(path, access_rights)
except OSError:
    print ("Creation of the Tiles folder {} failed.".format(path))
else:
    print ("All files will be downloaded to {}.".format(path))
    # for testing:
    # print ("Successfully created the tiles folder {}".format(path))

# number of X subfolders
x_folders = 8
# number of Y subfolders and Z images - different X folders have a different number of subfolders amd images
yz_array = [2**0, 2**1, 2**2, 2**3, 2**4, 2**5, 2**6, 2**7]

# main loop 
# creates the X folders
for x in range(x_folders):
    try:
        os.mkdir("{}/{}".format(path,x), access_rights)
    except OSError:
        print ("Failed to create the X folder - {}/{}.".format(path,x))
        break
    except:
        print("Something went wrong creating the X folder {},{}.".format(path,x))
        break
    else:
        print("Downloading images to {}/{}.".format(path,x))
    
        # creates the Y folders
        for y in range(yz_array[x]):
            try:
                os.mkdir("{}/{}/{}".format(path,x,y), access_rights)
            except OSError:
                print ("Failed to create the Y folder - {}/{}/{}.".format(path,x,y))
                break
            except:
                print("Something went wrong creating Y folder {}/{}/{}.".format(path,x,y))
                break
            else:
                pass
            
            # downloads the Z images
            for z in range(yz_array[x]):
                try:
                    urllib.request.urlretrieve("https://www.shiftingsands.gg//img/Leaflet/Maps/SleepingGiants/{}/{}/{}.png" \
                    .format(x,y,z), "{}/{}/{}/{}.png".format(path,x,y,z))
                except: 
                    print("Something went wrong downloading Z image {}/{}/{}/{}.png".format(path,x,y,z))
                    break
                else:
                    pass
    
    print("Finished filling folder {}/{}.".format(path,x) + "\n")
                    
print("Finished running.")
# flashes the taskbar icon
ctypes.windll.user32.FlashWindow(ctypes.windll.kernel32.GetConsoleWindow(), True)
print("Press Enter to close")
input("\n")
            
    
    
    
    
    