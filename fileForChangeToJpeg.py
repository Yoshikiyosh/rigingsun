from PIL import Image

# Load the webp image
img = Image.open("gtr_shanghai.webp")
# Save it as jpg
img.save("gtr_shanghai.jpg", "JPEG")

 
