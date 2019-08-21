clear; close all; clc;

cam = webcam(2);

while 1 == 1
    image = cam.snapshot();
    [position, area] = findCube(image)
end