#!/usr/bin/env python3
"""
HRadar — Server locale per la web app.
Avvia con:  python3 start_server.py
Poi apri:   http://localhost:8080
"""

import http.server
import socketserver
import os
import webbrowser
import sys

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

    def log_message(self, format, *args):
        print(f"[HRadar] {args[0]}")

if __name__ == '__main__':
    print(f"""
    ╔══════════════════════════════════════════╗
    ║          HRADAR — Talent Search          ║
    ║──────────────────────────────────────────║
    ║  Server attivo su http://localhost:{PORT}  ║
    ║  Premi Ctrl+C per fermare               ║
    ╚══════════════════════════════════════════╝
    """)

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            webbrowser.open(f"http://localhost:{PORT}")
        except:
            pass
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[HRadar] Server fermato.")
            sys.exit(0)
