import re


with open('nginx_logs.sql', 'r', encoding='utf-8') as file_1:
    for line in file_1:  # фаил читаем построчно, поэтому его размер может превышать ОЗУ ПК.
        # print(line, end='')
        remote_addr = re.search(r'^\d+\.\d+\.\d+\.\d+',line) #пытаемся записать IPv4
        if not remote_addr: # если это не IPv4
            remote_addr = re.search(r'(?:(^|:)(?:[0-9a-fA-F]{0,4})){1,8}',line) #то это IPv6
        request_datetime = re.search(r'\[\S+\s\+\d{4}\]', line)
        end_of_line = re.search(r'(?<=\]\s\").*$',line)
        splited_line = (end_of_line[0].split())
        request_type = splited_line[0]
        requested_resource = splited_line[1]
        response_code = splited_line[3]
        response_size = splited_line[4]
        print(f'parsed_raw = ({remote_addr[0]}, {request_datetime[0].strip("[]")}, {request_type},'
              f' {requested_resource}, {response_code}, {response_size})')
