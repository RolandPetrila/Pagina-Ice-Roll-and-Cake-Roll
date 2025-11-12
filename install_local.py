import http.server
import socketserver
import os

def start_server(port=8000):
    web_dir = os.path.join(os.path.dirname(__file__))
    os.chdir(web_dir)

    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Serverul local rulează pe http://localhost:{port}")
        print("Apăsați Ctrl+C pentru a opri serverul.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServerul a fost oprit.")

if __name__ == "__main__":
    start_server()