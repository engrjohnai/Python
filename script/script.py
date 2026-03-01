import re
from pathlib import Path
from typing import Optional


def resolve_target_directory() -> Path:
    """
    Resolve the directory where this script is located.
    Works on Windows, WSL, and Linux.
    """
    try:
        return Path(__file__).resolve().parent
    except NameError:
        return Path.cwd()


def extract_first_docstring_block(content: str) -> Optional[re.Match]:
    """
    Return the first triple-quoted docstring match object.
    """
    pattern = r'"""(.*?)"""'
    return re.search(pattern, content, re.DOTALL)


def normalize_text(text: str) -> str:
    """
    Normalize text for safe comparison.
    """
    return text.strip().replace("\r\n", "\n").strip()


def ensure_readme_matches_docstring(folder: Path, py_file: Path) -> None:
    """
    Ensure:
    - If docstring exists and README matches -> remove docstring
    - If docstring exists and README missing/mismatch -> create/update README then remove docstring
    - If no docstring -> skip
    """

    readme_path = folder / "README.md"

    try:
        content = py_file.read_text(encoding="utf-8")
    except Exception as e:
        print(f"[ERROR] Could not read {py_file}: {e}")
        return

    match = extract_first_docstring_block(content)

    if not match:
        print(f"[SKIP] No docstring found: {py_file}")
        return

    docstring_raw = match.group(1)
    docstring_clean = docstring_raw.strip("\n")

    readme_exists = readme_path.exists()

    readme_matches = False

    if readme_exists:
        try:
            readme_content = readme_path.read_text(encoding="utf-8")
            readme_matches = normalize_text(readme_content) == normalize_text(docstring_clean)
        except Exception as e:
            print(f"[ERROR] Could not read README {readme_path}: {e}")
            return

    # If README does not exist or does not match, create/update it
    if not readme_exists or not readme_matches:
        try:
            readme_path.write_text(docstring_clean, encoding="utf-8")
            print(f"[OK] README created/updated: {readme_path}")
        except Exception as e:
            print(f"[ERROR] Could not write README {readme_path}: {e}")
            return
    else:
        print(f"[OK] README already matches docstring: {readme_path}")

    # Remove only the first docstring block
    new_content = content[:match.start()] + content[match.end():]

    try:
        py_file.write_text(new_content.lstrip("\n"), encoding="utf-8")
        print(f"[OK] Removed docstring from: {py_file}")
    except Exception as e:
        print(f"[ERROR] Could not update {py_file}: {e}")


def process_folders(base_dir: Path) -> None:
    """
    Traverse all subfolders.
    For each folder:
        If it contains <foldername>.py, validate and clean docstring.
    """

    for folder in base_dir.rglob("*"):
        if not folder.is_dir():
            continue

        py_file = folder / f"{folder.name}.py"

        if py_file.exists() and py_file.is_file():
            ensure_readme_matches_docstring(folder, py_file)


def main() -> None:
    base_dir = resolve_target_directory()

    if not base_dir.exists():
        print(f"[ERROR] Directory does not exist: {base_dir}")
        return

    print(f"[START] Reviewing folders in: {base_dir}")
    process_folders(base_dir)
    print("[DONE] Review complete.")


if __name__ == "__main__":
    main()