from pathlib import Path
from PIL import Image
from datetime import datetime
import shutil


def batch_process_files(folder_path):
    """Main function to process all files
    
    Args:
        folder_path: Path to the folder containing files to process
    """
    
    # Convert to Path object if string is passed
    folder_path = Path(folder_path)
    
    if not folder_path.exists():
        print(f"Error: Folder '{folder_path}' doesn't exist!")
        return
    
    if not folder_path.is_dir():
        print(f"Error: '{folder_path}' is not a directory!")
        return
    
    # Create subdirectories for organizing before processing
    original_jpg_dir = folder_path / 'original_jpg'
    converted_jpg_dir = folder_path / 'converted_jpg'
    original_jpg_dir.mkdir(exist_ok=True)
    converted_jpg_dir.mkdir(exist_ok=True)
    
    # Get all files in the directory (excluding subdirectories)
    files = [f for f in folder_path.iterdir() if f.is_file()]
    
    # Get current date for naming
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Rename, convert, and organize
    for i, file in enumerate(files, start=1):
        original_suffix = file.suffix.lower()
        
        # Create new name with sequential numbering
        new_name = f'product_{today}_{i:03d}'
        
        # Check if file is PNG (needs conversion)
        if original_suffix == '.png':
            # Convert PNG to JPG
            print(f"Converting {file.name} to JPG...")
            
            # Open the PNG image
            img = Image.open(file)
            
            # Convert RGBA to RGB if necessary (PNG can have transparency)
            if img.mode == 'RGBA':
                # Create white background
                rgb_img = Image.new('RGB', img.size, (255, 255, 255))
                rgb_img.paste(img, mask=img.split()[3])  # Use alpha channel as mask
                img = rgb_img
            
            # Save as JPG in the converted directory
            new_file_path = converted_jpg_dir / f'{new_name}.jpg'
            img.save(new_file_path, 'JPEG', quality=95)
            img.close()
            
            # Remove original PNG file
            file.unlink()
            print(f"  → Converted and saved as {new_file_path.name}")
            
        else:
            # Original JPG/JPEG files - just rename and move
            # Normalize extension to .jpg
            new_file_path = original_jpg_dir / f'{new_name}.jpg'
            
            # If it's .jpeg, we need to handle conversion for consistency
            if original_suffix == '.jpeg':
                img = Image.open(file)
                img.save(new_file_path, 'JPEG', quality=95)
                img.close()
                file.unlink()
                print(f"Renamed and moved {file.name} → {new_file_path.name}")
            else:
                # Just rename and move .jpg files
                shutil.move(str(file), str(new_file_path))
                print(f"Moved {file.name} → {new_file_path.name}")
    
    print("\n✓ Batch processing complete!")
    print(f"✓ Original JPGs in: {original_jpg_dir}")
    print(f"✓ Converted JPGs in: {converted_jpg_dir}")
