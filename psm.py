import streamlit as st
import re

st.set_page_config(page_title="Login Page", page_icon="🔑", layout="centered")

# Custom CSS
st.markdown(
    """
    <style>
    .stTextInput>div>div>input {
        border: 2px solid #4CAF50;
        border-radius: 5px;
        padding: 10px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 14px 20px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTitle {
        color: #3366cc;
        text-align: center;
    }
    .stWarning, .stError, .stSuccess, .stInfo {
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .stWarning {
        background-color: #fff3cd;
        border: 1px solid #ffeeba;
        color: #856404;
    }
    .stError {
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
    }
    .stSuccess {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
    }
    .stInfo {
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        color: #0c5460;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def check_password_strength(password):
    score = 0
    feedback = []

# Password Criteria
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("⚠️ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 2
    else:
        feedback.append("⚠️ Password should include uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("⚠️ Password should include at least one number.")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("⚠️ Password should include at least one special character (!@#$%^&*).")

    return score, feedback

# Main Heading
st.write("**PASSWORD STRENGTH METER**  \nIf the password meets the criteria, then the login attempt is successful.")
st.title("Login Page 🔐")

#Input Bars
username = st.text_input("Username", placeholder="Enter your username")
password = st.text_input("Password", type="password", placeholder="Enter your password")

if st.button("Login"):
    if not username:
        st.warning("⚠️ Please enter a username.")
    elif not password:
        st.warning("⚠️ Please enter a password.")
    else:
        score, feedback = check_password_strength(password)

#Login Success/Failed
        if score == 5:
            st.success("✔️ Login attempt successful!")
        else:
            st.error("❌ Login failed. Password does not meet criteria.")

#Password Efficiency
        if score <= 2:
            st.warning("❌ Weak Password")
        elif score <= 4:
            st.info("⚠️ Moderate Password")
        elif score == 5:
            st.success("✔️ Strong Password")

#Feedback
        if feedback:
            with st.expander("⬇️ Improve your password"):
                for item in feedback:
                    st.write(item)
