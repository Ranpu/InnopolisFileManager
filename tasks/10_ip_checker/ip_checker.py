import re


def check_ip_address(ip):
    pattern = r"^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})(\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})){3}$"
    if re.match(pattern, ip):
        return "Корректный"
    else:
        return "Не корректный"


if __name__ == "__main__":
    while True:
        value = input("Введите IP адрес: ")
        if value == "exit":
            break
        print(check_ip_address(value))
