import base64

import dropbox

token = "sl.Br0teePR9W2Oby0NGXRyl2Rv-bD3dtCrVEWvjo_kEpfDMFkc9ruN0yu0r2tjPjd_n8EySUQxnSoyW8bx68EouNEdFryjyBcmevnWNYmcwg3hWNqr3lAbfSE8_okGHQjRhWx_7cV-Rileh8dvRNb4dOk"

dbx = dropbox.Dropbox(token)


def get_file_by_name(name):
    """Returns the file from the Dropbox folder by the name of the file"""
    try:
        metadata, data = dbx.files_download(f"/fiszki/{name}")
        base64_encoded_data = base64.b64encode(data.content)
        return base64_encoded_data.decode()

    except dropbox.exceptions.ApiError as err:
        print(f"API error: {err}")


def get_file_url_by_name(name):
    """Returns the url to the file with name"""
    try:
        link = dbx.sharing_create_shared_link_with_settings(f"/fiszki/{name}.jpg")
        print("URL to the file:", link.url)
        return link.url

    except dropbox.exceptions.ApiError as err:
        print(f"API Error: {err}")


def list_files_in_folder():
    """Returns list of all the file names from the Dropbox folder"""
    try:
        files = dbx.files_list_folder("/fiszki/").entries
        file_names = [file.name for file in files if isinstance(file, dropbox.files.FileMetadata)]
        return file_names
    except dropbox.exceptions.ApiError as err:
        print(f"API Error: {err}")
        return []
