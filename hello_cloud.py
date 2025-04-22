# #!/usr/bin/env python3

# import http.server
# import socketserver
# import sys

# PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080

# Handler = http.server.SimpleHTTPRequestHandler

# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print(f"🚀 Serveur en cours d'exécution sur le port {PORT}...")
#     httpd.serve_forever()
