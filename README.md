
# Streamlit Shortcuts

Streamlit Shortcuts allows you to easily add keyboard shortcuts to your Streamlit buttons.

## Installation

```bash
pip install streamlit-shortcuts
```

## Example

⭐ NEW! thanks to @quantum-ernest 
```python
import streamlit as st
import streamlit_shortcuts

def delete_callback():
    st.write("DELETED!")

streamlit_shortcuts.button("delete", on_click=delete_callback, shortcut="Ctrl+Shift+X")
```

🥱 Old 
```
import streamlit as st
from streamlit_shortcuts import add_keyboard_shortcuts

def delete_callback():
    st.write("DELETED!")

st.button("delete", on_click=delete_callback)

add_keyboard_shortcuts({
    'Ctrl+Shift+X': 'delete',
})
```

The 'Ctrl+Shift+X' combination will trigger "Another Button".

## Keys
- Modifiers: 'Ctrl', 'Shift', 'Alt', 'Meta' ('Cmd' on Mac or 'Win' on Windows, thanks to @toolittlecakes)  
- Common Keys: 'Enter', 'Escape', 'Space'
- Arrow Keys: 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown'

Examples of Key Combinations:
- 'Ctrl+Enter'
- 'Shift+ArrowUp'
- 'Alt+Space'

For a complete list of key values, refer to:
https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values


## Contributing

Contributions are welcome! If you have suggestions for improvements or bug fixes, please feel free to make a pull request or open an issue.

## Contributors
@toolittlecakes - Added 'Meta' modifier

@quantum-ernest - Improved usage ergonomics

@taylor-ennen - Fixed usage `flow` of code

## Credits
Solution seen on:
https://github.com/streamlit/streamlit/issues/1291

https://gist.github.com/brunomsantiago/e0ab366fc0dbc092c1a5946b30caa9a0

@brunomsantiago

@TomJohnH

And wrapped for comfier usage.
