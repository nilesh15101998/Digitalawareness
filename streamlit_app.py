import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from datetime import datetime
import uuid

st.set_page_config(page_title="Three Arrows Certificate Generator", layout="centered")

st.title("Three Arrows Family Certificate Generator")

# Upload Logo
logo_file = st.file_uploader("Upload Logo (PNG/JPG)", type=["png", "jpg", "jpeg"])

name = st.text_input("Enter Recipient Name")
website = st.text_input("Enter Website Name (example: www.threearrows.org)")

generate = st.button("Generate Certificate")

if generate and name and logo_file:

    # Create certificate canvas
    width, height = 1800, 1300
    cert = Image.new("RGB", (width, height), "#F8F5EF")
    draw = ImageDraw.Draw(cert)

    DEEP_BLUE = "#0B3D2E"

    # Load Logo
    logo = Image.open(logo_file).convert("RGBA")
    logo.thumbnail((200, 200))
    cert.paste(logo, (100, 80), logo)

    # Load Fonts (Make sure these files exist in repo)
    try:
        f_branding = ImageFont.truetype("PlayfairDisplay-Bold.ttf", 120)
        f_title = ImageFont.truetype("PlayfairDisplay-Bold.ttf", 90)
        f_name = ImageFont.truetype("PlayfairDisplay-Bold.ttf", 190)
        f_body = ImageFont.truetype("Montserrat-Regular.ttf", 55)
        f_small = ImageFont.truetype("Montserrat-Regular.ttf", 40)
    except:
        f_branding = f_title = f_name = ImageFont.load_default()
        f_body = f_small = ImageFont.load_default()

    # Website + Branding (Same Row)
    draw.text((width - 120, 150),
              website,
              font=f_small,
              fill=DEEP_BLUE,
              anchor="rm")

    # Title
    draw.text((width // 2, 350),
              "Certificate of Appreciation",
              font=f_title,
              fill=DEEP_BLUE,
              anchor="mm")

    # Sub text
    draw.text((width // 2, 500),
              "This certificate is proudly presented to",
              font=f_body,
              fill=DEEP_BLUE,
              anchor="mm")

    # BIG NAME
    draw.text((width // 2, 700),
              name.upper(),
              font=f_name,
              fill="#0A3D2E",
              anchor="mm")

    # Description
    draw.text((width // 2, 880),
              "In recognition of outstanding contribution and dedication.",
              font=f_body,
              fill=DEEP_BLUE,
              anchor="mm")

    # Signature Line
    draw.line((width - 600, 1050, width - 200, 1050),
              fill=DEEP_BLUE,
              width=5)

    draw.text((width - 400, 1010),
              "Signed by Three Arrows Family",
              font=f_small,
              fill=DEEP_BLUE,
              anchor="mm")

    # Certificate ID
    cert_id = str(uuid.uuid4())[:8].upper()
    date_today = datetime.today().strftime("%d %B %Y")

    draw.text((150, height - 120),
              f"Certificate ID: {cert_id}",
              font=f_small,
              fill=DEEP_BLUE)

    draw.text((width - 150, height - 120),
              f"Date: {date_today}",
              font=f_small,
              fill=DEEP_BLUE,
              anchor="ra")

    # Save as PNG
    buffer = BytesIO()
    cert.save(buffer, format="PNG")
    buffer.seek(0)

    st.success("Certificate Generated Successfully!")

    st.image(cert, use_column_width=True)

    st.download_button(
        label="Download Certificate (PNG)",
        data=buffer,
        file_name=f"Certificate_{cert_id}.png",
        mime="image/png"
    )

else:
    st.info("Upload logo, enter name and website, then click Generate.")
