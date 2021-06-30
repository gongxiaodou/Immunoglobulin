# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 18:27:29 2021

@author: Administrator
"""

#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
totalSize = 0
fileNum = 0
dirNum = 0
def visitDir(path):
    global totalSize
    global fileNum
    global dirNum
    for lists in os.listdir(path):
        sub_path = os.path.join(path, lists)
        if os.path.isfile(sub_path):
            fileNum = fileNum+1                      # 统计文件数量
            totalSize = totalSize+os.path.getsize(sub_path)  # 文件总大小
        elif os.path.isdir(sub_path):
            dirNum = dirNum+1                       
            visitDir(sub_path)                          
visitDir("E:/data/pssm/fasta/")
print(fileNum)
for i in range(1,fileNum+1):
    os.system("D:/blast-2.11.0+/bin/psiblast -query E:/data/pssm/fasta/"+ str(i)+"_ip.txt"+" -db D:/blast-2.11.0+/db/swissprot -num_iterations 3"+" -out_ascii_pssm "+str(i)+".pssm")

    
