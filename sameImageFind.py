from PIL import Image
import os


FOLDER = "novasImagens3/"
img_list = []
img_pixels_list = []


def find_repeated_image(pixel_list: list):
    for i in pixel_list:
        for j in pixel_list:
            if i[0] == j[0]:
                continue
            for x in range(i[1]):
                for y in range(i[2]):
                    pixel1 = i[3][x, y]
                    pixel2 = j[3][x, y]
                    if pixel1 != pixel2:
                        break
                    else:
                        print("\n\nAchei uma imagem repetida!\n")
                        print(f"Image {i[0]} == Image {j[0]}")
                        print("")
        

def create_pixel_list(image: str):
    image_name = image.replace(f"{FOLDER}", "")
    image = Image.open(image)
    width, height = image.size
    pixels = image.load()
    img_pixels_list.append([image_name, width, height, pixels])


def create_img_list():
    for img in os.listdir(FOLDER):
        img_list.append(f"{FOLDER}{img}")
    print("\nIMAGE LIST\n", img_list[:3], "\n\n")


def main():
    create_img_list()
    for i in img_list:
        create_pixel_list(i)
    print("\nDETAILS LIST\n", img_pixels_list[:3], "\n\n")
    find_repeated_image(img_pixels_list)

if __name__ == "__main__":
    main()
