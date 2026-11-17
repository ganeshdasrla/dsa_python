# DSA in Python

A hands-on project for learning data structures and algorithms, with examples,
tests, a virtual environment, and VS Code debugging. Requires Python 3.10+.

## Setup (Windows PowerShell)

The current workspace already has `.venv`. To recreate it in a fresh clone:

```powershell
python -m venv .venv
```

If `python` opens the Microsoft Store or fails, use `py -m venv .venv`, or
invoke your installed Python executable by its full path.

Install this project into its virtual environment once:

```powershell
.\.venv\Scripts\python.exe -m pip install -e .
```

This editable install makes `src/dsa_python` importable and picks up your code
changes immediately. Algorithms and tests use only the Python standard library;
installation may download the setuptools build tool.

Optional activation lets you type `python` instead of the full path:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use the full `.venv` interpreter path below.

## Run and test

```powershell
.\.venv\Scripts\python.exe main.py
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

## Debug in VS Code

1. Open this project folder. Install the recommended Python and Python Debugger
   extensions if prompted.
2. Run **Python: Select Interpreter** from Ctrl+Shift+P and select
   `.venv\Scripts\python.exe`.
3. Open an algorithm file, such as `src/dsa_python/heap_sort.py`, and set a
   breakpoint beside a line inside the algorithm.
4. Press F5 and choose **Debug active Python file (F5)**. The debugger uses the
   file currently open in the editor. Every supplied algorithm has a `main()`
   example at the bottom, so only that file runs. Use F10 to step over, F11 to
   step into, and the Variables/Watch panels to inspect values.
5. Use **Debug all tests** to step through tests. The Testing panel also supports
   running and debugging individual tests.

`main.py` intentionally runs all algorithm examples. Open it and press F5 only
when you want the complete project demo.

When you add a new algorithm, include the same `main()` pattern so the file can
be run and debugged independently:

```python
def main() -> None:
    values = [4, 1, 3, 2]
    print(your_algorithm(values))


if __name__ == "__main__":
    main()
```

## Project structure

```text
src/dsa_python/
    searching.py       # linear search and binary search
    sorting.py         # bubble sort
    heap_sort.py       # max-heap sort; runnable debugging example
    stack.py           # generic LIFO stack
tests/                 # unittest examples and edge cases
docs/learning-path.md  # topic roadmap and debugging exercise
main.py                # runnable examples
pyproject.toml         # editable package configuration
.vscode/               # interpreter, debugger and test discovery
```

Follow [the learning path](docs/learning-path.md) and add one topic at a time.

## GitHub

Create an empty repository on GitHub, leaving its README, license, and gitignore
options unselected. In a fresh folder, initialize Git with `git init -b main`.
Configure your real commit identity if needed, then publish:

```powershell
git config user.name "YOUR NAME"
git config user.email "YOUR VERIFIED OR GITHUB NOREPLY EMAIL"
git add .
git commit -m "Set up Python DSA learning project"
git remote add origin https://github.com/YOUR_USERNAME/DSA_Python.git
git push -u origin main
```

Replace the placeholders before running these commands. Git Credential Manager
can prompt you to sign in. `.venv`, caches, build files, and `.env` files are
excluded from version control.

For later practice sessions:

```powershell
git add src tests docs README.md
git commit -m "Describe the algorithm or exercise you added"
git push
```
