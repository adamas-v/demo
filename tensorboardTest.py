from tensorboardX import SummaryWriter
import torch
import torchvision
from matplotlib import pyplot
import os
## sythrthic same pictures
a = torch.rand(1,5,3)
a = torch.softmax(a,dim=1)
# a = a*255


figure1 = pyplot.figure()
pyplot.subplot(2,2,1)
a = torchvision.transforms.ToPILImage()(a)
pyplot.imshow(a)
pyplot.subplot(2,2,2)
pyplot.imshow(a)
pyplot.show

# import PIL.Image as Image
# img1 = Image.open('1.png').convert('RGB')
# img1 = torchvision.transforms.ToTensor()(img1)

# summarywriter = SummaryWriter('tensorboard4')
# summarywriter.add_images('featuremap_figure1',a)
# summarywriter.add_image(os.path.join('image','1'),img1,global_step=1)
# summarywriter.add_image(os.path.join('image','2'),img1,global_step=)
# summarywriter.add_image(os.path.join('image1','1'),img1)
# summarywriter.close()