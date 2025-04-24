from django.shortcuts import render,HttpResponse
from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width", initial-scale="1.0">
        <title>properties</title>
        <style>
            *{
                background-color: black;
            }
            table{
                width: 50%;
                border-collapse: collapse;
                margin: 80px 0;
            }
            th, td {
                border: 1px solid white;
                padding: 8px;
                text-align: left;
                color: white;
            }
            th{
                background-color: gold;
                color: black;
            }
            .head{
                text-align: center;
                font-size: 50px;
                color: gold
            }
        </style>
    </head>
    <body>
        <div class="head">
            <b>DEVICE PROPERTIES</b>
        </div>
        <center>
            <table style="border: 5px;">
                <tr>
                    <th>DEVICE NAME</th>
                    <td>KARTHIKEYAN S</td>
                </tr>
                <tr>
                    <th>PROCESSOR</th>
                    <td>13th Gen Intel(R) Core(TM) i5-13420H   2.10 GHz</td>
                </tr>
                <tr>
                    <th>INSTALLED RAM</th>
                    <td>16.0 GB (15.6 GB usable)</td>
                </tr>
                <tr>
                    <th>DEVICE ID</th>
                    <td>09AF23A3-44B3-4FC5-8C24-A8424E7DD6ED</td>
                </tr>
                <tr>
                    <th>PRODUCT ID</th>
                    <td>00342-42705-17452-AAOEM</td>
                </tr>
                <tr>
                    <th>SYSTEM TYPE</th>
                    <td>64-bit operating system, x64-based processor</td>
                </tr>
                <tr>
                    <th>PEN AND TOUCH</th>
                    <td>No pen or touch input is available for this display</td>
                </tr>
            </table>
        </center>
    </body>
</html>
'''
class Myserver(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200)
        self.send_header("content-type","text/html")
        self.end_headers()
        self.wfile.write(content.encode())
print("This is my webserver")
serveraddress=('',8000)
httpd = HTTPServer(serveraddress,Myserver)
httpd.serve_forever()
