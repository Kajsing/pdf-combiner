# PDF Merger Script

A Python script that scans a folder for PDF files and merges them into a single PDF file. This is a lightweight and efficient tool for automating PDF file organization.

## Features
- Automatically scans a specified folder for `.pdf` files.
- Merges all found PDF files into a single output file.
- Alphabetical sorting of PDF files for predictable merging order.
- Easy to configure and run.

## Requirements
- Python 3.6 or later
- `PyPDF2` library

### Install Dependencies
Run the following command to install the required library:
```bash
pip install PyPDF2
```

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pdf-merger-script.git
   cd pdf-merger-script
   ```

2. Run the script with the following command, specifying the folder containing your PDF files and the desired output filename:
   ```bash
   python pdf_merger.py /path/to/your/folder output.pdf
   ```

3. The merged PDF file will be saved with the name you provided (e.g., `output.pdf`).

## Customization
- **Folder Path**: Provide the folder path as an argument when running the script.
- **Output File Name**: Specify the desired output file name as an argument when running the script.

## Example
Imagine you have the following files in your folder:
```
/example_folder
  - doc1.pdf
  - doc2.pdf
  - appendix.pdf
```
Running the script with:
```bash
python pdf_merger.py /example_folder combined.pdf
```
will produce a new file called `combined.pdf`, containing the pages of all these files in the specified order.

## Contributing
Contributions are welcome! If you find any bugs or want to improve the script, feel free to submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Built using the [PyPDF2](https://pypi.org/project/PyPDF2/) library.
