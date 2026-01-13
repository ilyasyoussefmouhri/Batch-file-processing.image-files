from processor import setup_files
from processor import batch_process_files

def main():
   print("Step 1: Setting up practice files...")
    setup_files()
    
    print("\nStep 2: Processing files...")
    batch_process_files()
    
    print("\nCheck the 'photo_project' folder to see the results!")


if __name__ == "__main__":
   main()
