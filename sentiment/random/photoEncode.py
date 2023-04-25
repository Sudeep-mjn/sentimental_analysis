from email import message

from PIL import Image

# open the image and convert it to RGB mode
image = Image.open("goku.jfif").convert("RGB")

# get the width and height of the image
width, height = image.size

# create a new image to store the encoded data
encoded_image = Image.new("RGB", (width, height), "white")

# loop through each pixel in the image and encode the message
for x in range(width):
    for y in range(height):
        # get the RGB values of the pixel
        r, g, b = image.getpixel((x, y))

        # convert the RGB values to binary
        r_binary = format(r, '08b')
        g_binary = format(g, '08b')
        b_binary = format(b, '08b')

        # get the next bit of the message to encode
        bit = message[index]
        index += 1

        # encode the bit in the least significant bit of each RGB value
        r_binary = r_binary[:-1] + bit
        g_binary = g_binary[:-1] + bit
        b_binary = b_binary[:-1] + bit

        # convert the binary values back to integers
        r = int(r_binary, 2)
        g = int(g_binary, 2)
        b = int(b_binary, 2)

        # set the RGB values of the new image
        encoded_image.putpixel((x, y), (r, g, b))

# save the encoded image to a file
encoded_image.save("encoded_image.png")