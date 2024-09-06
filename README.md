# Instagram Non-Mutual Follower Checker

## Project Overview
This project provides a Python script that uses Selenium to log into an Instagram account, extract the lists of followers and followings, and identify users who are being followed but do not follow back (non-mutual followers). The script automates the process, simulating real user behavior to avoid detection by Instagram’s anti-scraping mechanisms.

## Features
- Automatically logs into Instagram with your provided credentials.
- Extracts followers and followings from any Instagram account.
- Compares followers and following to find non-mutual followers.
- Outputs the list of non-mutual followers.

## Prerequisites
To use this project, you need to have the following installed:
1. **Python 3.x**
2. **Selenium library** (installed in a virtual environment, see below).
3. **WebDriver** for your browser (e.g., ChromeDriver for Chrome or GeckoDriver for Firefox).