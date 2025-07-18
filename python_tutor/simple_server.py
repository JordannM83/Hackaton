#!/usr/bin/env python3
"""
Python Tutor API Server - Version Simple
"""

import sys
import json
import http.server
import socketserver
from urllib.parse import parse_qs

class SimpleCodeExecutor:
    def execute_python(self, code):
        """Exécute du code Python de manière simple"""
        try:
            # Capture de la sortie
            output = []
            
            # Environnement sécurisé
            def safe_print(*args):
                output.append(" ".join(str(arg) for arg in args))
            
            safe_globals = {
                '__builtins__': {
                    'print': safe_print,
                    'range': range,
                    'len': len,
                    'int': int,
                    'float': float,
                    'str': str,
                    'list': list,
                    'dict': dict,
                    'sum': sum,
                }
            }
            
            # Variables pour tracer
            local_vars = {}
            
            # Exécution ligne par ligne
            lines = code.strip().split('\n')
            trace = []
            
            for i, line in enumerate(lines, 1):
                if line.strip():
                    try:
                        exec(line, safe_globals, local_vars)
                        trace.append({
                            "line": i,
                            "locals": dict(local_vars),
                            "globals": {},
                            "output": "\n".join(output)
                        })
                    except Exception as e:
                        trace.append({
                            "line": i,
                            "locals": dict(local_vars),
                            "globals": {},
                            "output": "\n".join(output),
                            "error": str(e)
                        })
                        break
            
            return trace
            
        except Exception as e:
            return [{
                "line": -1,
                "locals": {},
                "globals": {},
                "output": "",
                "error": str(e)
            }]
    
    def execute(self, code, language):
        """Point d'entrée principal"""
        if language.lower() == 'python':
            return self.execute_python(code)
        else:
            return [{
                "line": -1,
                "locals": {},
                "globals": {},
                "output": "",
                "error": f"Langage '{language}' non supporté. Seul Python est disponible dans cette version."
            }]


class SimpleHandler(http.server.BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.executor = SimpleCodeExecutor()
        super().__init__(*args, **kwargs)
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def do_POST(self):
        if self.path == '/run':
            try:
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                data = json.loads(post_data.decode('utf-8'))
                
                code = data.get('code', '')
                language = data.get('language', 'python')
                
                trace = self.executor.execute(code, language)
                response = {"trace": trace}
                
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps(response).encode('utf-8'))
                
            except Exception as e:
                error_response = {"error": str(e), "trace": []}
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps(error_response).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_GET(self):
        if self.path == '/':
            response = {"message": "Python Tutor API", "status": "OK"}
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()


if __name__ == "__main__":
    PORT = 8002
    print(f"🚀 Serveur Python Tutor Simple")
    print(f"📍 URL: http://localhost:{PORT}")
    print(f"🐍 Support: Python uniquement")
    
    try:
        with socketserver.TCPServer(("", PORT), SimpleHandler) as httpd:
            print(f"✅ Serveur actif sur le port {PORT}")
            httpd.serve_forever()
    except Exception as e:
        print(f"❌ Erreur: {e}")
