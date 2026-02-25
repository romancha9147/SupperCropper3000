from PIL import Image
import numpy as np


def crop_to_content(image_path, output_path, threshold=30):
    """
    Crop image from top and bottom until non-black content is found.

    Args:
        image_path (str): Path to input image
        output_path (str): Path to save cropped image
        threshold (int): Value to consider as "non-black" (0-255)
    """
    # Open image and convert to grayscale for simplicity
    img = Image.open(image_path).convert('L')
    img_array = np.array(img)

    # Get image dimensions
    height, width = img_array.shape

    # Find top crop position
    top = 0
    for y in range(100, height):
        # Check if any pixel in this row is above threshold (non-black)
        if np.any(img_array[y] > threshold):
            top = y
            break

    # Find bottom crop position
    bottom = 1059
    for y in range(1059, top, -1):
        if np.any(img_array[y] > threshold):
            bottom = y
            break

    # Check if we found valid crop positions
    if bottom <= top:
        print("No non-black content found or invalid crop positions")
        return

    # Crop the image
    # Convert back to RGB if needed, then crop
    original_img = Image.open(image_path)
    cropped_img = original_img.crop((0, top, width, bottom + 1))

    # Save the result
    cropped_img.save(output_path)
    print(f"Cropped image saved to {output_path}")
    print(f"Cropped from top: {top}px, from bottom: {height - bottom - 1}px")


# Usage
#crop_to_content(input('enter the input jpg'), input('enter the output.jpg'))
#crop_to_content('C:/Users/Roman/Desktop/инфа/SuperCropper3000/images to crop/photo_1_2026-01-18_22-26-46.jpg', 'C:/Users/Roman/Desktop/инфа/SuperCropper3000/cropped images/cropphoto_1_2026-01-18_22-26-46.jpg')
#crop_to_content('C:/Users/Roman/Desktop/инфа/SuperCropper3000/images to crop/photo_2_2026-01-18_22-26-46.jpg', 'C:/Users/Roman/Desktop/инфа/SuperCropper3000/cropped images/cropphoto_2_2026-01-18_22-26-46.jpg')
#crop_to_content('C:/Users/Roman/Desktop/инфа/SuperCropper3000/images to crop/photo_3_2026-01-18_22-26-46.jpg', 'C:/Users/Roman/Desktop/инфа/SuperCropper3000/cropped images/cropphoto_3_2026-01-18_22-26-46.jpg')
for i in range(17, 22):
    crop_to_content(f"C:/Users/Roman/Desktop/инфа/SuperCropper3000/images to crop/photo_{i}_2026-01-23_00-53-14.jpg", f"C:/Users/Roman/Desktop/инфа/SuperCropper3000/cropped images/cropphoto_{i}_2026-01-23_00-53-14.jpg")