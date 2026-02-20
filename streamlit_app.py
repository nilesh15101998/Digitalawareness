import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import datetime
import io

# Page Config
st.set_page_config(page_title="Three Arrows Family", page_icon="🌿")

# Light background style
st.markdown("""
    <style>
    .stApp {
        background-color: #f4f9f4;
    }
    h1 {
        color: #1b5e20;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.image("logo.jpeg", width=150)
st.title("Three Arrows Family")
st.subheader("Step Out of the Phone – Step Into Life 🌿")

st.markdown("---")

# User Inputs
name = st.text_input("Full Name")
age = st.number_input("Age", min_value=5, max_value=100)
hours = st.slider("How many hours daily on Social Media & Reels?", 0, 15, 3)

st.markdown("### Consent Declaration")

consent = st.checkbox("""
I voluntarily pledge to:
• Reduce unnecessary social media usage  
• Avoid excessive reel scrolling  
• Focus on real-life growth  
• Improve discipline and confidence  
• Adopt real-life activities and goals  
""")

st.markdown("---")

if st.button("Generate Certificate"):

    if name == "" or not consent:
        st.error("Please enter your name and accept consent.")
    else:
        # Create blank certificate image
        width, height = 1200, 850
        certificate = Image.new("RGB", (width, height), "#fefcf7")
        draw = ImageDraw.Draw(certificate)

        # Decorative border
        border_color = (184, 134, 11)
        draw.rectangle([(20, 20), (width-20, height-20)], outline=border_color, width=8)

        # Load logo
        logo = Image.open("logo.jpeg")
        logo = logo.resize((180, 180))
        certificate.paste(logo, (width//2 - 90, 50))

        # Fonts (default safe fonts)
        try:
            title_font = ImageFont.truetype("arial.ttf", 60)
            subtitle_font = ImageFont.truetype("arial.ttf", 40)
            body_font = ImageFont.truetype("arial.ttf", 32)
        except:
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
            body_font = ImageFont.load_default()

        # Title
        draw.text((width/2, 260), "Certificate of Digital Discipline",
                  font=title_font, fill="#1b5e20", anchor="mm")

        today = datetime.date.today().strftime("%d %B %Y")

        body_text = f"""
This is to certify that {name}, aged {age} years,
has taken a conscious pledge to reduce digital distractions.

The participant reported spending approximately {hours} hours
daily on social media and reel consumption.

By this declaration, the participant commits to:
• Reducing unnecessary scrolling
• Building discipline and confidence
• Engaging in real-world activities
• Setting meaningful life goals

This pledge is made voluntarily on {today}.
"""

        draw.multiline_text((width/2, 420), body_text,
                            font=body_font, fill="black",
                            anchor="mm", align="center", spacing=10)

        # Footer
        draw.text((width/2, height-120),
                  "Three Arrows Family – A Sacred Service Since 2014",
                  font=subtitle_font, fill="#444444", anchor="mm")

        # Save to buffer
        buffer = io.BytesIO()
        certificate.save(buffer, format="PNG")
        buffer.seek(0)

        st.image(certificate, use_column_width=True)

        st.download_button(
            label="Download Certificate (PNG)",
            data=buffer,
            file_name=f"{name}_certificate.png",
            mime="image/png"
        )

        st.success("Certificate Generated Successfully 🌿")