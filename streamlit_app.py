import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import datetime
import io

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Three Arrows Family", page_icon="🌿", layout="wide")

# --- WEBSITE CSS STYLING ---
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f4c3a 0%, #1e6b4c 50%, #0d5e3f 100%);
}
.org-title {
    font-size: 48px;
    font-weight: 900;
    color: #FFD700;
    text-shadow: 3px 3px 6px rgba(0,0,0,0.5);
    font-family: 'Arial Black', sans-serif;
}
.tagline {
    font-size: 22px;
    color: #ECF0F1;
    font-style: italic;
    font-weight: 500;
}
/* Input Styling */
.stTextInput label, .stNumberInput label, .stSlider label {
    color: white !important;
    font-size: 18px !important;
    font-weight: 700 !important;
}
[data-testid="stTextInput"] input {
    background-color: #E8F0FE !important;
    border: 3px solid #FFD700 !important;
    border-radius: 8px;
    font-size: 18px !important;
    font-weight: bold !important;
}
[data-testid="stNumberInput"] input {
    background-color: #FFE5B4 !important;
    border: 3px solid #FFD700 !important;
    border-radius: 8px;
    font-size: 18px !important;
    font-weight: bold !important;
}
.consent-box {
    background: rgba(255,255,255,0.1);
    padding: 25px;
    border-radius: 15px;
    border: 2px solid #FFD700;
    margin: 20px 0;
}
.stButton > button {
    background: linear-gradient(90deg, #FFD700, #FFA500);
    color: #0f4c3a;
    font-size: 24px;
    font-weight: 900;
    border-radius: 12px;
    height: 70px;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
col1, col2 = st.columns([1,6])
with col1:
    try:
        st.image("logo.jpeg", width=130)
    except:
        st.write("🏹")

with col2:
    st.markdown("<div class='org-title'>THREE ARROWS FAMILY</div>", unsafe_allow_html=True)
    st.markdown("<div class='tagline'>A Shared Service Since 2014 ✦ Digital Wellness Advocates</div>", unsafe_allow_html=True)

st.markdown("---")

# --- USER INPUT FORM ---
col_f1, col_f2 = st.columns(2)
with col_f1:
    st.markdown("### 👤 FULL NAME")
    name = st.text_input("", placeholder="Enter your full name", label_visibility="collapsed")
    st.markdown("### 📱 DAILY SCREEN TIME")
    hours = st.slider("", 0, 15, 3, label_visibility="collapsed")

with col_f2:
    st.markdown("### 🎂 AGE")
    age = st.number_input("", min_value=5, max_value=100, step=1, value=25, label_visibility="collapsed")

st.markdown("""
<div class='consent-box'>
    <div style='color: #FFD700; font-size: 24px; font-weight: bold;'>📋 DIGITAL WELLBEING PLEDGE</div>
    <div style='color: white; border-left: 4px solid #FFD700; padding-left: 10px; margin: 10px 0;'>✓ I commit to reducing mindless scrolling and prioritizing real-world connections.</div>
</div>
""", unsafe_allow_html=True)

consent = st.checkbox("✅ I understand and accept the Digital Wellbeing Pledge")
generate = st.button("🎨 GENERATE CERTIFICATE", use_container_width=True)

# --- CERTIFICATE GENERATION ---
if generate:
    if not name or not consent:
        st.error("⚠️ Please enter your name and accept the pledge.")
    else:
        # 1. Canvas & Colors
        width, height = 1500, 1050
        GOLD, DEEP_BLUE, CREAM = "#C5A028", "#1B4D3E", "#FDFBF7"
        certificate = Image.new("RGB", (width, height), CREAM)
        draw = ImageDraw.Draw(certificate)

        # Borders
        draw.rectangle([(20, 20), (width-20, height-20)], outline=GOLD, width=15)
        draw.rectangle([(40, 40), (width-40, height-40)], outline=DEEP_BLUE, width=3)

        # 2. Font Fallback Logic (CRITICAL FIX)
        try:
            # These will fail on Streamlit Cloud unless you upload .ttf files to GitHub
            header_font = ImageFont.truetype("arialbd.ttf", 65)
            subtitle_font = ImageFont.truetype("ariali.ttf", 35)
            name_label_font = ImageFont.truetype("arial.ttf", 30)
            name_text_font = ImageFont.truetype("arialbd.ttf", 110)
            age_font = ImageFont.truetype("arialbd.ttf", 50)
            pledge_font = ImageFont.truetype("arial.ttf", 40)
            footer_font = ImageFont.truetype("arial.ttf", 25)
        except:
            # If fonts fail, this block ensures ALL variables are defined
            default = ImageFont.load_default()
            header_font = subtitle_font = name_label_font = name_text_font = \
            age_font = pledge_font = footer_font = default

        # 3. Logo
        try:
            logo_cert = Image.open("logo.jpeg").resize((180, 180))
            certificate.paste(logo_cert, (width//2 - 90, 60))
        except:
            pass

        # 4. Text Placement
        draw.text((width//2, 280), "THREE ARROWS FAMILY", font=header_font, fill=DEEP_BLUE, anchor="mm")
        draw.text((width//2, 340), "A Shared Service Since 2014", font=subtitle_font, fill=GOLD, anchor="mm")
        draw.text((width//2, 400), "CERTIFICATE OF DIGITAL DISCIPLINE", font=header_font, fill=DEEP_BLUE, anchor="mm")

        # 5. Highlighted Name Section
        name_y = 480
        draw.rectangle([(250, name_y), (1250, name_y+160)], fill="#E8F0FE", outline=GOLD, width=4)
        draw.text((width//2, name_y + 35), "THIS IS PROUDLY PRESENTED TO", font=name_label_font, fill="#666666", anchor="mm")
        draw.text((width//2, name_y + 105), name.upper(), font=name_text_font, fill=DEEP_BLUE, anchor="mm")

        # 6. Highlighted Age Section
        age_y = 660
        draw.rectangle([(width//2 - 200, age_y), (width//2 + 200, age_y+80)], fill="#FFE5B4", outline=DEEP_BLUE, width=3)
        draw.text((width//2, age_y + 40), f"AGE: {age} YEARS", font=age_font, fill=DEEP_BLUE, anchor="mm")

        # 7. Pledge Info
        pledge_text = f"Committed to reducing screen time from {hours} hrs to {max(1, hours-1)} hrs daily."
        draw.text((width//2, 820), pledge_text, font=pledge_font, fill="#333333", anchor="mm")

        # 8. Footer
        today = datetime.date.today().strftime("%d %B %Y")
        draw.text((150, 950), f"Date: {today}", font=footer_font, fill="#666666")
        draw.text((width-450, 950), "Verify: www.threearrowsfamily.org.in", font=footer_font, fill="#666666")

        # 9. Output
        buffer = io.BytesIO()
        certificate.save(buffer, format="JPEG", quality=100)
        buffer.seek(0)

        st.image(certificate, use_container_width=True)
        st.download_button("📥 DOWNLOAD CERTIFICATE", data=buffer, file_name=f"Cert_{name}.jpg", mime="image/jpeg", use_container_width=True)
        st.balloons()
