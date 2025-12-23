"""
Auto Quick Messenger
--------------------
A productivity tool designed to automate sending frequent text messages.
It reads configurations from an external JSON file.

Author: [Sizin Adınız / GitHub Kullanıcı Adınız]
Date: 2025
License: MIT
"""

import keyboard
import pyperclip
import time
import json
import os
import sys

# --- CONFIGURATION FILES ---
CONFIG_FILE = 'messages.json'
CLIPBOARD_DELAY = 0.1 

def load_messages(filename: str) -> dict:
    """
    Loads message mappings from a JSON file.
    """
    if not os.path.exists(filename):
        print(f"Error: Configuration file '{filename}' not found!")
        print("Please create a 'messages.json' file in the same directory.")
        return {}
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Error: '{filename}' is not a valid JSON file.")
        return {}

def send_message_payload(text_content: str) -> None:
    """
    Handles clipboard operations and inputs.
    """
    try:
        # Step 1: Remove the trigger key (Input Echo)
        keyboard.press_and_release('backspace')
        
        # Step 2: Copy content
        pyperclip.copy(text_content)
        time.sleep(CLIPBOARD_DELAY)
        
        # Step 3: Paste and Send
        keyboard.press_and_release('ctrl+v')
        keyboard.press_and_release('enter')
        
    except Exception as e:
        print(f"Error executing command: {e}")

def main():
    """
    Main application loop.
    """
    print("========================================")
    print("   AUTO QUICK MESSENGER - ACTIVE")
    print("========================================")

    # Load messages from JSON
    hotkey_mappings = load_messages(CONFIG_FILE)

    if not hotkey_mappings:
        print("\nNo messages loaded. Exiting...")
        time.sleep(3)
        sys.exit()

    print("Press 'ESC' to exit.\n")
    print("Active Hotkeys (from JSON):")

    for key, message in hotkey_mappings.items():
        keyboard.add_hotkey(key, send_message_payload, args=[message])
        
        preview = (message[:40] + '...') if len(message) > 40 else message
        print(f"  [{key}] -> {preview}")

    print("\nListening for input...")
    keyboard.wait('esc')
    print("\nExiting application. Goodbye!")

if __name__ == "__main__":
    main()