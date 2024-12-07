import click
import vimeo
import creds
import qrcode
import tempfile
import time
import subprocess

DEFAULT_VID_NAME='Unknown'
DEFAULT_VID_DESCR='Created by [ImageUploader](https://github.com/nosqlgeek/VideoUploader'

@click.command()
@click.argument('file')
@click.option('-n', '--name', default=DEFAULT_VID_NAME)
@click.option('-d', '--description', default=DEFAULT_VID_DESCR)
def main(file, name, description):
    print("Starting ...")
    uploadfile(file, name, description)


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
def uploadfile(file, name, descr):

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

def print_qr_code(path):
    print("Printing QR code ...")
    subprocess.run(["lp", path], check=True)
    print(f"Image {path} has been sent to the printer.")



if __name__ == '__main__':
    main()

