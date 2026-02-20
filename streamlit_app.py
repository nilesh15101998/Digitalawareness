import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import datetime
import io
import hashlib

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Three Arrows Family", page_icon="🏹", layout="wide")

# --- WEBSITE UI STYLING ---
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0d3b2e 0%, #1b5e46 50%, #0a4d34 100%);
}
.org-title {
    font-size: 52px;
    font-weight: 900;
    color: #FFD700;
    text-align: center;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
}
/* HIGH-VISIBILITY INPUTS */
[data-testid="stTextInput"] input {
    background-color: #f0f8ff !important;
    color: #004d40 !important; 
    border: 3px solid #FFD700 !important;
    font-size: 22px !important;
    font-weight: 800 !important;
}
.pledge-card {
    background: rgba(255, 255, 255, 0.15);
    padding: 25px;
    border-radius: 15px;
    border: 2px solid #FFD700;
    color: white;
}
.stButton > button {
    background: linear-gradient(90deg, #FFD700, #FFA500);
    color: #0d3b2e;
    font-size: 26px;
    font-weight: 900;
    border-radius: 50px;
    height: 75px;
}
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<div class='org-title'>THREE ARROWS FAMILY</div>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color:white;'>Digital Wellness Discipline Portal</h3>", unsafe_allow_html=True)

# --- INPUT SECTION ---
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("👤 FULL NAME", placeholder="Type your name here...")
    hours = st.slider("📱 CURRENT SCREEN TIME (HRS)", 0, 15, 4)

with col2:
    age = st.text_input("🎂 YOUR AGE", placeholder="e.g. 26 Years")
    st.info("💡 Today's easy pleasure steals Tomorrow's confidence!")

# --- THE PLEDGE ---
st.markdown("""
<div class='pledge-card'>
    <h4 style='color:#FFD700;'>📋 The Digital Discipline Pledge</h4>
    <p>• I commit to prioritizing real-world connections over mindless scrolling.</p>
    <p>• I recognize that repeated dopamine hits from short videos weaken focus.</p>
    <p>• I will replace screen time with sports, society connection, and clear goals.</p>
</div>
""", unsafe_allow_html=True)

consent = st.checkbox("✅ I accept this pledge for a better Digital Wellness")
generate = st.button("🎨 GENERATE MY BIG-FONT CERTIFICATE", use_container_width=True)

# --- CERTIFICATE GENERATION ---
if generate:
    if not name or not age or not consent:
        st.error("⚠️ Please provide your Name, Age, and accept the pledge!")
    else:
        # 1. Canvas & Color Palette
        width, height = 1800, 1300 # Larger canvas for bigger text
        DEEP_BLUE, GOLD, CREAM = "#1B4D3E", "#C5A028", "#FDFBF7"
        cert = Image.new("RGB", (width, height), CREAM)
        draw = ImageDraw.Draw(cert)

        # Unique ID
        unique_hash = hashlib.md5(f"{name}{datetime.datetime.now()}".encode()).hexdigest()[:4].upper()
        cert_id = f"3AF-2026-{unique_hash}"

        # 2. Border Design
        draw.rectangle([(40, 40), (width-40, height-40)], outline=GOLD, width=20)
        draw.rectangle([(70, 70), (width-70, height-70)], outline=DEEP_BLUE, width=4)

        # 3. Extra Large Fonts (Uploading .ttf to GitHub is recommended)
        try:
            f_branding = ImageFont.truetype("arialbd.ttf", 110) 
            f_title = ImageFont.truetype("arialbd.ttf", 80)
            f_name = ImageFont.truetype("arialbd.ttf", 160) # Massive Name
            f_body = ImageFont.truetype("arial.ttf", 45)
            f_side = ImageFont.truetype("arialbd.ttf", 35)
            f_footer = ImageFont.truetype("arial.ttf", 30)
        except:
            f_branding = f_title = f_name = ImageFont.load_default()
            f_body = f_side = f_footer = ImageFont.load_default()

        # 4. Assets Positioning
        # Logo - Top Left
        try:
            logo = Image.open("logo.jpeg").resize((220, 220))
            cert.paste(logo, (100, 100))
        except: pass

        # QR Code - Top Right
        try:
            qr = Image.open("qr_code.png").resize((200, 200))
            cert.paste(qr, (width - 300, 100))
        except: pass

        # 5. SIDEBAR CONTENT (Fills left and right space)
        # Left Side: Key Findings
        draw.text((120, 450), "KEY FINDINGS:", font=f_side, fill=GOLD)
        findings = ["• Short videos = repeated dopamine", "• More dopamine = less motivation", "• Scrolling = anxiety & emptiness"]
        for i, f in enumerate(findings):
            draw.text((120, 500 + (i*50)), f, font=f_footer, fill=DEEP_BLUE)

        # Right Side: Real Life Activities
        draw.text((width - 450, 450), "ADOPT REAL LIFE:", font=f_side, fill=GOLD)
        activities = ["• Connect with society", "• Adopt sports & discipline", "• Serve and volunteer", "• Set clear goals"]
        for i, a in enumerate(activities):
            draw.text((width - 450, 500 + (i*50)), a, font=f_footer, fill=DEEP_BLUE)

        # 6. CENTRAL TEXT LAYOUT
        draw.text((width//2, 220), "THREE ARROWS FAMILY", font=f_branding, fill=DEEP_BLUE, anchor="mm")
        draw.text((width//2, 300), "A Sacred Service Since 2014", font=f_body, fill=GOLD, anchor="mm")
        draw.text((width//2, 420), "CERTIFICATE OF DIGITAL DISCIPLINE", font=f_title, fill=DEEP_BLUE, anchor="mm")

        # Recipient Section (Large & Readable)
        draw.text((width//2, 550), "PROUDLY PRESENTED TO", font=f_body, fill="#555555", anchor="mm")
        draw.text((width//2, 680), name.upper(), font=f_name, fill=DEEP_BLUE, anchor="mm")
        draw.text((width//2, 780), f"AGE: {age.upper()}", font=f_title, fill=GOLD, anchor="mm")

        # Commitment Statement
        draw.text((width//2, 900), "COMMITMENT PLEDGE", font=f_title, fill=DEEP_BLUE, anchor="mm")
        pledge_text = f"Reducing daily screen time from {hours} hours to reclaim focus and confidence.\nStepping Out of the Phone and Stepping Into Life!"
        draw.multiline_text((width//2, 1000), pledge_text, font=f_body, fill="#333333", anchor="mm", align="center")

        # 7. FOOTER
        today = datetime.date.today().strftime("%d %B %Y")
        draw.text((150, 1200), f"Date: {today}", font=f_footer, fill="#777777")
        draw.text((width//2, 1200), f"Verification ID: {cert_id}", font=f_footer, fill=DEEP_BLUE, anchor="mm")
        draw.text((width-500, 1200), "Verify at: www.threearrowsfamily.org.in", font=f_footer, fill="#777777")

        # 8. OUTPUT
        buf = io.BytesIO()
        cert.save(buf, format="JPEG", quality=100)
        st.markdown("---")
        st.image(cert, use_container_width=True)
        st.download_button("📥 DOWNLOAD CERTIFICATE", data=buf.getvalue(), file_name=f"Cert_{cert_id}.jpg", mime="image/jpeg", use_container_width=True)
        st.balloons()
