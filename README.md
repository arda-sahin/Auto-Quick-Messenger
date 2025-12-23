# Auto Quick Messenger 🚀

**Auto Quick Messenger** is a lightweight, Python-based productivity tool designed to automate the process of sending repetitive text messages. It streamlines workflow by mapping custom text payloads to specific keyboard hotkeys.

Perfect for customer support agents, community managers, or anyone who frequently types the same phrases.

## 🌟 Features

* **Customizable Hotkeys:** Map any key (Numpad 1, F1, Alt+A, etc.) to specific text messages.
* **Separation of Concerns:** Configuration is managed via an external `messages.json` file, keeping the code clean and logic-free.
* **Input Echo Suppression:** Automatically removes the trigger key (e.g., '1') before pasting the text to ensure clean output.
* **Clipboard Management:** Uses system clipboard simulation for instant text insertion.
* **Error Handling:** Robust file checking and exception handling mechanisms.

## 📂 Project Structure

```text
Auto-Quick-Messenger/
├── main.py              # The main application script
├── messages.json        # Configuration file for hotkeys and texts
├── requirements.txt     # List of dependencies
└── README.md            # Project documentation

🛠️ Installation
Clone the repository (or download the files):

git clone [https://github.com/arda-sahin/Auto-Quick-Messenger.git](https://github.com/arda-sahin/Auto-Quick-Messenger.git)
cd Auto-Quick-Messenger

Install dependencies: This project requires keyboard and pyperclip libraries.
pip install -r requirements.txt

⚙️ Configuration
Open the messages.json file to customize your messages. The key represents the hotkey, and the value represents the text to be sent.

Example messages.json:
{
    "1": "Hello! How can I help you today?",
    "2": "Thank you for your purchase.",
    "3": "Please verify your email address.",
    "f1": "This is a custom message mapped to the F1 key."
}
Note: For Numpad keys, you can simply use numbers like "1", "2". For specific keys, you can use "f1", "ctrl+alt+a", etc.

🚀 Usage
Run the script via terminal:
python main.py

The application will display the loaded hotkeys and start listening in the background.
Press any of your configured keys to instantly paste and send the message.
Press ESC to stop the application.