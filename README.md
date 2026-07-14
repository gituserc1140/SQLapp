# SQL Joins Visualizer

This Streamlit app allows you to visualize SQL joins between tables in a SQLite database.

## Features
- Select tables for join
- Choose join type (INNER, LEFT, RIGHT, FULL)
- Select join column
- Display join results

## Prerequisites
- Python 3.7+
- Streamlit
- SQLite3
- Pandas

## Installation
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`

## Usage
1. Ensure you have a SQLite database named `example.db` in the same directory.
2. Select tables and join parameters from the sidebar.
3. Click 'Execute Join' to see the results.