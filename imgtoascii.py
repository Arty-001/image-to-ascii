from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# to resize the image
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height/width
    new_height = int(ratio*new_width*0.6)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

#converting image to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)
    
# converting pixels into ascii values
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)    

if __name__ == '__main__':
    
    
    path = input("Enter a valid pathname to an image:\n") # input the path of the immage from your respective folder
    try:
        image = Image.open(path)
    except:
        print(path, " is not a valid pathname to an image.")
        exit(0)
   

    new_width=100
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))
    
    
    pixel_count = len(new_image_data)  
    ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
    
    
    print(ascii_image)
    
    # printing ascii image into a text file
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)
    

#https://stackoverflow.com/questions/17856242/convert-string-to-image-in-python