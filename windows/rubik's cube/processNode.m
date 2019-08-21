close all; clear; clc;

% Subscribe to image feed
% Should use callbacks but not sure what name of passed image variable is
sub = rossubscriber('/usb_cam/image_raw');

% Create publishers
position = [0 0];
% area = 0;
[pub_pos, msg_p] = rospublisher('/processed/position', 'geometry_msgs/Point');
[pub_area, msg_a] = rospublisher('/processed/area', 'std_msgs/Float64');

pause(2);

r = rosrate(5);
while 1 == 1
  received = sub.LatestMessage;
  image = readImage(received);

  [position, area] = findCube(image);

  msg_p.X = position(1);
  msg_p.Y = position(2);
  msg_a.Data = area;
  
  send(pub_pos, msg_p);
  send(pub_area, msg_a);
  
  waitfor(r);
end