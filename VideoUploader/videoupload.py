import click
import vimeo
import creds
import qrcode
import tempfile
import time
import subprocess
from printer import BrotherQL600

DEFAULT_VID_NAME='Unknown'
DEFAULT_VID_DESCR='Created by [ImageUploader](https://github.com/nosqlgeek/VideoUploader'
DEFAULT_PRINTER=BrotherQL600()

@click.command()
@click.argument('file')
@click.option('-d', '--description', default=DEFAULT_VID_DESCR)
def main(file, description):
    print("Starting ...")
    id = generate_id()
    url = uploadfile(file, id, description)
    png = create_qr_code(id, url)
    print_qr_code(png)

'''
Generate an id based on the current time
'''
def generate_id():
    print("Generating id ...")
    id = str(time.time()).replace('.', '')
    print("The id is {}".format(id))
    return id


'''
Upload the file to Vimeo
'''
def uploadfile(file, name=DEFAULT_VID_NAME, descr=DEFAULT_VID_DESCR):

    print("Uploading the file to Vimeo ...")

    # Connect to Vimeo
    client = vimeo.VimeoClient(
        token=creds.VIMEO_CREDS['token'],
        key=creds.VIMEO_CREDS['key'],
        secret=creds.VIMEO_CREDS['secret']
    )

    # Upload the file
    uri = client.upload(file, data={
        'name': name,
        'description': descr,
        'privacy': {
            'view': 'unlisted'
        }
    })

    # Get the actual secret URL
    details = client.get(uri).json()
    url = details['link']
    print("The url is {}".format(url))

    return url

def create_qr_code(id, url):
    print("Generating QR code ...")
    image = qrcode.make(url)
    loc = '{}/{}.png'.format(tempfile.gettempdir(),id)
    image.save(loc)
    return loc

def print_qr_code(path, printer=DEFAULT_PRINTER):
    try:
        print("Printing QR code ...")
        subprocess.run(["lp","-d", printer.name, "-o", "media={}".format(printer.media_size), path], check=True)
        print("Image {} has been sent to the printer.".format(path))
        return True
    except:
        print("Could not print {}.".format(path))
        return False




if __name__ == '__main__':
    main()

