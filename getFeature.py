#提取手写数字位置


import numpy as np

def GetFeature(image):
    
    img_array = np.array(image.convert('1'))
    img_array = ~img_array

    for i in range(32):
        for j in range(32):
            if img_array[i, j] == True:
                 print('1', end='')
            else:
                 print('0', end='')
        print()
            #print(img_array[i,j])
    row_col = np.nonzero(img_array)

    print(row_col)



if __name__ == "__main__":
    image = []
    GetFeature(image)