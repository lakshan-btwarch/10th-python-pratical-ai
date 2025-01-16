import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('octopus.png')

# Display the image with a title
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Octopus')
plt.axis('off')
plt.show()
