from PyPDF2 import PdfReader

def extract_number_initial(reader):
    text = reader.pages[0].extract_text()
    if not text:
        raise ValueError("Número da página do Ministério Público da União não pode ser extraído.")

    for line in text.split("\n"):
        if "Ministério Público da União" in line:
            try:
                return int(line.split()[-1])
            except ValueError:
                continue
    raise ValueError("Ministério Público da União não encontrado.")

def search_procuradoria(reader, start_page):
    num_pages = len(reader.pages)
    for page_num in range(start_page, num_pages):
        text = reader.pages[page_num].extract_text()
        if not text:
            continue
        lines = text.split("\n")
        if "PROCURADORIA DA REPÚBLICA NO DISTRITO FEDERAL" in text:
            index_init = lines.index("PROCURADORIA DA REPÚBLICA NO DISTRITO FEDERAL")
            for i in range(index_init, len(lines)):
                line = lines[i]
                if line.startswith("PROCURADORIA") and "ESTADO" not in line:
                    print(line)

                if i > index_init and "ESTADO" not in line:
                    print(line)

                if "ESTADO" in line:
                    break
            break

def main():
    pdf_src = "01-08-2025.pdf"
    reader = PdfReader(pdf_src)

    try:
        start_page = extract_number_initial(reader)
        search_procuradoria(reader, start_page)
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()