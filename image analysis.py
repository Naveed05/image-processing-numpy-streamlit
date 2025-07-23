import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image
import requests
from io import BytesIO

def load_imag_from_url(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))
    

test_cricket_url = "https://static.toiimg.com/thumb/msid-122429246,imgsize-146042,width-400,resizemode-4/122429246.jpg"


test = load_imag_from_url(test_cricket_url)


plt.figure(figsize=(6,4))
plt.imshow(test)
plt.title("Test Cricket Image")
plt.axis('off')
plt.show()
# Load the image from the URL