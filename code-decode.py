# Import necessary libraries
#import base64
#from PIL import Image
#import io

# Base64 encoded string
#encoded_image = b"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"

# Decode the base64 string
#decoded_image = base64.b64decode(encoded_image)

# Convert bytes to image
#image = Image.open(io.BytesIO(decoded_image))
#image.show()





##################################################################################################################

import base64
from PIL import Image
import io

# Function to encode an image to base64 string
def encode_image(image_path):
    # Open the image file
    with open(image_path, "rb") as image_file:
        # Read the image file and encode it to base64
        encoded_string = base64.b64encode(image_file.read())
        return encoded_string

# Example usage
image_path = "G:/vairous1x/EduScrape/img/logo.png"
encoded_image = encode_image(image_path)
print(encoded_image)
