#!/usr/bin/env python
import PyPDF2

def main(args):
	with open("archivo_ejemplo.pdf", "rb") as archivo:
		reader = PyPDF2.PdfReader(archivo)
		
		# Definir las páginas de las cuales quieres extraer texto (en este caso páginas 2 a 5)
		for i in range(1, 5):
			pagina = reader.pages[i]
			texto = pagina.extract_text()
			print(f"Texto de la página {i + 1}:\n{texto}\n")
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
