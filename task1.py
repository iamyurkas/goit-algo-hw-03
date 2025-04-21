import os
import shutil
import argparse
from pathlib import Path

def copy_and_sort_files(src_dir, dest_dir):
    try:
        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)

            if os.path.isdir(item_path):
                # Inner folders
                copy_and_sort_files(item_path, dest_dir)

            elif os.path.isfile(item_path):
                # get extension or 'no_extension'
                ext = Path(item_path).suffix[1:] or 'no_extension'
                target_folder = os.path.join(dest_dir, ext)

                os.makedirs(target_folder, exist_ok=True)

                try:
                    shutil.copy2(item_path, target_folder)
                    print(f"[✓] Copied: {item_path} → {target_folder}")
                except Exception as e:
                    print(f"[!] Copy error {item_path}: {e}")

    except Exception as e:
        print(f"[!] Access error {src_dir}: {e}")

def main():
    """
    Run
        python sort_files_by_extension.py <source_directory> [destination_directory]

        <source_directory>       - mandatory argument, path to a source directory
        [destination_directory]  - not mandatory argument, path to a target directory
                                   (./dist by default)
    """
    
    parser = argparse.ArgumentParser(description="Copy & sort.")
    parser.add_argument("source", help="Source directory path")
    parser.add_argument("destination", nargs='?', default="dist", help="Target directory path ('dist' by defailt)")

    args = parser.parse_args()
    src_dir = os.path.abspath(args.source)
    dest_dir = os.path.abspath(args.destination)

    print(f"[D] Source directory: {src_dir}")
    print(f"[D] Target directory: {dest_dir}\n")

    if not os.path.exists(src_dir):
        print(f"[✗] No initial directory: {src_dir}")
        return

    os.makedirs(dest_dir, exist_ok=True)
    copy_and_sort_files(src_dir, dest_dir)
    print("\n[✓] Copied and sorted")

if __name__ == "__main__":
    main()
