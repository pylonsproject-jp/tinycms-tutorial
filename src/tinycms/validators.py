import magic

def image(node, value):
    mime = magic.from_buffer(value['fp'].read(), mime=True)
    value['fp'].seek(0)
    return mime.startswith('image/')
