# SpacerID

**SpacerID** is a simple, powerful and modular OSINT tool that scans public usernames across multiple online platforms. Designed to be beginner-friendly but extensible, it's ideal for red teamers, journalists, investigators, or anyone who wants to map online identities from a single alias.

---

## 🚀 Features

- Username lookup across many popular platforms (GitHub, Reddit, Instagram, etc.)
- Easy to add/remove platforms via `platforms.json`
- Saves found accounts to an output file
- Clean terminal output with optional colors (via `colorama`)
- Lightweight, fast, no external APIs
- Modular and open source

---

## 🛠️ Requirements

- Python 3.8+
- pip

Install dependencies:
```bash
pip install -r requirements.txt  # Or use --break-system-packages on Kali if needed
```

---

## 📖 Usage

```bash
python3 spacerid.py -u <username>
```

Example:
```bash
python3 spacerid.py -u johndoe
```

This will:
- Check the username `johndoe` across all platforms listed in `platforms.json`
- Show which accounts exist
- Save results to `output/johndoe_results.txt`

---

## 📚 Configuration (Add/Remove Platforms)

You can easily edit the `platforms.json` file to modify where SpacerID looks:

```json
{
  "GitHub": "https://github.com/{}",
  "Twitter": "https://twitter.com/{}",
  "Reddit": "https://www.reddit.com/user/{}"
  // Add or remove entries as needed
}
```

Use `{}` as a placeholder where the username will be injected.

---

## 🎓 License

**Recommended license: MIT License** — because:
- You allow anyone to use, copy, modify, and share the project
- You keep attribution to yourself
- It fits a hacker/open-source spirit

Let me know if you want a different license (GPL, AGPL, etc.)

---

## 🔍 Roadmap (Future Ideas)

- Add email or phone lookup module
- Export results in JSON/PDF
- Create a GUI or web version
- Add leak database/API integration
- Style terminal UI with `rich` or `typer`

---

## 💜 Author

Made with caffeine, frustration and focus by **Hyuga**

> "Everything leaves a trace. Even shadows."

