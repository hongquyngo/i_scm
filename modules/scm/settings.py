import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent.parent))

from utils.auth import AuthManager

# Now import other modules
from utils.scm.display_components import DisplayComponents
from utils.scm.session_state import initialize_session_state
from utils.scm.settings_manager import SettingsManager
from utils.scm.adjustments.time_adjustments import TimeAdjustmentManager
from utils.scm.adjustments.business_rules import BusinessRulesManager


# Authentication check
auth_manager = AuthManager()
if not auth_manager.check_session():
    st.warning("⚠️ Please login to access this page")
    st.stop()

# Initialize
initialize_session_state()
settings_manager = SettingsManager()

def show_settings():
    # Header
    DisplayComponents.show_page_header(
        title="Data Adjustment Settings",
        icon="⚙️",
        prev_page="pages/5_📌_PO_Suggestions.py",
        next_page=None
    )

    # Navigation in sidebar
    with st.sidebar:
        st.markdown("### 🧭 Navigation")
        
        # Navigation options
        nav_option = st.radio(
            "Select Category",
            ["⏱️ Time Adjustments", "📋 Allocation Rules", "📦 PO Rules"],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        # Quick stats
        st.markdown("### 📊 Quick Stats")
        
        if nav_option == "⏱️ Time Adjustments":
            rules_count = len(st.session_state.get('time_adjustment_rules', []))
            st.metric("Active Rules", rules_count)
            
            if rules_count > 0:
                st.caption(f"✅ {rules_count} time adjustment rules configured")
            else:
                st.caption("📝 No rules configured yet")
        
        elif nav_option == "📋 Allocation Rules":
            st.caption("📋 Configure allocation priorities")
        
        elif nav_option == "📦 PO Rules":
            st.caption("📦 Set purchase order parameters")

    # Main content area (full width)
    # Display content based on selection
    if nav_option == "⏱️ Time Adjustments":
        st.markdown("### ⏱️ Time Adjustments")
        st.markdown("Adjust dates for more accurate analysis")
        
        # Render time adjustments UI
        TimeAdjustmentManager.render_time_adjustments()
        
    elif nav_option == "📋 Allocation Rules":
        st.markdown("### 📋 Allocation Rules")
        st.markdown("Configure how inventory is allocated to orders")
        
        # Render allocation rules UI
        BusinessRulesManager.render_allocation_rules()
        
    elif nav_option == "📦 PO Rules":
        st.markdown("### 📦 PO Suggestion Rules")
        st.markdown("Configure purchase order generation parameters")
        
        # Render PO rules UI
        BusinessRulesManager.render_po_rules()

    # Footer
    st.markdown("---")
    st.caption("💡 Settings are applied to current session only. They will be saved when creating Allocation Plans or PO Suggestions.")

if __name__ == "__main__":
    # Run the main function to show the settings page
    show_settings()