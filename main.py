from PyPDF2 import PdfFileReader

ARMv8a_man_path = './manuals/DDI0487D_b_armv8_arm.pdf' 
 
def get_info(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
 
    print(info)
 
    author = info.author
    creator = info.creator
    producer = info.producer
    subject = info.subject
    title = info.title
 
if __name__ == '__main__':
    path = ARMv8a_man_path
    get_info(path)