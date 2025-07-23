import streamlit as st
import numpy as np
from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(page_title="Advanced Image Analyzer", layout="wide")

st.title("🖼️ Advanced Image Analysis App")
st.markdown("Upload or use default image for applying filters, exploring RGB channels, grayscale effects, and more!")

# Load image
@st.cache_data
def load_image():
    path = "C:/Users/mirza/Desktop/naveed photos/bumrah.jpeg"
    return Image.open(path).convert("RGB")

# Image
image = load_image()
st.image(image, caption="Original Image", use_container_width=True)

# Sidebar controls
st.sidebar.header("Image Transformations")

rotate = st.sidebar.slider("Rotate Image", 0, 360, 0)
flip = st.sidebar.radio("Flip Image", ["None", "Horizontal", "Vertical"])
brightness = st.sidebar.slider("Brightness", 0.5, 2.0, 1.0)
contrast = st.sidebar.slider("Contrast", 0.5, 2.0, 1.0)

# Apply transformations
processed_image = image.rotate(rotate)
if flip == "Horizontal":
    processed_image = processed_image.transpose(Image.FLIP_LEFT_RIGHT)
elif flip == "Vertical":
    processed_image = processed_image.transpose(Image.FLIP_TOP_BOTTOM)

enhancer_b = ImageEnhance.Brightness(processed_image)
processed_image = enhancer_b.enhance(brightness)

enhancer_c = ImageEnhance.Contrast(processed_image)
processed_image = enhancer_c.enhance(contrast)

st.subheader("🔧 Processed Image Preview")
st.image(processed_image, use_container_width=True)

# RGB Channels
st.subheader("🔬 RGB Channel Separation")
np_img = np.array(processed_image)
R, G, B = np_img[:, :, 0], np_img[:, :, 1], np_img[:, :, 2]

red_img = np.zeros_like(np_img)
green_img = np.zeros_like(np_img)
blue_img = np.zeros_like(np_img)

red_img[:, :, 0] = R
green_img[:, :, 1] = G
blue_img[:, :, 2] = B

cols = st.columns(3)
cols[0].image(red_img, caption="Red Channel", use_container_width=True)
cols[1].image(green_img, caption="Green Channel", use_container_width=True)
cols[2].image(blue_img, caption="Blue Channel", use_container_width=True)

# Grayscale with colormap
st.subheader("🎨 Grayscale + Colormap Visualization")
gray_img = processed_image.convert("L")
gray_np = np.array(gray_img)

colormap = st.selectbox("Choose a colormap", [
    "viridis", "plasma", "inferno", "magma", "cividis", "hot", "cool", "gray"
])

fig, ax = plt.subplots(figsize=(5, 5))
ax.imshow(gray_np, cmap=colormap)
ax.axis("off")
st.pyplot(fig)

# Zoom (crop)
st.subheader("🔍 Zoom into Image")
zoom_percent = st.slider("Zoom Level (%)", 10, 100, 100)

def crop_zoom(img, percent):
    width, height = img.size
    crop_width = int(width * percent / 100)
    crop_height = int(height * percent / 100)
    left = (width - crop_width) // 2
    top = (height - crop_height) // 2
    right = left + crop_width
    bottom = top + crop_height
    return img.crop((left, top, right, bottom)).resize((width, height))

zoomed = crop_zoom(processed_image, zoom_percent)
st.image(zoomed, caption=f"Zoomed Image ({zoom_percent}%)", use_container_width=True)

st.markdown("---")
st.markdown(" by Mirza Naveed Baig | Using Streamlit + PIL + NumPy + Matplotlib**")
