from typing import Callable, Dict

import streamlit.components.v1 as components
import streamlit as st

if "button_key_counter" not in st.session_state:
    st.session_state["button_key_counter"] = 1


def normalize_key_combination(combo: str) -> str:
    """Normalize key combination to a standard format."""
    parts = combo.lower().split("+")
    modifiers = sorted([p for p in parts if p in ["ctrl", "alt", "shift", "meta"]])
    other_keys = [p for p in parts if p not in modifiers]
    return "+".join(modifiers + other_keys)


def add_keyboard_shortcuts(
    keys_shortcuts_dict: Dict[str, str], target_element="button", action="click()"
):
    """add shortcuts

    Args:
        keys_shortcuts_dict (Dict[str, str]): A dictionary where keys are the streamlit id (key) of the target button
            and values are the keyboard shortcuts such as 'a', 'ctrl+shift+k' or 'cmd+enter'.
        target_element (str): The type of HTML element to target for the click event. Defaults to "button".
        action (str): The action to perform on the target element. Defaults to "click()".
            - calls element.`action` in JS, so action should be a method of the element along with any parameters.
    """
    if not isinstance(keys_shortcuts_dict, dict):
        raise TypeError("key_combinations must be a dictionary of key:shortcut pairs.")

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

    for key, shortcut in keys_shortcuts_dict.items():
        # to select the element, we find the div with the class 'st-key-{key}', then find the element within it
        normalized_combo = normalize_key_combination(shortcut)
        js_code += f"""
        if (checkCombo(e, '{normalized_combo}')) {{
            e.preventDefault();
            const container = doc.querySelector('.st-key-{key}');
            if (container) {{
                const element = container.querySelector('{target_element}');
                if (element) {{
                    element.{action};
                }}
            }} else {{
                console.warn("streamlit-shortcuts: Unable to find container with key '{key}'.");
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
    key=None,
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
        key (str): The unique id for the button, used to identify it in Streamlit.
            If None, a unique ID like `button_1` is generated automatically.
        hint (bool, optional): Whether to show the keyboard shortcut as a hint
            on the button label. Defaults to False.
        args (tuple, optional): Additional arguments to pass to the on_click function.
        **kwargs: Additional keyword arguments passed to the button function.

    Returns:
        The result of the Streamlit button function.

    Notes:
        This function integrates with Streamlit's `st.button` to display a
        button with an optional hint showing the associated keyboard shortcut.
    """
    # generate a unique key if not provided
    # we use a counter in the session state to ensure uniqueness
    # and we make sure to not overwrite existing keys
    if "button_key_counter" not in st.session_state:
        st.session_state["button_key_counter"] = 1

    while key is None or key in st.session_state:
        n = st.session_state["button_key_counter"]
        key = f"button_{n}"
        st.session_state["button_key_counter"] = n + 1

    if hint:
        button_label = f"{label} `{shortcut}`"
    else:
        button_label = label

    if args:
        button = st.button(
            label=button_label, key=key, on_click=on_click, args=args, **kwargs
        )
    else:
        button = st.button(label=button_label, key=key, on_click=on_click, **kwargs)

    # now that we have made the button, we can find it with JS and add the keyboard shortcut
    add_keyboard_shortcuts({key: shortcut})
    return button
