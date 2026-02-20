import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
from datetime import date

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Digital Wellness Commitment",
    page_icon="🏹",
    layout="centered"
)

# --- COLORS & STYLE ---
# Theme based on the reference image and logo
PRIMARY_COLOR = "#004e92"  # Deep Blue
SECONDARY_COLOR = "#d4af37" # Gold
BG_COLOR = "#fdfbf7"       # Off-white/Cream

st.markdown(f"""
    <style>
    .main {{
        background-color: {BG_COLOR};
    }}
    h1 {{
        color: {PRIMARY_COLOR};
        text-align: center;
    }}
    .stButton>button {{
        background-color: {PRIMARY_COLOR};
        color: white;
        border-radius: 20px;
        width: 100%;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
try:
    st.image("logo.png", width=150)
except FileNotFoundError:
    st.warning("⚠️ 'logo.png' not found. Please ensure it is in the same directory.")

st.title("Step Out of the Phone, Step Into Life")
st.write("Make a commitment today to reclaim your time and focus on real-life activities.")
st.markdown("---")

# --- INPUT FORM ---
with st.form("certificate_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name", placeholder="e.g., Rahul Sharma")
    with col2:
        age = st.number_input("Age", min_value=5, max_value=100, value=25)
    
    hours = st.slider("Current average hours spent scrolling daily?", 1, 12, 4)
    
    st.markdown(f"### The Commitment pledge")
    consent_text = f"I, hereby commit to reducing my daily social media scrolling from {hours} hours to less than **2 hours daily**, dedicating that time to real-life connections, goals, and service."
    st.info(consent_text)
    
    consent = st.checkbox("I accept this challenge and give my consent to generate this pledge certificate.")
    
    submitted = st.form_submit_button("✨ Generate My Certificate")


# --- CERTIFICATE GENERATION LOGIC ---
def generate_certificate(user_name, user_age, user_hours):
    # 1. Create Base Image (A4 Landscape-ish proportions)
    width, height = 1200, 850
    # Create cream background
    cert = Image.new('RGB', (width, height), BG_COLOR)
    draw = ImageDraw.Draw(cert)

    # 2. Draw Borders
    border_thickness = 30
    # Outer Gold Border
    draw.rectangle([(0, 0), (width, height)], outline=SECONDARY_COLOR, width=border_thickness)
    # Inner Thin Blue Border
    draw.rectangle([(border_thickness+10, border_thickness+10), (width-border_thickness-10, height-border_thickness-10)], outline=PRIMARY_COLOR, width=5)

    # 3. Load Fonts (with fallbacks for safety)
    try:
        # Adjust paths if your font filenames are different
        font_title = ImageFont.truetype("Roboto-Bold.ttf", 70)
        font_subtitle = ImageFont.truetype("Roboto-Bold.ttf", 30)
        font_name = ImageFont.truetype("GreatVibes-Regular.ttf", 130) # Fancy font for name
        font_body = ImageFont.truetype("Roboto-Bold.ttf", 35)
        font_small = ImageFont.truetype("Roboto-Bold.ttf", 25)
    except OSError:
        st.error("⚠️ Custom fonts not found. Using default ugly fonts. Please add Roboto-Bold.ttf and GreatVibes-Regular.ttf.")
        font_title = ImageFont.load_default()
        font_subtitle = ImageFont.load_default()
        font_name = ImageFont.load_default()
        font_body = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # 4. Place Elements using anchors for centering
    # (anchor='mm' means middle-middle alignment)

    # Place Logo at Top Center
    try:
        logo_img = Image.open("logo.png")
        # Resize logo to fit nicely
        logo_img.thumbnail((200, 200), Image.Resampling.LANCZOS)
        logo_w, logo_h = logo_img.size
        # Paste logo (using it as its own mask to keep transparency)
        cert.paste(logo_img, ((width - logo_w) // 2, 70), logo_img)
    except FileNotFoundError:
        draw.text((width//2, 100), "[LOGO MISSING]", fill="red", anchor="mm")

    # Main Heading
    draw.text((width//2, 330), "CERTIFICATE OF COMMITMENT", font=font_title, fill=PRIMARY_COLOR, anchor="mm")
    draw.text((width//2, 390), "Digital Wellness Initiative", font=font_subtitle, fill=SECONDARY_COLOR, anchor="mm")

    # Presented To
    draw.text((width//2, 470), "This pledge is proudly presented to", font=font_body, fill="black", anchor="mm")

    # The Name (Fancy Font)
    draw.text((width//2, 570), user_name, font=font_name, fill=PRIMARY_COLOR, anchor="mm")

    # The Commitment Text
    commitment_body = f"For acknowledging current usage of {user_hours} hours/day and committing to \nreduce screen time to prioritize real-life goals, society, and health."
    # Using multiline text drawing
    draw.multiline_text((width//2, 700), commitment_body, font=font_body, fill="black", anchor="mm", align="center")

    # Footer/Date
    today = date.today().strftime("%B %d, %Y")
    draw.text((200, 800), f"Date: {today}", font=font_small, fill="grey", anchor="mm")
    draw.text((width-200, 800), "Three Arrows Family Initiative", font=font_small, fill=SECONDARY_COLOR, anchor="mm")

    return cert


# --- MAIN APP FLOW ---
if submitted:
    if not name:
        st.error("Please enter your full name.")
    elif not consent:
        st.warning("You must agree to the commitment pledge to generate the certificate.")
    else:
        # Show a spinner while processing
        with st.spinner("Designing your certificate..."):
            # Call the generation function
            final_cert_image = generate_certificate(name, age, hours)
            
            # Convert PIL image to bytes for download
            buf = io.BytesIO()
            final_cert_image.save(buf, format="PNG")
            byte_im = buf.getvalue()

            st.success("Certificate Generated Successfully!")
            st.markdown("---")
            # Display the image
            st.image(final_cert_image, caption="Preview of your commitment", use_container_width=True)
            
            # Center the download button
            col_spacer1, col_btn, col_spacer2 = st.columns([1, 2, 1])
            with col_btn:
                st.download_button(
                    label="📩 Download Certificate (PNG)",
                    data=byte_im,
                    file_name=f"Digital_Wellness_Cert_{name.replace(' ', '_')}.png",
                    mime="image/png"
                )