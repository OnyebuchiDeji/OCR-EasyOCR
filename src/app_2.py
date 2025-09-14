"""
    Demonstrates how to check if a certain piece of text is present
"""

import easyocr

image_path = "./res/"

reader = easyocr.Reader(['en'])

def is_text_present(imageName):
    result = reader.readtext(image_path + imageName)

    return len(result) > 0


print(is_text_present("shakespeare_2.jpg"))
print(is_text_present("no_text.jpg"))