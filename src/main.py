from pathlib import Path
from indexer import generate_toc
from combiner import combine_md

def main():
    target_dir = Path('./markdown/')
    index_file = Path('./markdown/index.md')
    output_file = Path('./markdown/Resumen.md')
    
    try:
        print(generate_toc(target_dir, index_file))
        print()
        print(combine_md(target_dir, [index_file], output_file))
    except FileNotFoundError as e:
        print(e)
        return

if __name__ == '__main__':
    main()
