import videoupload

def test_upload():
    url = videoupload.uploadfile('test.mov', videoupload.DEFAULT_VID_NAME, videoupload.DEFAULT_VID_DESCR )
    print(url)

def test_qrcode():
    png = videoupload.create_qr_code("https://www.nosqlgeeks.com")
    print(png)

def test_upload_and_qr():

    id = videoupload.generate_id()
    url = videoupload.uploadfile('test.mov', id, videoupload.DEFAULT_VID_DESCR)
    png = videoupload.create_qr_code(url)
    videoupload.print_qr_code(png)




if __name__ == "__main__":
    #test_upload()
    #test_qrcode()
    test_upload_and_qr()


