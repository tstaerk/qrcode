import streamlit as st
import qrcode

# Title of the app
st.title('QR Code Generator')

# User input for the content of the QR code
data = st.text_input('Enter the data for the QR code:')

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

    # Display the QR code image
    st.image(img, caption='Generated QR Code', use_column_width=True)
