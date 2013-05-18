from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid_deform import FormView
from webhelpers2.text import urlify
import colander as c
import deform.widget as w
from deform import FileData

from .models import (
    Document,
    PersistentImage,
)
from . import validators as v
from . import memory_tmp_store


class DocumentSchema(c.Schema):
    title = c.SchemaNode(c.String())
    contents = c.SchemaNode(c.String(),
                            widget=w.RichTextWidget())


class PersistentImageSchema(c.Schema):
    title = c.SchemaNode(c.String())
    data = c.SchemaNode(FileData(),
                        widget=w.FileUploadWidget(memory_tmp_store),
                        validator=v.image)


@view_config(context='.interfaces.IPreview')
class PersistentImagePreview(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        self.request.response.content_type = self.context.content_type
        self.request.response.body = self.context.data
        return self.request.response

@view_config(context=".models.Folder", renderer="templates/folder.pt")
class FolderView(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        return dict()


@view_config(context=".models.Folder", renderer="templates/form.pt",
             name="add_document")
class AddDocumentView(FormView):
    schema = DocumentSchema()
    buttons = ('add',)

    @property
    def context(self):
        return self.request.context

    def add_success(self, values):
        doc = Document(**values)
        name = urlify(doc.title)
        self.context[name] = doc
        return HTTPFound(self.request.resource_url(doc))

@view_config(context=".models.Document",
             renderer="templates/document.pt")
def document_view(request):
    return dict()


@view_config(context=".models.Folder", renderer="templates/form.pt",
             name="add_image")
class AddImageView(FormView):
    schema = PersistentImageSchema()
    buttons = ('add',)

    @property
    def context(self):
        return self.request.context

    def add_success(self, values):
        image = PersistentImage(values['title'],
                                values['data']['fp'].read())
        name = urlify(image.title)
        self.context[name] = image
        return HTTPFound(self.request.resource_url(image))


@view_config(context=".models.PersistentImage",
             renderer="templates/image.pt")
def image_view(request):
    return dict()


@view_config(name="raw",
             context=".models.PersistentImage")
def image_raw_view(context, request):
    request.response.body = context.data
    return request.response
