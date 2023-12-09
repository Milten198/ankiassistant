import base64

import dropbox

token = "sl.BrYngWLFnOHlhzFqH0cMTIYgfxgVvKgLiMvgTIuBJubhhGbZEvBf6Zu4OrDUDwgoHrrItFUb8S5PVtOda5J5rt_f8ZcZVra6yXV3FLY6Nl8ej-hZ814v_8vCBIkOF6USfjsHupAjS7kk2kpU9WzY5HM"

dbx = dropbox.Dropbox(token)


def get_file_by_name(name):
    """Returns the file from the Dropbox folder by the name of the file"""
    try:
        metadata, data = dbx.files_download(f"/fiszki/{name}.jpg")
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
