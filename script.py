from PIL import ImageGrab, Image
import sys
import os


def exit_no_action(msg: str, exit_code=1):
    print(msg)
    sys.exit(exit_code)


def check_if_exists(filename: str):
   if os.path.exists(filename):
        user_input = input(f"The file '{filename}' already exists. Do you want to overwrite it? (y/n): ").lower()
        if user_input != 'y':
            exit_no_action("Operation canceled. The file was not overwritten.", 0)


def save(image, filename: str):
    check_if_exists(filename)
    image.save(filename)


def main():
    clip = ImageGrab.grabclipboard()
    if not clip:
        exit_no_action("No image in clipboard!")

    if len(sys.argv) != 2 or not sys.argv[1]:
        exit_no_action("Incorrect number of arguments! Must supply exactly one filename.")
    filename = sys.argv[1] + ".png"

    save(clip, filename)


if __name__ == '__main__':
    main()
