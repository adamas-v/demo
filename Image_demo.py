#operate Image by PIL.image
from PIL import Image
import torch
import numpy
image_tensor = torch.rand(3,128,128)
image_tensor_splice = torch.cat([image_tensor,image_tensor],dim = 2)
print('generate radom tensor for image as follow :\n',image_tensor)

from torchvision import transforms

image = transforms.ToPILImage()(image_tensor)
image_splice = transforms.ToPILImage()(image_tensor_splice)


from matplotlib import pyplot



pyplot.figure()
pyplot.subplot(2,2,1)
pyplot.imshow(image)
pyplot.subplot(2,2,2)
pyplot.imshow(image)
pyplot.subplot(2,2,3)
pyplot.imshow(image)
pyplot.subplot(2,2,4)
pyplot.imshow(image_splice)
pyplot.show()

#imshow of cv2
import cv2
cv2.namedWindow('yes')
cv2.imshow('yes', image_tensor_splice.transpose(0,2).numpy())#cv2 support H*W*C format
cv2.waitKey()

#imshow of Image
image = Image.open('1.png')
image.show()



