# 🔐 Auto Login Bot

This project demonstrates automated login for multiple websites using Python and Selenium. It is designed as a reusable baseline for automating login workflows, helping users kickstart secure and scalable browser automation across different platforms.

## ✅ Features

- 🔄 Automates login for multiple websites
- 🧱 Shared `BaseBot` class with per-site implementations
- 🔍 Headless or visible browser mode for debugging
- 📸 Screenshots captured on failure or timeout
- 🔐 Credential management via `.env` and `config.py`
- 🧪 Easily extendable to other sites

## 🧪 Supported Sites

- **GitHub** – logs into [github.com/login](https://github.com/login)
- **Quotes to Scrape** – demo site: [quotes.toscrape.com/login](https://quotes.toscrape.com/login)


## 📂 Project Structure
<pre> AutoLoginBot/ 
├── bots/ 
│ ├── base.py # Common base class for all bots 
│ ├── github_bot.py # GitHub-specific login logic 
│ └── quotes_bot.py # QuotesToScrape login logic 
├── config.py # Loads credentials from environment variables 
├── main.py # Entry point to launch selected bots 
├── requirements.txt # Python dependencies 
├── .env # Local credentials (not committed) 
├── screenshots/ # Automatically saved screenshots on error 
└── README.md # Project description and usage guide </pre>

## ⚙️ Setup Instructions

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

2. **Update the .env file with your credentials:**
    ```env
    GITHUB_USERNAME=your_github_username
    GITHUB_PASSWORD=your_github_password
    GITHUB_URL=https://github.com/login

    QUOTES_USERNAME=test
    QUOTES_PASSWORD=test
    QUOTES_URL=https://quotes.toscrape.com/login

3. **Run the bot:**
    ```bash
    python main.py

    You can toggle which bots run in main.py:

        SELECTED_BOTS = ["github", "quotes"]
        HEADLESS_MODE = False
        CLOSE_BROWSER = False

## 🚀 Why This Project?:
This tool serves as a clean and extendable template for automating login flows in professional or testing environments. It demonstrates:

Web automation with Selenium

Use of design patterns (inheritance, factory)

Robustness via waits, error handling, and screenshot logging

## 🛠️ Next Steps:
You can easily extend this project by:

Adding a new bot in bots/

Registering it in BOT_CLASSES and CONFIGS