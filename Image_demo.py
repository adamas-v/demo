#operate Image by PIL.image
from PIL import Image
import torch
image_tensor = torch.rand(3,128,128)
print('generate radom tensor for image as follow :\n',image_tensor)

from torchvision import transforms

image = transforms.ToPILImage()(image_tensor)


from matplotlib import pyplot
pyplot.figure()
pyplot.subplot(2,2,1)
pyplot.imshow(image)
pyplot.subplot(2,2,2)
pyplot.imshow(image)
pyplot.subplot(2,2,3)
pyplot.imshow(image)
pyplot.subplot(2,2,4)
pyplot.imshow(image)
pyplot.show()



