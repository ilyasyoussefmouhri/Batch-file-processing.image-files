import argparse
from processor import batch_process_files

def main():
 # Setup argument parser
    parser = argparse.ArgumentParser(description='Batch process images: rename, convert, and organize')
    parser.add_argument('folder_path', type=str, help='Path to the folder containing files to process')
    
    args = parser.parse_args()
    
    print(f"Processing files in: {args.folder_path}")
    batch_process_files(args.folder_path)
    print("\nCheck the folder to see the results!")


if __name__ == "__main__":
   main()
