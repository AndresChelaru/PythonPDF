#!/usr/bin/env python
#Instalamos la libreria con pip.
import PyPDF2

#Abrir archivo PDF, decir el número de páginas y abrir la primera.

def main(args):
	with open("archivo_ejemplo.pdf", "rb") as archivo:
		reader = PyPDF2.PdfReader(archivo)
		# Número de páginas
		print("Número de páginas:", len(reader.pages))
		# Obtener texto de la primera página
		page = reader.pages[0]
		print(page.extract_text())

#Abrir archivo PDF y ver las páginas elegidas.

	with open("archivo_ejemplo.pdf", "rb") as archivo:
		reader = PyPDF2.PdfReader(archivo)
		
		# Definir las páginas de las cuales quieres extraer texto (en este caso páginas 2 a 5)
		for i in range(1, 5):
			pagina = reader.pages[i]
			texto = pagina.extract_text()
			print(f"Texto de la página {i + 1}:\n{texto}\n")

#Combinar dos archivos PDF diferentes.
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

#Poner contraseña a un archivo PDF.

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
