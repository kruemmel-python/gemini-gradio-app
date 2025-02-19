# Gemini Gradio App
**Hinweis:** Im Projektordner befindet sich eine kostenlose PDF-Version des Taschenbuchs "Die Kunst des Prompting", das hilfreiche Informationen und Anleitungen zur Erstellung effektiver Prompts für KI-Modelle bietet.

[![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Eine modulare, objektorientierte Gradio-Anwendung zur Interaktion mit der Gemini API und zur Nutzung von OpenAI DALL·E.  
Dieses Projekt wurde von **Ralf Krümmel** entwickelt und demonstriert Best Practices in Python 3.12 unter Verwendung moderner Sprachfeatures (wie strukturelles Pattern Matching und den Union-Typ-Operator).

---

## Inhaltsverzeichnis

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

## Über das Projekt

Die **Gemini Gradio App** bietet eine interaktive Oberfläche zur Kommunikation mit der Gemini API und zur Nutzung von OpenAI DALL·E für die Bildgenerierung.  
Ein besonderes Highlight dieses Projekts ist die **Bildtransformation**:  
Die Transformation erfolgt über ein eigens entwickeltes neuronales Netzwerk, das ein völlig neues Bild **pixelweise** auf Basis der Farbwerte erstellt. Dabei wird jedes einzelne Pixel neu berechnet – so entsteht ein Bild, das in Struktur und Farbdynamik völlig eigenständig ist.

Das Projekt ist in mehrere Module unterteilt, wobei jeder „Tab“ eine eigene Funktionalität kapselt (z. B. Audio-Interaktion, Chat & Bildanalyse, Videoanalyse, Dateianalyse, Inhaltserstellung & Export, DALL·E Bildgenerierung, Informationsbereich, Mitarbeiterschulung und Mitarbeitertest).  
Ziel ist es, einen klar strukturierten, modularen und wartbaren Code bereitzustellen – ideal für den Unterricht und den praktischen Einsatz in modernen Python-Projekten.

---

## Features

- **Modularer Aufbau:** Jeder Tab ist in einem eigenen Modul implementiert und kann separat ausgeführt werden.
- **Objektorientierte Architektur:** Klassen kapseln die Logik und UI-Elemente, was den Code übersichtlich und wartbar macht.
- **Interaktion mit der Gemini API:** Senden von Audio-, Bild-, Video- und Datei-Anfragen an die Gemini API.
- **Bildgenerierung mit DALL·E:** Integration der OpenAI DALL·E API zur Bildgenerierung und anschließenden Transformation.
  - **Pixelweise Transformation:** Ein eigens entwickeltes neuronales Netzwerk transformiert das Eingabebild in unterschiedliche Bildformate, indem es **pixelweise** neue Farbinformationen berechnet – so entsteht ein völlig neues Bild.
- **Modernste Python 3.12 Features:** Verwendung von strukturellem Pattern Matching, Union-Typ-Operatoren und präziseren Fehlermeldungen.
- **Gradio-basierte UI:** Eine intuitive und interaktive Benutzeroberfläche, die sowohl als gesamtes Projekt als auch in Einzelkomponenten ausgeführt werden kann.
- **Mitarbeiterschulung:** Ein eigener Tab, der umfassende Schulungsinhalte zum verantwortungsvollen Umgang mit KI, insbesondere im Hinblick auf den EU AI Act, bereitstellt.
- **Mitarbeitertest:** Interaktive Tests (auch in erweiterten Versionen verfügbar), mit denen Mitarbeiter ihr Wissen zu den Compliance-Anforderungen und rechtlichen Rahmenbedingungen des EU AI Act überprüfen können.

---

## Projektstruktur

Das Repository ist wie folgt strukturiert:

```
gemini-gradio-app/
├── gemini_app.py         # Gemeinsame Funktionen, Klassen und API-Initialisierung
├── main.py               # Hauptprogramm zur Integration aller Tabs in eine Gradio-App
└── tabs/                 # Modulordner für alle UI-Tabs (jeder Tab als eigenständiges Modul)
    ├── __init__.py
    ├── tab_audio.py      # Audio-Interaktion (Standalone & integriert)
    ├── tab_chat.py       # Chat & Bildanalyse (Standalone & integriert)
    ├── tab_video.py      # Videoanalyse (Standalone & integriert)
    ├── tab_file.py       # Dateianalyse (Standalone & integriert)
    ├── tab_create.py     # Inhaltserstellung & Export (Standalone & integriert)
    ├── tab_dalle.py      # DALL·E Bildgenerierung & -Transformation (Standalone & integriert)
    ├── tab_info.py       # Informationen & Warnungen zur KI-Arbeit (Standalone & integriert)
    ├── tab_training.py   # Mitarbeiterschulung: Umfassende Schulungsinhalte zu KI und EU AI Act
    └── tab_mitarbeitertest.py  # Mitarbeitertest: Interaktive Tests zu EU AI Act und Compliance
```

Jeder Tab bietet zwei Methoden:
- `build_tab()`: Zum Integrieren in eine übergeordnete Gradio-Oberfläche.
- `run()`: Zum eigenständigen Ausführen und Testen des jeweiligen Tabs.

---

## Installation

1. **Repository klonen:**

   ```bash
   git clone https://github.com/kruemmel-python/gemini-gradio-app.git
   cd gemini-gradio-app
   ```

2. **Virtuelle Umgebung erstellen und aktivieren (optional, aber empfohlen):**

   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS / Linux:
   source venv/bin/activate
   ```

3. **Abhängigkeiten installieren:**

   Erstelle eine `requirements.txt` (falls noch nicht vorhanden) mit den notwendigen Paketen. Beispielinhalt:

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
   ```

   Dann:

   ```bash
   pip install -r requirements.txt
   ```

---

## Konfiguration

Erstelle eine `.env`-Datei im Hauptverzeichnis und füge Deine API-Schlüssel hinzu:

```ini
API_KEY=dein_gemini_api_key
OPENAI_API_KEY=dein_openai_api_key
```

Achte darauf, dass diese Datei nicht öffentlich zugänglich ist (über .gitignore in GitHub ausschließen).

---

## Nutzung

### Integrierter Modus

Um die gesamte App (mit allen Tabs) zu starten, führe in der Konsole im Projektverzeichnis folgenden Befehl aus:

```bash
python main.py
```

Dies startet die Gradio-Oberfläche, in der Du alle Module auswählen und interagieren kannst.

### Standalone-Modus einzelner Tabs

Jeder Tab kann auch eigenständig getestet werden. Beispielsweise:

- **Audio-Tab:**  
  Navigiere zu `tabs/tab_audio.py` und führe diesen aus:

  ```bash
  python tabs/tab_audio.py
  ```

- Analog gilt dies für `tab_chat.py`, `tab_video.py`, `tab_file.py`, `tab_create.py`, `tab_dalle.py`, `tab_info.py`, **`tab_training.py`** (Mitarbeiterschulung) und **`tab_mitarbeitertest.py`** (Mitarbeitertest).

---

## Mitarbeiterschulung & Mitarbeitertest

### Mitarbeiterschulung

Der **Mitarbeiterschulung-Tab** (Implementierung in `tabs/tab_training.py`) bietet umfassende Schulungsinhalte für den Umgang mit Künstlicher Intelligenz – insbesondere im Hinblick auf den EU AI Act. Die Schulung ist in vier Untertabs unterteilt:

- **Grundlagen KI & ML:**  
  Vermittelt die theoretischen Grundlagen der KI und des maschinellen Lernens, inklusive Definitionen, Lernverfahren, gängiger Modelle und Praxisbeispiele.

- **Verantwortungsbewusster Einsatz:**  
  Behandelt den sicheren und ethisch verantwortlichen Einsatz von KI-Systemen. Themen sind Risikobewertung, Sicherheitsprotokolle, Datenschutzmaßnahmen sowie ethische Überlegungen.

- **Rechtliche Rahmenbedingungen:**  
  Erläutert die gesetzlichen Vorgaben, insbesondere den EU AI Act, sowie Datenschutzbestimmungen (DSGVO) und ethische Aspekte. Dieser Tab vermittelt ein tiefgehendes Verständnis der rechtlichen und Compliance-Anforderungen.

- **Praktische Anwendung:**  
  Konzentriert sich auf die Integration von KI in Arbeitsprozesse, Validierung und Interpretation von KI-Ergebnissen und Fallstudien, um praxisnahes Wissen zu vermitteln.

### Mitarbeitertest

Der **Mitarbeitertest-Tab** (Implementierung in `tabs/tab_mitarbeitertest.py`) dient der interaktiven Überprüfung des Wissens zu den Inhalten des EU AI Acts und der damit verbundenen Compliance-Anforderungen. Neben einem Basis-Test gibt es auch erweiterte Versionen mit zahlreichen Fragen, die alle relevanten Aspekte (wie Risikokategorisierung, Datenschutz, technische Dokumentation, menschliche Aufsicht, Explainable AI und ethische Richtlinien) abfragen.  
Mitarbeiter, die diesen Test bestehen, können ihr Verständnis der gesetzlichen Rahmenbedingungen sowie die Einhaltung der internen Compliance-Richtlinien bestätigen.

---

## Beispiele

- **Audio-Interaktion:** Lade eine Audiodatei hoch und erhalte ein Transkript oder eine Analyse der Datei.
- **Chat & Bildanalyse:** Stelle eine Frage und lade optional ein Bild hoch, um eine Analyse zu erhalten.
- **DALL·E Bildgenerierung:** Generiere ein Bild basierend auf einem Textprompt und transformiere es anschließend (z. B. Helligkeit, Kontrast, Auflösung).

Weitere Details findest Du in den einzelnen Modulen.

---

## Mitwirken

Beiträge zum Projekt sind herzlich willkommen! Wenn Du Ideen, Verbesserungen oder Bugfixes einreichen möchtest, folge bitte diesen Schritten:

1. Forke das Repository.
2. Erstelle einen neuen Branch (`feature/xyz`).
3. Füge Deine Änderungen hinzu und committe sie.
4. Öffne einen Pull Request mit einer ausführlichen Beschreibung der Änderungen.

---

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Weitere Informationen findest Du in der [LICENSE](LICENSE)-Datei.

---

## Kontakt

Für Fragen oder Anregungen kannst Du Dich gerne an Ralf Krümmel wenden:

- GitHub: [kruemmel-python](https://github.com/kruemmel-python)

---

*Viel Spaß mit der Gemini Gradio App, beim Experimentieren mit moderner KI-Interaktion und bei der Mitarbeiterschulung zu den EU AI Act Anforderungen!*


![image](https://github.com/user-attachments/assets/ae64938c-5ffc-4e32-96f2-1c08f4f02c01)

![image](https://github.com/user-attachments/assets/0647db03-efe2-43b1-b649-8ac58785cd7c)

![image](https://github.com/user-attachments/assets/281b0327-575d-44bb-bb38-81b75f754b3c)



![image](https://github.com/user-attachments/assets/45721055-4bd3-4234-a073-3078bab1eda0)

