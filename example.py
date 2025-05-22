import streamlit as st
from src.streamlit_shortcuts.streamlit_shortcuts import button, add_keyboard_shortcuts


def main():
    st.title("Streamlit Shortcuts Example")

    # Example 1: Simple button with shortcut
    if button(
        "Click me!", "ctrl+shift+c", lambda: st.success("Button clicked!"), hint=True
    ):
        st.write("Button was clicked")

    # Example 2: Multiple shortcuts
    add_keyboard_shortcuts({"Save": "ctrl+shift+s", "Open": "ctrl+shift+o"})

    if st.button("Save", key="Save"):
        st.success("Saved! (You can also press Ctrl+Shift+S)")

    if st.button("Open", key="Open"):
        st.success("Opened! (You can also press Ctrl+Shift+O)")

    # Example 3: Button with arguments
    def greet(name):
        st.success(f"Hello, {name}!")

    button("Greet", "ctrl+shift+g", greet, hint=True, args=("World",))

    # Example 4: Custom target_element and action
    st.caption("Press Shift+F to focus on the text input field below.")
    title = st.text_input("Email addresss", placeholder="user@domain.com", key="movietitle", help="This example makes use of the `target_element` and `action` parameters")
    add_keyboard_shortcuts({"movietitle": "shift+f"}, target_element="input", action="focus()")

    # Button with shortcut to show a message with a link
    def open_link_message():
        st.write("If you want to use streamlit-shortcut in your projects, visit:")
        st.markdown(
            '<a href="https://github.com/adriangalilea/streamlit-shortcuts" target="_blank">Streamlit Shortcuts GitHub</a>',
            unsafe_allow_html=True,
        )

    button("Learn More", "ctrl+shift+l", open_link_message, hint=True)

    st.write("Try using the keyboard shortcuts!")


if __name__ == "__main__":
    main()
