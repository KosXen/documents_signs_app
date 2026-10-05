# Document Signature Management App

A lightweight web application for tracking documents as they move between people for signature. Built with Python (Flask), HTML and JavaScript, and packaged as a standalone Windows executable so non-technical users can run it with a double-click.

## Table of Contents

- [Features](#features)
- [Built With](#built-with)
- [Data Model](#data-model)
- [Getting Started](#getting-started)
- [Building the Executable](#building-the-executable)
- [Database](#database)
- [Project Structure](#project-structure)
- [How the Code Works](#how-the-code-works)
- [Configuration](#configuration)
- [Author](#author)

## Features

| Action | Description |
| **Create Document** | Adds a new document to the database with a given id, the creator's name (the first signer) and the name of the person who receives it next. |
| **Search Document** | Displays the information of the document with the given id. |
| **Update Document** | Records that the user has signed a document: their name is added to the list of signers, and the next recipient is updated. |
| **Complete Document** | Deletes the document from the database, after asking the user for confirmation. |
| **All Documents** | Lists every document currently in the database. |

Additional behavior:

- Document ids are validated (digits only, no duplicates).
- Clear error messages for missing or invalid documents.
- Password-protected access.

## Built With

- **Python 3** with **Flask**
- **HTML** (Jinja templates)
- **JavaScript**
- **PyInstaller** (to produce `signs.exe`)

## Data Model

Each document stores:

| Field | Description |
|---|---|
| `id` | Unique numeric identifier |
| `signed_from` | Names of everyone who has already signed |
| `tbs` | Name of the person who currently holds the document, to be signed |
| `date_created` | Date the document was created |
| `date_signed` | Date of the most recent signature |

## Getting Started

### Option 1: Run the executable (end users)

1. Double-click the `signs.exe` file you received.
2. A console window opens. Find the line that says `Running on ...` followed by an address such as `127.0.0.1:8000`.
3. Copy that address into your web browser.
4. Enter the password the first time you use the app.

### Option 2: Run from source (developers)

```bash
# 1. Clone the repository
git clone https://github.com/YOUR-USERNAME/YOUR-REPO.git
cd YOUR-REPO

# 2. Create and activate a virtual environment
python -m venv virtenv
virtenv\Scripts\activate        # Windows
# source virtenv/bin/activate   # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the app
python signs.py
```

Then open `http://127.0.0.1:8000` in your browser.

> The app runs on port **8000** by default. If that port is unavailable, change the port in the `app.run(...)` call at the bottom of `signs.py`.

## Building the Executable

From the project folder, with the virtual environment active:

```bash
pip install pyinstaller      # only if not already installed
pyinstaller app.spec
```

After a few seconds, a `dist` folder is created containing `signs.exe`.

- `app.spec` holds the PyInstaller settings that `signs.exe` needs to run correctly.
- `signs.py` contains the application logic.

## Database

If no database exists, the application creates one automatically and stores all records there. When running the executable, the database appears in the `dist` folder.

> **Tip:** Delete documents that are no longer needed (use *Complete Document*). A smaller database keeps the app fast.

## Project Structure

```
.
├── signs.py             # Main application: routes and database logic
├── app.spec             # PyInstaller configuration
├── requirements.txt     # Python dependencies
├── migrations/          # Database migration files
├── static/
│   └── index.js         # Client-side JavaScript
└── templates/           # HTML templates
    ├── index.html
    ├── record_info.html
    ├── update_record.html
    ├── delete_confirmation.html
    ├── delete_record.html
    └── all_records.html
```

## How the Code Works

`signs.py` handles the core functionality and communication with the database. Each feature has its own function, which does its work and then renders the matching HTML template with `render_template`.

| Function | Purpose |
|---|---|
| `create_record` | Checks that the id contains only digits and doesn't already exist, then creates the document. Shows an error otherwise. |
| `record_info` | Finds the document by id and shows its information, or an error if not found. |
| `update` | Updates the document with the given id. |
| `delete_record` | Looks up the document and, if it exists, asks for confirmation via `delete_confirmation.html`. |
| `delete_confirmed` | Deletes the document once the user confirms. |
| `all_info` | Shows all documents, or reports that the database is empty. |

### Templates

| File | Purpose |
|---|---|
| `index.html` | Home screen containing all the features |
| `record_info.html` | Shows the searched document, or a "not found" message |
| `update_record.html` | Confirms an update, or reports that the document doesn't exist |
| `delete_confirmation.html` | Asks for confirmation before deleting, or reports that the document doesn't exist |
| `delete_record.html` | Confirms that the document was deleted |
| `all_records.html` | Shows all documents, or reports that the database is empty |

## Configuration

- **Password:** access to the app is password-protected. The password is defined in `static/index.js`. Change it before deploying.
- **Port:** set in the `app.run(...)` call in `signs.py` (default `8000`).

## Author

**KOSTAS XENAKOUDIS**
[GitHub](https://github.com/KosXen) | [LinkedIn](https://www.linkedin.com/in/kostas-xenakoudis-851134228/)
