# **Generación de Números de Página en Archivos PDF**

Este script permite agregar números de página a un conjunto de archivos PDF. Es muy útil cuando se necesitan numerar grandes cantidades de documentos para su organización o presentación.

## **Especificaciones**

- **Entrada**: Un conjunto de archivos PDF en una carpeta específica (carpeta de entrada).
- **Proceso**: El script agrega números de página en formato "Página 1", "Página 2", etc., en el pie de cada página de los PDFs.
- **Salida**: Los archivos procesados se guardan en otra carpeta (carpeta de salida) con el mismo nombre de archivo, pero con el sufijo `-PROCESADO` añadido al nombre del archivo.

### **Requisitos**

Este script necesita las siguientes herramientas instaladas en tu computadora:

- **Python 3** (Cualquier versión 3.7 o superior).
- **Bibliotecas de Python**: `PyPDF2` y `reportlab`.

## **Pasos para ejecutar el script**

### 1. **Instalar Python**

Si aún no tienes Python instalado, sigue estos pasos:

1. **Descarga Python** desde el sitio web oficial: [Python.org](https://www.python.org/downloads/).
2. Durante la instalación, asegúrate de **marcar la casilla "Add Python to PATH"** para que Python se pueda ejecutar desde la terminal de comandos.

### 2. **Instalar Dependencias**

El script requiere algunas bibliotecas de Python para funcionar correctamente. Para instalarlas, sigue estos pasos:

1. **Abre la terminal o el símbolo del sistema**.
   - En **Windows**, puedes hacerlo presionando `Win + R`, luego escribe `cmd` y presiona `Enter`.
   
2. **Navega a la carpeta donde se encuentra el script**:
   
   Usa el comando `cd` para cambiar a la carpeta donde se encuentra el archivo `app.py`. Por ejemplo:

    ```bash
   cd "C:\Users\rbueno\Documents\Optimizacion Prodep - Reportes\PDF-Page-Edit"
    ```

3. **Crea un entorno virtual** (opcional, pero recomendado):

    Si no tienes experiencia con entornos virtuales, este paso es opcional, pero ayuda a mantener las dependencias organizadas y evita conflictos con otras aplicaciones.

    Para crear el entorno virtual, ejecuta:

    ```bash
    python -m venv .venv
    ```

4. **Activa el entorno virtual:**

    - En Windows:

        ```bash
        .\venv\Scripts\activate
        ```
        
    - En macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. **Instala las bibliotecas necesarias:**

    Con el entorno virtual activo, instala las bibliotecas necesarias ejecutando el siguiente comando en la terminal:

    ```bash
    pip install PyPDF2 reportlab
    ```

### 3. **Configurar el Script**

Antes de ejecutar el script, debes asegurarte de tener las carpetas de entrada y salida configuradas correctamente.

1. **Carpeta de entrada**: Aseguráte de tener toddos los archivos PDF que deseas procesar en una carpeta específica.

    **Ejemplo**:

    - **Ruta**: `C:/Users/rbueno/Documents/PDF's-Crudos`

    - Todos los PDFs que deseas numerar deben estar en esta carpeta.

2. **Carpeta de salida**: El script guardará los archivos procesados en una carpeta de salida. El nombre de los archivos procesados tendrá el sufijo `-PROCESADO` al final.

    **Ejemplo**:

    - **Ruta**: `C:/Users/rbueno/Documents/PDF's-Procesados`

    - Esta carpeta debe existir, o el script la creará automáticamente si no existe.

    **IMPORTANTE**: Si ya existe un archivo con el mismo nombre en la carpeta de salida, el script lo ignorará para evitar procesarlo nuevamente.

### **4. Ejecutar el Script**

Una vez que tengas todo configurado, es hora de ejecutar el script. En la terminal, ejecuta el siguiente comando:

```bash
python app.py
```

El script comenzará a procesar todos los archivos PDF en la carpeta de entrada, agregando los números de página al pie de cada página. Los archivos procesados se guardarán automáticamente en la carpeta de salida con el sufijo `-PROCESADO` agregado.

### **5. Verificar los Archivos Procesados**

Una vez que el script termine de ejecutarse, podrás encontrar los archivos procesados en la carpeta de salida (`PDF's-Procesados`). Los nombres de los archivos serán los mismos que los originales, pero con el sufijo `-PROCESADO` agregado al nombre del archivo.

**Ejemplo**:

- Archivo original: `documento.pdf`

- Archivo procesado: `documento-PROCESADO.pdf`

### **6. Mensajes de Estado**

Durante la ejecución del script, verás mensajes en la terminal para indicar lo siguiente:

- ✅: El archivo ha sido procesado y guardado con éxito.

- ⚡: El archivo ya ha sido procesado previamente, por lo que se ha saltado.

- ⚠️: Si hubo algún error al guardar el archivo.

**Ejemplo de salida en la terminal**:

```swift
🔄 Iniciando el procesamiento de archivos...
📄 Procesando el archivo: C:/Users/rbueno/Documents/PDF's-Crudos/documento.pdf
💾 Guardando el archivo procesado en: C:/Users/rbueno/Documents/PDF's-Procesados/documento-PROCESADO.pdf
✅ Números de página agregados con éxito. El archivo procesado se guardó como 'C:/Users/rbueno/Documents/PDF's-Procesados/documento-PROCESADO.pdf'.
⚡ El archivo 'documento.pdf' ya ha sido procesado. Saltando...
✅ ¡El procesamiento ha terminado con éxito!
```

## Conclusión
Este script es una herramienta simple y eficiente para agregar números de página a múltiples archivos PDF en una carpeta. Sigue los pasos indicados para configurarlo y ejecutarlo, y podrás procesar todos tus archivos con facilidad.

Si tienes alguna pregunta o necesitas asistencia, no dudes en contactar al equipo de soporte.

## Notas Adicionales:

- **Python**: Asegúrate de tener instalada la versión correcta de Python (3.7 o superior).

- **Entorno Virtual**: Recomendamos el uso de un entorno virtual para gestionar las dependencias de manera más eficiente.

- **Carpetas**: El script maneja automáticamente la creación de la carpeta de salida si no existe, y evita procesar archivos ya procesados.

## 🧑‍💻 Author

Proyecto desarrollado por **Rodrigo Bueno**.  

Para preguntas o contribuciones, contáctame:

📧 [ztmsiul79@gmail.com](mailto:ztmsiul79@gmail.com)  

🐈‍⬛ [github.com/LolRB](https://github.com/LolRB)