
# WLZBI - Terminal Logo & Typing Library

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PyPI Version](https://img.shields.io/pypi/v/wlzbi?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/wlzbi/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/wlzbi?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/wlzbi/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](https://github.com/wlzbi-exe/wlzbi/blob/main/LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/wlzbi-exe/wlzbi?style=for-the-badge&logo=github)](https://github.com/wlzbi-exe/wlzbi)
[![GitHub Issues](https://img.shields.io/github/issues/wlzbi-exe/wlzbi?style=for-the-badge&logo=github)](https://github.com/wlzbi-exe/wlzbi/issues)
[![Telegram](https://img.shields.io/badge/Telegram-@rejerks-blue?style=for-the-badge&logo=telegram)](https://t.me/rejerks)
[![Telegram Channel](https://img.shields.io/badge/Telegram-@wlzbi-blue?style=for-the-badge&logo=telegram)](https://t.me/wlzbi)

</div>

---

## 📖 Overview

**WLZBI** is a lightweight Python library designed to create visually appealing terminal logos and animated typing effects. With simple method chaining, you can generate ASCII art logos with custom alignment and create typewriter-style text output with various color options.

---

## ✨ Features

- **Logo Generation** - Create ASCII art logos with customizable text
- **Flexible Alignment** - Left, right, center, and centre alignment options
- **Animated Typing** - Typewriter effect with adjustable speed
- **Color Support** - 8 standard and 8 bold colors
- **Chained Methods** - Clean, intuitive API design
- **Zero External Dependencies** - Lightweight and portable

---

## 🚀 Installation

### PyPI Installation

```bash
pip install wlzbi
```

GitHub Installation

```bash
pip install git+https://github.com/wlzbi-exe/wlzbi.git
```

Local Development

Clone the repository and install in development mode:

```bash
git clone https://github.com/wlzbi-exe/wlzbi.git
cd wlzbi
pip install -e .
```

---

🎯 Quick Start

```python
import wlzbi

# Create a centered logo
wlzbi.logo("WLZBI", "Hello World").center()

# Type text with animation
wlzbi.type("Welcome to WLZBI!")
```

---

📚 API Reference

Logo API

wlzbi.logo(brand, text)

Creates a logo object with the given brand name and text.

Parameters:

· brand (str) - The brand/logo name to display
· text (str) - The text to display below the logo

Returns: Logo object with alignment methods

Alignment Methods

Method Description
.left() Align logo to the left
.right() Align logo to the right
.center() Align logo to the center
.centre() Align logo to the center (alternative spelling)

Example:

```python
import wlzbi

# Left aligned logo
wlzbi.logo("WLZBI", "Developer Tool").left()

# Center aligned logo
wlzbi.logo("WLZBI", "Terminal Art").center()

# Right aligned logo
wlzbi.logo("WLZBI", "Python Library").right()
```

---

Typing API

wlzbi.type(text, color=None, speed=0.05)

Displays text with a typewriter animation effect.

Parameters:

· text (str) - The text to display
· color (str, optional) - Color name for the text
· speed (float, optional) - Typing speed in seconds per character (default: 0.05)

Example:

```python
import wlzbi

# Basic typing
wlzbi.type("Hello, World!")

# Colored typing
wlzbi.type("Hello", "cyan")

# Colored typing with custom speed
wlzbi.type("Fast typing", "green", speed=0.01)
wlzbi.type("Slow typing", "yellow", speed=0.15)
```

---

Supported Colors

Standard Colors

Color Code
Black black
Red red
Green green
Yellow yellow
Blue blue
Magenta magenta
Cyan cyan
White white

Bold Colors

Color Code
Bold Black boldblack
Bold Red boldred
Bold Green boldgreen
Bold Yellow boldyellow
Bold Blue boldblue
Bold Magenta boldmagenta
Bold Cyan boldcyan
Bold White boldwhite

Example with colors:

```python
import wlzbi

# Standard colors
wlzbi.type("Red text", "red")
wlzbi.type("Green text", "green")
wlzbi.type("Cyan text", "cyan")

# Bold colors
wlzbi.type("Bold blue", "boldblue")
wlzbi.type("Bold magenta", "boldmagenta")
```

---

💡 Practical Examples

Combined Logo and Typing

```python
import wlzbi

# Display logo with animation
wlzbi.logo("WLZBI", "Terminal Library").center()
wlzbi.type("Initializing...", "cyan", speed=0.02)
wlzbi.type("Ready!", "green")
```

Custom Typing Speed

```python
import wlzbi

# Fast typing
wlzbi.type("Loading assets...", "yellow", speed=0.01)

# Normal typing
wlzbi.type("Processing data...", "blue", speed=0.05)

# Slow typing
wlzbi.type("Almost done...", "magenta", speed=0.1)
```

Colorful Banner

```python
import wlzbi

# Create a colorful welcome banner
wlzbi.logo("WLZBI", "Welcome").center()
wlzbi.type("Developed with ❤️", "boldcyan", speed=0.03)
```

---

📦 Dependencies

· Python 3.6+ - No external dependencies required

---

📂 Project Structure

```
wlzbi/
├── wlzbi/
│   ├── __init__.py
│   └── core.py
├── tests/
│   └── ...
├── README.md
├── LICENSE
└── setup.py
```

---

🛠️ Development

Running Tests

```bash
python -m unittest discover tests
```

Local Testing

```python
import wlzbi

# Test logo alignment
wlzbi.logo("TEST", "Left aligned").left()
wlzbi.logo("TEST", "Center aligned").center()
wlzbi.logo("TEST", "Right aligned").right()

# Test typing with various colors
wlzbi.type("Testing colors", "cyan")
wlzbi.type("Testing bold colors", "boldcyan")
```

---

🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (git checkout -b feature/amazing)
3. Commit your changes (git commit -m 'Add amazing feature')
4. Push to the branch (git push origin feature/amazing)
5. Open a Pull Request

Bug Reports

If you encounter any issues, please report them on the Issues page.

Feature Requests

Have an idea for improvement? Open a feature request and let's discuss!

---

👨‍💻 Developer

Alen from Kerala, India

· Telegram: @rejerks
· GitHub: wlzbi-exe

---

🌐 Community

Join our community channels:

· Official Telegram Channel: @wlzbi
· GitHub Repository: wlzbi-exe/wlzbi
· PyPI Package: wlzbi

---

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

⭐ Support

If you find this project useful, please consider:

· ⭐ Starring the repository on GitHub
· 📢 Sharing with others who might find it helpful
· 🐛 Reporting any issues you encounter

Your support helps make this project better!

---
<div align="center">

[![Telegram](https://img.shields.io/badge/Telegram-%40rejerks-blue?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/rejerks)
[![Channel](https://img.shields.io/badge/Channel-%40wlzbi-blue?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/wlzbi)
[![GitHub](https://img.shields.io/badge/GitHub-wlzbi--exe%2Fwlzbi-lightgrey?style=for-the-badge&logo=github&logoColor=white)](https://github.com/wlzbi-exe/wlzbi)
[![PyPI](https://img.shields.io/badge/PyPI-wlzbi-blue?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/wlzbi/)

</div>

<div align="center">

— @rejerks | WLZBI


</div>
