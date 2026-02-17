import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from datetime import datetime
import base64

def create_certificate(name: str, age: int) -> BytesIO:
    """Generate a digital awareness certificate as an image."""
    
    # Certificate dimensions
    width, height = 1200, 850
    
    # Create certificate with gradient-like background
    certificate = Image.new('RGB', (width, height), '#FFFEF7')
    draw = ImageDraw.Draw(certificate)
    
    # Draw decorative border
    border_color = '#1E3A5F'
    draw.rectangle([20, 20, width-20, height-20], outline=border_color, width=3)
    draw.rectangle([35, 35, width-35, height-35], outline='#D4AF37', width=2)
    draw.rectangle([45, 45, width-45, height-45], outline=border_color, width=1)
    
    # Draw corner decorations
    corner_size = 40
    corners = [(50, 50), (width-90, 50), (50, height-90), (width-90, height-90)]
    for x, y in corners:
        draw.rectangle([x, y, x+corner_size, y+corner_size], outline='#D4AF37', width=2)
    
    # Try to use a nice font, fall back to default if not available
    try:
        title_font = ImageFont.truetype("arial.ttf", 52)
        subtitle_font = ImageFont.truetype("arial.ttf", 28)
        name_font = ImageFont.truetype("arialbd.ttf", 44)
        text_font = ImageFont.truetype("arial.ttf", 22)
        small_font = ImageFont.truetype("arial.ttf", 18)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = title_font
        name_font = title_font
        text_font = title_font
        small_font = title_font
    
    # Header decoration
    draw.rectangle([100, 80, width-100, 85], fill='#D4AF37')
    
    # Title
    title = "CERTIFICATE"
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    draw.text(((width - title_width) // 2, 110), title, fill='#1E3A5F', font=title_font)
    
    # Subtitle
    subtitle = "of Digital Awareness"
    subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    draw.text(((width - subtitle_width) // 2, 175), subtitle, fill='#4A6FA5', font=subtitle_font)
    
    # Decorative line
    draw.rectangle([100, 225, width-100, 228], fill='#D4AF37')
    
    # "This is to certify that"
    certify_text = "This is to certify that"
    certify_bbox = draw.textbbox((0, 0), certify_text, font=text_font)
    certify_width = certify_bbox[2] - certify_bbox[0]
    draw.text(((width - certify_width) // 2, 270), certify_text, fill='#333333', font=text_font)
    
    # Name
    name_bbox = draw.textbbox((0, 0), name, font=name_font)
    name_width = name_bbox[2] - name_bbox[0]
    name_x = (width - name_width) // 2
    draw.text((name_x, 320), name, fill='#1E3A5F', font=name_font)
    
    # Underline for name
    draw.line([name_x - 20, 380, name_x + name_width + 20, 380], fill='#D4AF37', width=2)
    
    # Age
    age_text = f"Age: {age} years"
    age_bbox = draw.textbbox((0, 0), age_text, font=text_font)
    age_width = age_bbox[2] - age_bbox[0]
    draw.text(((width - age_width) // 2, 400), age_text, fill='#555555', font=text_font)
    
    # Pledge text
    pledge_lines = [
        "has taken the Digital Awareness Pledge and",
        "solemnly commits to the following:"
    ]
    
    y_pos = 460
    for line in pledge_lines:
        line_bbox = draw.textbbox((0, 0), line, font=text_font)
        line_width = line_bbox[2] - line_bbox[0]
        draw.text(((width - line_width) // 2, y_pos), line, fill='#333333', font=text_font)
        y_pos += 35
    
    # Commitment box
    draw.rectangle([150, 540, width-150, 620], outline='#1E3A5F', width=2, fill='#F5F5DC')
    
    commitment = '"I pledge to limit my social media usage'
    commitment2 = 'to no more than 3 hours per day."'
    
    commit_bbox = draw.textbbox((0, 0), commitment, font=text_font)
    commit_width = commit_bbox[2] - commit_bbox[0]
    draw.text(((width - commit_width) // 2, 555), commitment, fill='#1E3A5F', font=text_font)
    
    commit2_bbox = draw.textbbox((0, 0), commitment2, font=text_font)
    commit2_width = commit2_bbox[2] - commit2_bbox[0]
    draw.text(((width - commit2_width) // 2, 585), commitment2, fill='#1E3A5F', font=text_font)
    
    # Date
    current_date = datetime.now().strftime("%B %d, %Y")
    date_text = f"Issued on: {current_date}"
    date_bbox = draw.textbbox((0, 0), date_text, font=small_font)
    date_width = date_bbox[2] - date_bbox[0]
    draw.text(((width - date_width) // 2, 660), date_text, fill='#555555', font=small_font)
    
    # Signature line
    draw.line([width//2 - 120, 750, width//2 + 120, 750], fill='#333333', width=1)
    sig_text = "Digital Signature"
    sig_bbox = draw.textbbox((0, 0), sig_text, font=small_font)
    sig_width = sig_bbox[2] - sig_bbox[0]
    draw.text(((width - sig_width) // 2, 760), sig_text, fill='#555555', font=small_font)
    
    # Certificate ID
    cert_id = f"Certificate ID: DA-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    cert_bbox = draw.textbbox((0, 0), cert_id, font=small_font)
    draw.text((60, height - 60), cert_id, fill='#888888', font=small_font)
    
    # Footer decoration
    draw.rectangle([100, height-45, width-100, height-42], fill='#D4AF37')
    
    # Save to BytesIO
    img_buffer = BytesIO()
    certificate.save(img_buffer, format='PNG', quality=95)
    img_buffer.seek(0)
    
    return img_buffer


def main():
    st.set_page_config(
        page_title="Digital Awareness Certificate",
        page_icon="📜",
        layout="centered"
    )
    
    # Custom CSS
    st.markdown("""
        <style>
        .main-header {
            text-align: center;
            color: #1E3A5F;
            margin-bottom: 30px;
        }
        .stButton > button {
            background-color: #1E3A5F;
            color: white;
            width: 100%;
            padding: 10px;
            font-size: 18px;
            border-radius: 10px;
        }
        .stButton > button:hover {
            background-color: #2E5A8F;
        }
        .success-box {
            background-color: #D4EDDA;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            margin: 20px 0;
        }
        .info-box {
            background-color: #E7F3FF;
            padding: 15px;
            border-radius: 10px;
            margin: 10px 0;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown("<h1 class='main-header'>📜 Digital Awareness Certificate</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>Take the pledge for responsible social media usage</p>", unsafe_allow_html=True)
    
    st.divider()
    
    # Initialize session state
    if 'certificate_generated' not in st.session_state:
        st.session_state.certificate_generated = False
        st.session_state.certificate_data = None
    
    # Form
    with st.form("certificate_form"):
        st.subheader("📝 Enter Your Details")
        
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input(
                "Full Name",
                placeholder="Enter your full name",
                help="This name will appear on your certificate"
            )
        
        with col2:
            age = st.number_input(
                "Age",
                min_value=5,
                max_value=120,
                value=18,
                help="Your current age"
            )
        
        st.divider()
        
        # Pledge section
        st.subheader("🤝 Digital Awareness Pledge")
        
        st.markdown("""
            <div class='info-box'>
            <strong>By checking the box below, you solemnly pledge:</strong>
            <br><br>
            <em>"I commit to limiting my social media usage to no more than <strong>3 hours per day</strong>. 
            I understand that excessive social media use can affect my mental health, productivity, 
            and real-world relationships. I will strive to maintain a healthy digital balance."</em>
            </div>
        """, unsafe_allow_html=True)
        
        consent = st.checkbox(
            "✅ I take this pledge and commit to limiting my social media usage to 3 hours or less per day.",
            help="You must accept this pledge to generate your certificate"
        )
        
        submitted = st.form_submit_button("🎓 Generate My Certificate", use_container_width=True)
        
        if submitted:
            if not name.strip():
                st.error("⚠️ Please enter your name.")
            elif not consent:
                st.error("⚠️ Please accept the pledge to generate your certificate.")
            else:
                with st.spinner("🎨 Creating your certificate..."):
                    certificate_buffer = create_certificate(name.strip(), age)
                    st.session_state.certificate_generated = True
                    st.session_state.certificate_data = certificate_buffer
                    st.session_state.user_name = name.strip()
    
    # Display certificate if generated
    if st.session_state.certificate_generated and st.session_state.certificate_data:
        st.divider()
        
        st.markdown("""
            <div class='success-box'>
            <h3>🎉 Congratulations!</h3>
            <p>Your Digital Awareness Certificate has been generated successfully!</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Reset buffer position
        st.session_state.certificate_data.seek(0)
        
        # Display certificate preview
        st.subheader("📄 Your Certificate Preview")
        st.image(st.session_state.certificate_data, use_container_width=True)
        
        # Reset buffer position for download
        st.session_state.certificate_data.seek(0)
        
        # Download button
        st.download_button(
            label="📥 Download Certificate (PNG)",
            data=st.session_state.certificate_data,
            file_name=f"Digital_Awareness_Certificate_{st.session_state.user_name.replace(' ', '_')}.png",
            mime="image/png",
            use_container_width=True
        )
        
        # Reset button
        if st.button("🔄 Create Another Certificate", use_container_width=True):
            st.session_state.certificate_generated = False
            st.session_state.certificate_data = None
            st.rerun()
    
    # Footer
    st.divider()
    st.markdown("""
        <p style='text-align: center; color: #888; font-size: 12px;'>
        🌐 Digital Awareness Initiative | Promoting Responsible Social Media Usage<br>
        Made with ❤️ for a healthier digital lifestyle
        </p>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
