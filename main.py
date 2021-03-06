# this source is very dirty.
# just use this for catch up how craete idx from armv8 TRM.
# original manual can  get from here. 
# https://static.docs.arm.com/ddi0487/db/DDI0487D_b_armv8_arm.pdf

import PyPDF2
from PyPDF2 import PdfFileReader
import sys

ARMv8a_man_path = './manuals/DDI0487E_a_armv8_arm.pdf' 
_head_str =  '@DDI0487E_a_armv8_arm.pdf[ARM Architecture Reference Manual - ARMv8, for ARMv8-A architecture profile, 05 July 2019 (ARM DDI 0487E.a (ID070919))]\n\n'


def get_info(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
        outlines = pdf.outlines
    return pdf

def _setup_page_id_to_num(pdf, pages=None, _result=None, _num_pages=None):
    if _result is None:
        _result = {}
    if pages is None:
        _num_pages = []
        pages = pdf.trailer["/Root"].getObject()["/Pages"].getObject()
    t = pages["/Type"]
    if t == "/Pages":
        for page in pages["/Kids"]:
            _result[page.idnum] = len(_num_pages)
            _setup_page_id_to_num(pdf, page.getObject(), _result, _num_pages)
    elif t == "/Page":
        _num_pages.append(1)
    return _result

def recursive_seek(outlines, lst, dep=0):
    _dep = dep
    for i in range(0, len(outlines)):
        ele = outlines[i]
        if isinstance(ele, list):
            recursive_seek(ele, lst, _dep+1)
        elif isinstance(ele, PyPDF2.generic.Destination):
            tp = (_dep, str(ele.title), ele.page.idnum)
            lst.append(tp)
        else:
            print(ele)
            
def rm_title_idx(title):
    a = title.find(' ')
    if(a <= 0):
        print('error')
    ret = title[a+1:len(title)]
    return ret

def findout_point(pg_id_map, lst, catch=['alphabetical', 'instructions'], exclusive=['A32', 'AArch32', 'Statistical Profiling Extension']):
    ret = list()
    flag = False
    sub_flag = -1
    for i in range(0, len(lst)):
        ele = lst[i]
        dep = ele[0]
        title = ele[1]
        title_low = title.lower()
        if (flag == False):
            catch_check = int(0)
            print(len(catch))
            for ji in range(0, len(catch)):
                dd = catch[ji].lower()
                if title_low.find(dd) >=0:
                    catch_check = catch_check + 1
            if (catch_check == len(catch)):
                exclusive_check = int(0)
                for je in range(0, len(exclusive)):
                    if title_low.find(exclusive[je].lower()) >= 0:
                        exclusive_check = exclusive_check + 1
                if exclusive_check is 0:
                    print(title)
                    sub_flag = dep+1
                    flag = True
        else:
            if (sub_flag == dep) and (flag == True):
                title = rm_title_idx(title)
                tp = (title, pg_id_map[ele[2]]+1)
                #print(tp)
                ret.append(tp)
            elif (sub_flag > dep):
                sub_flag = -1
                flag = False                 
    return ret

def rm_title_idx(title):
    a = title.find(' ')
    if(a <= 0):
        print('error')
    ret = title[a+1:len(title)]
    return ret

def retake(lst):
    ret = list()
    prev_title = ''
    for i in range(0, len(lst)):
        ele = lst[i]
        title = ele[0]
        pgnum = ele[1]
        # remove (something)
        a = title.find(' (')
        if a > 0:
            title = title[0:a]
        # end of remove (something) 
        # check duplicate before
        if prev_title == title:
            continue
        # end of check duplication as before
        prev_title = title
        # append thing to new list
        box = title.split(', ')
        for j in range(0, len(box)):
            tp = (box[j], pgnum)
            ret.append(tp)
        # end of appending.
    return ret

def retake_a64si(lst):
    ret = list()
    prev_title = ''
    for i in range(0, len(lst)):
        ele = lst[i]
        title = ele[0]
        pgnum = ele[1]
        # remove (something)
        a = title.find(', ')
        if a > 0:
            title = title[0:a]
        # end of remove (something) 
        # find space and swap to _
        a = title.find(' ')
        if a > 0:
            title = title.replace(" ", "_")
        # end of swap to _
        # check duplicate before
        if prev_title == title:
            continue
        # end of check duplication as before
        tp = (title, pgnum)
        ret.append(tp)
        # end of appending.
    return ret
        
def write_to_idx(lst, head_str):
    f = open("AARCH64.idx", 'w')
    f.write(head_str)
    for i in range (0, len(lst) ):
        ele = lst[i]
        data = "%s,\t\t%d\n" % (ele[0].lower() , ele[1])
        f.write(data)
    f.close()

def main():
    path = ARMv8a_man_path
    pdf = (get_info(path))
    data = pdf.outlines
    sys.setrecursionlimit(10000)
    elelist = list()
    extra_temp = list()
    recursive_seek(data, elelist)
    pg_id_num_map = _setup_page_id_to_num(pdf)
    # for general things 
    ret = findout_point(pg_id_num_map, elelist)
    print('a64_si_stuff')
    # a64 si things
    a64si_ca = findout_point(pg_id_num_map, elelist, catch=['A64 System instructions for cache maintenance'])
    a64si_at = findout_point(pg_id_num_map, elelist, catch=['A64 System instructions for address translation'])
    a64si_tm = findout_point(pg_id_num_map, elelist, catch=['A64 System instructions for TLB maintenance'])
    a64si = retake_a64si(a64si_ca + a64si_at + a64si_tm)
    # end for a64 si things
    bb = retake(ret + a64si)
    write_to_idx(bb, _head_str)
    print('done')

if __name__ == "__main__":
    main()