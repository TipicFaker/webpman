import cv2
import os

#vibecoded piece of junk

def convert(dir):

    if not os.path.exists(dir):
        raise FileNotFoundError(f"The file {dir} does not exist.")
    
    if not dir.lower().endswith(('.webp')):
        raise ValueError("Unsupported file format. Please provide a WebP image file.")

    img = cv2.imread(dir)
    if img is None:
        raise ValueError("Failed to read the image. Please check the file path and format.")
    
    # Convert the image to JPG format
    jpg_filename = os.path.splitext(dir)[0] + '.jpg'
    cv2.imwrite(jpg_filename, img)
    print(f"Image converted and saved as {jpg_filename}")


dir = input("Enter the path to the WebP image: ")
convert(dir)