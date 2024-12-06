import click
import vimeo
import creds

@click.command()
@click.argument('file')
def main(file):
    print("Starting ...")
    uploadfile(file)


'''
Upload the file to Vimeo
'''
def uploadfile(file):

    print("Uploading the file to Vimeo ...")

    # Connect to Vimeo
    client = vimeo.VimeoClient(
        token=creds.VIMEO_CREDS['token'],
        key=creds.VIMEO_CREDS['key'],
        secret=creds.VIMEO_CREDS['secret']
    )

    # Upload the file
    uri = client.upload(file, data={
        'name': 'Test',
        'description': 'Test file',
        'privacy': {
            'view': 'unlisted'
        }
    })

    # Get the actual secret URL
    details = client.get(uri).json()
    url = details['link']

    return url

# TODO
def create_qr_code(url):
    pass


if __name__ == '__main__':
    main()

