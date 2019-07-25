clear; close all; clc;

cam = webcam(2);

while 1 == 1
    % Get snapshot and mask
    image = cam.snapshot();
    [BW,masked] = createMask(image);
    
    % Show masked image
    imshow(masked);
    hold on;
    
    % Fill holes
    BW = imfill(BW, 'holes');
    % imclose maybe
    
    % Find and show boundaries
    b = bwboundaries(BW, 'noholes');
    visboundaries(b);
    
    % Get stats
    stats = regionprops(BW);
    
    % Find last 10000+ pixel box
    % Should be changed to add up all the large areas and return center and
    % total area.
    for i = 1:size(stats)
        if stats(i).Area > 10000
            cube = stats(i);
        end
    end
    
    % TODO: Exception for when no cube found? The filter right now handles
    % this inherently.
    % TODO: Turn into function that returns area and center.
end