# pyClean

**pyClean** is a Python-based utility designed to clean and optimize Windows systems by removing unnecessary files and directories. It aims to provide functionality similar to CCleaner, helping users free up disk space and enhance system performance.

## Features

- Deletes temporary files from user and system directories.
- Cleans Windows Prefetch folder.
- Empties the Recycle Bin.
- Provides a simple command-line interface for ease of use.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/samlkey/pyClean.git
   cd pyClean
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install any required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the `main.py` script to run the application:

```bash
python main.py
```

## Project Structure

```
pyClean/
├── lib/
├── methods/
├── ui/
├── main.py
├── README.md
├── requirements.txt
└── desktop.ini
```

- `lib/`, `methods/`, and `ui/` directories contain modular components of the application.
- `main.py` is the entry point of the application.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

*Note: Ensure you run the script with appropriate permissions to allow deletion of system files and directories.*
