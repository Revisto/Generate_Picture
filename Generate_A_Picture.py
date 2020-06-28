from time import time
Before=time()

from PIL import Image
import numpy as np
from Generate_A_Random_List_Of_Pixels import CreatePixels

def CreatePicture(Name="Generated_Picture.png"):
   Pixels=CreatePixels(426,240)
   array = np.array(Pixels , dtype=np.uint8)
   new_image = Image.fromarray(array)
   new_image.save(Name)
   
   
CreatePicture()

print ("It Took >>>"+str(time()-Before)+"<<<  sec")





# H   E   L   P
#I t   Should Be Like This
#pixels = [
#   [(54, 54, 54), (232, 23, 93), (71, 71, 71), (168, 167, 167)],
#   [(204, 82, 122), (54, 54, 54), (168, 167, 167), (232, 23, 93)],
#   [(71, 71, 71), (168, 167, 167), (54, 54, 54), (204, 82, 122)],
#   [(168, 167, 167), (204, 82, 122), (232, 23, 93), (54, 54, 54)]
#]
