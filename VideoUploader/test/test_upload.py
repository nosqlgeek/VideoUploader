import videoupload

def test_upload():
    uri = videoupload.uploadfile('test.mov')
    print(uri)


if __name__ == "__main__":
    test_upload()


