import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import datetime
import io

st.set_page_config(page_title="Three Arrows Family", page_icon="🌿", layout="wide")

# -------------------- WEBSITE DESIGN --------------------
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

/* Form Styling */
.stTextInput label, .stNumberInput label, .stSlider label {
    color: white !important;
    font-size: 18px !important;
    font-weight: 700 !important;
}

/* Name input */
[data-testid="stTextInput"] input {
    background-color: #E8F0FE !important;
    border: 3px solid #FFD700 !important;
    border-radius: 8px;
    font-size: 18px !important;
    font-weight: bold !important;
    padding: 10px !important;
}

/* Age input */
[data-testid="stNumberInput"] input {
    background-color: #FFE5B4 !important;
    border: 3px solid #FFD700 !important;
    border-radius: 8px;
    font-size: 18px !important;
    font-weight: bold !important;
    padding: 10px !important;
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

# Consent Section
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
        # Certificate dimensions
        width, height = 1500, 1050
        certificate = Image.new("RGB", (width, height), "#FDF5E6")  # Old lace
        draw = ImageDraw.Draw(certificate)

        # Elegant border
        draw.rectangle([(30, 30), (width-30, height-30)], outline="#C5A028", width=5)
        draw.rectangle([(45, 45), (width-45, height-45)], outline="#F0C45A", width=2)
        
        # Corner decorations
        corner_len = 70
        corners = [(30,30), (width-30,30), (30,height-30), (width-30,height-30)]
        for x,y in corners:
            draw.ellipse([(x-10, y-10), (x+10, y+10)], fill="#C5A028")

        try:
            # Fonts - All sizes increased
            reg_font = ImageFont.truetype("arial.ttf", 28)
            org_font = ImageFont.truetype("arialbd.ttf", 65)  # Bold organization
            sub_font = ImageFont.truetype("ariali.ttf", 35)
            title_font = ImageFont.truetype("arialbd.ttf", 60)
            name_font = ImageFont.truetype("arialbd.ttf", 120)  # Very big name
            age_font = ImageFont.truetype("arialbd.ttf", 55)
            body_font = ImageFont.truetype("arial.ttf", 38)  # Bigger body text
            bold_font = ImageFont.truetype("arialbd.ttf", 42)
            small_font = ImageFont.truetype("arial.ttf", 30)
        except:
            reg_font = ImageFont.load_default()
            org_font = ImageFont.load_default()
            sub_font = ImageFont.load_default()
            title_font = ImageFont.load_default()
            name_font = ImageFont.load_default()
            age_font = ImageFont.load_default()
            body_font = ImageFont.load_default()
            bold_font = ImageFont.load_default()
            small_font = ImageFont.load_default()

        # Logo on LEFT (position 50, 40)
        try:
            logo = Image.open("logo.jpeg").resize((160, 160))
            certificate.paste(logo, (50, 40))
        except:
            pass

        # Registration number (top, aligned with logo)
        draw.text((230, 70), "REG: 2025013310014127", font=reg_font, fill="#666666")

        # THREE ARROWS FAMILY - CENTERED and BOLD
        org_text = "THREE ARROWS FAMILY"
        bbox = draw.textbbox((0, 0), org_text, font=org_font)
        org_width = bbox[2] - bbox[0]
        org_x = (width - org_width) // 2
        # Shadow effect
        draw.text((org_x+3, 103), org_text, font=org_font, fill="#888888")
        draw.text((org_x, 100), org_text, font=org_font, fill="#1B4D3E")

        # A Shared Service Since 2014 - Centered
        service_text = "A Shared Service Since 2014"
        bbox = draw.textbbox((0, 0), service_text, font=sub_font)
        service_width = bbox[2] - bbox[0]
        service_x = (width - service_width) // 2
        draw.text((service_x, 170), service_text, font=sub_font, fill="#C5A028")

        # Certificate Title - Centered
        title = "CERTIFICATE OF DIGITAL DISCIPLINE"
        bbox = draw.textbbox((0, 0), title, font=title_font)
        title_width = bbox[2] - bbox[0]
        title_x = (width - title_width) // 2
        draw.text((title_x, 240), title, font=title_font, fill="#1B4D3E")

        # Decorative line
        draw.line([(width/2-300, 310), (width/2+300, 310)], fill="#C5A028", width=4)

        # NAME WITH BOX - BIG and BOLD
        name_upper = name.upper()
        bbox = draw.textbbox((0, 0), name_upper, font=name_font)
        name_width = bbox[2] - bbox[0]
        name_height = bbox[3] - bbox[1]
        name_x = (width - name_width) // 2
        
        # Box around name (light blue background with border)
        box_padding = 40
        draw.rectangle([(name_x-box_padding, 350), 
                       (name_x+name_width+box_padding, 350+name_height+box_padding)], 
                      fill="#E8F0FE", outline="#C5A028", width=4)
        
        # Name text
        draw.text((name_x, 370), name_upper, font=name_font, fill="#1B4D3E")

        # AGE with yellow background
        age_text = f"Age: {age} Years"
        bbox = draw.textbbox((0, 0), age_text, font=age_font)
        age_width = bbox[2] - bbox[0]
        age_x = (width - age_width) // 2
        
        draw.rectangle([(age_x-20, 550), (age_x+age_width+20, 620)], 
                      fill="#FFE5B4", outline="#C5A028", width=3)
        draw.text((age_x, 580), age_text, font=age_font, fill="#1B4D3E")

        today = datetime.date.today().strftime("%d %B %Y")

        # Pledge text - BIGGER
        pledge = "has made a conscious decision to embrace digital wellbeing and mindful living"
        bbox = draw.textbbox((0, 0), pledge, font=body_font)
        pledge_width = bbox[2] - bbox[0]
        pledge_x = (width - pledge_width) // 2
        draw.text((pledge_x, 670), pledge, font=body_font, fill="#333333")

        # DIGITAL BALANCE COMMITMENT - BIGGER
        commitment = "✦ DIGITAL BALANCE COMMITMENT ✦"
        bbox = draw.textbbox((0, 0), commitment, font=bold_font)
        commit_width = bbox[2] - bbox[0]
        commit_x = (width - commit_width) // 2
        draw.text((commit_x, 750), commitment, font=bold_font, fill="#C5A028")

        # Benefits with bullet points - BIGGER TEXT
        benefits = [
            f"• Reducing daily screen time from {hours} to {max(1, hours-1)} hours daily",
            "• Prioritizing face-to-face conversations with family and friends",
            "• Engaging in physical activities and outdoor experiences",
            "• Reading books and learning new skills for personal growth",
            "• Being fully present without digital distractions"
        ]
        
        y_position = 820
        for benefit in benefits:
            bbox = draw.textbbox((0, 0), benefit, font=body_font)
            benefit_width = bbox[2] - bbox[0]
            benefit_x = (width - benefit_width) // 2
            draw.text((benefit_x, y_position), benefit, font=body_font, fill="#333333")
            y_position += 45

        # Bottom info
        draw.text((100, height-80), f"Date: {today}", font=small_font, fill="#666666")
        draw.text((width-350, height-80), f"ID: 3AF-{datetime.datetime.now().strftime('%Y%m%d')}", font=small_font, fill="#666666")

        # Inspirational quote
        quote = "✨ Every minute away from the screen is an investment in yourself! ✨"
        bbox = draw.textbbox((0, 0), quote, font=bold_font)
        quote_width = bbox[2] - bbox[0]
        quote_x = (width - quote_width) // 2
        draw.text((quote_x, height-120), quote, font=bold_font, fill="#C5A028")

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
        st.success("✨ Congratulations on your commitment to digital wellness!")
