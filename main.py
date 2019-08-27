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
