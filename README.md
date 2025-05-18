# Solar Challenge Week 1

This repository contains the code and dashboard for the Solar Challenge Week 1 project.

## Prerequisites
- Python 3.10 or higher
- Git

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/yourusername/solar-challenge-week1.git
cd solar-challenge-week1
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
# OR
.\venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Dashboard
```bash
streamlit run app/main.py
```

## Project Structure
```
solar-challenge-week1/
├── app/                  # Streamlit dashboard and utilities
│   ├── main.py
│   ├── utils.py
│   └── __init__.py
├── data/                 # Cleaned and raw data files
│   ├── benin_clean.csv
│   ├── sierraleone_clean.csv
│   ├── togo_clean.csv
│   ├── benin-malanville.csv
│   ├── sierraleone-bumbuna.csv
│   ├── togo-dapaong_qc.csv
│   └── ...
├── notebooks/            # Jupyter notebooks for EDA and analysis
│   ├── benin_eda.ipynb
│   ├── sierraleone_eda.ipynb
│   ├── togo_eda.ipynb
│   ├── compare_countries.ipynb
│   ├── README.md
│   └── __init__.py
├── scripts/              # Utility scripts
│   ├── README.md
│   └── __init__.py
├── tests/                # Test files
│   └── __init__.py
├── .github/              # GitHub Actions and workflows
│   └── workflows/
│       └── ci.yml
├── .vscode/              # VSCode settings
│   └── settings.json
├── requirements.txt      # Python dependencies
├── .gitignore            # Git ignore file
├── README.md             # Project setup and usage (this file)
└── venv/                 # Python virtual environment (not tracked)
```