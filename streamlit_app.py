import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import datetime
import io

st.set_page_config(page_title="Three Arrows Family", page_icon="🌿", layout="wide")

# -------------------- WEBSITE DESIGN --------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #6b8cff 100%);
    background-attachment: fixed;
}

/* Header Styling */
.org-title {
    font-size: 42px;
    font-weight: 800;
    background: linear-gradient(45deg, #FFD700, #FFA500);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
}

.tagline {
    font-size: 18px;
    color: #ffffff;
    margin-top: -5px;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
}

/* Button */
.stButton > button {
    background: linear-gradient(90deg, #FFD700, #FFA500);
    color: #2c3e50;
    font-size: 20px;
    font-weight: bold;
    border-radius: 50px;
    height: 55px;
    width: 100%;
    border: none;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    transition: all 0.3s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.3);
}

/* Form labels */
.stTextInput label, .stNumberInput label, .stSlider label {
    color: white !important;
    font-size: 16px !important;
    font-weight: 500 !important;
}

/* Consent checkbox */
.stCheckbox label {
    color: white !important;
    background: rgba(255,255,255,0.1);
    padding: 15px;
    border-radius: 10px;
    border-left: 4px solid #FFD700;
}

/* Form container */
[data-testid="stForm"] {
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(10px);
    padding: 30px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.2);
}

/* Success/Error messages */
.stAlert {
    border-radius: 10px;
    border-left: 4px solid #FFD700;
}
</style>
""", unsafe_allow_html=True)

# -------------------- HEADER (LOGO + NAME SAME ROW) --------------------
col1, col2 = st.columns([1,6])

with col1:
    st.image("logo.jpeg", width=110)

with col2:
    st.markdown("<div class='org-title'>Three Arrows Family</div>", unsafe_allow_html=True)
    st.markdown("<div class='tagline'>Step Out of the Phone – Step Into Life 🌿</div>", unsafe_allow_html=True)

st.markdown("---")

# -------------------- FORM --------------------
name = st.text_input("👤 Full Name")
age = st.number_input("🎂 Age", min_value=5, max_value=100)
hours = st.slider("📱 Daily Social Media & Reel Hours", 0, 15, 3)

st.markdown("### ✅ Consent Declaration")
consent = st.checkbox("""
I voluntarily pledge to:
• Reduce unnecessary scrolling  
• Improve discipline and confidence  
• Engage in real-life activities  
• Set meaningful life goals  
""")

generate = st.button("🌿 Generate Certificate")

# -------------------- CERTIFICATE DESIGN --------------------
if generate:

    if name == "" or not consent:
        st.error("Please enter your name and accept consent.")
    else:
        # Reduced dimensions from 1800x1200 to 1500x1000
        width, height = 1500, 1000
        certificate = Image.new("RGB", (width, height), "#faf7f2")  # Cream background
        draw = ImageDraw.Draw(certificate)

        # Border with increased margin for more content space
        margin = 120
        draw.rectangle([(margin, margin), (width-margin, height-margin)], outline="#d4af37", width=2)
        
        # Decorative corner elements
        corner_length = 30
        # Top-left corner
        draw.line([(margin, margin), (margin+corner_length, margin)], fill="#d4af37", width=2)
        draw.line([(margin, margin), (margin, margin+corner_length)], fill="#d4af37", width=2)
        # Top-right corner
        draw.line([(width-margin, margin), (width-margin-corner_length, margin)], fill="#d4af37", width=2)
        draw.line([(width-margin, margin), (width-margin, margin+corner_length)], fill="#d4af37", width=2)
        # Bottom-left corner
        draw.line([(margin, height-margin), (margin+corner_length, height-margin)], fill="#d4af37", width=2)
        draw.line([(margin, height-margin), (margin, height-margin-corner_length)], fill="#d4af37", width=2)
        # Bottom-right corner
        draw.line([(width-margin, height-margin), (width-margin-corner_length, height-margin)], fill="#d4af37", width=2)
        draw.line([(width-margin, height-margin), (width-margin, height-margin-corner_length)], fill="#d4af37", width=2)

        try:
            # Adjusted font sizes for new dimensions
            title_font = ImageFont.truetype("arial.ttf", 55)
            org_font = ImageFont.truetype("arial.ttf", 45)
            name_font = ImageFont.truetype("arial.ttf", 80)  # Reduced from 130
            reg_font = ImageFont.truetype("arial.ttf", 25)
            age_font = ImageFont.truetype("arial.ttf", 40)
            body_font = ImageFont.truetype("arial.ttf", 35)
            small_font = ImageFont.truetype("arial.ttf", 30)
        except:
            title_font = ImageFont.load_default()
            org_font = ImageFont.load_default()
            name_font = ImageFont.load_default()
            reg_font = ImageFont.load_default()
            age_font = ImageFont.load_default()
            body_font = ImageFont.load_default()
            small_font = ImageFont.load_default()

        # Load Logo - Properly sized and positioned
        logo = Image.open("logo.jpeg").resize((180, 180))  # Reduced from 240
        certificate.paste(logo, (150, 80))  # Adjusted position

        # Registration Number (from logo text)
        draw.text((350, 135),
                  "Reg: 202501331004127",
                  font=reg_font,
                  fill="#666666")

        # Organization Name - Properly positioned
        org_text = "THREE ARROWS FAMILY"
        bbox = draw.textbbox((0, 0), org_text, font=org_font)
        text_width = bbox[2] - bbox[0]
        org_x = (width - text_width) // 2  # Center horizontally
        draw.text((org_x, 160),
                  org_text,
                  font=org_font,
                  fill="#2c5f2d",
                  stroke_width=1,
                  stroke_fill="#1a3f1a")

        # Certificate Title
        title = "Certificate of Digital Discipline"
        draw.text((width/2, 250),
                  title,
                  font=title_font,
                  fill="#2c5f2d",
                  anchor="mm")
        
        # Decorative line under title
        draw.line([(width/2-200, 290), (width/2+200, 290)], fill="#d4af37", width=2)

        # User Name - Big and Bold but properly sized
        name_upper = name.upper()
        draw.text((width/2, 370),
                  name_upper,
                  font=name_font,
                  fill="#b8860b",
                  anchor="mm",
                  stroke_width=2,
                  stroke_fill="#8b6910")

        # Age
        draw.text((width/2, 430),
                  f"Age: {age} Years",
                  font=age_font,
                  fill="#1e4b8c",
                  anchor="mm")

        today = datetime.date.today().strftime("%d %B %Y")

        # Main body text
        intro_text = "has made a conscious decision to embrace digital wellbeing and mindful living"
        draw.multiline_text((width/2, 500),
                            intro_text,
                            font=body_font,
                            fill="#2c3e50",
                            anchor="mm",
                            align="center",
                            spacing=5)

        # Digital Balance Commitment Header
        draw.text((width/2, 570),
                  "Digital Balance Commitment",
                  font=body_font,
                  fill="#6b8e23",
                  anchor="mm")

        # Benefits text
        benefits = f"""By reducing daily screen time from {hours} hours, you're choosing to:

