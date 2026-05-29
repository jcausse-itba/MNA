import re
from pathlib import Path

TAB_SIZE_SPACES = 4

def generate_toc(target_dir: Path, output_file: Path) -> str:
    if not target_dir.exists():
        raise FileNotFoundError(f"Error: The directory '{target_dir}' does not exist.")

    md_files = sorted(
        [f for f in target_dir.glob("*.md")]
    )

    if not md_files:
        raise FileNotFoundError("No markdown files found in the directory.")

    toc_lines = ["# Indice\n"]

    # Regular expression to match #, ##, and ### headings
    # Ensures it only matches up to 3 hashtags followed by a space
    heading_pattern = re.compile(r"^(#{1,3})\s+(.+)$")

    for file_path in md_files:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                match = heading_pattern.match(line.strip())
                if match:
                    hashes, heading_text = match.groups()
                    level = len(hashes)

                    # Determine indentation based on heading level
                    # Level 1 (#)   -> 0 indents
                    # Level 2 (##)  -> 1 indent  (4 spaces)
                    # Level 3 (###) -> 2 indents (8 spaces)
                    indent = ' ' * (TAB_SIZE_SPACES * (level - 1))

                    # Format line: [indent]* [Heading Text](filename.md#anchor)
                    toc_line = f"{indent}* {heading_text}"
                    toc_lines.append(toc_line)

    # Write the collected TOC to index.md
    with open(output_file, "w", encoding="utf-8") as out_f:
        output = "\n".join(toc_lines) + "\n"
        out_f.write(output)

    return output
