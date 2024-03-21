import xmlrpc.client


def rpc_client():
    server = xmlrpc.client.ServerProxy("http://localhost:8000")

    message = input(">>> ")

    while message.lower().strip() != 'bye':
        server_response = server.answer(message)

        print('Received from server: ' + server_response)

        message = input(">>> ")


if __name__ == "__main__":
    rpc_client()
