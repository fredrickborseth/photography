from PIL import Image, ImageEnhance, ImageOps

def black_and_white(image):
    return ImageOps.grayscale(image)

def enhance_contrast(image):
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(1.8)

def create_sepia(image):
    bw = ImageOps.grayscale(image)
    return ImageOps.colorize(bw, "#704214", "#fff0c9")

