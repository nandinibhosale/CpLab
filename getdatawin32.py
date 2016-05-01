# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 08:59:13 2016

@author: Nandini Bhosale
"""

import win32com.client
import scipy

xl = win32com.client.gencache.EnsureDispatch("Excel.Application")
wb =xl.Workbooks('Linear.xlsx')
sheet=wb.Sheets('Data')

def getdata(sheet,Range):
    data=sheet.Range(Range).Value
    data=scipy.array(data)
    data=data.reshape((1,len(data)))[0]
    return data
    
x=getdata(sheet,"A2:A6")
y=getdata(sheet,"B2:B6")
yerr=getdata(sheet,"D2:D6")
print x