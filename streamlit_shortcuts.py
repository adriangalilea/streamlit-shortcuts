"""Keyboard shortcuts for Streamlit buttons and widgets."""

import json
import streamlit as st
import streamlit.components.v1 as components


def add_shortcuts(**shortcuts: str) -> None:
    """Add keyboard shortcuts to any Streamlit element with a key.

    Args:
        **shortcuts: key='shortcut' pairs, e.g. button1='ctrl+a', input2='alt+shift+x'
                    Modifiers: ctrl, alt, shift, meta (cmd on Mac)
                    Keys: any letter, number, or Enter, Escape, ArrowUp, etc.
    """
    assert shortcuts, "No shortcuts provided"

    js = (  # noqa: E501 (line length), W291 (trailing whitespace), W293 (blank line whitespace)
        """<script>
    const doc = window.parent.document;
    const shortcuts = """
        + json.dumps(shortcuts)
        + """;
    
    if (!doc) throw new Error('Not running in Streamlit context');
    
    doc.addEventListener('keydown', function(e) {
        for (const [key, shortcut] of Object.entries(shortcuts)) {
            const parts = shortcut.toLowerCase().split('+');
            const hasCtrl = parts.includes('ctrl');
            const hasAlt = parts.includes('alt');
            const hasShift = parts.includes('shift');
            const hasMeta = parts.includes('meta') || parts.includes('cmd');
            const mainKey = parts.find(p => !['ctrl', 'alt', 'shift', 'meta', 'cmd'].includes(p));
            
            if (hasCtrl === e.ctrlKey && 
                hasAlt === e.altKey && 
                hasShift === e.shiftKey && 
                hasMeta === e.metaKey && 
                e.key.toLowerCase() === mainKey) {
                
                e.preventDefault();
                
                let el = doc.querySelector(`.st-key-${key} button`) ||
                         doc.querySelector(`.st-key-${key} input`) ||
                         doc.querySelector(`[data-testid="${key}"]`) ||
                         doc.querySelector(`button:has([data-testid="baseButton-${key}"])`) ||
                         doc.querySelector(`[aria-label="${key}"]`);
                         
                if (!el) {
                    throw new Error('Element not found: ' + key + ' - keyboard shortcut will not work');
                }
                el.click();
                el.focus();
                break;
            }
        }
    });
    </script>"""
    )

    components.html(js, height=0, width=0)


def shortcut_button(label: str, shortcut: str, hint: bool = True, **kwargs) -> bool:  # noqa: FBT002 (boolean positional arg)
    """Streamlit button with a keyboard shortcut.

    Args:
        label: Button text (can be empty string)
        shortcut: Keyboard shortcut like 'ctrl+s', 'alt+shift+d', 'meta+k', or just 'x'
        hint: Show shortcut hint in button label (default: True)
        **kwargs: All other st.button args (key, type, disabled, use_container_width, etc.)

    Returns:
        bool: True if button was clicked (same as st.button)
    """
    assert label is not None, "Button label cannot be None"
    assert shortcut, "Shortcut parameter is required"

    # Generate key if not provided
    if "key" not in kwargs:
        kwargs["key"] = f"btn_{hash(label + shortcut) % 10000000}"

    # Add hint to label if requested
    button_label = f"{label} `{shortcut}`" if hint and label else label

    # Create button WITHOUT hint parameter
    clicked = st.button(button_label, **kwargs)

    # Add the shortcut
    add_shortcuts(**{kwargs["key"]: shortcut})

    return clicked
