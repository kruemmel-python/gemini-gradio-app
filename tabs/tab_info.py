#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modul: tab_info.py
Dieses Modul enthält die Klasse InfoTab, die den Informations-Tab mit Hinweisen und Warnungen zur Arbeit mit KI
sowohl als eigenständige Anwendung als auch als Tab bereitstellt.
"""

import gradio as gr

class InfoTab:
    def build_tab(self):
        with gr.TabItem("Info"):
            gr.Markdown(
                """
                # Wichtige Hinweise und Warnungen zur Arbeit mit Künstlicher Intelligenz (KI)

                **Haftungsausschluss:**
                - Die von der KI generierten Inhalte sind automatisiert und können Fehler oder Unstimmigkeiten enthalten.
                - Es wird dringend empfohlen, alle Ergebnisse kritisch zu prüfen und gegebenenfalls zu validieren.

                **Verantwortungsvoller Umgang:**
                - Verwende die KI-Tools ausschließlich für den vorgesehenen Zweck.
                - Vermeide den Einsatz von KI zur Erstellung von schädlichen, diskriminierenden oder illegalen Inhalten.
                - Denke daran: Die KI ist ein Hilfsmittel und kein Ersatz für menschliche Expertise.

                **Datenschutz und Sicherheit:**
                - Gib keine sensiblen oder personenbezogenen Daten in die KI-Systeme ein, sofern nicht ausdrücklich zugelassen.
                - Die Nutzung der APIs erfolgt auf eigenes Risiko. Achte darauf, dass alle Eingaben datenschutzkonform sind.

                **Rechtliche Hinweise:**
                - Die Nutzung der KI und der zugehörigen APIs unterliegt den Nutzungsbedingungen der jeweiligen Anbieter.
                - Beachte bei der Weitergabe von Inhalten stets die geltenden Urheberrechte und Lizenzbestimmungen.

                **Technische Hinweise:**
                - KI-Modelle können in manchen Fällen kontextbezogene oder fachlich korrekte Ergebnisse nicht garantieren.
                - Änderungen oder Anpassungen an den Ergebnissen sollten stets von Fachleuten überprüft werden.
                - Bei der Integration in produktive Umgebungen ist Vorsicht geboten, da unvorhergesehene Fehler auftreten können.

                **Zusätzliche Warnungen:**
                - Die KI ist ein Werkzeug, das bei unsachgemäßer Verwendung zu unerwünschten Ergebnissen führen kann.
                - Nutze die bereitgestellten Tools immer mit Bedacht und reflektiert.
                - Diese Hinweise dienen als allgemeiner Leitfaden und erheben keinen Anspruch auf Vollständigkeit oder Rechtsgültigkeit.

                ---
                *Hinweis: Diese Informationen sollen Dir helfen, die Risiken und Verantwortlichkeiten beim Einsatz von KI besser zu verstehen. Bitte informiere Dich regelmäßig über aktuelle Entwicklungen und Best Practices im Bereich der Künstlichen Intelligenz.*
                """
            )

    def run(self):
        demo = gr.Blocks(title="Info - Standalone")
        with demo:
            gr.Markdown(
                """
                # Wichtige Hinweise und Warnungen zur Arbeit mit Künstlicher Intelligenz (KI)

                **Haftungsausschluss:**
                - Die von der KI generierten Inhalte sind automatisiert und können Fehler oder Unstimmigkeiten enthalten.
                - Es wird dringend empfohlen, alle Ergebnisse kritisch zu prüfen und gegebenenfalls zu validieren.

                **Verantwortungsvoller Umgang:**
                - Verwende die KI-Tools ausschließlich für den vorgesehenen Zweck.
                - Vermeide den Einsatz von KI zur Erstellung von schädlichen, diskriminierenden oder illegalen Inhalten.
                - Denke daran: Die KI ist ein Hilfsmittel und kein Ersatz für menschliche Expertise.

                **Datenschutz und Sicherheit:**
                - Gib keine sensiblen oder personenbezogenen Daten in die KI-Systeme ein, sofern nicht ausdrücklich zugelassen.
                - Die Nutzung der APIs erfolgt auf eigenes Risiko. Achte darauf, dass alle Eingaben datenschutzkonform sind.

                **Rechtliche Hinweise:**
                - Die Nutzung der KI und der zugehörigen APIs unterliegt den Nutzungsbedingungen der jeweiligen Anbieter.
                - Beachte bei der Weitergabe von Inhalten stets die geltenden Urheberrechte und Lizenzbestimmungen.

                **Technische Hinweise:**
                - KI-Modelle können in manchen Fällen kontextbezogene oder fachlich korrekte Ergebnisse nicht garantieren.
                - Änderungen oder Anpassungen an den Ergebnissen sollten stets von Fachleuten überprüft werden.
                - Bei der Integration in produktive Umgebungen ist Vorsicht geboten, da unvorhergesehene Fehler auftreten können.

                **Zusätzliche Warnungen:**
                - Die KI ist ein Werkzeug, das bei unsachgemäßer Verwendung zu unerwünschten Ergebnissen führen kann.
                - Nutze die bereitgestellten Tools immer mit Bedacht und reflektiert.
                - Diese Hinweise dienen als allgemeiner Leitfaden und erheben keinen Anspruch auf Vollständigkeit oder Rechtsgültigkeit.

                ---
                *Hinweis: Diese Informationen sollen Dir helfen, die Risiken und Verantwortlichkeiten beim Einsatz von KI besser zu verstehen. Bitte informiere Dich regelmäßig über aktuelle Entwicklungen und Best Practices im Bereich der Künstlichen Intelligenz.*
                """
            )
        demo.launch()

if __name__ == "__main__":
    info_tab = InfoTab()
    info_tab.run()
