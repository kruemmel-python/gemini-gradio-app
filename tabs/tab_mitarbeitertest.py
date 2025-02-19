import gradio as gr
from typing import Union

class MitarbeiterTest:
    def __init__(self) -> None:
        # Definition der korrekten Antworten für alle Fragen
        self.korrekte_antworten: dict[str, str] = {
            "frage1": "Unannehmbares Risiko",
            "frage2": "Transparenz, Nachvollziehbarkeit, menschliche Aufsicht",
            "frage3": "Geldbußen, Marktrücknahme, zivilrechtliche Haftung",
            "frage4": "Unannehmbares Risiko, hohes Risiko, begrenztes Risiko, minimales Risiko",
            "frage5": "DSGVO, Datenschutz-Folgenabschätzung",
            "frage6": "Detaillierte technische Dokumentation und kontinuierliche Überwachung",
            "frage7": "Hohe Datenqualität und regelmäßige Überprüfungen",
            "frage8": "Menschliche Aufsicht und Eingriffsmöglichkeiten",
            "frage9": "Transparenzpflichten und Benachrichtigung der Nutzer",
            "frage10": "Regelmäßige Audits und externe Überprüfungen",
            "frage11": "Einhaltung der Vorgaben und kontinuierliche Verbesserung",
            "frage12": "Fallstudie: Überprüfung der Konformität eines KI-Systems"
        }
        # Definition der Fragen, inklusive zusätzlicher Erklärungen und weiterführender Links
        self.fragen: dict[str, dict[str, Union[str, list[str]]]] = {
            "frage1": {
                "text": "Welche Risikokategorie beschreibt KI-Systeme, die als eine klare Bedrohung für die Grundrechte angesehen werden und daher verboten sind?",
                "optionen": [
                    "Hochrisiko-KI-Systeme",
                    "Unannehmbares Risiko",
                    "Begrenztes Risiko",
                    "Minimales Risiko"
                ],
                "erklärung": (
                    "Diese Kategorie umfasst KI-Systeme, die inakzeptable Risiken für die Grundrechte darstellen. "
                    "Weitere Informationen findest Du beispielsweise unter: "
                    "https://digital-strategy.ec.europa.eu/en/policies/eu-regulation-artificial-intelligence"
                )
            },
            "frage2": {
                "text": "Welche Anforderungen gelten für Hochrisiko-KI-Systeme? (Wähle die beste Antwort)",
                "optionen": [
                    "Transparenz, Nachvollziehbarkeit, menschliche Aufsicht",
                    "Geringe Genauigkeit",
                    "Keine Dokumentation",
                    "Vollautomatischer Betrieb ohne Kontrolle"
                ],
                "erklärung": (
                    "Hochrisiko-Systeme müssen strenge Anforderungen erfüllen, um Sicherheit, Fairness und "
                    "Nachvollziehbarkeit zu gewährleisten."
                )
            },
            "frage3": {
                "text": "Welche rechtlichen Konsequenzen können bei Verstößen gegen den EU AI Act drohen?",
                "optionen": [
                    "Nichts",
                    "Geldbußen, Marktrücknahme, zivilrechtliche Haftung",
                    "Nur Verwarnungen",
                    "Nur interne Sanktionen"
                ],
                "erklärung": (
                    "Verstöße gegen den EU AI Act können erhebliche finanzielle und rechtliche Folgen nach sich ziehen."
                )
            },
            "frage4": {
                "text": "Wie werden KI-Systeme gemäß dem EU AI Act risikokategorisiert?",
                "optionen": [
                    "Nach Funktionsweise",
                    "Unannehmbares Risiko, hohes Risiko, begrenztes Risiko, minimales Risiko",
                    "Nach Popularität",
                    "Nach technischer Komplexität"
                ],
                "erklärung": (
                    "Die Kategorisierung erfolgt anhand des Risikopotenzials für Grundrechte und die Sicherheit der Nutzer."
                )
            },
            "frage5": {
                "text": "Welche Datenschutzregelungen sind bei der Entwicklung von KI-Systemen besonders relevant?",
                "optionen": [
                    "DSGVO, Datenschutz-Folgenabschätzung",
                    "Haftungsregelungen",
                    "Arbeitsrecht",
                    "Patentrecht"
                ],
                "erklärung": (
                    "Die DSGVO sowie die Durchführung einer Datenschutz-Folgenabschätzung sind zentral, um "
                    "den Schutz personenbezogener Daten sicherzustellen."
                )
            },
            "frage6": {
                "text": "Welche ergänzenden Maßnahmen sind erforderlich, um '100%ige' Konformität im Betrieb von Hochrisiko-KI-Systemen zu erreichen?",
                "optionen": [
                    "Standardmäßige Implementierung ohne weitere Maßnahmen",
                    "Detaillierte technische Dokumentation und kontinuierliche Überwachung",
                    "Nur manuelle Prüfungen",
                    "Ausschließlich externe Audits"
                ],
                "erklärung": (
                    "Neben der Einhaltung gesetzlicher Vorgaben sind detaillierte technische Dokumentation, "
                    "kontinuierliche Überwachung und regelmäßige Audits notwendig, um den Betrieb sicher und "
                    "konform zu halten."
                )
            },
            "frage7": {
                "text": "Welche Anforderungen gelten für die Datenqualität in Hochrisiko-KI-Systemen?",
                "optionen": [
                    "Hohe Datenqualität und regelmäßige Überprüfungen",
                    "Keine speziellen Anforderungen",
                    "Nur interne Überprüfungen",
                    "Datenqualität ist irrelevant"
                ],
                "erklärung": (
                    "Hochrisiko-KI-Systeme müssen hohe Standards an Datenqualität erfüllen und regelmäßig überprüft werden."
                )
            },
            "frage8": {
                "text": "Welche Rolle spielt die menschliche Aufsicht in Hochrisiko-KI-Systemen?",
                "optionen": [
                    "Menschliche Aufsicht und Eingriffsmöglichkeiten",
                    "Keine menschliche Aufsicht erforderlich",
                    "Nur bei Systemfehlern",
                    "Nur bei Nutzerbeschwerden"
                ],
                "erklärung": (
                    "Menschliche Aufsicht ist entscheidend, um sicherzustellen, dass KI-Systeme sicher und ethisch betrieben werden."
                )
            },
            "frage9": {
                "text": "Welche Transparenzpflichten gelten für bestimmte KI-Anwendungen?",
                "optionen": [
                    "Transparenzpflichten und Benachrichtigung der Nutzer",
                    "Keine Transparenzpflichten",
                    "Nur interne Transparenz",
                    "Nur bei behördlichen Anfragen"
                ],
                "erklärung": (
                    "Bestimmte KI-Anwendungen müssen transparent sein und Nutzer über ihre Funktionsweise informieren."
                )
            },
            "frage10": {
                "text": "Welche Maßnahmen sind notwendig, um die Konformität von Hochrisiko-KI-Systemen langfristig sicherzustellen?",
                "optionen": [
                    "Regelmäßige Audits und externe Überprüfungen",
                    "Keine zusätzlichen Maßnahmen",
                    "Nur interne Überprüfungen",
                    "Nur bei Beschwerden"
                ],
                "erklärung": (
                    "Regelmäßige Audits und externe Überprüfungen sind notwendig, um die Konformität langfristig sicherzustellen."
                )
            },
            "frage11": {
                "text": "Wie sollte ein Unternehmen mit den Vorgaben des EU AI Acts umgehen?",
                "optionen": [
                    "Einhaltung der Vorgaben und kontinuierliche Verbesserung",
                    "Ignorieren der Vorgaben",
                    "Einmalige Anpassung ohne weitere Überprüfungen",
                    "Nur bei behördlichen Anfragen reagieren"
                ],
                "erklärung": (
                    "Unternehmen sollten die Vorgaben einhalten und kontinuierlich verbessern, um langfristige Konformität zu gewährleisten."
                )
            },
            "frage12": {
                "text": "Fallstudie: Ein KI-System zur Gesichtserkennung wird in einem öffentlichen Raum eingesetzt. Welche Maßnahmen sind erforderlich, um die Konformität sicherzustellen?",
                "optionen": [
                    "Transparenzpflichten, Datenschutz-Folgenabschätzung, menschliche Aufsicht",
                    "Keine speziellen Maßnahmen",
                    "Nur technische Dokumentation",
                    "Nur interne Überprüfungen"
                ],
                "erklärung": (
                    "In diesem Fall sind Transparenzpflichten, eine Datenschutz-Folgenabschätzung und menschliche Aufsicht erforderlich."
                )
            }
        }

    def evaluate_answers(
        self,
        a1: str,
        a2: str,
        a3: str,
        a4: str,
        a5: str,
        a6: str,
        a7: str,
        a8: str,
        a9: str,
        a10: str,
        a11: str,
        a12: str
    ) -> str:
        """
        Diese Methode wertet die Antworten aus und liefert ein Ergebnis sowie detailliertes Feedback.
        Bei falschen Antworten werden zusätzliche Erklärungen und Links zu weiterführenden Informationen gegeben.
        """
        score = 0
        feedback = ""
        antworten: dict[str, str] = {
            "frage1": a1,
            "frage2": a2,
            "frage3": a3,
            "frage4": a4,
            "frage5": a5,
            "frage6": a6,
            "frage7": a7,
            "frage8": a8,
            "frage9": a9,
            "frage10": a10,
            "frage11": a11,
            "frage12": a12
        }
        for frage, antwort in antworten.items():
            if antwort == self.korrekte_antworten[frage]:
                score += 1
            else:
                feedback += f"{self.fragen[frage]['erklärung']}\n"
        result = f"Du hast {score} von 12 Fragen richtig beantwortet.\n"
        if score == 12:
            result += "Ausgezeichnet! Dein Wissen entspricht den höchsten Anforderungen des EU AI Acts."
        elif score >= 8:
            result += "Gut gemacht, aber es gibt noch Raum für Verbesserungen."
        else:
            result += "Bitte wiederhole die Schulungsinhalte und konsultiere die weiterführenden Materialien."
        if feedback:
            result += "\n\nFeedback:\n" + feedback
        return result

    def build_tab(self) -> None:
        """
        Diese Methode baut den erweiterten Tab für den Mitarbeitertest in der Gradio-App.
        """
        with gr.TabItem("Mitarbeitertest Erweitert"):
            gr.Markdown(
                """
                # Erweiterter Mitarbeitertest zum EU AI Act
                **Wichtig:**
                - Dieser Test ist nicht erschöpfend und deckt nicht alle Nuancen des EU AI Acts ab.
                - Er dient als Ergänzung zu umfassenderen Schulungen und Informationsmaterialien.
                - Je nach Mitarbeiterrolle kann der Test weiter angepasst werden.

                **Nächste Schritte für 100%ige Konformität:**
                - Zusätzliche, detailliertere Fragen (z.B. zu Datenqualität, technischer Dokumentation und menschlicher Aufsicht)
                - Einbau von Fallstudien oder Szenarien zur praxisnahen Überprüfung
                - Bereitstellung detaillierterer Erklärungen und weiterführender Links bei falschen Antworten
                """
            )
            # Aufbau der Fragen als Radiobuttons
            frage1 = gr.Radio(
                choices=self.fragen["frage1"]["optionen"],
                label=self.fragen["frage1"]["text"]
            )
            frage2 = gr.Radio(
                choices=self.fragen["frage2"]["optionen"],
                label=self.fragen["frage2"]["text"]
            )
            frage3 = gr.Radio(
                choices=self.fragen["frage3"]["optionen"],
                label=self.fragen["frage3"]["text"]
            )
            frage4 = gr.Radio(
                choices=self.fragen["frage4"]["optionen"],
                label=self.fragen["frage4"]["text"]
            )
            frage5 = gr.Radio(
                choices=self.fragen["frage5"]["optionen"],
                label=self.fragen["frage5"]["text"]
            )
            frage6 = gr.Radio(
                choices=self.fragen["frage6"]["optionen"],
                label=self.fragen["frage6"]["text"]
            )
            frage7 = gr.Radio(
                choices=self.fragen["frage7"]["optionen"],
                label=self.fragen["frage7"]["text"]
            )
            frage8 = gr.Radio(
                choices=self.fragen["frage8"]["optionen"],
                label=self.fragen["frage8"]["text"]
            )
            frage9 = gr.Radio(
                choices=self.fragen["frage9"]["optionen"],
                label=self.fragen["frage9"]["text"]
            )
            frage10 = gr.Radio(
                choices=self.fragen["frage10"]["optionen"],
                label=self.fragen["frage10"]["text"]
            )
            frage11 = gr.Radio(
                choices=self.fragen["frage11"]["optionen"],
                label=self.fragen["frage11"]["text"]
            )
            frage12 = gr.Radio(
                choices=self.fragen["frage12"]["optionen"],
                label=self.fragen["frage12"]["text"]
            )
            result_box = gr.Textbox(label="Testergebnis", interactive=False)
            submit_btn = gr.Button("Test auswerten")
            submit_btn.click(
                self.evaluate_answers,
                inputs=[frage1, frage2, frage3, frage4, frage5, frage6, frage7, frage8, frage9, frage10, frage11, frage12],
                outputs=result_box
            )

if __name__ == "__main__":
    with gr.Blocks(title="Erweiterter Mitarbeitertest - EU AI Act") as demo:
        MitarbeiterTestErweitert().build_tab()
    demo.launch()
