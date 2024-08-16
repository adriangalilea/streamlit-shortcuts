from typing import Callable, Dict

import streamlit.components.v1 as components
import streamlit as st


def add_keyboard_shortcuts(key_combinations: Dict[str, str]):
    if not isinstance(key_combinations, dict):
        raise TypeError("key_combinations must be a dictionary")

    js_code = """
    <script>
    const doc = window.parent.document;
    doc.addEventListener('keydown', function(e) {"""

    for combo, button_text in key_combinations.items():
        combo_parts = combo.split("+")
        condition_parts = [
            (
                f"e.{part.lower()}Key"
                if part in ["Ctrl", "Shift", "Alt"]
                else f"e.key === '{part}'"
            )
            for part in combo_parts
        ]
        condition_str = " && ".join(condition_parts)

        js_code += f"""
        if ({condition_str}) {{
            const button = Array.from(doc.querySelectorAll('button')).find(el => el.innerText === '{button_text}');
            if (button) {{
                button.click();
            }}
        }}"""

    js_code += """
    });
    </script>
    """

    components.html(js_code, height=0, width=0)


def button(
    label: str,
    shortcut: str,
    on_click: Callable[..., None],
    hint=False,
    *args,
    **kwargs,
):
    """
    Creates a button with an optional keyboard shortcut and hint.

    Args:
        label (str): The text to display on the button.
        shortcut (str): The keyboard shortcut associated with the button.
        on_click (Callable[..., None]): The function to call when the button is clicked.
        hint (bool, optional): Whether to show the keyboard shortcut as a hint on the button label. Defaults to False.
        *args: Additional positional arguments passed to the button function.
        **kwargs: Additional keyword arguments passed to the button function.

    Returns:
        The result of the Streamlit button function.

    Notes:
        This function integrates with Streamlit's `st.button` to display a button with an optional hint showing the associated
        keyboard shortcut.
    """
    key_combination = {shortcut: label}
    add_keyboard_shortcuts(key_combination)
    if hint is False:
        return st.button(label=label, on_click=on_click, args=args, **kwargs)
    return st.button(
        label=label + f"`{shortcut}`", on_click=on_click, args=args, **kwargs
    )
