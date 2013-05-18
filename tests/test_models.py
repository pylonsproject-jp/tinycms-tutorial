import pytest


def test_it():
    pass

class TestPersistentImage(object):
    @pytest.fixture
    def target(self):
        from tinycms.models import PersistentImage
        return PersistentImage

    def test_init(self, target):
        title = "title"
        im = b"test data"
        result = target(title, im=im)

        assert result.title == "title"
        assert result.data == b"test data"


class TestDocument(object):

    @pytest.fixture
    def target(self):
        from tinycms.models import Document
        return Document


    def test_init(self, target):
        result = target(u"testing",
                        u"testing content")

        assert result.title == u"testing"
        assert result.contents == u"testing content"
