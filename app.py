# app.py - iSCM Dashboard Main App

import streamlit as st
from utils.auth import AuthManager

# Page config
st.set_page_config(
    page_title="iSCM Dashboard",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize auth manager
auth_manager = AuthManager()

def show_login_page():
    """Display login page"""
    st.markdown("<h1 style='text-align: center;'>🏭 iSCM Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Intelligent Supply Chain Management</h3>", unsafe_allow_html=True)
    
    # Center the login form
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        with st.form("login_form"):
            st.subheader("🔐 Login")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            
            if st.form_submit_button("Login", use_container_width=True, type="primary"):
                if username and password:
                    success, user_info = auth_manager.authenticate(username, password)
                    if success:
                        auth_manager.login(user_info)
                        st.success("✅ Login successful!")
                        st.rerun()
                    else:
                        st.error("❌ Invalid username or password")
                else:
                    st.error("Please enter both username and password")

def show_main_page():
    """Display main page after login"""
    # Sidebar
    with st.sidebar:
        st.markdown(f"### 👤 Welcome, {auth_manager.get_user_display_name()}")
        st.markdown(f"**Role:** {st.session_state.get('user_role', 'N/A')}")
        st.markdown("---")
        
        if st.button("🚪 Logout", use_container_width=True):
            auth_manager.logout()
            st.rerun()
    
    # Main content
    st.markdown("<h1 style='text-align: center;'>🏭 Welcome to iSCM Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Your Intelligent Supply Chain Management System</h3>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Simple welcome message
    st.success(f"✅ You are successfully logged in as **{auth_manager.get_user_display_name()}**")
    
    st.info("📌 Use the navigation menu on the left to access different modules")

def main():
    """Main application entry point"""
    if not auth_manager.check_session():
        show_login_page()
    else:
        show_main_page()

if __name__ == "__main__":
    main()