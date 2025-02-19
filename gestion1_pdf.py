#!/usr/bin/env python
import PyPDF2

def main(args):
	with open("archivo_ejemplo.pdf", "rb") as archivo:
		reader = PyPDF2.PdfReader(archivo)
		# Número de páginas
		print("Número de páginas:", len(reader.pages))
		# Obtener texto de la primera página
		page = reader.pages[0]
		print(page.extract_text())
		
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
