# Student Grade Manager CLI

A command-line tool to manage student grades with persistent JSON storage.

## Usage

```bash
python src/cli.py add "Eren" 95
python src/cli.py list
python src/cli.py remove "Eren"
```

## Project Structure

- `src/models.py` — Student class
- `src/storage.py` — JSON persistence
- `src/cli.py` — CLI interface