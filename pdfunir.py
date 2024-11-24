#Para unir pdfs
import streamlit as st
from PyPDF2 import PdfMerger
from io import BytesIO

st.set_page_config(page_title="Unir PDFs")

def unirpdf(archivos):
    pdf_final = PdfMerger()
    for archivo in archivos:
        pdf_final.append(archivo)
    
    # Guardar el PDF unido en un objeto BytesIO
    salida = BytesIO()
    pdf_final.write(salida)
    pdf_final.close()
    salida.seek(0)
    return salida

def main():
     # Cargar múltiples archivos PDF
    st.title("Unir archivos PDF")
    archivos_datos = st.file_uploader("Sube tus PDFs aquí", type="pdf", accept_multiple_files=True)
    
    if archivos_datos:  # Mostrar los nombres de los archivos cargados
        st.write("Archivos cargados:")
        for archivo in archivos_datos:
            st.write(f"- {archivo.name}")
    
    # Botón para procesar la unión
    if st.button("Unir PDFs"):
        if archivos_datos:
            try:
                # Llamar a la función para unir PDFs
                pdf_unido = unirpdf(archivos_datos)
                
                # Botón de descarga para el archivo unido
                st.success("¡PDFs unidos con éxito!")
                st.download_button(
                    label="Descargar PDF Unido",
                    data=pdf_unido,
                    file_name="pdf_unido.pdf",
                    mime="application/pdf"
                )
            except Exception as e:
                st.error(f"Error al unir los PDFs: {e}")
                    

if __name__=='__main__':
    main()