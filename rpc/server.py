import xmlrpc.server
import bot


class Bot:
    @staticmethod
    def answer(query: str):
        return bot.bot_answer(query)


def rpc_server():
    server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000))
    server.register_instance(Bot())
    server.serve_forever()


if __name__ == '__main__':
    rpc_server()
