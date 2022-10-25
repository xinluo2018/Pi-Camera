## author: xin luo
## creat: 2022.3.18 # modify: xxxx
## des: download dem data from OpenTopography World DEM
## !!! The user should login OpenTopography firstly, because the dem download is requried.


import numpy as np
import cv2  
import glob

def jpg2video(paths_file, dir_save):
  '''
  des: convert .jpg formated images to video. 
  args:
    paths_file: list, contains all the images.
    dir_save: the directory to save the generated video.
  '''
  img_array = []
  for filename in paths_file:
      img = cv2.imread(filename)
      height, width, layers = img.shape
      size = (width,height)
      img_array.append(img)
  
  out = cv2.VideoWriter(dir_save+'/video.avi',cv2.VideoWriter_fourcc(*'mp4v'), 15, size)
  
  for i in range(len(img_array)):
      out.write(img_array[i])
  out.release()