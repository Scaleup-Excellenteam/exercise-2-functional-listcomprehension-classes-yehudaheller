from PIL import Image
from os import path


def decrypt_Image_Message(filepath):
    """
    Decrypts a message hidden in an image.

    @param filePath: The path to the image file.
    @type filePath: str

    @return: The decrypted message.
    @rtype: str
    """
    # Load image
    image = Image.open(filepath).convert("RGB")

    # Get dimensions of image
    width, height = image.size

    result_string = ""
    # Iterate over each pixel
    for x in range(width):
        for y in range(height):
            # Get RGB values of pixel
            r, g, b = image.getpixel((x, y))

            # Check if pixel is black
            if r == 0 and g == 0 and b == 0:
                # for debug: print(f"Found black pixel at ({x}, {y})")
                result_string += chr(y)  # convert the num of line that there black pixel to char
    return result_string


def get_encoded_file_path():
    """
    Prompts the user for a file path and returns it if it exists.

    @return: The path to the file.
    @rtype: str
    """
    while True:
        file_path = input("Enter file path: ")
        if path.exists(file_path):
            return file_path
        else:
            print("File path is incorrect. Please try again.")


filepath = get_encoded_file_path()
res_str = decrypt_Image_Message(filepath)
print(res_str)
