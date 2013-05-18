import base64
from repoze.folder import Folder
from persistent import Persistent
from ZODB.blob import Blob
from PIL import Image
from io import BytesIO

class Root(Folder):
    __parent__ = __name__ = None


class Document(Persistent):
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents

    def __html__(self):
        return self.title

class PersistentImage(Persistent):
    def __init__(self, title, im):
        self.title = title
        self._data = Blob()
        with self._data.open(mode="w") as f:
            f.write(im)

    @property
    def data(self):
        with self._data.open(mode="r") as f:
            return f.read()

    @property
    def thumbnail(self):
        buf = BytesIO(self.data)
        im = Image.open(buf)
        outbuf = BytesIO()
        #im.resize((100, 100)).save(outbuf, "PNG")
        im.thumbnail((100, 100))
        im.save(outbuf, "PNG")
        return outbuf.getvalue()

    def __html__(self):
        return '<img src="data:image/png;base64,{0}">'.format( base64.b64encode(self.thumbnail))

def appmaker(root):
    if 'app_root' not in root:
        app_root = Root()
        root['app_root'] = app_root
        import transaction
        transaction.commit()
    return root['app_root']
