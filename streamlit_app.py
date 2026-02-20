import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import datetime
import io

st.set_page_config(page_title="Three Arrows Family", page_icon="🌿", layout="wide")

# -------------------- WEBSITE DESIGN --------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f3f8f3 0%, #e8f5e9 50%, #fffdf6 100%);
}

/* Header Styling */
.org-title {
    font-size: 38px;
    font-weight: 800;
    color: #1b5e20;
}

.tagline {
    font-size: 18px;
    color: #444;
    margin-top: -5px;
}

/* Button */
.stButton > button {
    background: linear-gradient(90deg, #1b5e20, #2e7d32);
    color: white;
    font-size: 20px;
    border-radius: 8px;
    height: 55px;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# -------------------- HEADER (LOGO + NAME SAME ROW) --------------------
col1, col2 = st.columns([1,6])

with col1:
    st.image("logo.jpeg", width=110)

with col2:
    st.markdown("<div class='org-title'>Three Arrows Family</div>", unsafe_allow_html=True)
    st.markdown("<div class='tagline'>Step Out of the Phone – Step Into Life 🌿</div>", unsafe_allow_html=True)

st.markdown("---")

# -------------------- FORM --------------------
name = st.text_input("👤 Full Name")
age = st.number_input("🎂 Age", min_value=5, max_value=100)
hours = st.slider("📱 Daily Social Media & Reel Hours", 0, 15, 3)

st.markdown("### ✅ Consent Declaration")
consent = st.checkbox("""
I voluntarily pledge to:
• Reduce unnecessary scrolling  
• Improve discipline and confidence  
• Engage in real-life activities  
• Set meaningful life goals  
""")

generate = st.button("🌿 Generate Certificate")

# -------------------- CERTIFICATE DESIGN --------------------
if generate:

    if name == "" or not consent:
        st.error("Please enter your name and accept consent.")
    else:
        width, height = 1800, 1200
        certificate = Image.new("RGB", (width, height), "#fffdf5")
        draw = ImageDraw.Draw(certificate)

        # Border
        draw.rectangle([(40, 40), (width-40, height-40)], outline=(184,134,11), width=15)

        # Load Logo
        logo = Image.open("logo.jpeg").resize((180, 180))
        certificate.paste(logo, (120, 100))

        try:
            title_font = ImageFont.truetype("arial.ttf", 85)
            name_font = ImageFont.truetype("arial.ttf", 95)
            body_font = ImageFont.truetype("arial.ttf", 45)
            sign_font = ImageFont.truetype("arial.ttf", 40)
        except:
            title_font = ImageFont.load_default()
            name_font = ImageFont.load_default()
            body_font = ImageFont.load_default()
            sign_font = ImageFont.load_default()

        # Organization Name beside logo
        draw.text((350, 160),
                  "THREE ARROWS FAMILY",
                  font=body_font,
                  fill="#1b5e20")

        # Certificate Title
        draw.text((width/2, 400),
                  "Certificate of Digital Discipline",
                  font=title_font,
                  fill="#1b5e20",
                  anchor="mm")

        # Name in CENTER (BIG & BOLD)
        draw.text((width/2, 600),
                  name.upper(),
                  font=name_font,
                  fill="#b8860b",
                  anchor="mm")

        # Age below name
        draw.text((width/2, 680),
                  f"Age: {age} Years",
                  font=body_font,
                  fill="#1b5e20",
                  anchor="mm")

        today = datetime.date.today().strftime("%d %B %Y")

        body_text = f"""
has taken a conscious pledge to reduce digital distractions.

The participant reported spending approximately {hours} hours
daily on social media and reel consumption.

This pledge is voluntarily made on {today}.
"""

        draw.multiline_text((width/2, 850),
                            body_text,
                            font=body_font,
                            fill="black",
                            anchor="mm",
                            align="center",
                            spacing=20)

        # Signature Section
        draw.line((width-600, height-250, width-200, height-250),
                  fill="black", width=3)

        draw.text((width-400, height-220),
                  "Signed by Three Arrows Family",
                  font=sign_font,
                  fill="#1b5e20",
                  anchor="mm")

        # Save PNG
        buffer = io.BytesIO()
        certificate.save(buffer, format="PNG")
        buffer.seek(0)

        st.markdown("## 🎉 Certificate Preview")
        st.image(certificate, use_column_width=True)

        st.download_button(
            label="📥 Download Certificate (PNG)",
            data=buffer,
            file_name=f"{name}_certificate.png",
            mime="image/png"
        )

        st.success("Certificate Generated Successfully 🌿")
