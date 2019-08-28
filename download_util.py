import requests

def get_file_name_from_url(url):
    file_name_p = -1
    search_file_name = url[file_name_p]
    while search_file_name != "/":
        file_name_p += -1
        search_file_name = url[file_name_p]
    file_name = url[file_name_p + 1:]

    return file_name

def dl_file(url, file_path):
    response = requests.get(url)
    if response.status_code == 200:
        f = open(file_path, "wb")
        f.write(response.content)
        f.close()

    return 0