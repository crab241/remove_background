from rembg import remove
from PIL import Image
input_path = 'testimage.jpg' #enter the image file to remove BG
output_path = 'resulttest.png'#output the non-bg image file
inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)
Image.open("resulttest.png")