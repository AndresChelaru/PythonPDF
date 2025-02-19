#!/usr/bin/env python
import PyPDF2

def main(args):
#import PyPDF2

# Crear un objeto PdfWriter para el archivo combinado
	writer = PyPDF2.PdfWriter()

# Abrir los archivos PDF que deseas unir
	try:
		with open("archivo_ejemplo.pdf", "rb") as archivo1:
			reader1 = PyPDF2.PdfReader(archivo1)
		# Añadir todas las páginas de archivo1
			for pagina in reader1.pages:
				writer.add_page(pagina)

		with open("archivo_ejemplo2.pdf", "rb") as archivo2:
			reader2 = PyPDF2.PdfReader(archivo2)
		# Añadir todas las páginas de archivo2
			for pagina in reader2.pages:
				writer.add_page(pagina)

	# Escribir el archivo combinado
		with open("archivo_combinado.pdf", "wb") as salida:
			writer.write(salida)

		print("Archivos combinados con éxito.")

	except Exception as e:
		print(f"Ocurrió un error: {e}")

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
