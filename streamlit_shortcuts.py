"""Keyboard shortcuts for Streamlit buttons and widgets."""

import json
import streamlit as st
import streamlit.components.v1 as components


def add_shortcuts(**shortcuts: str | list[str]) -> None:
    """Add keyboard shortcuts to any Streamlit element with a key.

    Args:
        **shortcuts: key='shortcut' or key=['shortcut1', 'shortcut2'] pairs
                    e.g. button1='ctrl+a', button2=['arrowleft', 'a']
                    Modifiers: ctrl, alt, shift, meta (cmd on Mac)
                    Keys: any letter, number, or Enter, Escape, ArrowUp, etc.
    """
    assert shortcuts, "No shortcuts provided"

    # Normalize all shortcuts to lists
    normalized_shortcuts = {}
    for key, value in shortcuts.items():
        if isinstance(value, str):
            normalized_shortcuts[key] = [value]
        else:
            normalized_shortcuts[key] = value

    js = (  # noqa: E501 (line length), W291 (trailing whitespace), W293 (blank line whitespace)
        """<script>
    const doc = window.parent.document;
    const parentWindow = window.parent.window;
    const shortcuts = """
        + json.dumps(normalized_shortcuts)
        + """;
    
    if (!doc) throw new Error('Not running in Streamlit context');
    
    // One-time initialization of the listener
    if (!parentWindow.__streamlitShortcutsInitialized) {
        // Initialize the shortcuts map
        parentWindow.__streamlitShortcutsMap = {};
        
        // Create the permanent listener that reads from the map
        parentWindow.__streamlitShortcutsListener = function(e) {
            const allShortcuts = parentWindow.__streamlitShortcutsMap || {};
            for (const [key, shortcutList] of Object.entries(allShortcuts)) {
                // Ensure shortcutList is always an array
                const shortcuts = Array.isArray(shortcutList) ? shortcutList : [shortcutList];
                
                for (const shortcut of shortcuts) {
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
                            console.error('streamlit-shortcuts: Element not found for key "' + key + '" - keyboard shortcut will not work');
                            return;
                        }
                        el.click();
                        el.focus();
                        return; // Exit both loops after handling
                    }
                }
            }
        };
        
        // Attach the listener once
        doc.addEventListener('keydown', parentWindow.__streamlitShortcutsListener);
        
        // Mark as initialized
        parentWindow.__streamlitShortcutsInitialized = true;
    }
    
    // Always update the shortcuts map with new shortcuts
    Object.assign(parentWindow.__streamlitShortcutsMap, shortcuts);
    </script>"""
    )

    components.html(js, height=0, width=0)


def clear_shortcuts() -> None:
    """Remove all keyboard shortcuts and event listeners."""
    js = """<script>
    const doc = window.parent.document;
    const parentWindow = window.parent.window;
    
    // Remove the listener
    if (parentWindow.__streamlitShortcutsListener) {
        doc.removeEventListener('keydown', parentWindow.__streamlitShortcutsListener);
        parentWindow.__streamlitShortcutsListener = null;
    }
    
    // Clear all state
    parentWindow.__streamlitShortcutsMap = {};
    parentWindow.__streamlitShortcutsInitialized = false;
    </script>"""

    components.html(js, height=0, width=0)


def shortcut_button(
    label: str, shortcut: str | list[str], hint: bool = True, **kwargs
) -> bool:  # noqa: FBT002 (boolean positional arg)
    """Streamlit button with a keyboard shortcut.

    Args:
        label: Button text (can be empty string)
        shortcut: Single shortcut or list of shortcuts like 'ctrl+s', ['arrowleft', 'a'], etc.
        hint: Show shortcut hint in button label (default: True)
        **kwargs: All other st.button args (key, type, disabled, use_container_width, etc.)

    Returns:
        bool: True if button was clicked (same as st.button)
    """
    assert label is not None, "Button label cannot be None"
    assert shortcut, "Shortcut parameter is required"

    # Generate key if not provided
    shortcut_str = shortcut if isinstance(shortcut, str) else str(shortcut)
    if "key" not in kwargs:
        kwargs["key"] = f"btn_{hash(label + shortcut_str) % 10000000}"

    # Add hint to label if requested
    if hint and label:
        if isinstance(shortcut, str):
            button_label = f"{label} `{shortcut}`"
        else:
            # For multiple shortcuts, show them separated by " or "
            button_label = f"{label} `{' or '.join(shortcut)}`"
    else:
        button_label = label

    # Create button WITHOUT hint parameter
    clicked = st.button(button_label, **kwargs)

    # Add the shortcut
    add_shortcuts(**{kwargs["key"]: shortcut})

    return clicked
