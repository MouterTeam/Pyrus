# Pyrus (Python + Virus)

Pyrus is a fake "virus prank" made with Python. It simulates a system crash using fullscreen BSOD (Blue Screen of Death) images and disables common exit methods like ESC or Alt+F4. It's a harmless prank script for educational or entertainment purposes.

⚠️ **Warning:** Do **not** use this script to trick or harm others. Misuse could violate school, workplace, or legal policies.

---

## Features

- Fullscreen Tkinter window simulating a locked desktop
- Uses a screenshot of the actual desktop to mimic freezing
- Sequential display of fake BSOD images
- Disables standard exit methods (`ESC`, `Alt+F4`, window close button)
- Always-on-top window to block user interaction

---

## Requirements

- Python 3.x
- [Pillow](https://pypi.org/project/Pillow/)
- [PyAutoGUI](https://pypi.org/project/pyautogui/)

Install dependencies:

```bash
pip install pillow pyautogui
