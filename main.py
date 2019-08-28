import pandas as pd

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text


# def ocr_output(filename):
#
#     '''
#     This function will help out the text to an output file
#     '''
#
#     text = pytesseract.image_to_string(Image.open(filename))
#
#     with open("output.txt", "w") as f:
#         print(ocr_core('my data cropped.png', file=f))


print(ocr_core('example_pic_1.PNG'))
print(ocr_core('my data cropped.png'))

output = ocr_core('my data cropped.png')
file = open("output.txt", "w")
file.write(output)
file.close()

lineList = [line.strip('\n') for line in open('output.txt')]
print(lineList)

lineList = [x for x in lineList if x != '']

print(lineList)

res = [lineList[x:x+2] for x in range(0, len(lineList),2)]

print(res)

columns = ['Date', 'Weight']


df = pd.DataFrame(res, columns=columns)
print(df.head(10))
