import os
import argparse
from PyPDF2 import PdfMerger

def merge_pdfs_in_folder(folder_path, output_filename):
    """
    Scanner en mappe for PDF-filer og samler dem til én PDF-fil.

    Args:
        folder_path (str): Sti til mappen, der skal scannes.
        output_filename (str): Navn på outputfilen.
    """
    merger = PdfMerger()

    try:
        # Find alle PDF-filer i mappen
        pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

        # Sorter filerne alfabetisk for en fastlagt rækkefølge
        pdf_files.sort()

        if not pdf_files:
            print("Ingen PDF-filer fundet i mappen.")
            return

        print("Følgende PDF'er blev fundet og vil blive samlet:")
        for pdf in pdf_files:
            print(f"- {pdf}")
            merger.append(os.path.join(folder_path, pdf))

        # Gem den samlede PDF
        merger.write(output_filename)
        merger.close()
        print(f"PDF'er blev samlet succesfuldt til: {output_filename}")

    except Exception as e:
        print(f"Fejl under sammensætning: {e}")

if __name__ == "__main__":
    # Definer argumenter for scriptet
    parser = argparse.ArgumentParser(description="Saml PDF-filer fra en mappe til én PDF-fil.")
    parser.add_argument("folder", type=str, help="Stien til mappen, der indeholder PDF-filerne.")
    parser.add_argument("output", type=str, help="Navnet på output PDF-filen, inklusiv filtypen.")

    args = parser.parse_args()

    # Kør funktionen med de angivne argumenter
    merge_pdfs_in_folder(args.folder, args.output)
