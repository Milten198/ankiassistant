import base64

import dropbox

token = "sl.BrZZ1kBChdK1URYPkbC65kligtqdBxSQ_kgg3CvWCOM2Vh0ZOhsHKkROAL_Romq2Co2bi9VwLHoLaNMUO86eoRNSZnWFwubycw4mM7sHzzWuFLqwlcnFXVUAxI4vuvxZDL_PdBJRkS_zTEKY2TJzhWo"

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
