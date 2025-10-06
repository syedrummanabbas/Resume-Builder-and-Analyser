import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style.css")
st.title("Get In Touch With US!")
st.write("##")
 # Documentation: https://formsubmit.co/ !! change email !!
contact_form = """
    <form action="https://formsubmit.co/strawHatsdigipodium@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your Name" required>
    <input type="email" name="email" placeholder="Your Email" required>
    <textarea name="message" placeholder="Your message here" required></textarea>
    <button type="submit">Send</button>
    </form>
    
        """
    
left_col,right_col = st.columns(2)
with left_col:
    st.write(contact_form, unsafe_allow_html=True)
