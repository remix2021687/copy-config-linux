import shutil
import argparse
import sys
from datetime import datetime
from pathlib import Path

def copy_and_overwrite(src: str, dist: str, backup: bool = True):
    src_path = Path(src).expanduser().resolve()
    dist_path = Path(dist).expanduser().resolve()

    if not src_path.exists():
        print(f"Bad path {src} dont exist")
        sys.exit(1)

    if dist_path.exists() and backup:
        backup_path = dist_path.with_name(f"{dist_path.name}_backup_{datetime.now():%Y%m%d_%H%M%S}")
        print(f"Create backup: {backup_path}")
        shutil.copytree(dist_path, backup_path)

    if dist_path.exists():
        if dist_path.is_dir():
            print(f"Remove old folder: {dist_path}")
            shutil.rmtree(dist_path)
        else:
            print(f"Removing old file {dist_path}")
            dist_path.unlink()

    if src_path.is_dir():
        print(f"Copy folder: {src_path} > {dist_path}")
        shutil.copytree(src_path, dist_path)
    else:
        print(f"Copy file: {src_path} > {dist_path}")
        shutil.copy2(src_path, dist_path)

    print("Copy cfg files is completed")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Copy files/directories with overwrite + backup")
    parser.add_argument("source", help="Source file/folder")
    parser.add_argument("dest", help='Destination path')
    parser.add_argument('-n', "--non_backup", action="store_true", help="Disable automation backup")

    args = parser.parse_args()

    copy_and_overwrite(args.source, args.dest, backup=not args.non_backup)





