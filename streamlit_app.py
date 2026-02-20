import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import datetime
import io
import hashlib

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Three Arrows Family", page_icon="🏹", layout="wide")

# --- IMPROVED WEBSITE CSS ---
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

/* FIX: Input text visibility (Dark Green on Light Backgrounds) */
[data-testid="stTextInput"] input {
    background-color: #f0f8ff !important;
    color: #004d40 !important; 
    border: 3px solid #FFD700 !important;
    font-size: 20px !important;
    font-weight: 800 !important;
}

[data-testid="stNumberInput"] input {
    background-color: #fff9e6 !important;
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

# --- HEADER SECTION ---
st.markdown("<div class='org-title'>THREE ARROWS FAMILY</div>", unsafe_allow_html=True)
st.markdown("<div class='tagline'>A Sacred Service Since 2014 | Reg: 2025013310014127</div>", unsafe_allow_html=True)

# --- USER FORM ---
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("👤 FULL NAME", placeholder="Enter your full name")
    hours = st.slider("📱 CURRENT DAILY SCROLLING (HRS)", 0, 15, 4)

with col2:
    age = st.number_input("🎂 YOUR AGE", min_value=5, max_value=100, value=25)
    st.info("💡 Step Out of the Phone, Step Into Life!")

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
generate = st.button("🎨 GENERATE MY CERTIFICATE", use_container_width=True)

# --- CERTIFICATE GENERATION LOGIC ---
if generate:
    if not name or not consent:
        st.error("⚠️ Please provide your name and accept the pledge first!")
    else:
        # 1. Canvas Dimensions
        width, height = 1500, 1050
        DEEP_BLUE, GOLD, CREAM = "#1B4D3E", "#C5A028", "#FDFBF7"
        cert = Image.new("RGB", (width, height), CREAM)
        draw = ImageDraw.Draw(cert)

        # 2. UNIQUE ID GENERATION
        # Generates a short unique hex code based on Name and Timestamp
        unique_hash = hashlib.md5(f"{name}{datetime.datetime.now()}".encode()).hexdigest()[:4].upper()
        cert_id = f"3AF-{datetime.date.today().year}-{unique_hash}"

        # 3. Border (Reduced Margin)
        margin = 35 
        draw.rectangle([(margin, margin), (width-margin, height-margin)], outline=GOLD, width=12)
        draw.rectangle([(margin+15, margin+15), (width-margin-15, height-margin-15)], outline=DEEP_BLUE, width=3)

        # 4. Fonts
        try:
            f_title = ImageFont.truetype("arialbd.ttf", 75)
            f_subtitle = ImageFont.truetype("arial.ttf", 35)
            f_name = ImageFont.truetype("arialbd.ttf", 130)
            f_body = ImageFont.truetype("arial.ttf", 42)
            f_bold_body = ImageFont.truetype("arialbd.ttf", 44)
            f_footer = ImageFont.truetype("arial.ttf", 28)
        except:
            f_title = f_name = f_bold_body = ImageFont.load_default()
            f_subtitle = f_body = f_footer = ImageFont.load_default()

        # 5. Content Placement
        try:
            logo = Image.open("logo.jpeg").resize((160, 160))
            cert.paste(logo, (width//2 - 80, 70))
        except:
            pass

        draw.text((width//2, 260), "THREE ARROWS FAMILY", font=f_title, fill=DEEP_BLUE, anchor="mm")
        draw.text((width//2, 320), "A Sacred Service Since 2014 | Reg: 2025013310014127", font=f_subtitle, fill=GOLD, anchor="mm")
        draw.text((width//2, 400), "CERTIFICATE OF DIGITAL DISCIPLINE", font=f_bold_body, fill=DEEP_BLUE, anchor="mm")
        draw.text((width//2, 460), "✨ LIVE THE REAL LIFE, STOP THE VIRTUAL! ✨", font=f_subtitle, fill=GOLD, anchor="mm")

        # NAME (Clean - No Box)
        draw.text((width//2, 530), "Proudly presented to", font=f_body, fill="#555555", anchor="mm")
        draw.text((width//2, 620), name.upper(), font=f_name, fill=DEEP_BLUE, anchor="mm")
        
        # High-Contrast Age Box
        age_box = [width//2 - 180, 700, width//2 + 180, 770]
        draw.rectangle(age_box, fill="#FFE5B4", outline=DEEP_BLUE, width=2)
        draw.text((width//2, 735), f"AGE: {age} YEARS", font=f_bold_body, fill=DEEP_BLUE, anchor="mm")

        # BENEFITS/COMMITMENTS
        y_benefits = 830
        draw.text((width//2, y_benefits), "MY COMMITMENT TO DIGITAL WELLNESS", font=f_bold_body, fill=DEEP_BLUE, anchor="mm")
        
        commitment_lines = [
            f"• Reducing daily screen time from {hours} hrs to {max(1, hours-1)} hrs to regain focus.",
            "• Adopting real-life activities: Society connection, sports, and volunteering.",
            "• Guarding my dopamine hits to maintain high motivation and clear goals.",
            "• Prioritizing the Real Life over the Virtual World."
        ]
        
        y_text = y_benefits + 50
        for line in commitment_lines:
            draw.text((width//2, y_text), line, font=f_body, fill="#333333", anchor="mm")
            y_text += 45

        # 6. Footer (Including the New Certificate ID)
        today = datetime.date.today().strftime("%d %B %Y")
        draw.text((150, 1000), f"Date: {today}", font=f_footer, fill="#777777")
        draw.text((width//2, 1000), f"Certificate ID: {cert_id}", font=f_footer, fill=DEEP_BLUE, anchor="mm")
        draw.text((width-450, 1000), "Verify at: www.threearrowsfamily.org.in", font=f_footer, fill="#777777")

        # 7. Output
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
