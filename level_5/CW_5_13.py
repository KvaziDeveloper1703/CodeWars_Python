"""
Write a function that takes a URL as a string and parses out only the domain name, returning it as a string.

Examples:
url = "http://github.com/carbonfive/raygun"   → "github"
url = "http://www.zombie-bites.com"           → "zombie-bites"
url = "https://www.cnet.com"                  → "cnet"

Напишите функцию, которая принимает URL в виде строки и извлекает только доменное имя (без префиксов http://, https://, www. и без пути).

Примеры:
url = "http://github.com/carbonfive/raygun"   → "github"
url = "http://www.zombie-bites.com"           → "zombie-bites"
url = "https://www.cnet.com"                  → "cnet"
"""

def domain_name(url):
    if url.startswith("http://"):
        url = url[7:]
    elif url.startswith("https://"):
        url = url[8:]

    if url.startswith("www."):
        url = url[4:]

    domain = url.split(".")[0]

    return domain

print(domain_name("http://github.com/carbonfive/raygun"))   # Ожидаемый результат: "github"
print(domain_name("http://www.zombie-bites.com"))           # Ожидаемый результат: "zombie-bites"
print(domain_name("https://www.cnet.com"))                  # Ожидаемый результат: "cnet"
print(domain_name("www.google.com"))                        # Ожидаемый результат: "google"
print(domain_name("youtube.com"))                           # Ожидаемый результат: "youtube"
