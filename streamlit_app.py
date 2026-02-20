import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import datetime
import io
import hashlib

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Three Arrows Family", page_icon="🏹", layout="wide")

# --- CLEAR & PROFESSIONAL UI STYLING ---
st.markdown("""
<style>
/* Modern Green Gradient Background */
.stApp {
    background: linear-gradient(135deg, #0d3b2e 0%, #1b5e46 50%, #0a4d34 100%);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.org-title {
    font-size: 52px;
    font-weight: 900;
    color: #FFD700;
    text-align: center;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
}

.tagline {
    font-size: 20px;
    color: #ECF0F1;
    text-align: center;
    margin-bottom: 30px;
    font-weight: 500;
}

/* HIGH-VISIBILITY INPUTS */
[data-testid="stTextInput"] input, [data-testid="stNumberInput"] input {
    background-color: #f0f8ff !important;
    color: #004d40 !important; 
    border: 3px solid #FFD700 !important;
    font-size: 20px !important;
    font-weight: 800 !important;
    border-radius: 10px;
}

/* Pledge Box Styling */
.pledge-card {
    background: rgba(255, 255, 255, 0.15);
    padding: 25px;
    border-radius: 15px;
    border: 2px solid #FFD700;
    margin: 20px 0;
    color: white;
}

.pledge-item {
    margin-bottom: 10px;
    font-size: 18px;
    border-left: 4px solid #FFD700;
    padding-left: 15px;
}

.stButton > button {
    background: linear-gradient(90deg, #FFD700, #FFA500);
    color: #0d3b2e;
    font-size: 24px;
    font-weight: 900;
    border-radius: 50px;
    height: 70px;
    border: none;
    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
}
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<div class='org-title'>THREE ARROWS FAMILY</div>", unsafe_allow_html=True)
st.markdown("<div class='tagline'>A Sacred Service Since 2014 | Digital Wellness Initiative</div>", unsafe_allow_html=True)

# --- INPUT SECTION ---
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("👤 FULL NAME", placeholder="Type your name here...")
    hours = st.slider("📱 DAILY SCREEN TIME (HRS)", 0, 15, 4)

with col2:
    age = st.text_input("🎂 YOUR AGE", placeholder="e.g. 26 Years")
    st.info("💡 Step Out of the Phone, Step Into Life!")

# --- THE PLEDGE (BEFORE CONSENT) ---
st.markdown("### 📋 The Digital Discipline Pledge")
st.markdown("""
<div class='pledge-card'>
    <div class='pledge-item'><b>Stop the Virtual, Live the Real:</b> I commit to prioritizing face-to-face society connections.</div>
    <div class='pledge-item'><b>Guard Tomorrow's Confidence:</b> I recognize that easy pleasures like scrolling steal my future motivation.</div>
    <div class='pledge-item'><b>Defeat the Dopamine Loop:</b> I will reduce repeated dopamine hits from short videos to regain focus.</div>
    <div class='pledge-item'><b>Active Living:</b> I will replace idle scrolling with sports, learning, and clear personal goals.</div>
</div>
""", unsafe_allow_html=True)

consent = st.checkbox("✅ I solemnly pledge to follow these Digital Wellness principles.")
generate = st.button("🎨 GENERATE MY OFFICIAL CERTIFICATE", use_container_width=True)

# --- CERTIFICATE GENERATION ---
if generate:
    if not name or not age or not consent:
        st.error("⚠️ Please provide your Name, Age, and accept the pledge first!")
    else:
        # 1. Canvas & Color Palette
        width, height = 1500, 1050
        DEEP_BLUE, GOLD, CREAM = "#1B4D3E", "#C5A028", "#FDFBF7"
        cert = Image.new("RGB", (width, height), CREAM)
        draw = ImageDraw.Draw(cert)

        # Unique ID for Verification
        unique_hash = hashlib.md5(f"{name}{datetime.datetime.now()}".encode()).hexdigest()[:4].upper()
        cert_id = f"3AF-2026-{unique_hash}"

        # 2. Border Design (Reduced Margin)
        draw.rectangle([(30, 30), (width-30, height-30)], outline=GOLD, width=15)
        draw.rectangle([(50, 50), (width-50, height-50)], outline=DEEP_BLUE, width=3)

        # 3. Clean Fonts
        try:
            # For best results, upload 'Roboto-Bold.ttf' to your GitHub repo
            f_branding = ImageFont.truetype("arialbd.ttf", 90) 
            f_title = ImageFont.truetype("arialbd.ttf", 65)
            f_name = ImageFont.truetype("arialbd.ttf", 115)
            f_body = ImageFont.truetype("arial.ttf", 36)
            f_footer = ImageFont.truetype("arial.ttf", 26)
        except:
            # Fallback to standard system fonts
            f_branding = f_title = f_name = ImageFont.load_default()
            f_body = f_footer = ImageFont.load_default()

        # 4. Assets Positioning
        # Logo - Top Left
        try:
            logo = Image.open("logo.jpeg").resize((185, 185))
            cert.paste(logo, (85, 85))
        except: pass

        # QR Code - Top Right
        try:
            qr = Image.open("qr_code.png").resize((165, 165))
            cert.paste(qr, (width - 250, 85))
        except: pass

        # 5. Text Layout
        draw.text((width//2, 175), "THREE ARROWS FAMILY", font=f_branding, fill=DEEP_BLUE, anchor="mm")
        draw.text((width//2, 245), "A Sacred Service Since 2014", font=f_body, fill=GOLD, anchor="mm")
        
        draw.text((width//2, 360), "CERTIFICATE OF DIGITAL DISCIPLINE", font=f_title, fill=DEEP_BLUE, anchor="mm")
        draw.text((width//2, 420), "✨ LIVE THE REAL LIFE, STOP THE VIRTUAL! ✨", font=f_body, fill=GOLD, anchor="mm")

        # Recipient Section
        draw.text((width//2, 510), "This certificate is proudly presented to", font=f_body, fill="#555555", anchor="mm")
        draw.text((width//2, 605), name.upper(), font=f_name, fill=DEEP_BLUE, anchor="mm")
        draw.text((width//2, 690), f"AGE: {age.upper()}", font=f_title, fill=GOLD, anchor="mm")

        # Commitment Points
        y_commit = 760
        draw.text((width//2, y_commit), "MY DIGITAL WELLNESS COMMITMENT", font=f_title, fill=DEEP_BLUE, anchor="mm")
        
        pledges = [
            f"• Reducing daily screen time from {hours} hrs to focus on real goals.",
            "• Replacing virtual scrolling with physical sports and society service.",
            "• Prioritizing mental clarity over repeated dopamine hits from short videos.",
            "• Stepping Out of the Phone and Stepping Into Life!"
        ]
        
        for i, line in enumerate(pledges):
            draw.text((width//2, y_commit + 55 + (i*42)), line, font=f_body, fill="#333333", anchor="mm")

        # 6. Footer
        today = datetime.date.today().strftime("%d %B %Y")
        draw.text((120, 950), f"Date: {today}", font=f_footer, fill="#777777")
        draw.text((width//2, 950), f"Verification ID: {cert_id}", font=f_footer, fill=DEEP_BLUE, anchor="mm")
        draw.text((width-450, 950), "Verify at: www.threearrowsfamily.org.in", font=f_footer, fill="#777777")

        # 7. Rendering
        buf = io.BytesIO()
        cert.save(buf, format="JPEG", quality=100)
        
        st.markdown("---")
        st.image(cert, use_container_width=True)
        st.download_button(
            label="📥 DOWNLOAD MY OFFICIAL CERTIFICATE",
            data=buf.getvalue(),
            file_name=f"Digital_Discipline_{cert_id}.jpg",
            mime="image/jpeg",
            use_container_width=True
        )
        st.balloons()
