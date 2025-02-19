#!/usr/bin/env python
import PyPDF2


def main(args):
	with open("archivo_contraseña.pdf", "rb") as archivo:
		reader = PyPDF2.PdfReader(archivo)
		writer = PyPDF2.PdfWriter()

    # Añadir todas las páginas al escritor
		for pagina in reader.pages:
			writer.add_page(pagina)

    # Añadir una contraseña al PDF
		writer.encrypt("contraseña")

    # Guardar el PDF con la contraseña
		with open("archivo_protegido.pdf", "wb") as salida:
			writer.write(salida)

	print("Archivo PDF protegido con contraseña.")
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
