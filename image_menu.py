from PIL import Image, ImageEnhance, ImageOps
from image_effects import *

def show_menu():
    print("\n")
    print("Choose effect:")
    print("1 - black-white")
    print("2 - enhance contrast")
    print("3 - sepia")
    print("4 - close")

def main():
    picture_path = input("Type in picture path (f.ex mypic.jpg): ")
    
    try:
        image = Image.open(picture_path)
    except FileNotFoundError:
        print("Can't find picture, please check filename and location.")
        return
    
    while True:
        show_menu()
        choice = input("your choice: ")

        if choice == "1":
            result = black_and_white(image)
            result.save("black_and_white_out.jpg")
            print("File saved as black_and_white_out.jpg")

        elif choice == "2":
            result = enhance_contrast(image)
            result.save("contrast_out.jpg")
            print("File saved as contrast_out.jpg")

        elif choice == "3":
            result = create_sepia(image)
            result.save("sepia_out.jpg")
            print("File saved aas sepia_out.jpg")

        elif choice == "4":
            print("Closing.")
            break

        else:
            print("Not an option, try again.")

if __name__ == "__main__":
    main()


