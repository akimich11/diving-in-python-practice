import asyncio

all_data = dict()


def process_data(request):
    try:
        if request[0] != 'put' and request[0] != 'get':
            return 'error\nwrong command\n\n'
        metrics = request[1]

        if request[0] == 'put':
            if len(request) != 4:
                return 'error\nwrong command\n\n'
            value = float(request[2])
            timestamp = int(request[3])

            if metrics in all_data:
                for element in all_data[metrics]:
                    if element[1] == timestamp:
                        all_data[metrics].remove(element)
                        break
                all_data[metrics].append((value, timestamp))
            else:
                all_data[metrics] = [(value, timestamp)]
            return 'ok\n\n'

        output = 'ok\n'
        if request[0] == 'get':
            if len(request) != 2:
                return 'error\nwrong command\n\n'
            if metrics == '*':
                for key in all_data:
                    for metric in all_data[key]:
                        output += f'{key} {metric[0]} {metric[1]}\n'
            elif request[1] in all_data:
                for metric in all_data[metrics]:
                    output += f'{metrics} {metric[0]} {metric[1]}\n'
    except IndexError:
        return 'error\nwrong command\n\n'
    except ValueError:
        return 'error\nwrong command\n\n'

    return output + '\n'


class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = process_data(data.decode('utf8').split())
        self.transport.write(resp.encode('utf8'))


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coroutine = loop.create_server(ClientServerProtocol, host, port)
    server = loop.run_until_complete(coroutine)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
