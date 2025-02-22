import os
import gradio as gr
import fitz  # PyMuPDF
import logging
import shutil
from pdfid.pdfid import PDFiD

# Logging einrichten
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Verzeichnisse für hochgeladene und bereinigte PDFs
UPLOAD_FOLDER = "uploads"
BEREINIGTE_FOLDER = "bereinigte_pdfs"
ALLOWED_EXTENSIONS = {'pdf'}
VERBOTENE_OBJEKTE = ["/JavaScript", "/JS", "/AA", "/OpenAction", "/Launch", "/EmbeddedFile", "/RichMedia", "/URI", "/AcroForm", "/XFA", "/ObjStm"]

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(BEREINIGTE_FOLDER, exist_ok=True)

def ist_erlaubte_datei(dateiname):
    return '.' in dateiname and dateiname.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def analysiere_pdf_mit_pdfid(pdf_pfad):
    try:
        logging.info(f"PDFiD Analyse gestartet für: {pdf_pfad}")
        root = PDFiD(pdf_pfad)
        objekte = {}
        gefundene_objekte_meldungen = []
        
        for obj in VERBOTENE_OBJEKTE:
            elements = root.getElementsByTagName(obj)
            for element in elements:
                if element.firstChild and element.firstChild.nodeValue and int(element.firstChild.nodeValue) > 0:
                    anzahl = int(element.firstChild.nodeValue)
                    objekte[obj] = anzahl
                    logging.warning(f"PDFiD Warnung: Verdächtiges Objekt '{obj}' gefunden ({anzahl} mal)")
                    gefundene_objekte_meldungen.append(f"  - {obj} ({anzahl} mal)")

        if not objekte:
            return [], "PDFiD: Keine verdächtigen Objekte im Oberflächenscan gefunden."
        else:
            return objekte, "PDFiD: Verdächtige Objekte gefunden:\n" + "\n".join(gefundene_objekte_meldungen)
    except Exception as e:
        logging.error(f"Fehler bei der PDF-Analyse mit PDFiD: {e}")
        return {}, f"PDFiD Fehler: {e}"

def erweiterte_pdf_analyse(pdf_pfad):
    try:
        logging.info(f"Erweiterte PDF-Analyse gestartet für: {pdf_pfad}")
        doc = fitz.open(pdf_pfad)
        verdächtige_objekte_meldungen = []

        for seite in doc:
            for annot in seite.annots() or []:
                if annot and ("/AA" in str(annot) or "/JavaScript" in str(annot)):
                    verdächtige_objekte_meldungen.append(f"❌ Verdächtige Annotation mit JavaScript/AA gefunden: {annot}")
                    logging.warning(f"Erweiterte Analyse: Verdächtige Annotation gefunden: {annot}")

        for obj in doc:
            obj_text = obj.read_bytes()
            for verbotene in VERBOTENE_OBJEKTE:
                if verbotene.encode() in obj_text:
                    verdächtige_objekte_meldungen.append(f"❌ Verdächtiges eingebettetes Objekt gefunden: {verbotene}")
                    logging.warning(f"Erweiterte Analyse: Verdächtiges eingebettetes Objekt gefunden: {verbotene}")

        if not verdächtige_objekte_meldungen:
            return [], "Erweiterte Analyse: Keine verdächtigen Objekte gefunden."
        else:
            return verdächtige_objekte_meldungen, "Erweiterte Analyse: Verdächtige Objekte gefunden:\n" + "\n".join(verdächtige_objekte_meldungen)
    except Exception as e:
        logging.error(f"Fehler bei der erweiterten PDF-Analyse: {e}")
        return ["❌ Fehler bei der tiefgehenden Analyse"], f"Erweiterte Analyse Fehler: {e}"

def bereinige_pdf(pdf_pfad, output_pfad):
    try:
        logging.info(f"Starte Bereinigung der PDF: {pdf_pfad}")
        doc = fitz.open(pdf_pfad)
        if not doc.page_count:
            logging.error("PDF ist leer oder enthält keine Seiten!")
            return False

        writer = fitz.open()
        for seite in doc:
            writer.insert_pdf(doc, from_page=seite.number, to_page=seite.number)

        writer.save(output_pfad)
        writer.close()
        logging.info(f"PDF erfolgreich bereinigt und gespeichert unter: {output_pfad}")
        return True
    except Exception as e:
        logging.error(f"Fehler beim Bereinigen der PDF: {e}")
        return False

