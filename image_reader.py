import pickle
from PIL import Image
import glob, os

from math import log


def generate_dataset(features, dependent_variable, image_dir, hexagon_count):
    # type: (list, list, Any, int) -> None
    print("Generating training data for {0}".format(image_dir))
    i = 0
    for image in os.listdir(image_dir):
        features_image = []
        dependent_variable.append(hexagon_count)
        img = Image.open(image_dir + '/' + image)
        pix = img.load()
        width, height = img.size
        for x in range(0, width - 1):
            features_image.append([])
            for y in range(0, height - 1):
                r, g, b = pix[x, y]
                features_image[x].append(log(r + 1) + log(g + 1) + log(b + 1))
                # features_image[x].append(pix[x, y])
        features.append(features_image)
        i += 1
        print '\r>> Completed ' + str(i) + ' images.',
    return None


# TODO don't hardcode
starting_dir = 'E:/dev/git/deep-learning/images'

zero_hexagon_images = starting_dir + '/0'
one_hexagon_images = starting_dir + '/1'
two_hexagon_images = starting_dir + '/2'
three_hexagon_images = starting_dir + '/3'

training = []
image_classification = []

generate_dataset(training, image_classification, zero_hexagon_images, 0)
generate_dataset(training, image_classification, one_hexagon_images, 1)
generate_dataset(training, image_classification, two_hexagon_images, 2)
generate_dataset(training, image_classification, three_hexagon_images, 3)

with open("./training/training.txt", 'w') as handle:
    pickle.dump(training, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open("./training/dependent.txt", 'w') as handle:
    pickle.dump(image_classification, handle, protocol=pickle.HIGHEST_PROTOCOL)
