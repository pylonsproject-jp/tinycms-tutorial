from zope.interface import Interface, Attribute


class IPreviewContainer(Interface):
    pass

class IPreview(Interface):
    data = Attribute(u"data to preview")

    content_type = Attribute(u"type of this data")
