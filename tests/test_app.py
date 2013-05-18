import pytest
from testfixtures import TempDirectory
import os
here = os.path.dirname(__file__)

@pytest.fixture
def dummy_image(request):
    return open(os.path.join(here, "r-penta64.png")).read()

@pytest.fixture
def d(request):
    d = TempDirectory()
    def fin():
        d.cleanup()
    request.addfinalizer(fin)
    return d

def test_app(d, dummy_image):
    zodbfile = os.path.join(d.path, "Data.fs")
    settings = {
        "zodbconn.uri": "file://%s?blobstorage_dir=%s" % (zodbfile, d.path),
    }
    import webtest
    from tinycms import main
    app = main({}, **settings)
    app = webtest.TestApp(app)
    res = app.get("/add_document")
    res.form['title'] = "test doc"
    res.form['contents'] = "test document"
    res = res.form.submit('add')
    assert res.location == 'http://localhost/test-doc/'

    res = app.get(res.location)

    assert "test doc" in res.body
    assert "test document" in res.body

    res = app.get('/add_image')

    res.form['title'] = "test image"
    #res.form['upload'] = ("test", b"test content")
    res.form['upload'] = ("test", dummy_image)
    res = res.form.submit('add')

    assert res.location == 'http://localhost/test-image/'

    res = app.get(res.location)

    assert "test image" in res.body
    assert "http://localhost/test-image/raw" in res.body
    res = app.get("http://localhost/test-image/raw")
    assert res.body == dummy_image
