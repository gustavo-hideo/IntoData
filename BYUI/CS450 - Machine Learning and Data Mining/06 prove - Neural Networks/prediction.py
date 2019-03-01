"""
GUSTAVO HIDEO HIGA CORREA
CS 450
06 PROVE: NEURAL NETWORKS PART 1
PREDICTION
"""

import cv2

# LOADING NN ALGORITHM IF (AND ONLY IF) IT'S NOT LOADED YET
"""
if 'ran' in locals(): 
    pass
else:
    exec(open('C:/DataScience/IntoData/BYUI/CS450 - Machine Learning and Data Mining/06 prove - Neural Networks/nn.py').read())
"""


img = cv2.imread('C:/DataScience/IntoData/BYUI/CS450 - Machine Learning and Data Mining/06 prove - Neural Networks/handwritten_number.png', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (28,28))
img = img[np.newaxis,:,:,np.newaxis]
img_data = np.array(img/255)
print(np.argmax(model.predict(img_data)[0]))

