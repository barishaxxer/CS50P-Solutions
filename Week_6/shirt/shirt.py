import sys
from PIL import Image, ImageOps


def main():
    if (
        len(sys.argv) != 3
        or not sys.argv[1].lower().endswith((".jpg", ".jpeg", ".png"))
        or not sys.argv[2].lower().endswith((".jpg", ".jpeg", ".png"))
    ):
        sys.exit("Invalid arguments.")
    elif sys.argv[1].split(".")[1] != sys.argv[2].split(".")[1]:
        sys.exit("Invalid arguments.")

    try:
        with Image.open(sys.argv[1]) as img, Image.open("shirt.png") as shirt:
            resized = ImageOps.fit(img, shirt.size)
            resized.paste(shirt, shirt)
            resized.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Invalid files.")


main()
