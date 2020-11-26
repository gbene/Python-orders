'''
author: Gabriele Benedetti

25/11/2020

aim:
Apply certain masks to a specific range of images:

photo 1: '' Links_Initial.jpg ''
photo 2 to 21: '' Links_Regular.jpg ''
photo 22: '' Midden_Initial.jpg ''
photo 23 to 42: '' Midden_Regular.jpg ''
photo 43: '' Rechts_Initial.jpg ''
photo 44 to 63: ''Rechts_Regular.jpg ''
'''
# IMPORTS
import Metashape as mt
import os

# VARIABLES
chunk = mt.app.document.chunk #define the current working chunk
cameras = chunk.cameras #define the cameras in the chunk

img_path = mt.app.getExistingDirectory() # ask the folder path of the masks
tol = mt.app.getInt("Choose tolerance value for masking") #ask for the masking tolerance value
os.chdir(img_path) #change directory to that path

# EXECUTION


chunk.importMasks(path='Links_Initial.jpg',source=MaskSourceBackground,operation=MaskOperationReplacement, tolerance=tol,cameras=cameras[0])
chunk.importMasks(path='Links_Regular.jpg',source=MaskSourceBackground,operation=MaskOperationReplacement,tolerance=tol,cameras=cameras[1:21])
chunk.importMasks(path='Midden_Initial.jpg',source=MaskSourceBackground,operation=MaskOperationReplacement,tolerance=tol,cameras=cameras[21])
chunk.importMasks(path='Midden_Regular.jpg',source=MaskSourceBackground,operation=MaskOperationReplacement,tolerance=tol,cameras=cameras[22:42])
chunk.importMasks(path='Rechts_Initial.jpg',source=MaskSourceBackground,operation=MaskOperationReplacement,tolerance=tol,cameras=cameras[42])
chunk.importMasks(path='Rechts_Regular.jpg',source=MaskSourceBackground,operation=MaskOperationReplacement,tolerance=tol,cameras=cameras[43:64])
