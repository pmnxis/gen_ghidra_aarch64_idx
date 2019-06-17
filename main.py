import PyPDF2
from PyPDF2 import PdfFileReader
import sys

ARMv8a_man_path = './manuals/DDI0487D_b_armv8_arm.pdf' 
 

def get_info(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
        outlines = pdf.outlines
    return outlines

def recursive_seek(outlines, lst, dep=0):
    _dep = dep
    for i in range(0, len(outlines)):
        ele = outlines[i]
        if isinstance(ele, list):
            recursive_seek(ele, lst, _dep+1)
        elif isinstance(ele, PyPDF2.generic.Destination):
            lst.append((_dep, str(ele.title)))
        else:
            print(type(ele))

def findout_point(lst, catch='Alphabetical'):
    ret = list()
    flag = False
    sub_flag = -1
    for i in range(0, len(lst)):
        ele = lst[i]
        dep = ele[0]
        title = ele[1]
        if (flag == False):
            if title.find(catch) >= 0:
                #print('Find', end='')
                print(title)
                sub_flag = dep+1
                flag = True
        else:
            if (sub_flag == dep) and (flag == True):
                #print('sub', end='')
                print(ele[1])
                ret.append(ele)
            elif (sub_flag > dep):
                sub_flag = -1
                flag = False
    return ret

elelist = list()
sys.setrecursionlimit(550000)  
path = ARMv8a_man_path
data = (get_info(path))
recursive_seek(data, elelist)
ret = findout_point(elelist)
print(len(ret))
#print(ret)
    #print(type(ele))