from tensorflow_for_poets_2.scripts import label_image
import os
test_dir = "/home/snc19/Desktop/My-Marcel-Test-JPG/"
labels_dir = ['A']#,'B','C','Point','Five','V']

total_img=0
correct_img=0
for dir_num in range(len(labels_dir)):
    for imgfile in os.listdir(test_dir+labels_dir[dir_num]):
        total_img+=1
        klass = label_image.main_label(test_dir+labels_dir[dir_num]+"/"+imgfile)
        if (klass==labels_dir[dir_num].lower()):
            correct_img+=1
        print(1.0*correct_img/total_img)
