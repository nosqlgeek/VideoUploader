class Printer:
    def __init__(self, name:str, media_size:str):
        self.name = name
        self.media_size = media_size

class BrotherQL600(Printer):
    def __init__(self):
        super().__init__('Brother_QL_600', '62mm')