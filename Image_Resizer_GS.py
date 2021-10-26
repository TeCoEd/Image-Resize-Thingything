# Importing Image class from PIL module
from PIL import Image
import glob
import os
from time import sleep
path = "/home/pi/Python_Resize/images_to_resize"

# Pulls in all the image file names from the folder
def get_imlist(path):
       
    list_of_images_in_folder =  [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpeg')]
    print ("...finding images")
    sleep(2)
    print ("")
    sleep(1)
    print ("...found the following images")
    print ("")
    sleep(1)
    print (list_of_images_in_folder)
    print ("")
    
     
    # Enter the new size that you want
    print ("Please enter your new sizes in pixels")
    print ("")
    width_new = int(input("Enter that width "))
    height_new = int(input("Enter that height "))
    
    new_image_fill_name = 0
    
    for image in list_of_images_in_folder:
        
        # Opens a image in RGB mode

        #print (image)

        sleep (1)
        original_im = Image.open(image)
        # Resize the image
        newsize = (width_new, height_new)
        final_image = original_im.resize(newsize)
        #final_image = final_image.convert('LA')
        # Shows the image in image viewer
        final_image.show() # for testing

        #extract the filename from the image list
        extract_filename = image
        start = extract_filename.find("resize/")
        #print (start) for testing
        final_filename = extract_filename[start+7:]
        print (final_filename) #for testing  

        #sleep (5)
        # Saves the new image
        '''change the file names!'''
        final_image.save("/home/pi/Python_Resize/new_resized_" + final_filename)
        
        #new_image_fill_name =+ 1

#CONVERT TO GRAYSCALE
def get_imlist_gs(path):
       
    list_of_images_in_folder =  [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpeg')]
    print ("")   
    print ("...finding images")
    sleep(1)
    print ("")
    sleep(1)
    print ("...found the following images")
    print ("")
    sleep(1)
    print (list_of_images_in_folder)
    print ("")
    
     
    # Enter the new size that you want
    print ("Please enter your new sizes in pixels")
    print ("")
    width_new = int(input("Enter that width "))
    height_new = int(input("Enter that height "))
    
    new_image_fill_name = 0
    
    for image in list_of_images_in_folder:
        
        # Opens a image in RGB mode

        #print (image)

        sleep (1)
        original_im = Image.open(image)
        # Resize the image
        newsize = (width_new, height_new)
        final_image = original_im.resize(newsize)
        final_image = final_image.convert('LA')
        # Shows the image in image viewer
        final_image.show() # for testing

        #extract the filename from the image list
        extract_filename = image
        start = extract_filename.find("resize/")
        finish = extract_filename.find(".jpeg")
        #print (start) #for testing
        #print (finish) #for testing
        final_filename = extract_filename[start+7:finish]
        #print (final_filename) #for testing  

        #sleep (15)
        # Saves the new image
        '''change the file names!'''
        final_image.save("/home/pi/Python_Resize/new_resized_" + final_filename + ".png")
        
        #new_image_fill_name =+ 1
        

#MAIN PROGRAM
print ("Welcome to the image resizer")
sleep(1)
print ("")
print ("Ensure that all image are in the Folder before you continue")
sleep(1)
print ("")
grayscale = input("Would you like the images to be saved in grayscale? (Y/N) ")
if grayscale.upper() == "Y":
    get_imlist_gs(path)
else:    
    get_imlist(path)
print ("")
print ("All images have been resized")
        

