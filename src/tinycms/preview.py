from zope.interface import implementer
import magic
from .interfaces import IPreview

class PreviewContainer(object):
    def __init__(self, memory_tmp_store):
        self.memory_tmp_store = memory_tmp_store

    def __getitem__(self, key):
        if key not in self.memory_tmp_store:
            return None

        return Preview(self.memory_tmp_store[key])

@implementer(IPreview)
class Preview(object):
    def __init__(self, data):
        self.data = data
        self.content_type = magic.from_buffer(self.data, mime=True)
