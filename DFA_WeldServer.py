from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

# Set inital parameters
nozzle = 0 

HOST_NAME = '127.0.0.1'  # locathost - http://127.0.0.1
# Maybe set this to 1234 / So, complete address would be: http://127.0.0.1:1234
PORT_NUMBER = 1234

# Handler of HTTP requests / responses
class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        
    def do_GET(s):
        global weld_gun
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()

        path = s.path
        if path.find("/") != -1 and len(path) == 1:
            s.wfile.write(
                bytes('<html><head><title>Cool interface.</title></head>', 'utf-8'))
            s.wfile.write(
                bytes("<body><p>Current path: " + path + "</p>", "utf-8"))
            s.wfile.write(bytes('</body></html>', "utf-8"))
        elif path.find("/info") != -1:
            s.wfile.write(
                bytes('<html><head><title>Cool interface.</title></head>', 'utf-8'))
            s.wfile.write(
                bytes("<body><p>Current path: " + path + "</p>", "utf-8"))
            s.wfile.write(bytes("<body><p>Let's check the volumes for the welding gun!</p>", "utf-8"))
            s.wfile.write(bytes('</body></html>', "utf-8"))
        elif path.find("/setInput") != -1:
            s.send_response(200)
            s.send_header("Content-type", "text/html")
            s.end_headers()
            s.wfile.write(bytes('<form action="/setInput.php" method="post" enctype="multipart/form-data">', 'utf-8'))
            s.wfile.write(bytes('<html><body><h2>Weldability Checker:</h2>', "utf-8"))

            s.wfile.write(bytes('<br>Upload your .prt file containing the welding lines<br><input type="file" name="prtFileUploaded" id="prtFileUploaded">', "utf-8"))
            s.wfile.write(bytes('<br><input type="submit" value="Upload file" name="Upload file">', "utf-8"))

            s.wfile.write(bytes('<br><br>Selct type of nozzle:<br><select name="nozzle" id="nozzle"><option value="RECESSED">Recessed</option><option value="FLUSH">Flush</option><option value="PROTRUDING">Protruding</option><option value="ADJUSTABLE">Adjustable</option><option value="CUSTOM">Custom</option></select>', "utf-8"))
            s.wfile.write(bytes('<br><br><input type="submit" value="Submit"></form><p> Click "Submit" to submit file and nozzle to check weldability.</p>', "utf-8"))
            s.wfile.write(bytes('<br><h3>Weldability check :</h3>', "utf-8"))
            s.wfile.write(bytes('<img src="theProduct.png" width="400" height="275"></body></html>', "utf-8"))

            s.wfile.write(bytes('<?php $info = pathinfo($_FILES["userFile"]["name"]); $newname = "newname".prt; $target = "prtFiles/".$newname; move_uploaded_file( $_FILES["userFile"]["tmp_name"], $target); ?>', "utf-8"))
        
        else:   
            s.send_response(200)
            s.send_header("Content-type", "text/html")
            s.end_headers()
            s.wfile.write(
                bytes('<html><head><title>Cool interface.</title></head>', 'utf-8'))
            s.wfile.write(
                bytes("<body><p>The path: " + path + "</p>", "utf-8"))
            s.wfile.write(bytes('</body></html>', "utf-8"))

def do_POST(s):

        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()

        # Check what is the path
        path = s.path
        print("Path: ", path)
        if path.find("/setInput") != -1:
            content_len = int(s.headers.get('Content-Length'))
            post_body = s.rfile.read(content_len)
            param_line = post_body.decode()
            print("Body: ", param_line)

            ctype, pdict = cgi.parse_header(
                self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('message')

            s.send_response(200)
            s.send_header("Content-type", "text/html")
            s.end_headers()
            s.wfile.write(bytes('<form action="/setInput" method="post" enctype="multipart/form-data">', 'utf-8'))
            s.wfile.write(bytes('<html><body><h2>Weldability Checker:</h2>', "utf-8"))
            s.wfile.write(bytes('<br> Thank you for using oour weldability checker!'))

            s.wfile.write(bytes('<br>Upload your .prt file containing the welding lines<br><input type="file" name="prtFileUploaded" id="prtFileUploaded">', "utf-8"))
            s.wfile.write(bytes('<br><input type="submit" value="Upload file" name="Upload file">', "utf-8"))

            s.wfile.write(bytes('<br><br>Selct type of nozzle:<br><select name="nozzle" id="nozzle"><option value="RECESSED">Recessed</option><option value="FLUSH">Flush</option><option value="PROTRUDING">Protruding</option><option value="ADJUSTABLE">Adjustable</option><option value="CUSTOM">Custom</option></select>', "utf-8"))
            s.wfile.write(bytes('<br><br><input type="submit" value="Submit"></form><p> Click "Submit" to submit file and nozzle to check weldability.</p>', "utf-8"))
            s.wfile.write(bytes('<br><h3>Weldability check :</h3>', "utf-8"))
            s.wfile.write(bytes('<img src="theProduct.png" width="400" height="275"></body></html>', "utf-8"))

            return nozzle

        else:
            s.send_response(200)
            s.send_header("Content-type", "text/html")
            s.end_headers()
            s.wfile.write(
                bytes('<html><head><title>Cool interface.</title></head>', 'utf-8'))
            s.wfile.write(
                bytes("<body><p>The path: " + path + "</p>", "utf-8"))
            s.wfile.write(bytes('</body></html>', "utf-8"))


        

if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()