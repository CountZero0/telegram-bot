# Notifier telegram bot

This bot notifies you, when your [homework](https://dvmn.org/) get's code review.

## Features
- `long polling` API utilization
- Notifies on every code review
- Tells code review result
- You can easy deploy it on any server

## Installation

1.Python 3.6+ should be already installed.

2. Download project
```
cd to downloaded directory
```

3. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

4. Install requirements
```bash
pip install -r requirements.txt
```

5. Run telegram bot
```bash
python main.py
```