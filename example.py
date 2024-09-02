import streamlit as st
from src.streamlit_shortcuts.streamlit_shortcuts import button, add_keyboard_shortcuts

def main():
    st.title("Streamlit Shortcuts Example")

    # Example 1: Simple button with shortcut
    if button("Click me!", "ctrl+c", lambda: st.success("Button clicked!"), hint=True):
        st.write("Button was clicked")

    # Example 2: Multiple shortcuts
    add_keyboard_shortcuts({
        "ctrl+s": "Save",
        "ctrl+o": "Open"
    })

    if st.button("Save"):
        st.success("Saved! (You can also press Ctrl+S)")

    if st.button("Open"):
        st.success("Opened! (You can also press Ctrl+O)")

    # Example 3: Button with arguments
    def greet(name):
        st.success(f"Hello, {name}!")

    button("Greet", "ctrl+g", greet, hint=True, args=("World",))

    st.write("Try using the keyboard shortcuts!")

if __name__ == "__main__":
    main()
