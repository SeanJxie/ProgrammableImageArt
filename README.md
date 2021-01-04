# ProgrammableImageArt
Using code to make art.

# Dependencies
Uses ```numpy```, ```PIL```, and ```keyboard```.

# Usage
In the ```run.txt``` file, you have control over the color of every pixel on the canvas of size 1000 by 1000. As such, a lot of manipulation can be done in order to produce unique images. The color of a pixel at ```(x, y)``` is can be accessed via ```image[x, y]```. For example, if we wanted to color the point (0, 0) white, we would use the RGB value for white ```(255, 255, 255)```:
```
image[0, 0] = (255, 255, 255)
```

If we wanted to change all pixels, ```x``` and ```y``` would be used rather than actual coordinate values like in the example above. For example, if we wanted to color the entire canvas white:
```
image[x, y] = (255, 255, 255)
```

The ```math``` library is available for use as well. For example,
```
if math.dist((512, 512), (x, y)) == 100:
    image[x, y] = (255, 255, 255)
```
would produce a white circle outline with radius 100 centered at the middle of the image.

By default, all values on the canvas are ```(0, 0, 0)```; black.

To run the ```run.txt``` file, start CMD in the same directory and enter
```
py runfile.py
```

As mentioned above, the ```math``` library is available for use, alongside ```random``` and a customizable ```util```.

Specifically, If you'd like to add custom functions, write them into the ```util.py``` file. These functions can be called from ```run.txt``` using standard ```util.function()``` convention.


You can also directly write Python code into the ```run.py``` file that is generated after a ```py runfile.py``` call.


Many neat patterns can be generated with a few simple lines of code defining a basic rule. Below are just a few examples:
![ball](https://github.com/SeanJxie/ProgrammableImageArt/blob/main/samples/ball.png)
![sin](https://github.com/SeanJxie/ProgrammableImageArt/blob/main/samples/sin.png)
![static](https://github.com/SeanJxie/ProgrammableImageArt/blob/main/samples/static_circle.png)
![grad](https://github.com/SeanJxie/ProgrammableImageArt/blob/main/samples/gradient.png)
![waves](https://github.com/SeanJxie/ProgrammableImageArt/blob/main/samples/waves.png)
![bwgrad](https://github.com/SeanJxie/ProgrammableImageArt/blob/main/samples/bwgrad.png)

