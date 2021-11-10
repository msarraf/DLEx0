#import os.path
import json
#import scipy.misc
import numpy as np
#import skimage
from skimage.transform import resize
import matplotlib.pyplot as plt
#from PIL import Image


class ImageGenerator:
    def __init__(self, file_path: str, label_path: str, batch_size: int, image_size: list[int], rotation=False,
                 mirroring=False, shuffle=False):
        self.file_path = file_path
        self.lable_path = label_path
        self.batch_size = batch_size
        self.image_size = image_size
        self.rotatation = rotation
        self.mirroring = mirroring
        self.shuffle = shuffle
        self.datanumber = 0
        self.current_epoch_number = 0
        self.one_epoch_finished = 0
        self.class_dict = {0: 'airplane', 1: 'automobile', 2: 'bird', 3: 'cat', 4: 'deer', 5: 'dog', 6: 'frog',
                           7: 'horse', 8: 'ship', 9: 'truck'}
        self.random_numbers_full = np.random.randint(0, 100, 100)
    def next(self):

        if self.shuffle:
            if self.batch_size + self.datanumber >= 100:
                random_numbers = self.random_numbers_full[self.datanumber:100]
                random_numbers_rest = self.random_numbers_full[0:self.batch_size + self.datanumber-100]
                random_numbers = np.append(random_numbers, random_numbers_rest)
                self.datanumber = self.datanumber + self.batch_size - 100
                self.one_epoch_finished = 1
                self.random_numbers_full = np.random.randint(0, 100, 100)
            else:
                random_numbers = self.random_numbers_full[self.datanumber: self.batch_size + self.datanumber]
                self.datanumber = self.datanumber + self.batch_size
                if self.one_epoch_finished:
                    self.current_epoch_number += 1
                    self.one_epoch_finished = 0
        else:
            random_numbers = np.arange(self.datanumber, self.batch_size + self.datanumber)
            self.datanumber = self.datanumber + self.batch_size
            if self.one_epoch_finished:
                self.current_epoch_number += 1
                self.one_epoch_finished = 0
            if self.datanumber >= 100:
                random_numbers = np.arange(self.datanumber - self.batch_size, 100)
                random_numbers_rest = np.arange(0, self.datanumber - 100)
                random_numbers = np.append(random_numbers, random_numbers_rest)
                self.datanumber = self.datanumber - 100
                self.one_epoch_finished = 1
        lables_json = open(self.lable_path, )
        lable_datas = json.load(lables_json)
        lables_json.close()
        images = np.zeros((self.batch_size, self.image_size[0], self.image_size[1], 3))
        lables = np.zeros((self.batch_size), dtype=np.int64)
        index = 0
        for i in random_numbers:
            image = np.load(self.file_path + str(i) + '.npy')
            resized_image = resize(image, self.image_size)
            if self.mirroring:
                resized_image = np.flip(resized_image, np.random.randint(0, 2, 1))
            if self.rotatation:
                resized_image = np.rot90(resized_image, np.random.randint(1, 4, 1))
            images[index, :, :, :] = resized_image
            lables[index] = lable_datas[str(i)]
            index = index + 1
        return (images, lables)

    def augment(self, img):
        # this function takes a single image as an input and performs a random transformation
        # (mirroring and/or rotation) on it and outputs the transformed image
        # TODO: implement augmentation function
        return img


    def current_epoch(self):
        # return the current epoch number
        return self.current_epoch_number

    def class_name(self, x):

        return self.class_dict[x]

    def show(self, images):

        fig = plt.figure()
        counter = 1
        #size = np.shape(images[0])[0]
        for i in images[0]:
            a = fig.add_subplot(2, 3, counter, )
            a.set_xlabel(self.class_name(images[1][counter - 1]))
            plt.imshow(i)
            counter = counter + 1
        plt.show()
