from pathlib import Path
from indexer import generate_toc
from combiner import combine_md

TARGET_DIR = Path('./markdown/')
HEADING_FILE = Path('./markdown/heading.md')
INDEX_FILE = Path('./markdown/index.md')
OUTPUT_FILE = Path('./markdown/Resumen.md')

def get_markdown_files(target_dir: Path) -> list[Path]:
    IGNORED_FILES = [INDEX_FILE.name, HEADING_FILE.name, OUTPUT_FILE.name]

    if not target_dir.exists():
        raise FileNotFoundError(f"Error: The directory '{target_dir}' does not exist.")

    md_files = sorted(
        [f for f in target_dir.glob("*.md") if f.name not in IGNORED_FILES]
    )

    if not md_files:
        raise FileNotFoundError("No markdown files found in the directory.")

    return md_files

def main():
    try:
        md_files = get_markdown_files(TARGET_DIR)
        generate_toc(md_files, INDEX_FILE)
        combine_md(md_files, [HEADING_FILE, INDEX_FILE], OUTPUT_FILE)
    except (FileNotFoundError, PermissionError) as error:
        print(error)
        return

if __name__ == '__main__':
    main()
