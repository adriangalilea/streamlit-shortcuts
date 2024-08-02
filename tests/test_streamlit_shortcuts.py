from streamlit_shortcuts import add_keyboard_shortcuts, button
import pytest

def test_add_keyboard_shortcuts_exists():
    assert callable(add_keyboard_shortcuts)

def test_button_exists():
    assert callable(button)

def test_add_keyboard_shortcuts_accepts_dict():
    try:
        add_keyboard_shortcuts({})
    except TypeError:
        pytest.fail("add_keyboard_shortcuts should accept a dictionary")

def test_button_accepts_arguments():
    def dummy_callback():
        pass
    try:
        button("Test", "ctrl+t", dummy_callback)
    except TypeError:
        pytest.fail("button should accept label, shortcut, and callback arguments")

def test_add_keyboard_shortcuts_rejects_non_dict():
    with pytest.raises(TypeError):
        add_keyboard_shortcuts("not a dict")

def test_button_rejects_invalid_arguments():
    with pytest.raises(TypeError):
        button(123, "ctrl+t", lambda: None)  # label should be a string

def test_button_callback_execution():
    called = False
    def test_callback():
        nonlocal called
        called = True
    
    btn = button("Test", "ctrl+t", test_callback)
    btn.click()  # Simulate button click
    assert called, "Callback should have been executed"
