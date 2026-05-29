from pathlib import Path
from indexer import generate_toc
from combiner import combine_md

def main():
    target_dir = Path('./markdown/')
    heading_file = Path('./markdown/heading.md')
    index_file = Path('./markdown/index.md')
    output_file = Path('./markdown/Resumen.md')
    
    try:
        generate_toc(target_dir, index_file)
        print()
        combine_md(target_dir, [heading_file, index_file], output_file)
    except FileNotFoundError as e:
        print(e)
        return

if __name__ == '__main__':
    main()
