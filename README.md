# Batch Image Processor

A Python script for batch processing image files with automated renaming, format conversion, and organization.

## Features

- **Batch Renaming**: Renames all files with a consistent pattern (`product_YYYY-MM-DD_001.jpg`)
- **Format Conversion**: Automatically converts PNG files to JPG format
- **Smart Organization**: Separates files into two directories:
  - `original_jpg/` - Files that were originally JPG/JPEG
  - `converted_jpg/` - Files converted from PNG to JPG
- **Quality Preservation**: Maintains high image quality (95% JPEG quality)
- **Transparency Handling**: Properly converts PNG transparency to white background

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. Clone or download this repository

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Process all images in a folder:

```bash
python main.py /path/to/your/images
```

### Examples

```bash
# Process images in the current directory
python main.py .

# Process images in a specific folder
python main.py ./photo_project

# Process images with absolute path
python main.py /home/user/pictures/vacation
```

## What It Does

1. **Scans** the specified folder for image files (JPG, JPEG, PNG)
2. **Creates** two subdirectories: `original_jpg/` and `converted_jpg/`
3. **Renames** all files with the pattern: `product_YYYY-MM-DD_XXX.jpg`
   - YYYY-MM-DD is today's date
   - XXX is a sequential number (001, 002, 003...)
4. **Converts** PNG files to JPG format
5. **Organizes** files into appropriate directories based on their original format

## File Structure After Processing

```
your_folder/
├── original_jpg/
│   ├── product_2026-01-13_001.jpg
│   ├── product_2026-01-13_002.jpg
│   └── product_2026-01-13_003.jpg
└── converted_jpg/
    ├── product_2026-01-13_004.jpg
    └── product_2026-01-13_005.jpg
```

## Supported Formats

- **Input**: JPG, JPEG, PNG
- **Output**: JPG (standardized)

## Important Notes

- ⚠️ **Backup your files**: The script modifies and deletes original files. Always work on copies!
- The script processes only files in the specified directory (not subdirectories)
- PNG files with transparency are converted with a white background
- All output files use `.jpg` extension for consistency

## Error Handling

The script includes validation for:
- Non-existent folder paths
- Invalid directory paths
- File access issues

## Customization

You can modify the script to:
- Change the naming prefix (currently "product")
- Adjust JPEG quality (currently 95)
- Modify date format
- Add additional file formats
- Process subdirectories recursively

## Troubleshooting

**"Folder doesn't exist" error:**
- Check that the path is correct
- Use absolute paths if relative paths aren't working

**Permission denied errors:**
- Ensure you have write permissions for the folder
- On Unix systems, you may need to use `sudo` or change file permissions

**Module not found errors:**
- Run `pip install -r requirements.txt` to install dependencies

## License

This project is open source and available for personal and commercial use.

## Contributing

Feel free to fork, modify, and submit pull requests for improvements!
