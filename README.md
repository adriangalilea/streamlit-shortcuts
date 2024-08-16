
# Streamlit Shortcuts

Streamlit Shortcuts allows you to easily add keyboard shortcuts to your Streamlit buttons.

## Installation

```bash
pip install streamlit-shortcuts
```

## Example

```python
import streamlit as st
import streamlit_shortcuts

def delete_callback():
    st.write("DELETED!")

streamlit_shortcuts.button("delete", on_click=delete_callback, shortcut="Ctrl+Shift+X", hint=True)
```

⭐ NEW in v0.1.5: Support for args and kwargs
```python
import streamlit as st
import streamlit_shortcuts

def delete_callback(item_id, user="anonymous"):
    st.write(f"Item {item_id} DELETED by {user}!")

streamlit_shortcuts.button(
    "Delete",
    shortcut="Ctrl+Shift+X",
    on_click=delete_callback,
    hint=True,
    args=(42,),
    kwargs={"user": "admin"},
    type="primary"
)
```

This creates a primary Streamlit button labeled "Delete" with the shortcut "Ctrl+Shift+X".
When clicked (or activated via shortcut), it calls `delete_callback(42, user="admin")`.

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


## Versioning

We use semantic versioning. The current version is stored in the `VERSION` file in the root of the repository.

## Contributing

Contributions are welcome! If you have suggestions for improvements or bug fixes, please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bugfix
3. Make your changes
4. Add or update tests as necessary
5. Update the `VERSION` file if your changes warrant a version bump
6. Submit a pull request

Please make sure to update tests as appropriate and adhere to the existing coding style.

## Releasing New Versions

To release a new version:

1. Update the `VERSION` file with the new version number
2. Commit the change: `git commit -am "Bump version to X.Y.Z"`
3. Create a new tag: `git tag vX.Y.Z`
4. Push the changes and the tag: `git push && git push --tags`

The GitHub Actions workflow will automatically create a new release and publish to PyPI.

## Contributors
- @toolittlecakes - Added 'Meta' modifier
- @quantum-ernest - Improved usage ergonomics
- @taylor-ennen - Fixed usage `flow` of code

## Credits
Solution inspired by:
- https://github.com/streamlit/streamlit/issues/1291
- https://gist.github.com/brunomsantiago/e0ab366fc0dbc092c1a5946b30caa9a0

Special thanks to @brunomsantiago and @TomJohnH for their initial work on this concept.

Wrapped and extended for easier usage by the Streamlit Shortcuts team.
