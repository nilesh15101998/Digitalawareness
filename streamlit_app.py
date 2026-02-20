import streamlit as st
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import datetime
import io

st.set_page_config(page_title="Three Arrows Family", page_icon="🌿", layout="wide")

# -------------------- WEBSITE DESIGN --------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #1a2a6c, #b21f1f, #fdbb2d);
    background-attachment: fixed;
}

/* Header Styling */
.org-title {
    font-size: 48px;
    font-weight: 900;
    background: linear-gradient(45deg, #FFD700, #FFA500, #FF6347);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    font-family: 'Arial Black', sans-serif;
}

.tagline {
    font-size: 20px;
    color: #ffffff;
    margin-top: -5px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    font-style: italic;
}

/* Button */
.stButton > button {
    background: linear-gradient(90deg, #FFD700, #FFA500);
    color: #2c3e50;
    font-size: 22px;
    font-weight: bold;
    border-radius: 50px;
    height: 60px;
    width: 100%;
    border: none;
    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    transition: all 0.3s ease;
}

/* Form styling */
.stTextInput label, .stNumberInput label, .stSlider label {
    color: white !important;
    font-size: 18px !important;
    font-weight: 600 !important;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
}

.stTextInput input, .stNumberInput input {
    background: rgba(255,255,255,0.9);
    border: 2px solid #FFD700;
    border-radius: 10px;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# -------------------- HEADER --------------------
col1, col2 = st.columns([1,6])

with col1:
    st.image("logo.jpeg", width=120)

with col2:
    st.markdown("<div class='org-title'>THREE ARROWS FAMILY</div>", unsafe_allow_html=True)
    st.markdown("<div class='tagline'>Step Out of the Phone – Step Into Life 🌿</div>", unsafe_allow_html=True)

st.markdown("---")

# -------------------- FORM --------------------
with st.form(key="certificate_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("👤 FULL NAME", placeholder="Enter your name")
        hours = st.slider("📱 Daily Screen Time", 0, 15, 3)
    
    with col2:
        age = st.number_input("🎂 AGE", min_value=5, max_value=100, step=1)
        st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### ✅ DIGITAL WELLBEING PLEDGE")
    consent = st.checkbox("""
    I voluntarily commit to:
    • Reducing mindless scrolling • Building real connections
    • Improving daily focus • Living life intentionally
    """)
    
    generate = st.form_submit_button("🎨 CREATE CERTIFICATE")

# -------------------- CERTIFICATE DESIGN --------------------
if generate:

    if name == "" or not consent:
        st.error("⚠️ Please enter your name and accept the pledge.")
    else:
        # Create a beautiful certificate with larger dimensions
        width, height = 2000, 1400
        certificate = Image.new("RGB", (width, height), "#fef9e7")  # Warm cream
        draw = ImageDraw.Draw(certificate)

        # Elegant border with gold gradient effect
        for i in range(10):
            opacity = 255 - i * 20
            draw.rectangle([(i*2, i*2), (width-i*2, height-i*2)], 
                          outline=(212, 175, 55, opacity), width=3)

        # Decorative elements
        # Top and bottom gold bars
        draw.rectangle([(0, 0), (width, 60)], fill="#d4af37")
        draw.rectangle([(0, height-60), (width, height)], fill="#d4af37")
        
        # Side decorative patterns
        for y in range(100, height-100, 50):
            draw.ellipse([(20, y), (40, y+20)], fill="#d4af37", outline="#b8860b")

        # Try to use multiple fonts for better appearance
        try:
            # Try to load different fonts - you can add more font files
            fonts_available = []
            font_options = [
                "arialbd.ttf",  # Arial Bold
                "arial.ttf",
                "timesbd.ttf",  # Times Bold
                "times.ttf",
                "courbd.ttf",   # Courier Bold
                "cour.ttf"
            ]
            
            for font_name in font_options:
                try:
                    fonts_available.append(font_name)
                except:
                    continue
            
            # Use available fonts with fallbacks
            title_font = ImageFont.truetype("arialbd.ttf", 90) if "arialbd.ttf" in fonts_available else ImageFont.load_default()
            org_font = ImageFont.truetype("arialbd.ttf", 100) if "arialbd.ttf" in fonts_available else ImageFont.load_default()
            name_font = ImageFont.truetype("timesbd.ttf", 160) if "timesbd.ttf" in fonts_available else ImageFont.truetype("arialbd.ttf", 160)
            reg_font = ImageFont.truetype("arial.ttf", 35)
            age_font = ImageFont.truetype("arialbd.ttf", 80) if "arialbd.ttf" in fonts_available else ImageFont.load_default()
            body_font = ImageFont.truetype("arial.ttf", 55)
            bold_font = ImageFont.truetype("arialbd.ttf", 60) if "arialbd.ttf" in fonts_available else ImageFont.load_default()
        except:
            # Fallback to default
            title_font = ImageFont.load_default()
            org_font = ImageFont.load_default()
            name_font = ImageFont.load_default()
            reg_font = ImageFont.load_default()
            age_font = ImageFont.load_default()
            body_font = ImageFont.load_default()
            bold_font = ImageFont.load_default()

        # Load and place logo - bigger and centered
        try:
            logo = Image.open("logo.jpeg").resize((250, 250))
            certificate.paste(logo, (100, 80))
        except:
            pass

        # Registration number from logo
        draw.text((400, 150), "REG: 202501331004127", font=reg_font, fill="#666666")

        # Organization Name - VERY BIG AND BOLD at top center
        org_text = "THREE ARROWS FAMILY"
        bbox = draw.textbbox((0, 0), org_text, font=org_font)
        text_width = bbox[2] - bbox[0]
        org_x = (width - text_width) // 2
        # Add shadow effect
        draw.text((org_x+3, 203), org_text, font=org_font, fill="#888888")  # Shadow
        draw.text((org_x, 200), org_text, font=org_font, fill="#1b5e20")  # Main text

        # Certificate Title with style
        title = "CERTIFICATE OF DIGITAL DISCIPLINE"
        bbox = draw.textbbox((0, 0), title, font=title_font)
        title_width = bbox[2] - bbox[0]
        title_x = (width - title_width) // 2
        draw.text((title_x, 320), title, font=title_font, fill="#8B4513")

        # Decorative line under title
        draw.line([(width/2-300, 420), (width/2+300, 420)], fill="#d4af37", width=5)

        # USER NAME - EXTREMELY BIG AND BOLD
        name_upper = name.upper()
        bbox = draw.textbbox((0, 0), name_upper, font=name_font)
        name_width = bbox[2] - bbox[0]
        name_x = (width - name_width) // 2
        
        # Shadow for name
        draw.text((name_x+5, 485), name_upper, font=name_font, fill="#c0c0c0")
        # Main name in gold with gradient effect
        draw.text((name_x, 480), name_upper, font=name_font, fill="#FFD700")
        
        # Add a subtle glow effect
        for offset in range(1, 4):
            draw.text((name_x-offset, 480-offset), name_upper, font=name_font, 
                     fill=(255, 215, 0, 50), stroke_width=0)

        # Age - BIG and in different color
        age_text = f"Age: {age} Years"
        bbox = draw.textbbox((0, 0), age_text, font=age_font)
        age_width = bbox[2] - bbox[0]
        age_x = (width - age_width) // 2
        draw.text((age_x, 620), age_text, font=age_font, fill="#4169E1")  # Royal blue

        today = datetime.date.today().strftime("%d %B %Y")

        # Main pledge text
        pledge = "has made a conscious decision to embrace digital wellbeing and mindful living."
        bbox = draw.textbbox((0, 0), pledge, font=body_font)
        pledge_width = bbox[2] - bbox[0]
        pledge_x = (width - pledge_width) // 2
        draw.text((pledge_x, 720), pledge, font=body_font, fill="#2c3e50")

        # Digital Balance Commitment header
        commitment = "🌟 DIGITAL BALANCE COMMITMENT 🌟"
        bbox = draw.textbbox((0, 0), commitment, font=bold_font)
        commit_width = bbox[2] - bbox[0]
        commit_x = (width - commit_width) // 2
        draw.text((commit_x, 820), commitment, font=bold_font, fill="#228B22")

        # Benefits with bullet points
        benefits = [
            f"• By reducing daily screen time from {hours} hours, you're choosing to:",
            "• Reclaim precious moments for real connections",
            "• Nurture your mental clarity and focus",
            "• Discover joy in offline activities",
            "• Build stronger relationships with loved ones"
        ]
        
        y_position = 920
        for benefit in benefits:
            bbox = draw.textbbox((0, 0), benefit, font=body_font)
            benefit_width = bbox[2] - bbox[0]
            benefit_x = (width - benefit_width) // 2
            if benefit.startswith("• By"):
                draw.text((benefit_x, y_position), benefit, font=bold_font, fill="#8B4513")
            else:
                draw.text((benefit_x, y_position), benefit, font=body_font, fill="#2c3e50")
            y_position += 65

        # Inspirational quote
        quote = "✨ Every minute away from the screen is an investment in yourself! ✨"
        bbox = draw.textbbox((0, 0), quote, font=bold_font)
        quote_width = bbox[2] - bbox[0]
        quote_x = (width - quote_width) // 2
        draw.text((quote_x, 1220), quote, font=bold_font, fill="#d4af37")

        # Date and certificate number
        cert_number = f"Cert No: 3AF-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        draw.text((width-300, height-80), cert_number, font=reg_font, fill="#888888")
        draw.text((150, height-80), f"Date: {today}", font=reg_font, fill="#888888")

        # Save as JPEG with high quality
        buffer = io.BytesIO()
        certificate.save(buffer, format="JPEG", quality=95, optimize=True)
        buffer.seek(0)

        # Display certificate
        st.markdown("## 🎉 YOUR CERTIFICATE IS READY!")
        st.image(certificate, use_column_width=True)

        # Download button
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.download_button(
                label="📥 DOWNLOAD CERTIFICATE (JPEG)",
                data=buffer,
                file_name=f"{name}_digital_discipline_certificate.jpg",
                mime="image/jpeg",
                use_container_width=True
            )

        # Celebration
        st.balloons()
        st.success("""
        ### ✨ CONGRATULATIONS! ✨
        
        Your certificate has been created successfully. 
        Display it proudly as a reminder of your commitment to digital wellbeing!
        """)
        
        # Share achievement
        with st.expander("📱 Share Your Achievement"):
            st.markdown("""
            Share on social media:
            ```
            I just took the Digital Discipline pledge with Three Arrows Family! 
            Join me in stepping out of the phone and into life! 🌿
            #DigitalWellbeing #ThreeArrowsFamily #MindfulLiving
            ```
            """)
