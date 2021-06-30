# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 09:13:33 2021

@author: fcl
"""

import numpy as np

def fun_calVal_Pij(arrPssm, i_col, j_col, supNumOfSum, mean_i,mean_j, lg):
    #
    val_curTask = 0
    #
    for j in range(supNumOfSum):
        #
#        pass
        val_curTask += ((arrPssm[j][i_col]-mean_i)*(arrPssm[j+lg+1][j_col]-mean_j))/supNumOfSum
#        val_curTask += ((arrPssm[j][i_col]-mean_i)(arrPssm[j+lg][j_col]-mean_j))/supNumOfSum
    
    #
#    print(val_curTask)
    return val_curTask

def fun_red400Mat_380(pssm):
    #
    ls_outVec380 = []
    # 
    for i in range(20):
        curLineNum = i
        curLineList = pssm[i]
        #
        ls_outVec19 = [curLineList[i] for i in range(20) if i!=curLineNum]
        #
        ls_outVec380.extend(ls_outVec19)
    #
    return ls_outVec380
        

def calcOneValue(pssmMat, Lag, seqLen):
    #
    pssm400 = np.zeros([20,20])
    #

    arr_pssm = np.array(pssmMat)
    #
    ls_fnlRslt_AcPssm = []
    #
    ls_meanVal_forCols = arr_pssm.mean(axis=0)
    
    #
    for lg in range(Lag):
        #
        i_supmumOfSum = seqLen - lg - 1
        #
        for i in range(20):
            for j in range(20):
                if i==j:
                    pssm400[i,j] = 0
                else:
                    #
                    mean_i = ls_meanVal_forCols[i]
                    mean_j = ls_meanVal_forCols[j]
                    val_ij = fun_calVal_Pij(arr_pssm, i, j, i_supmumOfSum, mean_i,mean_j, lg)
                    #
                    pssm400[i,j] = val_ij

        ls_vec380_curLg = fun_red400Mat_380(pssm400)
        ls_fnlRslt_AcPssm.extend(ls_vec380_curLg)
        
    #
    return ls_fnlRslt_AcPssm
                