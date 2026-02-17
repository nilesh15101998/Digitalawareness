import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

# 1. UI Setup
st.title("?? Certificate Generator")
st.write("Enter your details to generate your custom certificate.")

name = st.text_input("Full Name", placeholder="e.g. John Doe")
age = st.text_input("Age", placeholder="e.g. 25")

# 2. Certificate Logic
if st.button("Preview Certificate"):
    if name and age:
        try:
            # Open the template (Ensure 'template.png' is in your GitHub repo)
            img = Image.open("template.png").convert("RGB")
            draw = ImageDraw.Draw(img)
            
            # Load a font (Streamlit Cloud usually has standard fonts)
            # You can also upload a .ttf file to your repo to be safe
            try:
                font = ImageFont.truetype("Arial.ttf", 80)
            except:
                font = ImageFont.load_default()

            # Coordinates: You will need to adjust (x, y) based on your image
            # 1000, 700 is often near the center of a standard template
            draw.text((1000, 700), name, fill="black", font=font, anchor="mm")
            draw.text((1000, 850), f"Age: {age}", fill="black", font=font, anchor="mm")

            # Show preview
            st.image(img, caption="Your Generated Certificate", use_container_width=True)

            # Prepare for download
            buf = io.BytesIO()
            img.save(buf, format="PNG")
            byte_im = buf.getvalue()

            st.download_button(
                label="Download Certificate",
                data=byte_im,
                file_name=f"Certificate_{name}.png",
                mime="image/png"
            )
        except FileNotFoundError:
            st.error("Error: Please upload a 'template.png' file to the folder.")
    else:
        st.warning("Please enter both Name and Age.")