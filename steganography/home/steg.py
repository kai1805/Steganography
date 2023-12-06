import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib.colors import NoNorm
import math

TERMINATE_CHARACTER = '|'
PATH = "./media/"

"""
read_image:
  color: True => reading as color image (default) in RGB format
  color: False => reading as gray
"""
def read_image(filename, color=True):
    # print(filename)
    image = cv2.imread(filename, 1 if color else 0)
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

"""
if image_data is in color format then RGB must be used
"""
def write_image(filename, image_data):
    image_data = cv2.cvtColor(image_data, cv2.COLOR_RGB2BGR)
    cv2.imwrite(filename, image_data)

def test(img_name):
    image1 = read_image(img_name, True)
    write_image('image2.png', image1)
    image2 = read_image('image2.png', True)
    for i in range(20):
        for j in range(3):
            print(image1[i][j], ' -- ', image2[i][j])


def show_image(image, title="sample", figsize=(8,6), tickoff=False):
    plt.figure(figsize=figsize)
    if image.ndim == 2:
        plt.imshow(image, cmap="gray", norm=NoNorm())
    else:
        plt.imshow(image)
    plt.title(title)
    plt.show()

def convert_decimal_to_bin(num):
    if num <= 0: 
        return ''
    if num % 2 == 0:
        return convert_decimal_to_bin(num // 2) + '0'
    return convert_decimal_to_bin(num // 2) + '1'

def convert_bin_to_decimal(bin):
    res = 0
    for i in range(len(bin)):
        res += int(bin[len(bin) - i - 1]) * 2**i
    return chr(res)

def steganography(img_name, text):
    text += TERMINATE_CHARACTER
    
    image = read_image(PATH + img_name, True)
    #image = (row, col, dim)  
    print(image.shape)
    print(image.shape[0] * image.shape[1])      
    # print(image[0])

    original_width = image.shape[0]
    original_height = image.shape[1]
    image = image.reshape((image.shape[0] * image.shape[1],3))
    
    #convert a text to a binary ascii array
    ascii_num_array = [ord(x) for x in text]
    bin_num_array = [convert_decimal_to_bin(x) for x in ascii_num_array]
    print(bin_num_array)

    for j in range(len(bin_num_array)):
        num_leading_0s = 8 - len(bin_num_array[j])
        # Leading 0s -> even
        for k in range(num_leading_0s):
            if image[j * 3 + k // 3][k % 3] % 2 != 0: image[j * 3 + k // 3][k % 3] -= 1
        for k in range(len(bin_num_array[j])):
            idx = j * 3 + (k + num_leading_0s) // 3
            idx1 = (k + num_leading_0s) % 3
            if (image[idx][idx1] % 2 == 0 and bin_num_array[j][k] == '1') or \
                (image[idx][idx1] % 2 != 0 and bin_num_array[j][k] == '0'):
                image[idx][idx1] -= 1
    

    image = image.reshape(original_width, original_height, 3)

    file_name = img_name
    file_name = file_name.split(".")
    file_name, file_extension = file_name[0], "png"
    file_name = file_name + "_encoded." + file_extension
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imwrite(PATH + file_name, image)

    return file_name

def steganography_decode(img_name):
    image = read_image(PATH + img_name)

    original_width = image.shape[0]
    original_height = image.shape[1]
    image = image.reshape((original_width * original_height), 3)

    plain_text = ""
    bin_char = ""
    for i in range(image.shape[0]):
        done = False
        for j in range(3):
            if (image[i, j] % 2 == 0):
                bin_char += '0'
            else:
                bin_char += '1'

            if len(bin_char) == 8:
                char = convert_bin_to_decimal(bin_char)
                # print(char, "-", bin_char)
                bin_char = ""
                if char != TERMINATE_CHARACTER:
                    plain_text += char
                else:
                    done = True
                    break
                break
        if done:
            break

    return plain_text

def display(image):
    image = image.astype("uint8")

    plt.imshow(image)
    plt.title("After Encoded")
    plt.show()

# test = 'abc def'

#chr(x): number to ascii character
#ord(x): character to number
# print(ascii_num_array)

# encoded_image = steganography('test.jpg', 'abcxyz')
# print("Text after decode:", steganography_decode(encoded_image))
# test('test.jpg')