• Reclaim precious moments for real connections
• Nurture your mental clarity and focus
• Discover joy in offline activities
• Build stronger relationships with loved ones"""

        draw.multiline_text((width/2, 680),
                            benefits,
                            font=small_font,
                            fill="#2c3e50",
                            anchor="mm",
                            align="center",
                            spacing=8)

        # Inspirational quote
        quote = "✨ Every minute away from the screen is an investment in yourself! ✨"
        draw.text((width/2, 850),
                  quote,
                  font=small_font,
                  fill="#b8860b",
                  anchor="mm")

        # Certificate number and date at bottom
        cert_number = f"Cert No: 3AF-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        draw.text((width-200, height-70),
                  cert_number,
                  font=reg_font,
                  fill="#a9a9a9",
                  anchor="mm")

        draw.text((200, height-70),
                  f"Date: {today}",
                  font=reg_font,
                  fill="#a9a9a9",
                  anchor="mm")

        # Save PNG
        buffer = io.BytesIO()
        certificate.save(buffer, format="PNG")
        buffer.seek(0)

        st.markdown("## 🎉 Your Certificate")
        st.image(certificate, use_column_width=True)

        st.download_button(
            label="📥 Download Certificate (PNG)",
            data=buffer,
            file_name=f"{name}_digital_discipline_certificate.png",
            mime="image/png"
        )

        st.balloons()
        st.success("""
        ✨ Certificate Generated Successfully! 
        
        Remember: Your journey to digital wellbeing starts today. 
        Every mindful moment away from the screen is a victory! 🌿
        """)
