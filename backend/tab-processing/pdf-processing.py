import fitz  # PyMuPDF
import re
import numpy as np

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def parse_tab_text(raw_text):
    # Regex to match tab lines starting with e|, B|, G|, D|, A|, or E|
    tab_lines = re.findall(r'^[eBGDAE]\|[^\n]+', raw_text, re.MULTILINE)

    # Initialize tab matrix (6 strings)
    tab_matrix = [[] for _ in range(6)]

    # Map strings to index
    string_map = {'e|': 0, 'B|': 1, 'G|': 2, 'D|': 3, 'A|': 4, 'E|': 5}

    # Process each line
    for line in tab_lines:
        string_id = line[:2]  # Get string (e|, B|, etc.)
        frets = re.findall(r'[\dXx()-<>\uEAD8]+', line[2:])  # Extract frets (including muted X)

        # Convert frets to numbers or -1 for muted
        processed_frets = []
        for fret in frets:
            if fret in ('X', 'x'):
                processed_frets.append(-1)
            elif fret.isdigit():
                processed_frets.append(int(fret))
            else:
                # Handle slides (e.g., (1)), harmonics (<12>), etc.
                processed_frets.append(int(re.sub(r'[^\d]', '', fret)) if re.sub(r'[^\d]', '', fret) else -1)

        # Align frets to the correct string
        tab_matrix[string_map[string_id]].extend(processed_frets)

    # Pad strings to the same length
    max_length = max(len(s) for s in tab_matrix)
    tab_matrix = [s + [-1] * (max_length - len(s)) for s in tab_matrix]

    return np.array(tab_matrix).T  # Shape (time_steps, 6)


if __name__ == "__main__":  
    file_path = "pdf-tabs/ThinkingOutLoud.pdf"
    raw_text = extract_text_from_pdf(file_path)
    formatted_text = parse_tab_text(raw_text)
    print(formatted_text)
