# ProgrammableImageArt
Write code, make pretty pictures.

# Dependencies
Uses ```numpy```, ```PIL```, and ```keyboard```.

# Usage
In the ```run.txt``` file, you have control over the color of every pixel on the canvas of size 1000 by 1000. As such, a lot of manipulation can be done in order to produce unique images. The color of a pixel at ```(x, y)``` is can be accessed via ```image[x, y]```. For example, if we wanted to color the canvas white, we would use the RGB value for white ```(255, 255, 255)```:
```
image[x, y] = (255, 255, 255)
```
The ```math.py``` file is available for use as well. For example,
```
if math.dist((512, 512), (x, y)) == 100:
    image[x, y] = (255, 255, 255)
```
would produce a white circle outline with radius 100 centered at the middle of the image.

By default, all values on the canvas are ```(0, 0, 0)```; black.

Many neat patterns can be generated with a few simple lines of code defining a basic rule. Below are just a few examples:
![sin](https://github.com/SeanJxie/ProgrammableImageArt/blob/main/samples/sin.png)
![grad](https://github.com/SeanJxie/ProgrammableImageArt/blob/main/samples/gradient.png)
![waves](https://github.com/SeanJxie/ProgrammableImageArt/blob/main/samples/waves.png)

To run the ```run.txt``` file, start CMD in the same directory and enter
```
py runfile.py
```


You can also directly write Python code into the ```run.py``` file that is generated after a ```py runfile.py``` call.
