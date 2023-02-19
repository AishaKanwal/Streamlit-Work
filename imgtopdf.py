import os
from PIL import Image
from io import BytesIO
from PyPDF2 import PdfWriter, PdfReader
import streamlit as st

st.set_option('deprecation.showfileUploaderEncoding', False)

st.title('Image to PDF Converter | Aisha Kanwal')

uploaded_files = st.file_uploader('Choose images', accept_multiple_files=True, type=['png', 'jpg', 'jpeg'])
if uploaded_files:
    images = []
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file)
        image = image.convert('RGB') # Convert image to RGB mode
        images.append(image)

    if images:
        # Create a new PDF file and add the images as new pages
        pdf_bytes = BytesIO()
        pdf_writer = PdfWriter()
        for img in images:
            img_bytes = BytesIO()
            img.save(img_bytes, format='PDF')
            img_bytes.seek(0)
            pdf_reader = PdfReader(img_bytes)
            pdf_writer.add_page(pdf_reader.pages[0])

        # Create a download link for the PDF file
        pdf_bytes = BytesIO()
        pdf_writer.write(pdf_bytes)
        pdf_bytes.seek(0)
        file_names = [os.path.splitext(file.name)[0] for file in uploaded_files]
        if len(file_names) > 1:
            file_name = '-'.join(file_names) + '.pdf'
        else:
            file_name = file_names[0] + '.pdf'
        st.download_button('Download PDF', pdf_bytes, file_name=file_name, mime='application/pdf')