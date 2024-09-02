from typing import Callable, Dict
import re

import streamlit.components.v1 as components
import streamlit as st


def normalize_key_combination(combo: str) -> str:
    """Normalize key combination to a standard format."""
    parts = combo.lower().split('+')
    modifiers = sorted([p for p in parts if p in ['ctrl', 'alt', 'shift', 'meta']])
    other_keys = [p for p in parts if p not in modifiers]
    return '+'.join(modifiers + other_keys)


def add_keyboard_shortcuts(key_combinations: Dict[str, str]):
    if not isinstance(key_combinations, dict):
        raise TypeError("key_combinations must be a dictionary")

    js_code = """
    <script>
    const doc = window.parent.document;
    const normalizeKey = (key) => {
        const special = {
            'control': 'ctrl',
            'command': 'meta',
            'cmd': 'meta',
            'option': 'alt',
            'return': 'enter'
        };
        return special[key.toLowerCase()] || key.toLowerCase();
    };
    const checkCombo = (e, combo) => {
        const parts = combo.split('+');
        const modifiers = parts.filter(p => ['ctrl', 'alt', 'shift', 'meta'].includes(p));
        const otherKeys = parts.filter(p => !modifiers.includes(p));
        return (
            modifiers.every(mod => e[`${mod}Key`]) &&
            !['ctrl', 'alt', 'shift', 'meta'].filter(mod => !modifiers.includes(mod)).some(mod => e[`${mod}Key`]) &&
            otherKeys.some(key => normalizeKey(e.key) === key)
        );
    };
    doc.addEventListener('keydown', function(e) {
    """

    for combo, button_text in key_combinations.items():
        normalized_combo = normalize_key_combination(combo)
        js_code += f"""
        if (checkCombo(e, '{normalized_combo}')) {{
            e.preventDefault();
            const button = Array.from(doc.querySelectorAll('button')).find(el => el.innerText.includes('{button_text}'));
            if (button) {{
                button.click();
            }}
        }}
        """

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
    args=None,
    **kwargs,
):
    """
    Creates a button with an optional keyboard shortcut and hint.

    Args:
        label (str): The text to display on the button.
        shortcut (str): The keyboard shortcut associated with the button.
        on_click (Callable[..., None]): The function to call when the button is clicked.
        hint (bool, optional): Whether to show the keyboard shortcut as a hint on the button label. Defaults to False.
        args (tuple, optional): Additional arguments to pass to the on_click function.
        **kwargs: Additional keyword arguments passed to the button function.

    Returns:
        The result of the Streamlit button function.

    Notes:
        This function integrates with Streamlit's `st.button` to display a button with an optional hint showing the associated
        keyboard shortcut.
    """
    key_combination = {shortcut: label}
    add_keyboard_shortcuts(key_combination)
    
    if hint:
        button_label = f"{label} `{shortcut}`"
    else:
        button_label = label
    
    if args:
        return st.button(label=button_label, on_click=on_click, args=args, **kwargs)
    else:
        return st.button(label=button_label, on_click=on_click, **kwargs)
