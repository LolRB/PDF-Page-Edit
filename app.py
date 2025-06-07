"""
Este script permite agregar números de página a un conjunto de archivos PDF.

Utilizando las bibliotecas PyPDF2 y reportlab, el programa procesa todos los archivos PDF de la
carpeta de entrada, agrega números de página al pie de cada página en el formato "Página 1",
"Página 2", etc., y guarda el resultado en una carpeta de salida especificada. El script verifica
si el archivo ya ha sido procesado previamente para evitar procesar el mismo archivo más de una vez.

El script utiliza la función `enumerate` para iterar sobre las páginas del PDF y
agregar los números de página de manera eficiente y legible.

Dependencias:
- PyPDF2: Para leer y escribir archivos PDF.
- reportlab: Para generar el contenido de los números de página en un PDF temporal.

Funcionamiento:
1. Leer los archivos PDF de la carpeta de entrada.
2. Agregar los números de página a cada archivo PDF.
3. Verificar si el archivo ya fue procesado (si existe en la carpeta de salida).
4. Guardar el archivo procesado en la carpeta de salida, con un sufijo "-PROCESADO" en el nombre.

Uso:
1. Coloca todos los archivos PDF a procesar en la carpeta de entrada.
2. El archivo de salida se guardará en la carpeta de salida con los números de página agregados.

Ejemplo:
    input_folder = "C:/Ruta/a/carpeta/de/entrada"
    output_folder = "C:/Ruta/a/carpeta/de/salida"
    process_all_pdfs(input_folder, output_folder)

Notas:
- Si un archivo PDF ya existe en la carpeta de salida, será ignorado para evitar duplicados.
- Los nombres de los archivos procesados se mantienen igual,
    pero se les agrega el sufijo "-PROCESADO" al nombre del archivo.
"""

import os
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PyPDF2 import PdfReader, PdfWriter

# Constantes para las rutas de los archivos de entrada y salida
INPUT_FOLDER = (
    "C:/Users/rbueno/Documents/PDF's-Crudos"  # Carpeta que contiene los PDFs de entrada
)
OUTPUT_FOLDER = (
    "C:/Users/rbueno/Documents/PDF's-Procesados"  # Carpeta donde guarda PDFs procesados
)


def add_page_numbers(input_pdf, output_pdf):
    """
    Agrega números de página al pie de cada página en el PDF de entrada
    y guarda el resultado en el PDF de salida.

    Args:
        input_pdf (str): La ruta del archivo PDF de entrada
            al que se le agregarán los números de página.

        output_pdf (str): La ruta del archivo PDF de salida
            donde se guardará el PDF con los números de página.

    Returns:
        None
    """
    # Verificar si la carpeta de salida existe, si no, crearla
    output_dir = os.path.dirname(output_pdf)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"✅ Se ha creado la carpeta: {output_dir}")

    print(f"📄 Procesando el archivo: {input_pdf}")
    print(f"💾 Guardando el archivo procesado en: {output_pdf}")

    # Leer el PDF existente
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # Iterar sobre las páginas en el PDF utilizando enumerate
    for i, page in enumerate(reader.pages):
        # Crear un PDF temporal para contener los números de página
        packet = BytesIO()
        c = canvas.Canvas(packet, pagesize=letter)

        # Crear el texto del número de página y dibujarlo en el pie de página
        c.setFont("Helvetica", 12)
        page_num_text = f"Página {i + 1}"
        c.drawString(
            500, 10, page_num_text
        )  # Posición para pie de página, se pueden ajustar X y Y
        c.showPage()  # Termina la página actual en el canvas

        # Finalizar el PDF en el buffer
        c.save()  # Guardar el contenido de la página en el buffer

        # Volver al inicio del buffer BytesIO
        packet.seek(0)

        # Crear un nuevo PDF con el número de página y fusionarlo con la página original
        page_number_pdf = PdfReader(packet)
        page.merge_page(page_number_pdf.pages[0])

        # Añadir la página modificada al escritor de salida
        writer.add_page(page)

    # Escribir el contenido modificado en un nuevo archivo
    try:
        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)
        print(
            f"✅ Números de página agregados con éxito. Archivo se guardó como '{output_pdf}'."
        )

    except ValueError as e:
        print(f"⚠️ Error al guardar el archivo: {e}")


def process_all_pdfs(input_folder, output_folder):
    """
    Procesa todos los archivos PDF en la carpeta de entrada y los guarda con números de página
    en la carpeta de salida, evitando procesar los que ya han sido procesados.

    Args:
        input_folder (str): Carpeta que contiene los archivos PDF de entrada.
        output_folder (str): Carpeta donde se guardarán los archivos PDF procesados.

    Returns:
        None
    """
    # Verificar si la carpeta de salida existe, si no, crearla
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"✅ Se ha creado la carpeta de salida: {output_folder}")

    # Iterar sobre todos los archivos en la carpeta de entrada
    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):  # Solo procesar archivos .pdf
            input_pdf = os.path.join(input_folder, filename)

            # Crea el nombre del archivo procesado en la carpeta de salida con sufijo "-PROCESADO"
            output_pdf = os.path.join(
                output_folder, f"{os.path.splitext(filename)[0]}-PROCESADO.pdf"
            )

            # Verificar si el archivo ya ha sido procesado (si existe en la carpeta de salida)
            if os.path.exists(output_pdf):
                print(f"⚡ El archivo '{filename}' ya ha sido procesado. Saltando...")
                continue  # Saltar este archivo

            # Llamar a la función para agregar números de página
            add_page_numbers(input_pdf, output_pdf)


# Ejecutar el procesamiento de todos los PDFs en la carpeta de entrada
print("🔄 Iniciando el procesamiento de archivos...")
process_all_pdfs(INPUT_FOLDER, OUTPUT_FOLDER)
print("✅ ¡El procesamiento ha terminado con éxito!")
