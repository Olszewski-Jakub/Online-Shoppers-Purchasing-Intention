#!/usr/bin/env python3
"""Package runtime project files and reports for a milestone submission."""

import argparse
import os
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


PROJECT_ROOT = Path(__file__).resolve().parent.parent
SUBMISSION_DIRECTORIES = {"data", "notebooks", "src", "reports"}
ROOT_FILES = {"README.md", "pyproject.toml", "uv.lock"}
EXCLUDED_DIRECTORIES = {
    ".git", ".idea", ".vscode", ".venv", "venv", "env", "__pycache__",
    ".ruff_cache", ".pytest_cache", ".mypy_cache", ".ipynb_checkpoints",
    "build", "dist", "htmlcov", "node_modules",
}


def milestone_number(value: str) -> str:
    value = value.strip()
    if not value.isascii() or not value.isdecimal() or int(value) < 1:
        raise argparse.ArgumentTypeError("milestone must be a positive integer")
    return str(int(value))


def excluded(path: Path) -> bool:
    return (
        path.is_symlink()
        or path.name in {".DS_Store", "Thumbs.db", ".gitkeep", "coverage.xml"}
        or path.name.startswith(".coverage")
        or (path.name.startswith(".env") and path.name not in {".env.example", ".env.template"})
        or path.suffix.lower() in {".pyc", ".pyo", ".zip"}
    )


def write_archive(destination: Path) -> None:
    # Exclusive creation prevents accidentally replacing a previous submission.
    with ZipFile(destination, "x", compression=ZIP_DEFLATED) as archive:
        for path in sorted(PROJECT_ROOT.iterdir()):
            if path.is_file() and not excluded(path):
                if path.name in ROOT_FILES or path.suffix == ".py":
                    archive.write(path, path.name)

        for name in sorted(SUBMISSION_DIRECTORIES):
            directory = PROJECT_ROOT / name
            if not directory.is_dir() or directory.is_symlink():
                continue
            for current, directories, files in os.walk(directory):
                directories[:] = sorted(
                    name for name in directories
                    if name not in EXCLUDED_DIRECTORIES
                    and not name.endswith(".egg-info")
                    and not excluded(Path(current) / name)
                )
                current = Path(current)
                # Preserve empty project directories without their .gitkeep files.
                archive.write(current, current.relative_to(PROJECT_ROOT).as_posix() + "/")
                for name in sorted(files):
                    path = current / name
                    if not excluded(path):
                        archive.write(path, path.relative_to(PROJECT_ROOT))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("milestone", nargs="?", type=milestone_number,
                        help="positive milestone number (prompted if omitted)")
    args = parser.parse_args()
    number = args.milestone
    if number is None:
        try:
            number = milestone_number(input("Milestone number: "))
        except (argparse.ArgumentTypeError, EOFError) as error:
            parser.error(str(error))
    destination = PROJECT_ROOT / f"23710521_Milestone{number}.zip"
    try:
        write_archive(destination)
    except FileExistsError:
        parser.error(f"archive already exists: {destination}")
    print(f"Created {destination}")


if __name__ == "__main__":
    main()
