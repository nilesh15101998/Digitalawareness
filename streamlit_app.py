import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import datetime
import io
import hashlib

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Three Arrows Family", page_icon="🏹", layout="wide")

# --- WEBSITE CSS STYLING ---
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
    margin-bottom: 0px;
}

.tagline {
    font-size: 20px;
    color: #ECF0F1;
    text-align: center;
    margin-bottom: 30px;
}

/* HIGH CONTRAST INPUTS: Dark Green text on light backgrounds */
[data-testid="stTextInput"] input {
    background-color: #f0f8ff !important;
    color: #004d40 !important; 
    border: 3px solid #FFD700 !important;
    font-size: 20px !important;
    font-weight: 800 !important;
}

.pledge-container {
    background: rgba(255, 255, 255, 0.1);
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #FFD700;
    margin-bottom: 20px;
}

.stButton > button {
    background: linear-gradient(90deg, #FFD700, #FFA500);
    color: #0d3b2e;
    font-size: 22px;
    font-weight: bold;
    border-radius: 50px;
    height: 60px;
    transition: 0.3s;
}
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<div class='org-title'>THREE ARROWS FAMILY</div>", unsafe_allow_html=True)
st.markdown("<div class='tagline'>Step Out of the Phone, Step Into Life | Reg: 2025013310014127</div>", unsafe_allow_html=True)

# --- USER FORM ---
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("👤 FULL NAME", placeholder="Enter your full name")
    hours = st.slider("📱 CURRENT DAILY SCROLLING (HRS)", 0, 15, 4)

with col2:
    # Changed to text input as requested
    age = st.text_input("🎂 YOUR AGE", placeholder="e.g. 25 Years")
    st.info("💡 Today's easy pleasure steals Tomorrow's confidence!")

st.markdown("### 📋 The Digital Discipline Pledge")
with st.container():
    st.markdown("""
    <div class='pledge-container'>
        <p style='color: white; font-size: 16px;'>
        ✓ I commit to <b>Stop the Virtual</b> and <b>Live the Real Life</b>.<br>
        ✓ I recognize that easy pleasure (scrolling) steals my tomorrow's confidence.<br>
        ✓ I will replace screen time with sports, society connection, and clear goals.<br>
        ✓ I commit to reducing my scrolling to reclaim focus and motivation.
        </p>
    </div>
    """, unsafe_allow_html=True)

consent = st.checkbox("✅ I accept this pledge for a better Digital Wellness")
generate = st.button("🎨 GENERATE MY OFFICIAL CERTIFICATE", use_container_width=True)

# --- CERTIFICATE GENERATION LOGIC ---
if generate:
    if not name or not age or not consent:
        st.error("⚠️ Please provide your Name, Age, and accept the pledge first!")
    else:
        # 1. Compact Dimensions (1200x950 to fit on screen)
        width, height = 1200, 950 
        DEEP_BLUE, GOLD, CREAM = "#1B4D3E", "#C5A028", "#FDFBF7"
        cert = Image.new("RGB", (width, height), CREAM)
        draw = ImageDraw.Draw(cert)

        # 2. UNIQUE ID
        unique_hash = hashlib.md5(f"{name}{datetime.datetime.now()}".encode()).hexdigest()[:4].upper()
        cert_id = f"3AF-{datetime.date.today().year}-{unique_hash}"

        # 3. Borders
        margin = 30
        draw.rectangle([(margin, margin), (width-margin, height-margin)], outline=GOLD, width=10)
        draw.rectangle([(margin+12, margin+12), (width-margin-12, height-margin-12)], outline=DEEP_BLUE, width=2)

        # 4. Fonts
        try:
            f_title = ImageFont.truetype("arialbd.ttf", 60)
            f_name = ImageFont.truetype("arialbd.ttf", 95)
            f_body = ImageFont.truetype("arial.ttf", 30)
            f_bold = ImageFont.truetype("arialbd.ttf", 34)
            f_footer = ImageFont.truetype("arial.ttf", 22)
        except:
            f_title = f_name = f_bold = ImageFont.load_default()
            f_body = f_footer = ImageFont.load_default()

        # 5. Asset Placement
        try:
            logo = Image.open("logo.jpeg").resize((120, 120))
            cert.paste(logo, (width//2 - 60, 50))
        except: pass

        draw.text((width//2, 210), "THREE ARROWS FAMILY", font=f_title, fill=DEEP_BLUE, anchor="mm")
        draw.text((width//2, 260), "CERTIFICATE OF DIGITAL DISCIPLINE", font=f_bold, fill=DEEP_BLUE, anchor="mm")
        draw.text((width//2, 300), "✨ LIVE THE REAL LIFE, STOP THE VIRTUAL! ✨", font=f_body, fill=GOLD, anchor="mm")

        # Name Section (No Box)
        draw.text((width//2, 360), "Proudly presented to", font=f_body, fill="#555555", anchor="mm")
        draw.text((width//2, 430), name.upper(), font=f_name, fill=DEEP_BLUE, anchor="mm")
        draw.text((width//2, 500), f"AGE: {age.upper()}", font=f_bold, fill=GOLD, anchor="mm")

        # Commitment Section
        y_commit = 550
        draw.text((width//2, y_commit), "MY DIGITAL WELLNESS COMMITMENT", font=f_bold, fill=DEEP_BLUE, anchor="mm")
        
        commitments = [
            f"• Reducing scrolling from {hours} hrs to regain confidence and focus.",
            "• Adopting sports, discipline, and society connection.",
            "• Guarding focus from repeated dopamine hits.",
            "• Stepping Out of the Phone and Stepping Into Life!"
        ]
        
        for i, line in enumerate(commitments):
            draw.text((width//2, y_commit + 40 + (i*32)), line, font=f_body, fill="#333333", anchor="mm")

        # 6. Bottom Graphics (Happy Pics & QR)
        try:
            happy_img = Image.open("happy_pics.png").resize((380, 160))
            cert.paste(happy_img, (width//2 - 190, 715))
        except: pass

        try:
            qr = Image.open("qr_code.png").resize((110, 110))
            cert.paste(qr, (width - 170, 780))
        except: pass

        # 7. Footer Info
        today = datetime.date.today().strftime("%d %B %Y")
        draw.text((80, 900), f"Date: {today}", font=f_footer, fill="#777777")
        draw.text((width//2, 900), f"Verification ID: {cert_id}", font=f_footer, fill=DEEP_BLUE, anchor="mm")
        draw.text((width-210, 915), "Scan to Verify", font=f_footer, fill=GOLD)

        # 8. Output
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
