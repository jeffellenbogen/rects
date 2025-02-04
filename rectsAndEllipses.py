
# Used in main loop
from time import sleep
import random

###################################
# Graphics imports, constants and structures
###################################
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw

# this is the size of ONE of our matrixes. 
matrix_rows = 32 
matrix_columns = 32 

# how many matrixes stacked horizontally and vertically 
matrix_horizontal = 5 
matrix_vertical = 3

total_rows = matrix_rows * matrix_vertical
total_columns = matrix_columns * matrix_horizontal

options = RGBMatrixOptions()
options.rows = matrix_rows 
options.cols = matrix_columns 
options.chain_length = matrix_horizontal
options.parallel = matrix_vertical 


'''options.hardware_mapping = 'adafruit-hat-pwm' 
'''
#options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
options.hardware_mapping = 'regular'  

options.gpio_slowdown = 2

matrix = RGBMatrix(options = options)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
white = (250,250,250)
black = (0,0,0)

xCenterPt = total_columns/2 - 1
yCenterPt = total_rows/2 - 1
incrementer = 4
lineWidth = 2

###################################
# Main loop 
###################################
image = Image.new("RGB", (total_columns,total_rows))
draw = ImageDraw.Draw(image)


while True:
  incrementer = random.randint(2,10)
  lineWidth = random.randint(1,incrementer/2)
  randomColor = random.randint(0,360)
  rectColor ="hsl({}, 100%, 50%)".format(randomColor) 
  ellipseColor ="hsl({}, 100%, 50%)".format(randomColor+180)  

  for i in range (0, total_rows/2, incrementer):
    for j in range (lineWidth):
      draw.rectangle((xCenterPt - i - j, yCenterPt - i - j, xCenterPt + i + j, yCenterPt + i + j), outline = (rectColor))
      matrix.SetImage(image, 0, 0)
    sleep (.05)  
    for j in range (lineWidth):  
      draw.ellipse((xCenterPt- i - incrementer/2 - j,yCenterPt - i - incrementer/2 - j,xCenterPt + i + incrementer/2 + j,yCenterPt + i + incrementer/2 + j), outline = (ellipseColor))
      matrix.SetImage(image, 0, 0)  
    sleep (.05)

  ########################################
  # Erase whole matrix by setting to black
  #########################################
  sleep(2)
  draw.rectangle((0,0,total_columns,total_rows), fill = (black))
  matrix.SetImage(image, 0, 0)  

try:
  print("Press CTRL-C to stop")
  while True:
    sleep(100)
except KeyboardInterrupt:
  exit(0)

