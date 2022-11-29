from astroNN.datasets import galaxy10
import cv2

images, labels = galaxy10.load_data()
print(images.shape)



features = ['Disk, Face-on, No Spiral', 'Smooth, Completely round', 'Smooth, in-between round', 'Smooth, Cigar shaped', 'Disk, Edge-on, Rounded Bulge', 'Disk, Edge-on, Boxy Bulge',
            'Disk, Edge-on, No Bulge','Disk, Face-on, Tight Spiral', 'Disk, Face-on, Medium Spiral', 'Disk, Face-on, Loose Spiral']


for i in images:
    x=i.shape[0]
    name=features[labels[x]]
    cv2.imwrite(name+str(x)+'.png',images[i])
