import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import datetime
import io

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Three Arrows Family", page_icon="🌿", layout="wide")

# --- WEBSITE CSS STYLING ---
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f4c3a 0%, #1e6b4c 50%, #0d5e3f 100%);
}

.org-title {
    font-size: 48px;
    font-weight: 900;
    color: #FFD700;
    text-shadow: 3px 3px 6px rgba(0,0,0,0.5);
    font-family: 'Arial Black', sans-serif;
}

/* FIX: Name input text color visibility */
[data-testid="stTextInput"] input {
    background-color: #E8F0FE !important;
    color: #0f4c3a !important; /* Forces text to be dark green/visible */
    border: 3px solid #FFD700 !important;
    border-radius: 8px;
    font-size: 18px !important;
    font-weight: bold !important;
    padding: 10px !important;
}

[data-testid="stNumberInput"] input {
    background-color: #FFE5B4 !important;
    color: #0f4c3a !important;
    border: 3px solid #FFD700 !important;
    border-radius: 8px;
    font-size: 18px !important;
}

.stButton > button {
    background: linear-gradient(90deg, #FFD700, #FFA500);
    color: #0f4c3a;
    font-size: 24px;
    font-weight: 900;
    border-radius: 12px;
    height: 70px;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
col1, col2 = st.columns([1,6])
with col1:
    try:
        st.image("logo.jpeg", width=130)
    except:
        st.write("🏹")

with col2:
    st.markdown("<div class='org-title'>THREE ARROWS FAMILY</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:white;'>A Sacred Service Since 2014</p>", unsafe_allow_html=True)

# --- FORM ---
col_f1, col_f2 = st.columns(2)
with col_f1:
    name = st.text_input("👤 FULL NAME", placeholder="Enter your name here")
    hours = st.slider("📱 CURRENT SCREEN TIME (HRS)", 0, 15, 5)

with col_f2:
    age = st.number_input("🎂 AGE", min_value=5, max_value=100, value=25)

consent = st.checkbox("✅ I accept the Digital Wellbeing Pledge")
generate = st.button("🎨 GENERATE CERTIFICATE")

# --- CERTIFICATE LOGIC ---
if generate:
    if not name or not consent:
        st.error("Please fill in your name and accept the pledge.")
    else:
        width, height = 1500, 1100
        GOLD, DEEP_BLUE, CREAM = "#C5A028", "#1B4D3E", "#FDFBF7"
        cert = Image.new("RGB", (width, height), CREAM)
        draw = ImageDraw.Draw(cert)

        # Borders
        draw.rectangle([(25, 25), (width-25, height-25)], outline=GOLD, width=15)
        draw.rectangle([(45, 45), (width-45, height-45)], outline=DEEP_BLUE, width=3)

        # Fonts
        try:
            title_f = ImageFont.truetype("arialbd.ttf", 70)
            sub_f = ImageFont.truetype("ariali.ttf", 35)
            name_f = ImageFont.truetype("arialbd.ttf", 120)
            body_f = ImageFont.truetype("arial.ttf", 35)
            bold_f = ImageFont.truetype("arialbd.ttf", 40)
        except:
            title_f = sub_f = name_f = body_f = bold_f = ImageFont.load_default()

        # Logo
        try:
            logo = Image.open("logo.jpeg").resize((180, 180))
            cert.paste(logo, (width//2 - 90, 60))
        except:
            pass

        # Text Elements
        draw.text((width//2, 280), "THREE ARROWS FAMILY", font=title_f, fill=DEEP_BLUE, anchor="mm")
        draw.text((width//2, 340), "A Sacred Service Since 2014", font=sub_f, fill=GOLD, anchor="mm")
        draw.text((width//2, 420), "CERTIFICATE OF DIGITAL WELLNESS", font=title_f, fill=DEEP_BLUE, anchor="mm")

        # NAME (No Box)
        draw.text((width//2, 500), "This certificate is proudly presented to", font=body_f, fill="#666666", anchor="mm")
        draw.text((width//2, 600), name.upper(), font=name_f, fill=DEEP_BLUE, anchor="mm")
        draw.text((width//2, 680), f"Age: {age} Years", font=bold_f, fill=GOLD, anchor="mm")

        # BENEFITS SECTION
        draw.text((width//2, 760), "✦ RECOGNIZED BENEFITS OF THIS COMMITMENT ✦", font=bold_f, fill=DEEP_BLUE, anchor="mm")
        
        benefits = [
            "• Enhanced Mental Clarity and Focus on Life Goals",
            "• Improved Sleep Quality and Physical Energy Levels",
            "• Deepened Real-World Connections with Family and Society",
            "• Reduced Anxiety and Freedom from Mindless Scrolling",
            "• Increased Productivity and Time for Personal Growth"
        ]
        
        y_text = 810
        for line in benefits:
            draw.text((width//2, y_text), line, font=body_f, fill="#333333", anchor="mm")
            y_text += 45

        # Footer
        today = datetime.date.today().strftime("%d %B %Y")
        draw.text((width//2, 1040), f"Date: {today}  |  Verify at: www.threearrowsfamily.org.in", font=body_f, fill="#666666", anchor="mm")

        # Download
        buf = io.BytesIO()
        cert.save(buf, format="JPEG")
        st.image(cert, use_container_width=True)
        st.download_button("📥 DOWNLOAD CERTIFICATE", data=buf.getvalue(), file_name=f"Cert_{name}.jpg", mime="image/jpeg")