def pdf_scanner(pdf_pfad):
    if not ist_erlaubte_datei(pdf_pfad):
        return "❌ Ungültiger Dateityp.", None

    logging.info(f"Starte Sicherheits-Scan für PDF: {pdf_pfad}")
    pdfid_objekte, pdfid_meldung = analysiere_pdf_mit_pdfid(pdf_pfad)
    tiefen_scan_objekte, tiefen_scan_meldung = erweiterte_pdf_analyse(pdf_pfad)

    gesamt_meldung = ""
    if pdfid_objekte or tiefen_scan_objekte:
        gesamt_meldung += "⚠️ **Verdächtige Objekte gefunden!**\n"
        if pdfid_objekte:
            gesamt_meldung += pdfid_meldung + "\n"
        if tiefen_scan_objekte:
            gesamt_meldung += tiefen_scan_meldung + "\n"

        bereinigte_pdf_pfad = os.path.join(BEREINIGTE_FOLDER, f"{os.path.basename(pdf_pfad).split('.')[0]}_cleaned.pdf")
        if bereinige_pdf(pdf_pfad, bereinigte_pdf_pfad):
            gesamt_meldung += "\n✅ Bereinigte Version erfolgreich erstellt: " + bereinigte_pdf_pfad
            return gesamt_meldung, bereinigte_pdf_pfad
        else:
            gesamt_meldung += "\n❌ Fehler beim Bereinigen der PDF. Bitte öffnen Sie die Datei nicht!"
            return gesamt_meldung, None
    else:
        return "✅ **Keine verdächtigen Objekte gefunden.**", pdf_pfad


def scan_pdf(file):
    if file is None:
        return "❌ Keine Datei hochgeladen.", None

    upload_pfad = os.path.join(UPLOAD_FOLDER, os.path.basename(file.name))
    shutil.copy(file.name, upload_pfad)
    logging.info(f"Datei hochgeladen und gespeichert unter: {upload_pfad}")
    return pdf_scanner(upload_pfad)

with gr.Blocks() as iface:
    gr.Markdown("## PDF Sicherheitsprüfung CipherCore")
    pdf_file_input = gr.File(label="📂 Lade eine PDF hoch.")
    scan_button = gr.Button("Scan PDF")
    ergebnis_textbox = gr.Textbox(label="Ergebnis der Prüfung", interactive=False)
    bereinigte_pdf_output = gr.File(label="📥 Bereinigte PDF (falls nötig)")
    scan_button.click(scan_pdf, inputs=[pdf_file_input], outputs=[ergebnis_textbox, bereinigte_pdf_output])


# Gradio-Oberfläche
with gr.Blocks() as iface:
    gr.Markdown("## PDF Sicherheitsprüfung CipherCore")
    gr.Markdown("Analysiert PDF-Dateien auf schädliche Inhalte wie JavaScript, eingebettete Dateien und Formularaktionen.")

    pdf_file_input = gr.File(label="📂 Lade eine PDF hoch.")
    scan_button = gr.Button("Scan PDF")
    ergebnis_textbox = gr.Textbox(label="Ergebnis der Prüfung", interactive=False)
    bereinigte_pdf_output = gr.File(label="📥 Bereinigte PDF (falls nötig)")

    scan_button.click(scan_pdf, inputs=[pdf_file_input], outputs=[ergebnis_textbox, bereinigte_pdf_output])


# 📌 Tab-Klasse für Gradio - Unverändert gelassen, da nicht direkt angefragt.
class PdfScanTab:
    def __init__(self):
        pass

    def build_tab(self):
        with gr.TabItem("PDF Scan", id="pdf_scan_tab"):
            gr.Markdown("## PDF Sicherheitsprüfung CipherCore")
            gr.Markdown("Diese PDF-Sicherheitsprüfung analysiert Ihr Dokument auf potenziell gefährliche Inhalte. Wir suchen nach verdächtigen Objekten wie JavaScript, eingebetteten Dateien, automatischen Aktionen und mehr.")

            with gr.Column():
                pdf_file_input = gr.File(label="📂 Lade eine PDF hoch.")
                scan_button = gr.Button("Scan PDF")
                ergebnis_textbox = gr.Textbox(label="Ergebnis der Prüfung", interactive=False)
                bereinigte_pdf_output = gr.File(label="📥 Bereinigte PDF (falls nötig)")

                scan_button.click(scan_pdf, inputs=[pdf_file_input], outputs=[ergebnis_textbox, bereinigte_pdf_output])