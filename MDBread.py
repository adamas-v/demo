import os
import lmdb
import pdb

mdbpath = 'D:/CopyofUSCISI-CMFD-Full/USCISI-CMFD/'
env_vb = lmdb.Environment(mdbpath)

txn = env_vb.begin()
# print(txn.get(str(200))
for key,value in txn.cursor():
    value = str(value, encoding="utf-8")
    other,img = value.split('"image_jpeg_buffer"',1)
    img1 = img.split(",",-1)
    pdb.set_trace()
    # with open('byte.txt','w') as f :
    #     f.write(value)
    # break
env_vb.close()