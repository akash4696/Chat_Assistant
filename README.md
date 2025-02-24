# SQLite Chat Assistant

## Overview
This is a Python-based chat assistant that interacts with an SQLite database to answer user queries about employees and departments.

## How It Works
- The assistant accepts natural language queries.
- It converts queries into SQL to fetch data from the database.
- It responds with clear, formatted answers.

## Supported Queries
- "Show me all employees in the [department] department."
- "Who is the manager of the [department] department?"
- "List all employees hired after [date]."
- "What is the total salary expense for the [department] department?"

## Running Locally
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run the app: `python app.py`.
4. Access the chat assistant at `http://127.0.0.1:5000/chat`.

## Known Limitations
- Limited natural language understanding.
- No authentication or rate limiting for the API.
