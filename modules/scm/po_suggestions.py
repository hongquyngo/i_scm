# pages/5_📌_PO_Suggestions.py
import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent.parent))
from utils.auth import AuthManager

# Check authentication
auth_manager = AuthManager()
if not auth_manager.check_session():
    st.warning("⚠️ Please login to access this page")
    st.stop()

def show_po_suggestions():
    # === Header ===
    st.title("📌 PO Suggestions")
    st.markdown("---")

    # === Coming Soon Message ===
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown("""
        ## 🚀 Coming Soon!
        
        ### AI-Powered Purchase Order Recommendations
        
        We're building an intelligent system that will:
        
        #### 📊 **Smart Analysis**
        - Analyze demand patterns and forecast future needs
        - Calculate optimal order quantities (EOQ)
        - Consider lead times and safety stock requirements
        
        #### 🤖 **AI Features**
        - Machine learning-based demand prediction
        - Intelligent supplier selection
        - Automated PO generation from GAP analysis
        - Natural language queries for PO insights
        
        #### 🎯 **Key Benefits**
        - Reduce stockouts by 30%
        - Optimize inventory costs
        - Automate repetitive procurement tasks
        - Data-driven decision making
        
        ---
        
        **Expected Launch: Q4 2025**
        
        📧 Questions? Contact the SCM team
        """)
        
        # Simple beta signup
        with st.expander("🔔 Get notified when available"):
            email = st.text_input("Email for updates:", placeholder="your.email@company.com")
            if st.button("Notify Me", type="primary"):
                if email:
                    st.success("✅ We'll notify you when PO Suggestions launches!")
                else:
                    st.error("Please enter your email")

    # === Footer ===
    st.markdown("---")
    st.caption("SCM Control Center v1.0")

if __name__ == "__main__":
    # Run the main function to show the PO suggestions page
    show_po_suggestions()