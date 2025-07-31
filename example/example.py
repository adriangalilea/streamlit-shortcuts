import streamlit as st
from streamlit_shortcuts import shortcut_button, add_shortcuts


st.title("⌨️ Streamlit Shortcuts Demo")

# Demo 1: Easy mode - shortcut_button

col1, col2, col3 = st.columns(3)

# Initialize saved data in session state
if "saved_data" not in st.session_state:
    st.session_state.saved_data = {"name": "John Doe", "email": "john@example.com"}
if "form_data" not in st.session_state:
    st.session_state.form_data = {"name": "", "email": ""}

with col1:
    if shortcut_button("⚡ Save", "ctrl+shift+s"):
        st.session_state.saved_data = st.session_state.form_data.copy()
        st.success("Saved!")

with col2:
    if shortcut_button("📂 Load", "ctrl+shift+o"):
        st.session_state.form_data = st.session_state.saved_data.copy()
        st.info("Loaded saved data!")
        st.rerun()

with col3:
    if shortcut_button("🗑️ Delete", "ctrl+shift+d"):
        st.session_state.form_data = {"name": "", "email": ""}
        st.warning("Cleared!")
        st.rerun()

# Demo 2: Power mode - works with ANY widget

# Use session state for form fields
st.write("**Name** — `Ctrl+Shift+N` to focus")
st.session_state.form_data["name"] = st.text_input(
    "Your name",
    key="name",
    value=st.session_state.form_data.get("name", ""),
    label_visibility="collapsed",
)

st.write("**Email** — `Ctrl+Shift+E` to focus")
st.session_state.form_data["email"] = st.text_input(
    "Email",
    key="email",
    value=st.session_state.form_data.get("email", ""),
    label_visibility="collapsed",
)

if shortcut_button(
    "Submit", "ctrl+shift+enter", key="submit", use_container_width=True
):
    name = st.session_state.form_data.get("name", "")
    email = st.session_state.form_data.get("email", "")
    if name and email:
        st.balloons()
        st.success(f"Welcome {name}! We'll email you at {email}")
    else:
        st.warning("Please fill in both fields!")

# Add shortcuts to ANY widget with a key
add_shortcuts(
    name="ctrl+shift+n",  # Focus name field
    email="ctrl+shift+e",  # Focus email field
)

st.divider()

# Demo 3: Multiple shortcuts - Vim motions + Arrow keys
st.subheader("🎮 Multiple Shortcuts per Button - Vim keys + Arrows")

st.markdown("""
- **h** / **←** : Move left
- **j** / **↓** : Move down  
- **k** / **↑** : Move up
- **l** / **→** : Move right
""")

# Initialize direction state
if "direction" not in st.session_state:
    st.session_state.direction = "Press a key..."

# Create a centered layout for arrow keys
_, col1, col2, col3, _ = st.columns([2, 1, 1, 1, 2])

with col2:
    if shortcut_button("⬆️", ["k", "arrowup"], hint=False, key="up_btn"):
        st.session_state.direction = "⬆️ UP"

_, col1, col2, col3, _ = st.columns([2, 1, 1, 1, 2])

with col1:
    if shortcut_button("⬅️", ["h", "arrowleft"], hint=False, key="left_btn"):
        st.session_state.direction = "⬅️ LEFT"

with col2:
    if shortcut_button("⬇️", ["j", "arrowdown"], hint=False, key="down_btn"):
        st.session_state.direction = "⬇️ DOWN"

with col3:
    if shortcut_button("➡️", ["l", "arrowright"], hint=False, key="right_btn"):
        st.session_state.direction = "➡️ RIGHT"

# Display direction
st.text_area("Direction", st.session_state.direction, height=100, disabled=True)


# Canary build - dev only
st.divider()
with st.expander("🐛 Canary Debug: Comparing button rendering (dev only)"):
    st.write("Regular st.button:")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.button("Primary", type="primary", key="test1")
    with c2:
        st.button("Secondary", type="secondary", key="test2")
    with c3:
        st.button("Tertiary", type="tertiary", key="test3")

    st.write("Our shortcut_button:")
    c1, c2, c3 = st.columns(3)
    with c1:
        shortcut_button("Primary", "x", type="primary", key="test4")
    with c2:
        shortcut_button("Secondary", "y", type="secondary", key="test5")
    with c3:
        shortcut_button("Tertiary", "z", type="tertiary", key="test6")
