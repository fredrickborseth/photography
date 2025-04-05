from PIL import Image, ImageEnhance, ImageOps

# open picture to work with
image = Image.open("my_pic.jpg")

# convert the image to black and white
bw = ImageOps.grayscale(image)
bw.save("bw_image.jpg")

# enhance contrast
enhancer = ImageEnhance.Contrast(image)
contrast = enhancer.enhance(1.8)
contrast.save("image_contrast.jpg")

# make it sepia ( with greyscale and color tone)
def create_sepia(image):
    bw = ImageOps.grayscale(image)
    sepia = ImageOps.colorize(bw, "#704214", "#fff0c9")
    return sepia

sepia = create_sepia(image)
sepia.save("image_sepia.jpg")

print("Done! Images are saved.")

