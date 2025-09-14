"""
    Demonstration of use of EasyOCR Cleaner
"""

import easyocr


reader = easyocr.Reader(['en'])

image_path = "./res/"

images = ["sign_board_image_1.jpg", "sign_board_image_3.jpg", "sign_board_image_5.jpg"]

def extract_and_save(name):
    result = reader.readtext(image_path + name)

    o_text = ""
    for (bbox, text, prob) in result:
        o_text += text + " "

    print(o_text)

    o_name = "extracted-" + name.split(".")[0] + "_" + name.split(".")[1] + ".txt"
    with open(o_name, "w") as wfs:
        wfs.write(o_text)
    
def main():
    for img in images:
        extract_and_save(img)

if __name__ == "__main__":
    main()