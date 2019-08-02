close all; clear; clc;

sub = rossubscriber('/usb_cam/image_raw');

pause(2);

r = rosrate(5);

while 1 == 1
    received = sub.LatestMessage;
    image = readImage(received);
    imshow(image);
    
    waitfor(r);
end