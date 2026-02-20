import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import datetime
import io

st.set_page_config(page_title="Three Arrows Family", page_icon="🌿", layout="wide")

# -------------------- WEBSITE DESIGN --------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0B3B2A 0%, #1A4D3E 50%, #0F4C3A 100%);
}

/* Header Styling */
.org-title {
    font-size: 42px;
    font-weight: 900;
    color: #FFD700;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    font-family: 'Arial Black', sans-serif;
}

.tagline {
    font-size: 18px;
    color: #ECF0F1;
    font-style: italic;
}

/* Form Styling */
.stTextInput label, .stNumberInput label, .stSlider label {
    color: white !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}

/* Age input specific styling */
[data-testid="stNumberInput"] {
    background-color: #2E5C4E !important;
    border-radius: 10px;
    padding: 5px;
}

[data-testid="stNumberInput"] input {
    background-color: #FFE5B4 !important;
    color: #000000 !important;
    font-weight: bold !important;
    font-size: 18px !important;
}

/* Other inputs */
.stTextInput input, .stSlider {
    background-color: rgba(255,255,255,0.9) !important;
    border-radius: 10px;
}

/* Button */
.stButton > button {
    background: linear-gradient(90deg, #FFD700, #FFA500);
    color: #0B3B2A;
    font-size: 20px;
    font-weight: bold;
    border-radius: 10px;
    height: 50px;
    width: 100%;
    border: none;
    font-family: 'Arial Black', sans-serif;
}
</style>
""", unsafe_allow_html=True)

# -------------------- HEADER --------------------
col1, col2 = st.columns([1,6])

with col1:
    st.image("logo.jpeg", width=100)

with col2:
    st.markdown("<div class='org-title'>THREE ARROWS FAMILY</div>", unsafe_allow_html=True)
    st.markdown("<div class='tagline'>A Shared Service Since 2014</div>", unsafe_allow_html=True)

st.markdown("---")

# -------------------- FORM --------------------
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("👤 FULL NAME", placeholder="Enter your full name")
    hours = st.slider("📱 DAILY SCREEN TIME (HOURS)", 0, 15, 3)

with col2:
    age = st.number_input("🎂 AGE", min_value=5, max_value=100, step=1, value=25)
    st.markdown("<br>", unsafe_allow_html=True)

st.markdown("### 📝 DIGITAL WELLBEING PLEDGE")
consent = st.checkbox("""
I voluntarily commit to reducing screen time and embracing mindful living
""")

generate = st.button("🎨 GENERATE CERTIFICATE")

# -------------------- CERTIFICATE DESIGN --------------------
if generate:

    if name == "" or not consent:
        st.error("⚠️ Please enter your name and accept the pledge.")
    else:
        # OPTIMAL DIMENSIONS - Perfect for viewing and printing
        width, height = 1200, 800
        certificate = Image.new("RGB", (width, height), "#FDF5E6")  # Old lace background
        draw = ImageDraw.Draw(certificate)

        # Simple, clean border
        draw.rectangle([(20, 20), (width-20, height-20)], outline="#C5A028", width=3)
        
        # Top and bottom decorative lines
        draw.rectangle([(40, 10), (width-40, 15)], fill="#C5A028")
        draw.rectangle([(40, height-15), (width-40, height-10)], fill="#C5A028")

        # Load fonts with specific sizes for readability
        try:
            # Title fonts
            header_font = ImageFont.truetype("arialbd.ttf", 36)  # Bold for headers
            org_font = ImageFont.truetype("arialbd.ttf", 42)     # Organization name
            name_font = ImageFont.truetype("arialbd.ttf", 54)    # User name - Big but readable
            sub_font = ImageFont.truetype("arial.ttf", 28)       # Subtitles
            reg_font = ImageFont.truetype("arial.ttf", 20)       # Registration
            body_font = ImageFont.truetype("arial.ttf", 24)      # Body text
            age_font = ImageFont.truetype("arialbd.ttf", 32)     # Age
        except:
            header_font = ImageFont.load_default()
            org_font = ImageFont.load_default()
            name_font = ImageFont.load_default()
            sub_font = ImageFont.load_default()
            reg_font = ImageFont.load_default()
            body_font = ImageFont.load_default()
            age_font = ImageFont.load_default()

        # Logo - Properly sized
        try:
            logo = Image.open("logo.jpeg").resize((120, 120))
            certificate.paste(logo, (50, 40))
        except:
            pass

        # Registration Number
        draw.text((200, 70), "REG: 202501331004127", font=reg_font, fill="#666666")

        # Organization Name - Clean and bold
        draw.text((200, 100), "THREE ARROWS FAMILY", font=org_font, fill="#1B4D3E")
        
        # "A Shared Service Since 2014"
        draw.text((200, 145), "A Shared Service Since 2014", font=sub_font, fill="#C5A028")

        # Certificate Title
        title = "CERTIFICATE OF DIGITAL DISCIPLINE"
        # Center the title
        bbox = draw.textbbox((0, 0), title, font=header_font)
        title_width = bbox[2] - bbox[0]
        title_x = (width - title_width) // 2
        draw.text((title_x, 200), title, font=header_font, fill="#1B4D3E")

        # Horizontal line
        draw.line([(width/2-200, 250), (width/2+200, 250)], fill="#C5A028", width=2)

        # User Name - BIG and CLEAR
        name_upper = name.upper()
        bbox = draw.textbbox((0, 0), name_upper, font=name_font)
        name_width = bbox[2] - bbox[0]
        name_x = (width - name_width) // 2
        draw.text((name_x, 280), name_upper, font=name_font, fill="#000000")

        # Age with background color
        age_text = f"Age: {age} Years"
        bbox = draw.textbbox((0, 0), age_text, font=age_font)
        age_width = bbox[2] - bbox[0]
        age_x = (width - age_width) // 2
        
        # Draw background for age (light yellow)
        draw.rectangle([(age_x-10, 340), (age_x+age_width+10, 390)], 
                      fill="#FFE5B4", outline="#C5A028", width=1)
        draw.text((age_x, 360), age_text, font=age_font, fill="#1B4D3E")

        # Pledge text
        pledge = "has made a conscious decision to embrace digital wellbeing and mindful living"
        bbox = draw.textbbox((0, 0), pledge, font=body_font)
        pledge_width = bbox[2] - bbox[0]
        pledge_x = (width - pledge_width) // 2
        draw.text((pledge_x, 430), pledge, font=body_font, fill="#333333")

        # Digital Balance Commitment
        commitment = "• DIGITAL BALANCE COMMITMENT •"
        bbox = draw.textbbox((0, 0), commitment, font=header_font)
        commit_width = bbox[2] - bbox[0]
        commit_x = (width - commit_width) // 2
        draw.text((commit_x, 490), commitment, font=header_font, fill="#C5A028")

        today = datetime.date.today().strftime("%d %B %Y")

        # Benefits text
        benefits = [
            f"By reducing daily screen time from {hours} hours, you're choosing to:",
            "• Reclaim precious moments for real connections",
            "• Nurture your mental clarity and focus",
            "• Discover joy in offline activities",
            "• Build stronger relationships with loved ones"
        ]
        
        y_position = 550
        for i, benefit in enumerate(benefits):
            if i == 0:
                font = body_font
            else:
                font = sub_font
            bbox = draw.textbbox((0, 0), benefit, font=font)
            benefit_width = bbox[2] - bbox[0]
            benefit_x = (width - benefit_width) // 2
            draw.text((benefit_x, y_position), benefit, font=font, fill="#333333")
            y_position += 35

        # Date at bottom
        date_text = f"Pledge taken on: {today}"
        draw.text((100, height-60), date_text, font=reg_font, fill="#666666")

        # Certificate number
        cert_number = f"Cert No: 3AF-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        draw.text((width-350, height-60), cert_number, font=reg_font, fill="#666666")

        # Inspirational line
        quote = "Every minute away from the screen is an investment in yourself!"
        bbox = draw.textbbox((0, 0), quote, font=sub_font)
        quote_width = bbox[2] - bbox[0]
        quote_x = (width - quote_width) // 2
        draw.text((quote_x, height-100), quote, font=sub_font, fill="#C5A028")

        # Save as JPEG
        buffer = io.BytesIO()
        certificate.save(buffer, format="JPEG", quality=100, optimize=True)
        buffer.seek(0)

        # Display certificate
        st.markdown("## ✅ YOUR CERTIFICATE IS READY")
        st.image(certificate, use_column_width=True)

        # Download button
        st.download_button(
            label="📥 DOWNLOAD CERTIFICATE (JPEG)",
            data=buffer,
            file_name=f"{name}_digital_discipline_certificate.jpg",
            mime="image/jpeg",
            use_container_width=True
        )

        st.balloons()
        st.success("🎉 Certificate generated successfully! It's now ready to download and share.")
