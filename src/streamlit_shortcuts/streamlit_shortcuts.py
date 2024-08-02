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


def button(label: str, shortcut: str, on_click: Callable[..., None], *args, **kwargs):
    shortcut = {shortcut: label}
    add_keyboard_shortcuts(shortcut)
    return st.button(label=label, on_click=on_click, args=args, **kwargs)
