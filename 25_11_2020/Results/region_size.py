'''
script by: Gabriele Benedetti

28/11/2020
'''

# IMPORTS
import Metashape as mt
import statistics as st

# VARIABLES
chunk = mt.app.document.chunk #define active chunk
sparse_point = chunk.point_cloud #define the sparse point cloud
points = sparse_point.points #define points of sparse point cloud
T = chunk.transform.matrix #transform matrix
x,y,z=[],[],[]
#S = chunk.transform.scale #scale factor of the active chunk
crs = chunk.crs #coordinate system

#user input
x_uplim = mt.app.getFloat("Choose an upper x lim (eg. 0.9)")
x_lowlim = mt.app.getFloat("Choose a lower x lim (eg. 0.1)")
y_uplim = mt.app.getFloat("Choose an upper y lim (eg. 5.5)")
y_lowlim = mt.app.getFloat("Choose a lower y lim (eg. 1)")
z_uplim = mt.app.getFloat("Choose a upper z lim (eg. 1)")
z_lowlim = mt.app.getFloat("Choose a lower z lim (eg. 0)")

x_delta = x_uplim-x_lowlim

# EXECUTION

# find center of point cloud (used to center the bounding box)



# find points that have local coordinates less than 0.1, 0.9 (x) and 1, 5.5 (y)
for point in points:
    geo_points = crs.project(T.mulp(point.coord[:3])) #convert from internal system to local
    if geo_points[0]<= x_lowlim or geo_points[0]>= x_uplim or geo_points[1]<= y_lowlim or geo_points[1]>= y_uplim or geo_points[2]<=0 or geo_points[2]>=1:
        None
    else:
        coord = T*point.coord #transform coordinates with the matrix
        x.append(coord[0])
        y.append(coord[1])
        z.append(coord[2])


mini,mini_x = mt.Vector([min(x),min(y),min(z)]), mt.Vector([min(x)+x_delta,min(y),min(z)]) #minimum values of x,y and z and x opposite
maxi,maxi_x = mt.Vector([max(x),max(y),max(z)]), mt.Vector([max(x)-x_delta,max(y),max(z)])#maximum values of x,y and z and x opposite

center = (maxi+mini)/2 #bounding box center

# this is horrible!

chunk.addMarker(T.inv().mulp(center))
chunk.addMarker(T.inv().mulp(mini))
chunk.addMarker(T.inv().mulp(mini_x))
chunk.addMarker(T.inv().mulp(maxi))
chunk.addMarker(T.inv().mulp(maxi_x))


for marker in chunk.markers:
    if 'target' in marker.label:
        marker.reference.enabled=False
    elif 'point' in marker.label:
        vector = marker.reference.location
        vector[2] = center[2]
        marker.reference.location = vector
        marker.reference.enabled=True

chunk.updateTransform()


chunk.region.center=chunk.transform.matrix.inv().mulp(center) #set the center of bounding box
chunk.region.rot = chunk.transform.matrix.rotation().t()

limits = maxi-mini #bounding box limits
limits[2] = z_uplim-z_lowlim
chunk.region.size=limits/chunk.transform.matrix.scale() #set the dimensions of the bounding box
#chunk.region.rot = T.rotation().t() #rotate region to level


print(chunk.region.size)
