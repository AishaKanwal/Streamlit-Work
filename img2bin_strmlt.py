import streamlit as st
from PIL import Image
import numpy as np
import os

def main():
    st.title("Convert BMP Files into BIN Files")

    # Left column with information
    left_column = st.sidebar
    left_column.title("Why Conversion!")
    left_column.write("#### The bin files will be loaded on DMD to display the images.")
    left_column.write("###### O/P files will be saved in DMD_Aisha folder with the same name as of *.bmp file.")
    left_column.write("#### For Example:") 
    left_column.write("###### Input is: 'image.bmp', then output will be: 'image.bin'")

    # Right column with file uploader and image conversion
    right_column, _ = st.columns(2)
    right_column.write("**Upload BMP images**")
    uploaded_files = right_column.file_uploader("Other than *.bmp images, it will give you an error!", type=["bmp"], accept_multiple_files=True)

    if uploaded_files:
        for uploaded_file in uploaded_files:
            # Display uploaded image in the right column
            image = Image.open(uploaded_file)
            image_width = 200
            right_column.image(image, caption=f"Uploaded Image: {uploaded_file.name}", width=image_width)

            # Convert image to binary
            binary_data = convert_to_binary(image)

            # Get the directory path of the uploaded image file
            directory_path = os.path.dirname(uploaded_file.name)

            # Save binary data to a file in the same directory
            save_binary(binary_data, directory_path, uploaded_file.name)

def convert_to_binary(image):
    width, height = image.size
    # Extracting pixel data
    pixel_data = list(image.getdata())
    # Convert pixel values to 0s and 1s
    binary_data = [False if pixel_value == 0 else True for pixel_value in pixel_data]
    # Reshape pixel data into a 2D list (rows x cols)
    pixel_data_2d = [binary_data[i * width:(i + 1) * width] for i in range(height)]
    # Convert the 2D boolean array into a numpy array of uint8 (8-bit unsigned integers)
    byte_array = np.packbits(pixel_data_2d, axis=1)
    return byte_array

def save_binary(byte_array, directory_path, file_name):
    # Base name of the file without extension
    base_name = os.path.splitext(file_name)[0]
    # Output file name with .bin extension
    bin_file = os.path.join(directory_path, f"{base_name}.bin")
    # Save byte array to the binary file
    with open(bin_file, 'wb') as file:
        file.write(byte_array)
    st.success(f"File created as: {bin_file}")

if __name__ == "__main__":
    main()

    
# run command in anaconda prompt to run the code.
# first open the path (in this case, the path is: 
# (base) C:\Users\Aisha Kanwal\OneDrive - University of Strathclyde\DMD_Aisha)
# streamlit run img2bin_strmlt.py

### --------------------------------------------
### --------------------------------------------
### --------------------------------------------

