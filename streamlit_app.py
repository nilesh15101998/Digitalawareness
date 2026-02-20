import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import datetime
import io
import hashlib

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Three Arrows Family", page_icon="🏹", layout="wide")

# --- PROFESSIONAL WEBSITE UI STYLING ---
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0d3b2e 0%, #1b5e46 50%, #0a4d34 100%);
}
.org-title {
    font-size: 48px;
    font-weight: 900;
    color: #FFD700;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    margin: 0;
}
/* Input visibility for high-standard project presentation */
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

# --- WEBSITE HEADER ---
header_col1, header_col2 = st.columns([1, 6])
with header_col1:
    try:
        st.image("logo.jpeg", width=120)
    except:
        st.write("🏹")
with header_col2:
    st.markdown("<div class='org-title'>THREE ARROWS FAMILY</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:white; font-size:18px;'>Step Out of the Phone, Step Into Life | Digital Wellness Initiative</p>", unsafe_allow_html=True)

st.markdown("---")

# --- INPUT SECTION ---
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("👤 FULL NAME", placeholder="Type your full name...")
    hours = st.slider("📱 DAILY SCREEN TIME (HRS)", 0, 15, 4)
with col2:
    age_input = st.text_input("🎂 YOUR AGE", placeholder="e.g. 26 Years")
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
generate = st.button("🎨 GENERATE MY OFFICIAL CERTIFICATE", use_container_width=True)

# --- CERTIFICATE GENERATION ---
if generate:
    if not name or not consent:
        st.error("⚠️ Please provide your Name and accept the pledge first!")
    else:
        # 1. Canvas Setup
        width, height = 1800, 1300 
        DEEP_BLUE, GOLD, CREAM = "#1B4D3E", "#C5A028", "#FDFBF7"
        cert = Image.new("RGB", (width, height), CREAM)
        draw = ImageDraw.Draw(cert)

        # Unique ID Generation
        unique_hash = hashlib.md5(f"{name}{datetime.datetime.now()}".encode()).hexdigest()[:4].upper()
        cert_id = f"3AF-2026-{unique_hash}"

        # 2. Strict Boundary Borders
        margin_inner = 70
        draw.rectangle([(40, 40), (width-40, height-40)], outline=GOLD, width=20)
        draw.rectangle([(margin_inner, margin_inner), (width-margin_inner, height-margin_inner)], outline=DEEP_BLUE, width=4)

        # 3. Custom Fonts (Playfair and Montserrat files)
        try:
            f_branding = ImageFont.truetype("PlayfairDisplay-Bold.ttf", 100) 
            f_title = ImageFont.truetype("PlayfairDisplay-Bold.ttf", 80)
            f_name = ImageFont.truetype("PlayfairDisplay-Bold.ttf", 155)
            f_body = ImageFont.truetype("Montserrat-Regular.ttf", 40)
            f_side_title = ImageFont.truetype("PlayfairDisplay-Bold.ttf", 42)
            f_side_body = ImageFont.truetype("Montserrat-Regular.ttf", 34)
            f_footer = ImageFont.truetype("Montserrat-Regular.ttf", 28)
        except:
            f_branding = f_title = f_name = f_body = f_side_title = f_side_body = f_footer = ImageFont.load_default()

        # 4. Corner Assets
        try:
            logo_img = Image.open("logo.jpeg").resize((220, 220))
            cert.paste(logo_img, (110, 110))
            qr_img = Image.open("qr_code.png").resize((200, 200))
            cert.paste(qr_img, (width - 320, 110))
        except: pass

        # 5. SIDEBAR CONTENT
        # Left Side: Adopt Real Life
        x_left = 130
        draw.text((x_left, 480), "ADOPT REAL LIFE:", font=f_side_title, fill=GOLD)
        activities = ["• Connect with society deeply", "• Adopt sports and discipline", "• Serve and volunteer daily", "• Set and pursue clear goals"]
        for i, a in enumerate(activities):
            draw.text((x_left, 540 + (i*55)), a, font=f_side_body, fill=DEEP_BLUE)

        # Right Side: Key Findings (Positioned right)
        x_right = width - 600
        draw.text((x_right, 480), "KEY FINDINGS (2023-2025):", font=f_side_title, fill=GOLD)
        findings = ["• Short videos = repeated hits", "• More dopamine = less motivation", "• Passive scrolling = anxiety", "• Pleasure steals confidence"]
        for i, f in enumerate(findings):
            draw.text((x_right, 540 + (i*55)), f, font=f_side_body, fill=DEEP_BLUE)

        # 6. CENTRAL CONTENT
        draw.text((width//2, 220), "THREE ARROWS FAMILY", font=f_branding, fill=DEEP_BLUE, anchor="mm")
        draw.text((width//2, 300), "A Shared Service Since 2014 | Step Into Life", font=f_body, fill=GOLD, anchor="mm")
        draw.text((width//2, 420), "CERTIFICATE OF DIGITAL DISCIPLINE", font=f_title, fill=DEEP_BLUE, anchor="mm")

        # Name Section: Shifted further down as requested
        name_y_label = 700
        name_y_text = 830
        draw.text((width//2, name_y_label), "PROUDLY PRESENTED TO:", font=f_body, fill="#555555", anchor="mm")
        draw.text((width//2, name_y_text), name.upper(), font=f_name, fill=DEEP_BLUE, anchor="mm")

        # Commitment Pledge: Positioned below name
        draw.text((width//2, 1030), "COMMITMENT PLEDGE", font=f_title, fill=DEEP_BLUE, anchor="mm")
        pledge_text = f"Reducing daily screen time from {hours} hours to reclaim focus and confidence.\nPrioritizing the Real World over the Virtual World."
        draw.multiline_text((width//2, 1120), pledge_text, font=f_body, fill="#333333", anchor="mm", align="center")

        # 7. FOOTER (Strictly within boundaries)
        footer_y_base = 1180
        footer_y_secondary = 1210
        today = datetime.date.today().strftime("%d %B %Y")
        
        # Left-aligned footer information
        draw.text((150, footer_y_base), f"Date: {today}", font=f_footer, fill="#777777")
        draw.text((150, footer_y_secondary), "Verify at: www.threearrowsfamily.org.in", font=f_footer, fill="#777777")
        
        # Center-aligned Verification ID
        draw.text((width//2, footer_y_base), f"Verification ID: {cert_id}", font=f_footer, fill=DEEP_BLUE, anchor="mm")

        # 8. OUTPUT
        buf = io.BytesIO()
        cert.save(buf, format="JPEG", quality=100)
        st.markdown("---")
        st.image(cert, use_container_width=True)
        st.download_button("📥 DOWNLOAD MY OFFICIAL CERTIFICATE", data=buf.getvalue(), file_name=f"Digital_Discipline_{cert_id}.jpg", mime="image/jpeg", use_container_width=True)
        st.balloons()
