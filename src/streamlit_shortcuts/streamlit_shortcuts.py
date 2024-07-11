from typing import Callable, Dict

import streamlit.components.v1 as components
import streamlit as st


# TODO add keyboard hint to button (streamlit-extras)
# https://arnaudmiribel.github.io/streamlit-extras/extras/keyboard_text/

def add_keyboard_shortcuts(key_combinations: Dict[str, str]):
    """
    Add keyboard shortcuts to trigger Streamlit buttons.

    Keys:
    - Modifiers: 'Ctrl', 'Shift', 'Alt'
    - Common Keys: 'Enter', 'Escape', 'Space'
    - Arrow Keys: 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown'

    Examples of Key Combinations:
    - 'Ctrl+Enter'
    - 'Shift+ArrowUp'
    - 'Alt+Space'

    For a complete list of key values, refer to:
    https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values

    Args:
        key_combinations (dict[str, str]): A dictionary mapping from key combination strings to button labels.
    """
    js_code = """
    <script>
    const doc = window.parent.document;
    doc.addEventListener('keydown', function(e) {"""

    for combo, button_text in key_combinations.items():
        combo_parts = combo.split('+')
        condition_parts = [
            f"e.{part.lower()}Key" if part in ['Ctrl', 'Shift', 'Alt']
            else f"e.key === '{part}'"
            for part in combo_parts
        ]
        condition_str = ' && '.join(condition_parts)

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


def button(label: str, shortcut: str, on_click: Callable[..., None]):
    shortcut={shortcut: label}
    st.button(label=label, on_click=on_click)
    add_keyboard_shortcuts(shortcut)
