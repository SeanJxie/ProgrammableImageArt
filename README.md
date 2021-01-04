# ProgrammableImageArt
Write code, make pretty pictures.

# Dependencies
Uses ```numpy```, ```PIL```, and ```keyboard```.

# Usage
In the ```run.txt``` file, you have control over the color of every pixel on the canvas of size 1024 by 1024. The pixels can be accessed via ```image[x, y]```. For example, if we wanted to paint the canvas white (RGB(255, 255, 255)), we type in the ```run.txt``` file:
```
image[x, y] = (255, 255, 255)
```
The ```math.py``` file is available to use as well. For example,
```
if math.dist((512, 512), (x, y)) == 100:
    image[x, y] = (255, 255, 255)
```
would produce a white circle with radius 100 centered at the middle of the image.

To run the ```run.txt``` file, start CMD in the same directory and enter
```
py runfile.py
```


You can also directly write Python code into the ```template``` file.
