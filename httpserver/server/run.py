# -*- coding: utf-8 -*-
import socket
import os


def get_response(request):
    request_text = request.decode()
    if request_text == "":
        response = get_http_response(404, "Not found") + get_html_page("Page not found")
        return response.encode()
    request_lines = request_text.split("\n")
    method = request_lines[0].split()[0]
    if method != "GET":
        response = get_http_response(404, "Not found") + get_html_page("Page not found")
        return response.encode()
    path = request_lines[0].split()[1]
    if path == "/":
        user_agent = "empty User-Agent"
        for line in request_lines:
            if "User-Agent:" in line:
                user_agent = " ".join(line.split()[1:])
        response = get_http_response(200, "OK") + get_html_page("Hello mister! <br />You are: " + user_agent)
        return response.encode()
    if path == "/test/":
        response = get_http_response(200, "OK") + get_html_page(request_text)
        return response.encode()
    if path == "/media/":
        files = os.listdir("./files")
        response = get_http_response(200, "OK") + get_html_page(str(files))
        return response.encode()
    if path[0:7] == "/media/":
        file_path = "./files/" + path[7:]
        if os.path.isfile(file_path):
            content = "empty content of file"
            with open(file_path) as file:
                content = file.read()
            response = get_http_response(200, "OK") + get_html_page(content)
            return response.encode()
        else:
            response = get_http_response(404, "Not found") + get_html_page("File not found")
            return response.encode()
    response = get_http_response(404, "Not found") + get_html_page("Page not found")
    return response.encode()


def get_http_response(code, code_description):
    return "HTTP/1.1 " + str(code) + " " + code_description + "\n\n"


def get_html_page(text):
    return "<html>\n<body>\n" + text + "\n</body>\n</html>\n"


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))  # Связываем серверный сокет с IP localhost'a (обычно 127.0.0.1), порт 8000
server_socket.listen(0)  # Ставим сервер на прослушку, устанавливаем на 0 максимальное количество ожидающих содинений

print('Started')

while 1:
    try:
        (client_socket, address) = server_socket.accept()
        print('Got new client', client_socket.getsockname())  # IP и порт нового сокета для обмена данными
        request_string = client_socket.recv(2048)  # Получение данных по сокету (не более 2048 байт за раз)
        client_socket.send(get_response(request_string))  # Отправка данных по сокету в виде ответа на запрос клиента
        client_socket.close()
    except KeyboardInterrupt:  # В случае сигнала прерывания (^C) возникает данное исключение
        print('Stopped')
        server_socket.close()  # Данное приложение (сервер) закрывает соединение
        exit()
