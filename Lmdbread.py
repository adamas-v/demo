# -*- coding: utf-8 -*- 
import lmdb 
import pdb
import PIL.Image as Image
import urllib3
import os
#PIL图像处理标准库
from io import BytesIO 
 
env_db = lmdb.Environment('H:/USCISI-CMFD') ##***修改为你的数据集文件夹的地址
 
txn = env_db.begin() 

 
for key, value in txn.cursor():          #遍历
  key = str(key,encoding='utf-8')         #bytes转化成字符
  # pdb.set_trace()
  value_eval = eval(value)               #bytes转化成字典  
  print(value_eval.keys())               #看看字典有什么对象
  data = value_eval['image_jpeg_buffer']  #这里我取出了图像的数据
  data = bytes(data)                      #将图像单独转回到bytes 
  bytes_stream = BytesIO(bytes(data))     #将bytes结果转化为字节流  
  roiimg = Image.open(bytes_stream)       #字节流读取到图片
  roiimg.save(f"{key}.jpeg")              #保存图片


 
env_db.close() 