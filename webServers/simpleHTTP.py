#Import HTTP server package. This module allows us to setup a HTTP server that serves the current directory
import http.server
#Import socketserver package. This module allows us to use and bind to a particular port
import socketserver
#Specify port number
port = 8001
#Implement the solution. Bind to port 8001 using TCP, and list the current directory.
with socketserver.TCPServer(('', port), http.server.SimpleHTTPRequestHandler) as httpd:
    print(f"Serving at port {port}")
    httpd.serve_forever()
