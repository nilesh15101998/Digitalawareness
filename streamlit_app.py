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

/* Header Styling */
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

/* Form Inputs Styling */
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

/* Consent section */
.consent-box {
    background: rgba(255,255,255,0.1);
    padding: 25px;
    border-radius: 15px;
    border: 2px solid #FFD700;
    margin: 20px 0;
}

.consent-title {
    color: #FFD700;
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 15px;
}

.consent-point {
    color: white;
    font-size: 18px;
    padding: 8px;
    margin: 5px 0;
    background: rgba(255,255,255,0.1);
    border-left: 4px solid #FFD700;
}

/* Button */
.stButton > button {
    background: linear-gradient(90deg, #FFD700, #FFA500);
    color: #0f4c3a;
    font-size: 24px;
    font-weight: 900;
    border-radius: 12px;
    height: 70px;
    width: 100%;
    border: none;
    font-family: 'Arial Black', sans-serif;
    box-shadow: 0 6px 12px rgba(0,0,0,0.3);
}
</style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
col1, col2 = st.columns([1,6])
with col1:
    try:
        st.image("logo.jpeg", width=130)
    except:
        st.error("Logo not found")

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

# Consent Section
st.markdown("""
<div class='consent-box'>
    <div class='consent-title'>📋 DIGITAL WELLBEING PLEDGE</div>
    <div class='consent-point'>✓ I commit to reducing mindless scrolling by at least 1 hour daily</div>
    <div class='consent-point'>✓ I will prioritize real-world connections over virtual interactions</div>
    <div class='consent-point'>✓ I pledge to be fully present with family and friends</div>
</div>
""", unsafe_allow_html=True)

consent = st.checkbox("✅ I understand and accept the Digital Wellbeing Pledge")
generate = st.button("🎨 GENERATE CERTIFICATE", use_container_width=True)

# --- CERTIFICATE GENERATION LOGIC ---
if generate:
    if name == "" or not consent:
        st.error("⚠️ Please enter your name and accept the pledge.")
    else:
        # 1. Canvas Setup
        width, height = 1500, 1050
        certificate = Image.new("RGB", (width, height), "#FDFBF7") # Cream background
        draw = ImageDraw.Draw(certificate)

        # 2. Colors & Border
        GOLD = "#C5A028"
        DEEP_BLUE = "#1B4D3E"
        draw.rectangle([(20, 20), (width-20, height-20)], outline=GOLD, width=15)
        draw.rectangle([(40, 40), (width-40, height-40)], outline=DEEP_BLUE, width=3)

        # 3. Fonts (Default fallbacks included)
        try:
            header_font = ImageFont.truetype("arialbd.ttf", 65)
            subtitle_font = ImageFont.truetype("ariali.ttf", 35)
            name_label_font = ImageFont.truetype("arial.ttf", 30)
            name_text_font = ImageFont.truetype("arialbd.ttf", 110)
            age_font = ImageFont.truetype("arialbd.ttf", 50)
            pledge_font = ImageFont.truetype("arial.ttf", 40)
            footer_font = ImageFont.truetype("arial.ttf", 25)
        except:
            header_font = name_text_font = age_font = ImageFont.load_default()

        # 4. Header & Logo
        try:
            logo_cert = Image.open("logo.jpeg").resize((180, 180))
            certificate.paste(logo_cert, (width//2 - 90, 60))
        except:
            pass

        draw.text((width//2, 280), "THREE ARROWS FAMILY", font=header_font, fill=DEEP_BLUE, anchor="mm")
        draw.text((width//2, 340), "A Sacred Service Since 2014", font=subtitle_font, fill=GOLD, anchor="mm")
        draw.text((width//2, 400), "CERTIFICATE OF DIGITAL DISCIPLINE", font=header_font, fill=DEEP_BLUE, anchor="mm")

        # 5. NAME SECTION (Contrasting Blue Background)
        name_upper = name.upper()
        box_w, box_h = 1000, 160
        box_x, box_y = (width - box_w) // 2, 480
        draw.rectangle([(box_x, box_y), (box_x + box_w, box_y + box_h)], fill="#E8F0FE", outline=GOLD, width=4)
        
        draw.text((width//2, box_y + 30), "THIS IS PROUDLY PRESENTED TO", font=name_label_font, fill="#666666", anchor="mm")
        draw.text((width//2, box_y + 100), name_upper, font=name_text_font, fill=DEEP_BLUE, anchor="mm")

        # 6. AGE SECTION (Contrasting Yellow Background)
        age_text = f"AGE: {age} YEARS"
        age_box_w, age_box_h = 400, 80
        age_x, age_y = (width - age_box_w) // 2, 660
        draw.rectangle([(age_x, age_y), (age_x + age_box_w, age_y + age_box_h)], fill="#FFE5B4", outline=DEEP_BLUE, width=3)
        draw.text((width//2, age_y + 40), age_text, font=age_font, fill=DEEP_BLUE, anchor="mm")

        # 7. THE PLEDGE
        reduction = f"Committing to reduce daily scrolling from {hours} hrs to {max(1, hours-1)} hrs."
        draw.text((width//2, 800), "Has pledged to reclaim time for real-life activities and wellness.", font=pledge_font, fill="#333333", anchor="mm")
        draw.text((width//2, 860), reduction, font=pledge_font, fill=DEEP_BLUE, anchor="mm")

        # 8. FOOTER
        today = datetime.date.today().strftime("%d %B %Y")
        draw.text((150, 950), f"Date: {today}", font=footer_font, fill="#666666")
        draw.text((width-450, 950), f"Verify: www.threearrowsfamily.org.in", font=footer_font, fill="#666666")

        # 9. OUTPUT
        buffer = io.BytesIO()
        certificate.save(buffer, format="JPEG", quality=100)
        buffer.seek(0)

        st.markdown("---")
        st.image(certificate, use_container_width=True)
        st.download_button(
            label="📥 DOWNLOAD YOUR PLEDGE CERTIFICATE",
            data=buffer,
            file_name=f"Wellness_Cert_{name.replace(' ', '_')}.jpg",
            mime="image/jpeg",
            use_container_width=True
        )
        st.balloons()
