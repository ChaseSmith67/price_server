
## How to Use the Microservice

This script can be run from the directory where the file is located
by opening a terminal and typing `$python3 server.py`.
You should get a message indicating that the server has started.
The HTTP server will be running on localhost (127.0.0.1) port 8080.

## Endpoints

The call to the server should include a path of either "/products" to
return a JSON object containing all the available data, or you can also
include a specific id like this '/products/{id}' to return only the data
associated with that id. 

**Example:** "127.0.0.1:8080/products/4" should return {'id': 5, 'price': 5300}.

If a request is made for a product that does not exist, an error is returned
as a JSON object, like this {"error": "Product not found"}.

## Sequence Diagram

![Sequence Diagram for Price Server](https://github.com/ChaseSmith67/price_server/blob/main/Sequence_diagram.png)
