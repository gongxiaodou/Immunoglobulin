# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 12:58:11 2021

@author: Administrator
"""
import os

def formateachline(eachline):
    col = eachline[0:2].strip() 
    begin = 2 
    for i in range(20): 
        begin = begin
        end = begin + 4
        col += ',' + eachline[begin:end].strip()
        begin = end
    col += ']'+','+'\n' 
    return col

def simplifypssm(pssmdir,newdir):
    listfile = os.listdir(pssmdir)
    for eachfile in listfile:
        with open(pssmdir + '/' + eachfile,'r') as inputpssm:
            with open(newdir + '/' + eachfile,'w') as outfile:
                count = 0
                for eachline in inputpssm:
                    each_line = eachline[7:]
                    count +=1
                    if count <= 3:
                        continue
                    if not len(each_line.strip()):
                        break
                    oneline = formateachline(each_line)
                    one_line ='['+ oneline[1:]
                    outfile.write(''.join(one_line))

pssmdir = 'C:/Users/Administrator/Desktop/pss/oldpssm'
newdir = 'C:/Users/Administrator/Desktop/pss/newpssm'
simplifypssm(pssmdir, newdir)

