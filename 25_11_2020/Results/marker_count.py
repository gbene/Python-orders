'''
author: Gabriele Benedetti

25/11/2020

aim:
Count the total number of markers detected in a chunk 
'''



# IMPORTS
import Metashape as mt

# VARIABLES

chunk = mt.app.document.chunk #define the active chunk
cameras = chunk.cameras #define a list of the cameras inside the chunk
n_cameras = len(chunk.cameras) #number of cameras

# EXECUTION

'''
There isn't a direct way to count markers in every image. To resolve this
problem we can use the function detectMarkers for every image. Normally this
function is applied to the whole chunk but the problem is that same markers
are grouped togeather and so we do not rappresent the total number of detected
markers. To avoid this annoince we can apply the function separately to every
image. In this way every marker found is considered as separate.
After that we can calculate the total number of markers simply by the length of
the list of markers present in the chunk.

This process leaves a very messy workplace so after the counting all of the
markers are removed and then detected again this time considering the whole
chunk.

With this solution at the end you will have the total numers of detected markers
and the tidy workspace that is normally produced after a target detection.
'''

chunk.remove(chunk.markers) #remove previous markers


for camera in cameras:
    chunk.detectMarkers(cameras=camera)
total_markers = len(chunk.markers)
chunk.remove(chunk.markers)
chunk.detectMarkers()
print('found {} markers in {} images (1:{} ratio)'.format(total_markers,n_cameras,total_markers/n_cameras))
