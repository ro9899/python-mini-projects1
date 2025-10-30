"""
pdf_compare.py

Checks if two PDF files are identical in two ways:
1) Byte-for-byte identical (exact file equality)
2) If not identical bytes, compares extracted text content page-by-page
   (uses PyPDF2 to extract text; this helps detect PDFs that differ in metadata only)

Usage:
    python pdf_compare.py file1.pdf file2.pdf
"""
import sys
import hashlib

# PyPDF2 is used for text extraction if files are not byte-equal.
# Install: pip install PyPDF2
try:
    from PyPDF2 import PdfReader
except Exception:
    PdfReader = None


def file_hash(path, chunk_size=8192):
    """Return SHA256 hash of a file (used for quick byte-equality check)."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def extract_text(path):
    """Extract concatenated text from all pages of a PDF using PyPDF2.
    Returns a single string (lowercased and stripped) for comparison.
    If PyPDF2 is not available, returns None.
    """
    if PdfReader is None:
        return None
    try:
        reader = PdfReader(path)
        texts = []
        for page in reader.pages:
            # page.extract_text() returns text or None
            text = page.extract_text() or ""
            texts.append(text)
        full = "\n".join(texts)
        # Normalize whitespace and lowercase to make comparison a bit tolerant
        return " ".join(full.split()).strip().lower()
    except Exception:
        return None


def compare_pdfs(path1, path2):
    """Compare two PDFs and print results."""
    # 1) Quick byte-hash check
    h1 = file_hash(path1)
    h2 = file_hash(path2)
    if h1 == h2:
        print("Result: Files are byte-for-byte identical.")
        return

    print("Files differ at byte-level (different hashes).")

    # 2) Try text extraction comparison if possible
    text1 = extract_text(path1)
    text2 = extract_text(path2)

    if text1 is None or text2 is None:
        print("Text extraction not available or failed. Can't compare content.")
        print("Suggestion: install PyPDF2 (`pip install PyPDF2`) to compare text content.")
        return

    if text1 == text2:
        print("Result: Files differ as files but textual content is identical.")
    else:
        print("Result: Textual content differs between the two PDFs.")

    # Optionally show short diff-ish summary
    # show first 300 chars of each (for quick human check)
    print("\n--- Sample from file1 (first 300 chars) ---")
    print(text1[:300] + ("..." if len(text1) > 300 else ""))
    print("\n--- Sample from file2 (first 300 chars) ---")
    print(text2[:300] + ("..." if len(text2) > 300 else ""))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pdf_compare.py file1.pdf file2.pdf")
        sys.exit(1)
    path_a = sys.argv[1]
    path_b = sys.argv[2]
    compare_pdfs(path_a, path_b)
