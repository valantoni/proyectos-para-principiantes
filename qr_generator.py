import qrcode
import streamlit as st

filename = "qr_codes/qr_code.png"

def generate_qr_code(url, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

#create a streamlit app 
st.set_page_config(page_title="QR Code Generator", page_icon="🌐", layout="centered")
st.image("images/supports.JPG", use_column_width=True)
st.title("QR Code Generator")
url = st.text_input("Enter the URL")

if st.button("Generate QR Code"):
    generate_qr_code(url, filename)
    st.image(filename, use_column_width=True)
    with open(filename, "rb") as f:
                    image_data = f.read()  
    download = st.download_button(label="Download QR", data=image_data, file_name="qr_generated.png")



