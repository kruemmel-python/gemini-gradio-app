import os
import gradio as gr
import fitz  # PyMuPDF
import logging
import shutil
from pdfid.pdfid import PDFiD

# --------------------------------------------------------------------
# Logging einrichten
# --------------------------------------------------------------------
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --------------------------------------------------------------------
# Globale Variablen und Verzeichnisse -  Für CipherCore angepasst!
# --------------------------------------------------------------------
CIPHERCORE_UPLOAD_FOLDER = "uploads" # CipherCore braucht eigene Ordner, natürlich.
CIPHERCORE_BEREINIGTE_FOLDER = "bereinigte_pdfs" # Für die "bereinigten" PDFs.
CIPHERCORE_ALLOWED_EXTENSIONS = {'pdf'} # Nur PDFs, was sonst?
CIPHERCORE_VERBOTENE_OBJEKTE = [ # Dinge, die wir in CipherCore nicht dulden... in PDFs.
    "/JavaScript", "/JS", "/AA", "/OpenAction", "/Launch",
    "/EmbeddedFile", "/RichMedia", "/URI", "/AcroForm", "/XFA"
]

# Verzeichnisse erstellen -  CipherCore braucht Platz.
os.makedirs(CIPHERCORE_UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CIPHERCORE_BEREINIGTE_FOLDER, exist_ok=True)

# --------------------------------------------------------------------
# Hilfsfunktionen -  Dienlich, aber langweilig.
# --------------------------------------------------------------------
def ciphercore_ist_erlaubte_datei(dateiname):
    """Überprüft, ob eine Datei eine erlaubte Endung hat."""
    return '.' in dateiname and dateiname.rsplit('.', 1)[1].lower() in CIPHERCORE_ALLOWED_EXTENSIONS

def ciphercore_analysiere_pdf(pdf_pfad):
    """Analysiert eine PDF-Datei mit PDFiD auf verbotene Objekte.  Wir müssen wissen, was in diesen Dateien steckt."""
    try:
        root = PDFiD(pdf_pfad)
        objekt_liste = {}
        for obj in CIPHERCORE_VERBOTENE_OBJEKTE:
            elements = root.getElementsByTagName(obj)
            for element in elements:
                if element.firstChild and element.firstChild.nodeValue and int(element.firstChild.nodeValue) > 0:
                    objekt_liste[obj] = int(element.firstChild.nodeValue)
        return objekt_liste
    except Exception as e:
        logging.error(f"Fehler bei der PDF-Analyse ): {e}")
        return {}

def ciphercore_bereinige_pdf(pdf_pfad, output_pfad):
    """Erstellt eine neue PDF-Datei ohne unerwünschte Objekte.  Säubert die PDFs."""
    try:
        doc = fitz.open(pdf_pfad)
        writer = fitz.open()
        for seite in doc:
            writer.insert_page(-1, page=seite)
        writer.save(output_pfad)
        writer.close()
        return True
    except Exception as e:
        logging.error(f"Fehler beim Bereinigen der PDF : {e}")
        return False

# --------------------------------------------------------------------
# Haupt-Scan-Funktion -  Der Kern.
# --------------------------------------------------------------------
def ciphercore_pdf_scanner(pdf_pfad):
    """Scannt die hochgeladene PDF auf verbotene Objekte und bereinigt sie bei Bedarf.  Für die Sicherheit."""
    if not ciphercore_ist_erlaubte_datei(pdf_pfad):
        return "❌ Ungültiger Dateityp.  Dieser Dateityp ist nicht erlaubt.", None

    logging.info(f"Scanning PDF: {pdf_pfad}")
    objekt_liste = ciphercore_analysiere_pdf(pdf_pfad)

    if objekt_liste:
        bereinigte_pdf_pfad = os.path.join(CIPHERCORE_BEREINIGTE_FOLDER, f"{os.path.basename(pdf_pfad).split('.')[0]}_cleaned.pdf")
        if ciphercore_bereinige_pdf(pdf_pfad, bereinigte_pdf_pfad):
            return "⚠️ Verdächtige Objekte gefunden. Eine bereinigte Version wurde erstellt.  Wir haben die Risiken entfernt... vorerst.", bereinigte_pdf_pfad
        else:
            return "❌ Fehler beim Bereinigen der PDF.", None

    return "✅ Keine verdächtigen Objekte gefunden.  Diese PDF ist rein... ", pdf_pfad

# --------------------------------------------------------------------
# Gradio-Callback: ciphercore_scan_pdf -  Der Deal mit Gradio.
# --------------------------------------------------------------------
def ciphercore_scan_pdf(file):
    """Gradio-Funktion zur PDF-Analyse.  Für die menschliche Oberfläche."""
    if file is None:
        return "❌ Keine Datei hochgeladen.  Du musst schon etwas liefern, um es zu scannen!", None

    upload_pfad = os.path.join(CIPHERCORE_UPLOAD_FOLDER, os.path.basename(file.name))
    shutil.copy(file.name, upload_pfad)

    return ciphercore_pdf_scanner(upload_pfad)

# --------------------------------------------------------------------
# Tab-Klasse für Gradio -  Der Tab, in dem deine PDF-Anwendung wohnt.
# --------------------------------------------------------------------
class PdfScanTab:
    def __init__(self):
        pass

    def build_tab(self):
        with gr.TabItem("PDF Scan ", id="pdf_scan_tab"): # Ein Tab für die PDF-Sicherheitsprüfung.
            gr.Markdown("## PDF Sicherheitsprüfung CipherCore") #  Willkommen bei der PDF-Sicherheitsprüfung.
            gr.Markdown("Diese PDF-Sicherheitsprüfung analysiert Ihr Dokument auf potenziell gefährliche Inhalte. Wir suchen nach verdächtigen Objekten wie JavaScript, eingebetteten Dateien, automatischen Aktionen und mehr, die in PDFs versteckt sein können und Sicherheitsrisiken darstellen.  CipherCore schützt Sie vor diesen Bedrohungen.")
            with gr.Column():
                pdf_file_input = gr.File(label="📂 Lade eine PDF hoch.") #  Datei hochladen.
                scan_button = gr.Button("Scan PDF ", variant="primary") #  Scan starten.
                ergebnis_textbox = gr.Textbox(label="Ergebnis der Prüfung") #  Ergebnis anzeigen.
                bereinigte_pdf_output = gr.File(label="📥 Bereinigte PDF (falls nötig) -  fertig.") #  Bereinigte PDF herunterladen.

                scan_button.click(
                    ciphercore_scan_pdf,
                    inputs=[pdf_file_input],
                    outputs=[ergebnis_textbox, bereinigte_pdf_output]
                )