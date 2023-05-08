# Author: Chase Smith
# GitHub username: ChaseSmith67
# Date: 5/7/23
# Description: Simple pricing service provided over HTTP. Start the server by running this file.
#       Then, you can request data at 127.0.0.1:8080/products and receive the data as JSON. You can
#       also add an ID to the path to get price information for a specific product.
#       eg. 127.0.0.1:8080/products/1 returns {'id': 1, 'price': 5000}


from http.server import BaseHTTPRequestHandler, HTTPServer
import json

data = {
    'products': [
        {'id': 1, 'price': 5000}, {'id': 2, 'price': 3500}, {'id': 3, 'price': 4200}, {'id': 4, 'price': 6200},
        {'id': 5, 'price': 5300}, {'id': 6, 'price': 2900}, {'id': 7, 'price': 4850}, {'id': 8, 'price': 6500},
        {'id': 9, 'price': 4200}, {'id': 10, 'price': 5250}, {'id': 11, 'price': 4300}, {'id': 12, 'price': 7900},
        {'id': 13, 'price': 4250}, {'id': 14, 'price': 3700}, {'id': 15, 'price': 7200}, {'id': 16, 'price': 2200},
        {'id': 17, 'price': 7300}, {'id': 18, 'price': 3900}, {'id': 19, 'price': 5850}, {'id': 20, 'price': 3900},
        {'id': 21, 'price': 6850}, {'id': 22, 'price': 3550}, {'id': 23, 'price': 4350}, {'id': 24, 'price': 6150},
        {'id': 25, 'price': 3300}, {'id': 26, 'price': 2400}, {'id': 27, 'price': 2950}, {'id': 28, 'price': 9400},
        {'id': 29, 'price': 5850}, {'id': 30, 'price': 7500}, {'id': 31, 'price': 3400}, {'id': 32, 'price': 6800},
        {'id': 33, 'price': 2300}, {'id': 34, 'price': 2900}, {'id': 35, 'price': 4850}
    ]
}


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        if self.path == '/products':
            self.wfile.write(bytes(json.dumps(data), 'utf-8'))
        elif self.path[-1].isdigit():
            if self.path[-2].isdigit():
                prod_id = int(self.path[-2:]) - 1
            else:
                prod_id = int(self.path[-1]) - 1
            if prod_id >= len(data['products']):
                self.wfile.write(bytes(json.dumps({'error': 'Product not found'}), 'utf-8'))
            else:
                self.wfile.write(bytes(json.dumps(data['products'][prod_id]), 'utf-8'))
        else:
            pass
        return


if __name__ == '__main__':
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Starting Price Server...')
    httpd.serve_forever()
