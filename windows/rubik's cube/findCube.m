function [position, area] = findCube(image)
% findCube: Returns position and area of green face of cube

% Filter image
[BW,masked] = createMask(image);

% Show masked image
imshow(masked);
hold on;

% Fill holes
BW = imfill(BW, 'holes');

% Find and show boundaries
b = bwboundaries(BW, 'noholes');
visboundaries(b);

% Get stats
stats = regionprops(BW);
    
% Find last 10000+ pixel box
% Should be changed to add up all the large areas and return center and
% total area.
if size(stats) > 0
    cube = stats(1);
    for i = 1:size(stats)
        if stats(i).Area > 10000
            cube = stats(i);
        end
    end
end

% TODO: Exception for when no cube found?
% TODO: Maybe change cube so that it's an array.

if exist('cube', 'var')
    position = cube.Centroid;
    area = cube.Area;
else
    position = [-1 -1];
    area = -1;
end

end

