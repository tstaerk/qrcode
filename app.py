import streamlit as st
import qrcode
from io import BytesIO

# Title of the app
st.title('QReative, you creative QR Code Generator')

# User input for the content of the QR code
data = st.text_input('Enter the data for the QR code:','https://www.staerk.de/thorsten')

# Check if the user entered some data
if data:
    # Create a QR code from the input data
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image of the QR code
    img = qr.make_image(fill='black', back_color='white')
    # Convert the image to a byte format
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    # Display the QR code image
    st.image(img_byte_arr, caption='Generated QR Code', use_container_width=True)
