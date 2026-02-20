import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import datetime
import io
import base64

st.set_page_config(page_title="Three Arrows Family", page_icon="🌿", layout="centered")

# ---------- CUSTOM CSS DESIGN ----------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #f6f9f6 0%, #e8f5e9 50%, #fdfbf3 100%);
    font-family: 'Segoe UI', sans-serif;
}

.main-card {
    background: white;
    padding: 40px;
    border-radius: 20px;
    box-shadow: 0px 8px 30px rgba(0,0,0,0.08);
}

h1 {
    text-align: center;
    color: #1b5e20;
    font-weight: 700;
}

.sub-text {
    text-align: center;
    color: #555;
    margin-bottom: 30px;
}

.stButton > button {
    background: linear-gradient(90deg, #1b5e20, #2e7d32);
    color: white;
    font-size: 18px;
    border-radius: 10px;
    height: 50px;
    width: 100%;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #2e7d32, #1b5e20);
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
logo = Image.open("logo.jpeg")
st.image(logo, width=130)

st.markdown("<h1>Three Arrows Family</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-text'>Step Out of the Phone – Step Into Life 🌿</p>", unsafe_allow_html=True)

st.markdown("---")

# ---------- FORM SECTION ----------
with st.container():
    st.markdown("<div class='main-card'>", unsafe_allow_html=True)

    name = st.text_input("👤 Full Name")
    age = st.number_input("🎂 Age", min_value=5, max_value=100)

    hours = st.slider("📱 How many hours daily on Social Media & Reels?", 0, 15, 3)

    st.markdown("### ✅ Consent Declaration")

    consent = st.checkbox("""
    I voluntarily pledge to:
    • Reduce unnecessary social media usage  
    • Avoid excessive reel scrolling  
    • Focus on real-life growth  
    • Improve discipline and confidence  
    • Adopt real-life activities and goals  
    """)

    generate = st.button("🌿 Generate Certificate")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------- CERTIFICATE GENERATION ----------
if generate:

    if name == "" or not consent:
        st.error("Please enter your name and accept consent.")
    else:
        width, height = 1400, 1000
        certificate = Image.new("RGB", (width, height), "#fffdf5")
        draw = ImageDraw.Draw(certificate)

        # Gold border
        draw.rectangle([(30, 30), (width-30, height-30)], outline=(184, 134, 11), width=12)

        # Logo
        logo = logo.resize((200, 200))
        certificate.paste(logo, (width//2 - 100, 80))

        try:
            title_font = ImageFont.truetype("arial.ttf", 70)
            body_font = ImageFont.truetype("arial.ttf", 38)
            footer_font = ImageFont.truetype("arial.ttf", 32)
        except:
            title_font = ImageFont.load_default()
            body_font = ImageFont.load_default()
            footer_font = ImageFont.load_default()

        draw.text((width/2, 330), "Certificate of Digital Discipline",
                  font=title_font, fill="#1b5e20", anchor="mm")

        today = datetime.date.today().strftime("%d %B %Y")

        text = f"""
This is to proudly certify that {name}, aged {age} years,
has taken a conscious step towards reducing digital distractions.

The participant previously reported spending approximately {hours} hours
daily on social media and reel consumption.

By this declaration, the participant commits to:

• Reducing unnecessary scrolling
• Building discipline and confidence
• Engaging in real-world activities
• Setting meaningful life goals

This pledge is made voluntarily on {today}.
"""

        draw.multiline_text((width/2, 600), text,
                            font=body_font,
                            fill="black",
                            anchor="mm",
                            align="center",
                            spacing=15)

        draw.text((width/2, height-150),
                  "Three Arrows Family – A Sacred Service Since 2014",
                  font=footer_font,
                  fill="#555",
                  anchor="mm")

        buffer = io.BytesIO()
        certificate.save(buffer, format="PNG")
        buffer.seek(0)

        st.markdown("### 🎉 Certificate Preview")
        st.image(certificate, use_column_width=True)

        st.download_button(
            label="📥 Download Certificate (PNG)",
            data=buffer,
            file_name=f"{name}_certificate.png",
            mime="image/png"
        )

        st.success("Certificate Generated Successfully 🌿")
