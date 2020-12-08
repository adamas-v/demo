import os

#create new directories
p = './test'
if os.path.exists(p)==False:
    os.mkdir('./test')

#create new files
file = open('./test/a.txt','a')

#write into txt
file.write('fgeyuc sgfhdhskjlfuoihuiuidsrui g\n')
file.writelines(['dgyuuyruda\n','fgyuyarui\n','hfugias\n'])
file.close()

#read from txt
file = open('./test/a.txt','r')
lines = file.readlines()
file.seek(0)#游标复位
print(lines)


#load and save of numpy
import numpy as np
a = np.array([1,1,2,34,5,9 ])
np.save('./test/0',a)

A = np.load('./test/0.npy')
print(A)

#savez and load of numpy

az = np.array([1,2,3,4,6,7,8,9])
np.savez('./test/0',az = az)
az = np.load('./test/0.npz')

#savetxt and load of numpy
atxt = np.array([1,2,3,4,5,6,7])
np.savetxt('./test/0.txt',atxt)
data = open('./test/0.txt','a')
print(data.tell())
data.writelines(['fgyuahrui\n','fgyeqyuhq\n'])
print(data.tell())
data.close()

#save and load of torch
import torch
a = torch.tensor((3,4))
torch.save(a,'./test/atorch.pth')
a = torch.load('./test/atorch.pth')
print(a)

a = open('./test/0.txt','r')
a.readlines()