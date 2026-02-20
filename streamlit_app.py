import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import datetime
import io
import hashlib

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Three Arrows Family", page_icon="🏹", layout="wide")

# --- WEBSITE CSS STYLING ---
# High-contrast styling for inputs to ensure visibility
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

/* FIX: Name and Age input text color (Dark Green on Light Backgrounds) */
[data-testid="stTextInput"] input {
    background-color: #f0f8ff !important;
    color: #004d40 !important; 
    border: 3px solid #FFD700 !important;
    font-size: 20px !important;
    font-weight: 800 !important;
    padding: 10px !important;
}

.stButton > button {
    background: linear-gradient(90deg, #FFD700, #FFA500);
    color: #0d3b2e;
    font-size: 22px;
    font-weight: bold;
    border-radius: 50px;
    height: 60px;
}
</style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown("<div class='org-title'>THREE ARROWS FAMILY</div>", unsafe_allow_html=True)
st.markdown("<div class='tagline'>Step Out of the Phone, Step Into Life | Reg: 2025013310014127</div>", unsafe_allow_html=True)

# --- USER FORM ---
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("👤 FULL NAME", placeholder="Enter your full name")
    hours = st.slider("📱 CURRENT DAILY SCROLLING (HRS)", 0, 15, 4)

with col2:
    age = st.text_input("🎂 YOUR AGE", placeholder="e.g. 26 Years")
    st.info("💡 Live the Real Life, Stop the Virtual!")

consent = st.checkbox("✅ I commit to the Digital Discipline Pledge")
generate = st.button("🎨 GENERATE MY OFFICIAL CERTIFICATE", use_container_width=True)

# --- CERTIFICATE GENERATION LOGIC ---
if generate:
    if not name or not age or not consent:
        st.error("⚠️ Please provide your Name, Age, and accept the pledge!")
    else:
        # 1. Dimensions & Canvas
        width, height = 1500, 1000 
        DEEP_BLUE, GOLD, CREAM = "#1B4D3E", "#C5A028", "#FDFBF7"
        cert = Image.new("RGB", (width, height), CREAM)
        draw = ImageDraw.Draw(cert)

        # 2. UNIQUE ID GENERATION
        unique_hash = hashlib.md5(f"{name}{datetime.datetime.now()}".encode()).hexdigest()[:4].upper()
        cert_id = f"3AF-{datetime.date.today().year}-{unique_hash}"

        # 3. Compact Borders
        margin = 35
        draw.rectangle([(margin, margin), (width-margin, height-margin)], outline=GOLD, width=12)
        draw.rectangle([(margin+15, margin+15), (width-margin-15, height-margin-15)], outline=DEEP_BLUE, width=3)

        # 4. Fonts (Optimized for 1500px width)
        try:
            # f_branding is set to approx bold size 45 for this resolution
            f_branding = ImageFont.truetype("arialbd.ttf", 90) 
            f_title = ImageFont.truetype("arialbd.ttf", 60)
            f_name = ImageFont.truetype("arialbd.ttf", 110)
            f_body = ImageFont.truetype("arial.ttf", 35)
            f_footer = ImageFont.truetype("arial.ttf", 25)
        except:
            f_branding = f_title = f_name = ImageFont.load_default()
            f_body = f_footer = ImageFont.load_default()

        # 5. ASSET POSITIONING
        # Logo - Top Left
        try:
            logo = Image.open("logo.jpeg").resize((180, 180))
            cert.paste(logo, (80, 80))
        except:
            pass

        # QR Code - Top Right
        try:
            qr = Image.open("qr_code.png").resize((160, 160))
            cert.paste(qr, (width - 240, 80))
        except:
            pass

        # 6. TEXT CONTENT (Centered Layout)
        # Main Branding
        draw.text((width//2, 170), "THREE ARROWS FAMILY", font=f_branding, fill=DEEP_BLUE, anchor="mm")
        draw.text((width//2, 240), "A Sacred Service Since 2014", font=f_body, fill=GOLD, anchor="mm")
        
        # Certificate Titles
        draw.text((width//2, 350), "CERTIFICATE OF DIGITAL DISCIPLINE", font=f_title, fill=DEEP_BLUE, anchor="mm")
        draw.text((width//2, 410), "✨ LIVE THE REAL LIFE, STOP THE VIRTUAL! ✨", font=f_body, fill=GOLD, anchor="mm")

        # Recipient Information
        draw.text((width//2, 500), "This certificate is proudly presented to", font=f_body, fill="#555555", anchor="mm")
        draw.text((width//2, 590), name.upper(), font=f_name, fill=DEEP_BLUE, anchor="mm")
        draw.text((width//2, 670), f"AGE: {age.upper()}", font=f_title, fill=GOLD, anchor="mm")

        # Commitment Points
        y_commit = 740
        draw.text((width//2, y_commit), "MY DIGITAL WELLNESS COMMITMENT", font=f_title, fill=DEEP_BLUE, anchor="mm")
        
        commitments = [
            f"• Reducing daily scrolling from {hours} hrs to prioritize focus and health.",
            "• Adopting real-life activities: society connection, sports, and discipline.",
            "• Stepping Out of the Phone, Stepping Into Life!"
        ]
        
        for i, line in enumerate(commitments):
            draw.text((width//2, y_commit + 50 + (i*40)), line, font=f_body, fill="#333333", anchor="mm")

        # 7. FOOTER
        today = datetime.date.today().strftime("%d %B %Y")
        draw.text((100, 930), f"Date: {today}", font=f_footer, fill="#777777")
        draw.text((width//2, 930), f"Verification ID: {cert_id}", font=f_footer, fill=DEEP_BLUE, anchor="mm")
        draw.text((width-400, 930), "Verify at: www.threearrowsfamily.org.in", font=f_footer, fill="#777777")

        # 8. OUTPUT & DOWNLOAD
        buf = io.BytesIO()
        cert.save(buf, format="JPEG", quality=100)
        
        st.markdown("---")
        st.image(cert, use_container_width=True)
        st.download_button(
            label="📥 DOWNLOAD MY OFFICIAL CERTIFICATE",
            data=buf.getvalue(),
            file_name=f"Digital_Wellness_{cert_id}.jpg",
            mime="image/jpeg",
            use_container_width=True
        )
        st.balloons()
