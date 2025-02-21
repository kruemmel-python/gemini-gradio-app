
# Gemini Gradio App
**Hinweis:** Im Projektordner befindet sich eine kostenlose PDF-Version des Taschenbuchs "Die Kunst des Prompting", das hilfreiche Informationen und Anleitungen zur Erstellung effektiver Prompts für KI-Modelle bietet.

[![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Eine modulare, objektorientierte Gradio-Anwendung zur Interaktion mit der Gemini API und zur Nutzung von OpenAI DALL·E.  
Dieses Projekt wurde von **Ralf Krümmel, Entwickler bei CipherCore**, entwickelt und demonstriert Best Practices in Python 3.12. **CipherCore hat dieses Projekt entwickelt, um es als Schulungs- und Demonstrationsplattform für sichere KI-Entwicklung zu nutzen.**

---
![image](https://github.com/user-attachments/assets/54dca67f-f0e8-40f3-a332-3a2996770154)


## 📌 Inhaltsverzeichnis

- [Über das Projekt](#über-das-projekt)
- [Features](#features)
- [Projektstruktur](#projektstruktur)
- [Installation](#installation)
- [Konfiguration](#konfiguration)
- [Nutzung](#nutzung)
  - [Integrierter Modus](#integrierter-modus)
  - [Standalone-Modus einzelner Tabs](#standalone-modus-einzelner-tabs)
- [Mitarbeiterschulung & Mitarbeitertest](#mitarbeiterschulung--mitarbeitertest)
- [Beispiele](#beispiele)
- [Mitwirken](#mitwirken)
- [Lizenz](#lizenz)
- [Kontakt](#kontakt)

---

## 🛠️ Über das Projekt

Die **Gemini Gradio App** bietet eine interaktive Oberfläche zur Kommunikation mit der Gemini API und zur Nutzung von OpenAI DALL·E für die Bildgenerierung.  

Ein besonderes Highlight dieses Projekts ist die **Bildtransformation**:  
Die Transformation erfolgt über ein eigens entwickeltes neuronales Netzwerk, das ein völlig neues Bild **pixelweise** auf Basis der Farbwerte erstellt.  

Zusätzlich enthält das Projekt eine **PDF-Sicherheitsprüfung**, mit der **verdächtige Objekte in PDF-Dateien analysiert und entfernt** werden können.  

---

## 🚀 Features

- **Modularer Aufbau:** Jeder Tab ist ein eigenständiges Modul und kann unabhängig ausgeführt werden.  
- **Objektorientierte Architektur:** Der Code ist übersichtlich und leicht erweiterbar.  
- **Interaktion mit der Gemini API:** Senden von Audio-, Bild-, Video- und Datei-Anfragen an die Gemini API.  
- **Bildgenerierung mit DALL·E:** KI-gestützte Generierung und Transformation von Bildern.  
- **📄 PDF-Sicherheitsprüfung:**  
  - Erkennt **potenziell gefährliche eingebettete Skripte** (JavaScript, Launch-Aktionen etc.).  
  - Erstellt automatisch eine **bereinigte PDF-Version**, falls nötig.  
  - **Visuelle Darstellung der PDF-Struktur** in der Gradio-Oberfläche.  
- **Modernste Python 3.12 Features:**  
  - Verwendung von **strukturellem Pattern Matching**, **Union-Typ-Operatoren** und **präziseren Fehlermeldungen**.  
- **Gradio-basierte UI:** Intuitive und interaktive Benutzeroberfläche.  
- **Mitarbeiterschulung & Mitarbeitertest:**  
  - Umfassende **Compliance- & Sicherheits-Schulungen** zum EU AI Act.  
  - **Interaktive Tests** zur Wissensüberprüfung.  

---

## 📂 Projektstruktur

```
gemini-gradio-app/
├── gemini_app.py          # Gemeinsame Funktionen, Klassen & API-Initialisierung
├── main.py                # Hauptprogramm zur Integration aller Tabs
└── tabs/                  # Modulordner für UI-Tabs (jeder Tab als eigenständiges Modul)
    ├── __init__.py
    ├── tab_audio.py       # Audio-Interaktion
    ├── tab_chat.py        # Chat & Bildanalyse
    ├── tab_video.py       # Videoanalyse
    ├── tab_file.py        # Dateianalyse
    ├── tab_create.py      # Inhaltserstellung & Export
    ├── tab_dalle.py       # DALL·E Bildgenerierung & Transformation
    ├── tab_pdf_scan.py    # 📄 PDF-Sicherheitsprüfung (NEU!)
    ├── tab_info.py        # Informationen & Warnungen zur KI-Arbeit
    ├── tab_training.py    # Mitarbeiterschulung zum EU AI Act
    ├── tab_mitarbeitertest.py  # Interaktive Tests zur Compliance
```

---

## 🛠️ Installation

1. **Repository klonen:**
   ```bash
   git clone https://github.com/kruemmel-python/gemini-gradio-app.git
   cd gemini-gradio-app
   ```

2. **Virtuelle Umgebung erstellen und aktivieren (empfohlen):**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS / Linux:
   source venv/bin/activate
   ```

3. **Abhängigkeiten installieren:**
   ```bash
   pip install -r requirements.txt
   ```

   Falls `requirements.txt` fehlt:
   ```txt
   gradio
   numpy
   pillow
   python-dotenv
   openai
   requests
   torch
   opencv-python
   python-docx
   pandas
   fpdf
   pymupdf
   pdfid
   ```

---

## 🖥️ Nutzung

### **Integrierter Modus**
Alle Module starten:
```bash
python main.py
```

### **Standalone-Modus einzelner Tabs**
Nur die **PDF-Sicherheitsprüfung** starten:
```bash
python tabs/tab_pdf_scan.py
```

---

## 📄 PDF-Sicherheitsprüfung

Die **PDF-Analyse** erkennt und entfernt gefährliche Objekte aus PDFs.  
- **Funktionen:**
  - Scannt PDFs auf **versteckte Skripte & verdächtige Objekte** (JavaScript, Formulare, eingebettete Dateien).  
  - Erstellt eine **sichere, bereinigte Version**, falls nötig.  
  - **Einfache Bedienung über Gradio**.  

---

## 📌 Beispiele

- **🔍 PDF-Analyse:** Lade eine verdächtige PDF hoch, um sie auf Schadcode zu überprüfen.  
- **📸 DALL·E Bildgenerierung:** Erstelle KI-Bilder mit optionaler Transformation.  
- **📝 Mitarbeiterschulung:** Erlerne die Grundlagen des EU AI Acts.  

---

## 🤝 Mitwirken

Pull Requests sind willkommen!  
- Forke das Repository.  
- Erstelle einen Branch (`feature/xyz`).  
- Füge Deine Änderungen hinzu & committe sie.  
- Öffne einen Pull Request.  

---

## 📜 Lizenz

MIT-Lizenz – vollständige Details in der [LICENSE](LICENSE)-Datei.  

---

## 📬 Kontakt

Für Fragen oder Anregungen:  
GitHub: [kruemmel-python](https://github.com/kruemmel-python)  

---

![image](https://github.com/user-attachments/assets/bb3df836-5ab5-4ab3-9d3c-b85788de28fc)

![image](https://github.com/user-attachments/assets/afa896f5-258f-4fcd-ab84-36a5dbc43b7d)

![image](https://github.com/user-attachments/assets/c3827756-7bfa-4b43-9a4d-1d078d81b841)

![image](https://github.com/user-attachments/assets/741bae4e-5c58-4e64-8798-ad8fb15ca66f)


![image](https://github.com/user-attachments/assets/ce05a6f7-7ea4-4391-b794-789fa6d9a2f4)





