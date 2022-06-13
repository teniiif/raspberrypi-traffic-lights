# Raspberry Pi Traffic Lights
## Overview

The traffic light follows the sequence for a steady traffic light and allows for a pedestrian crosswalk. The light remains steady until "someone" pushes the button. After which, the green light changes to yellow for 5 seconds as with most traffic lights and then changes to red for 15 seconds. During hwich, the pedestrian should have crossed the road safely and then the light turns green again. 

## Materials Used
* Raspberry Pi
* Breadboard
* 1 resistor (220 ohm)
* 3 LEDs (1 red, 1 yellow, 1 green)
* 1 push button
* 5 male-to-female jumper wires
* 3 male to male jumper wires

## Wiring 
The table below ahows what the GPIO pins on the Raspberry Pi are connected to
GPIO pin  | Component
------------- | -------------
GPIO 17  | Red LED
GPIO 27 | Yellow LED
GPIO 22  | Green LED
GPIO 23 | Push Button

The images below show the wiring diagram as well as the schematics for the traffic light.

<p align="center">
<img width="500" src="https://user-images.githubusercontent.com/85775364/172915931-a915d0c7-7b19-415f-9816-9038616b1f02.jpg" alt="traffic_light" >
</p> <p align="center">
  Wiring Diagram
</p> <p align="center">
<img width="500" src="https://user-images.githubusercontent.com/85775364/172916402-3a96996f-d9ab-4469-a086-c2415ff230a8.jpg" alt="traffic_light" >
</p><p align="center">
  Schematic
</p>


## Demo
Click the image below to play the video
<p align="center">
<a href="https://youtube.com/shorts/CE5YG9M9c4w?feature=share" target="_blank"><img src="https://user-images.githubusercontent.com/85775364/172287368-cde8e429-58db-4ac0-9074-8d4f8e088de3.jpg" alt="Traffic Light Video" width="400" height="500" /></a>
</p>
