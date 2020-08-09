import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def mean_filter():
    img = np.array(Image.open('1.bmp'))
    width = img.shape[0]
    height = img.shape[1]
    new_image = np.copy(img)
    for i in range(width):
        for j in range(height):
            if i == 0 or j == 0 or i == width - 1 or j == height - 1:
                continue
            list_rgb = np.empty((9, 4), "int")
            list_rgb[0][0], list_rgb[0][1], list_rgb[0][2] = img[i + 0, j + 0, 0], img[i + 0, j + 0, 1], img[i + 0, j + 0, 2]
            list_rgb[1][0], list_rgb[1][1], list_rgb[1][2] = img[i + 1, j + 0, 0], img[i + 1, j + 0, 1], img[i + 1, j + 0, 2]
            list_rgb[2][0], list_rgb[2][1], list_rgb[2][2] = img[i + 0, j + 1, 0], img[i + 0, j + 1, 1], img[i + 0, j + 1, 2]
            list_rgb[3][0], list_rgb[3][1], list_rgb[3][2] = img[i + 1, j + 1, 0], img[i + 1, j + 1, 1], img[i + 1, j + 1, 2]
            list_rgb[4][0], list_rgb[4][1], list_rgb[4][2] = img[i - 0, j - 1, 0], img[i - 0, j - 1, 1], img[i - 0, j - 1, 2]
            list_rgb[5][0], list_rgb[5][1], list_rgb[5][2] = img[i - 1, j - 1, 0], img[i - 1, j - 1, 1], img[i - 1, j - 1, 2]
            list_rgb[6][0], list_rgb[6][1], list_rgb[6][2] = img[i - 1, j - 0, 0], img[i - 1, j - 0, 1], img[i - 1, j - 0, 2]
            list_rgb[7][0], list_rgb[7][1], list_rgb[7][2] = img[i - 1, j + 1, 0], img[i - 1, j + 1, 1], img[i - 1, j + 1, 2]
            list_rgb[8][0], list_rgb[8][1], list_rgb[8][2] = img[i + 1, j - 1, 0], img[i + 1, j - 1, 1], img[i + 1, j - 1, 2]

            sumR, sumG, sumB = 0, 0, 0
            for k in range(9):
                sumR += list_rgb[k][0]
                sumG += list_rgb[k][1]
                sumB += list_rgb[k][1]
            new_image[i, j][0] = sumR / 9
            new_image[i, j][1] = sumG / 9
            new_image[i, j][2] = sumB / 9

    fig = plt.figure(figsize=(20, 10))
    fig.add_subplot(121)
    plt.imshow(img)
    fig.add_subplot(122)
    plt.imshow(new_image)
    plt.show()


if __name__ == '__main__':
    mean_filter()
