# CyberSentinels-OSint

**CyberSentinels-OSint** is an OSINT (Open Source Intelligence) tool designed to track someone across various platforms. It is modular, extensible, and user-friendly, providing insights into the presence of specific email addresses or usernames on supported services.
It is the OFFICIAL italian's ethical hackers community [CyberSentinels](https://cybersentinels.net)

---

## Features

- **Email Tracking**: Identify platforms where a given email address is registered.
- **Username Tracking**: Find platforms where a specific username is active.
- **Many others will be implemented**
- Modular design with separate modules for email and username tracking.
- Command-line interface for easy interaction.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/0xZ3r0D4y/CyberSentinels-OSint.git
   cd CyberSentinels-OSint
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the tool:
   ```bash
   python main.py
   ```

---

## Usage

1. **Start the tool**:
   Execute the `main.py` file:
   ```bash
   python main.py
   ```

2. **Select a module**:
   - **1 - Email Tracker**: Enter an email to check its presence across platforms.
   - **2 - Username Tracker**: Enter a username to find its accounts on various platforms.
   - **99 - Exit**: Exit the tool.

---

## Modules

### Email Tracker
The `EmailTracker` module checks if an email is registered on various platforms.  

**Platforms Supported**:
- Instagram
- Twitter
- Pinterest
- Patreon
- Spotify
- Firefox
- LastPass
- Archive.org
- PornHub
- Xnxx
- XVideos

**Example**:
```bash
[?] Enter the email to track: example@example.com
[+] Accounts Found (Note: May include false positives):
    1 - Instagram
    2 - Twitter
```

---

### Username Tracker
The `UsernameTracker` module identifies the presence of a username across various platforms.  

**A Lot of Platforms Are Supported**

**Example**:
```bash
[?] Enter the username to track: exampleuser
[+] Accounts Found (Note: May include false positives):
    1 - Twitter
    2 - GitHub
```

---

## Dependencies

- **requests**: For making HTTP requests to APIs.
- **beautifulsoup4**: For web scraping when needed.

Install dependencies with:
```bash
pip install -r requirements.txt
```

---

## Extending the Tool

### Adding a New Platform
1. Update `EmailTracker` or `UsernameTracker` in their respective modules.
2. Define a new method for the specific platform.
3. Use HTTP requests or web scraping to implement tracking logic.
4. Add the platform name to the supported platforms list.

### Adding a New Module
1. Create the module inside of the `modules` folder.
2. Import the module inside of `main.py`.
3. Add the module to the menu and the match.
4. Test the module and fix any bugs, if any.

---

## Disclaimer
This tool is intended for educational and ethical purposes only. Misuse may lead to legal consequences. Always respect the terms of service of the platforms you interact with.

## Collaborating
Collaborations are welcome, feel free to clone this repo, edit and ask for the merge!

---

## License
This project is licensed under the [MIT License](LICENSE).