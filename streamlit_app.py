import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import datetime
import io

st.set_page_config(page_title="Three Arrows Family", page_icon="🌿", layout="wide")

# -------------------- WEBSITE DESIGN --------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0a3e2f 0%, #1a4f3a 50%, #0d4b32 100%);
}

/* Header Styling */
.org-title {
    font-size: 48px;
    font-weight: 900;
    color: #FFD700;
    text-shadow: 3px 3px 6px rgba(0,0,0,0.5);
    font-family: 'Arial Black', sans-serif;
    letter-spacing: 1px;
}

.tagline {
    font-size: 22px;
    color: #ECF0F1;
    font-style: italic;
    font-weight: 500;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

/* Form Styling */
.stTextInput label, .stNumberInput label, .stSlider label {
    color: white !important;
    font-size: 18px !important;
    font-weight: 700 !important;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
}

/* Name input background */
[data-testid="stTextInput"] input {
    background-color: #E8F0FE !important;
    border: 3px solid #FFD700 !important;
    border-radius: 8px;
    font-size: 18px !important;
    font-weight: bold !important;
    color: #000000 !important;
    padding: 10px !important;
}

/* Age input background */
[data-testid="stNumberInput"] {
    background-color: transparent !important;
}
[data-testid="stNumberInput"] input {
    background-color: #FFE5B4 !important;
    border: 3px solid #FFD700 !important;
    border-radius: 8px;
    font-size: 18px !important;
    font-weight: bold !important;
    color: #000000 !important;
    padding: 10px !important;
}

/* Slider styling */
.stSlider {
    background-color: rgba(255,255,255,0.1) !important;
    padding: 15px !important;
    border-radius: 10px !important;
}

/* Consent section */
.consent-box {
    background-color: rgba(255,255,255,0.15);
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
    font-family: 'Arial Black', sans-serif;
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
    color: #0a3e2f;
    font-size: 24px;
    font-weight: 900;
    border-radius: 12px;
    height: 70px;
    width: 100%;
    border: none;
    font-family: 'Arial Black', sans-serif;
    letter-spacing: 1px;
    box-shadow: 0 6px 12px rgba(0,0,0,0.3);
    margin: 20px 0;
}
</style>
""", unsafe_allow_html=True)

# -------------------- HEADER --------------------
col1, col2 = st.columns([1,6])

with col1:
    st.image("logo.jpeg", width=130)

with col2:
    st.markdown("<div class='org-title'>THREE ARROWS FAMILY</div>", unsafe_allow_html=True)
    st.markdown("<div class='tagline'>A Shared Service Since 2014 ✦ Digital Wellness Advocates</div>", unsafe_allow_html=True)

st.markdown("---")

# -------------------- FORM --------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 👤 FULL NAME")
    name = st.text_input("", placeholder="Enter your full name", label_visibility="collapsed")
    
    st.markdown("### 📱 DAILY SCREEN TIME")
    hours = st.slider("", 0, 15, 3, label_visibility="collapsed")

with col2:
    st.markdown("### 🎂 AGE")
    age = st.number_input("", min_value=5, max_value=100, step=1, value=25, label_visibility="collapsed")
    st.markdown("<br><br>", unsafe_allow_html=True)

# Consent Section with better points
st.markdown("""
<div class='consent-box'>
    <div class='consent-title'>📋 DIGITAL WELLBEING PLEDGE</div>
    <div class='consent-point'>✓ I commit to reducing mindless scrolling by at least 1 hour daily</div>
    <div class='consent-point'>✓ I will prioritize real-world connections over virtual interactions</div>
    <div class='consent-point'>✓ I pledge to be fully present with family and friends</div>
    <div class='consent-point'>✓ I will use saved time for personal growth and learning</div>
    <div class='consent-point'>✓ I commit to tracking my screen time weekly</div>
</div>
""", unsafe_allow_html=True)

consent = st.checkbox("✅ I understand and accept the Digital Wellbeing Pledge")

generate = st.button("🎨 GENERATE CERTIFICATE", use_container_width=True)

# -------------------- CERTIFICATE DESIGN --------------------
if generate:

    if name == "" or not consent:
        st.error("⚠️ Please enter your name and accept the pledge.")
    else:
        # Certificate dimensions - optimal for readability
        width, height = 1400, 1000
        certificate = Image.new("RGB", (width, height), "#FDF5E6")  # Old lace
        draw = ImageDraw.Draw(certificate)

        # Double border for elegance
        draw.rectangle([(20, 20), (width-20, height-20)], outline="#C5A028", width=4)
        draw.rectangle([(35, 35), (width-35, height-35)], outline="#F0C45A", width=2)
        
        # Decorative corners
        corner_len = 60
        positions = [(20,20), (width-20,20), (20,height-20), (width-20,height-20)]
        for x,y in positions:
            draw.ellipse([(x-8, y-8), (x+8, y+8)], fill="#C5A028")

        try:
            # Fonts - all sizes increased for better readability
            org_main_font = ImageFont.truetype("arialbd.ttf", 70)    # Main organization
            org_sub_font = ImageFont.truetype("ariali.ttf", 35)      # Sub text
            title_font = ImageFont.truetype("arialbd.ttf", 60)       # Certificate title
            name_font = ImageFont.truetype("arialbd.ttf", 110)       # Name - VERY BIG
            age_font = ImageFont.truetype("arialbd.ttf", 55)         # Age
            body_font = ImageFont.truetype("arial.ttf", 32)          # Body text
            bold_font = ImageFont.truetype("arialbd.ttf", 36)        # Bold body
            small_font = ImageFont.truetype("arial.ttf", 25)         # Small text
            reg_font = ImageFont.truetype("arial.ttf", 22)           # Registration
        except:
            org_main_font = ImageFont.load_default()
            org_sub_font = ImageFont.load_default()
            title_font = ImageFont.load_default()
            name_font = ImageFont.load_default()
            age_font = ImageFont.load_default()
            body_font = ImageFont.load_default()
            bold_font = ImageFont.load_default()
            small_font = ImageFont.load_default()
            reg_font = ImageFont.load_default()

        # Logo
        try:
            logo = Image.open("logo.jpeg").resize((150, 150))
            certificate.paste(logo, (50, 30))
        except:
            pass

        # Registration
        draw.text((220, 60), "REG: 202501331004127", font=reg_font, fill="#666666")

        # THREE ARROWS FAMILY - Big and Bold
        draw.text((220, 100), "THREE ARROWS FAMILY", font=org_main_font, fill="#1B4D3E")
        draw.text((220, 160), "A Shared Service Since 2014", font=org_sub_font, fill="#C5A028")

        # Certificate Title
        title = "CERTIFICATE OF DIGITAL DISCIPLINE"
        bbox = draw.textbbox((0, 0), title, font=title_font)
        title_width = bbox[2] - bbox[0]
        title_x = (width - title_width) // 2
        draw.text((title_x, 230), title, font=title_font, fill="#1B4D3E")

        # Decorative line
        draw.line([(width/2-250, 300), (width/2+250, 300)], fill="#C5A028", width=4)

        # FULL NAME with background
        name_upper = name.upper()
        bbox = draw.textbbox((0, 0), name_upper, font=name_font)
        name_width = bbox[2] - bbox[0]
        name_x = (width - name_width) // 2
        
        # Background for name (light blue)
        draw.rectangle([(name_x-30, 330), (name_x+name_width+30, 470)], 
                      fill="#E8F0FE", outline="#C5A028", width=3)
        draw.text((name_x, 400), name_upper, font=name_font, fill="#1B4D3E")

        # AGE with yellow background
        age_text = f"Age: {age} Years"
        bbox = draw.textbbox((0, 0), age_text, font=age_font)
        age_width = bbox[2] - bbox[0]
        age_x = (width - age_width) // 2
        
        draw.rectangle([(age_x-20, 490), (age_x+age_width+20, 560)], 
                      fill="#FFE5B4", outline="#C5A028", width=2)
        draw.text((age_x, 520), age_text, font=age_font, fill="#1B4D3E")

        today = datetime.date.today().strftime("%d %B %Y")

        # Pledge text
        pledge = "has made a conscious decision to embrace digital wellbeing and mindful living"
        bbox = draw.textbbox((0, 0), pledge, font=body_font)
        pledge_width = bbox[2] - bbox[0]
        pledge_x = (width - pledge_width) // 2
        draw.text((pledge_x, 600), pledge, font=body_font, fill="#333333")

        # Commitment header
        commitment = "✦ DIGITAL BALANCE COMMITMENT ✦"
        bbox = draw.textbbox((0, 0), commitment, font=bold_font)
        commit_width = bbox[2] - bbox[0]
        commit_x = (width - commit_width) // 2
        draw.text((commit_x, 660), commitment, font=bold_font, fill="#C5A028")

        # Benefits with bullet points
        benefits = [
            f"• Reducing daily screen time from {hours} to {max(1, hours-1)} hours daily",
            "• Prioritizing face-to-face conversations with family and friends",
            "• Engaging in physical activities and outdoor experiences",
            "• Reading books and learning new skills",
            "• Being fully present without digital distractions"
        ]
        
        y_position = 720
        for benefit in benefits:
            bbox = draw.textbbox((0, 0), benefit, font=body_font)
            benefit_width = bbox[2] - bbox[0]
            benefit_x = (width - benefit_width) // 2
            draw.text((benefit_x, y_position), benefit, font=body_font, fill="#333333")
            y_position += 40

        # Date and certificate info
        draw.text((100, height-80), f"Pledge Date: {today}", font=small_font, fill="#666666")
        draw.text((width-350, height-80), f"Certificate ID: 3AF-{datetime.datetime.now().strftime('%Y%m%d')}", font=small_font, fill="#666666")

        # Inspirational quote
        quote = "✨ Every minute away from the screen is an investment in yourself! ✨"
        bbox = draw.textbbox((0, 0), quote, font=bold_font)
        quote_width = bbox[2] - bbox[0]
        quote_x = (width - quote_width) // 2
        draw.text((quote_x, height-130), quote, font=bold_font, fill="#C5A028")

        # Save certificate
        buffer = io.BytesIO()
        certificate.save(buffer, format="JPEG", quality=100, optimize=True)
        buffer.seek(0)

        # Display
        st.markdown("## 🎉 YOUR CERTIFICATE IS READY")
        st.image(certificate, use_column_width=True)

        st.download_button(
            label="📥 DOWNLOAD CERTIFICATE (JPEG)",
            data=buffer,
            file_name=f"{name}_digital_discipline_certificate.jpg",
            mime="image/jpeg",
            use_container_width=True
        )

        st.balloons()
        st.success("✨ Congratulations on taking this important step towards digital wellness!")
