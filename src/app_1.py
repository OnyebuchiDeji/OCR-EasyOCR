"""
    Demonstration of use of EasyOCR

    EasyOCR extracts the text as well as the bounding box of the text

    It does not work very well for images with skewed and rotated text
"""

import easyocr


reader = easyocr.Reader(['en'])

image_path = "./res/"
# name = "text_image.png"
name = "shakespeare_2.jpg"

#   for some reason, the below adds new text into the output of what it detects: `City elit, Cras leo eget eget`
result = reader.readtext(image_path + name)

# print(result)
o_text = ""
for (bbox, text, prob) in result:
    o_text += text + " "

print(o_text)

o_name = "extracted-" + name.split(".")[0] + "_" + name.split(".")[1] + ".txt"
with open(o_name, "w") as wfs:
    wfs.write(o_text)