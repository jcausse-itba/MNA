from pathlib import Path

def combine_md(md_files: list[Path], prepend_files: list[Path], output_file: Path) -> None:

    file_list = prepend_files + md_files
    
    output = ''
    total_lines = 0
    
    with open(output_file, "w", encoding="utf-8") as out_f:
        for file_path in file_list:
            
            output += file_path.name + ': '
            line_count = 0
            
            with open(file_path, "r", encoding="utf-8") as in_f:
                for line in in_f:
                    out_f.write(line)
                    line_count += 1
                line_count -= 1

            out_f.write('\n')
            out_f.write('---')
            out_f.write('\n')
            line_count += 3
            
            output += f'- {line_count} lines written\n'
            total_lines += line_count
            
    print(output + f'Total lines written: {total_lines}')
