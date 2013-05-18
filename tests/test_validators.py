import pytest
import os

here = os.path.dirname(__file__)



class TestImage(object):
    @pytest.fixture
    def dummy_image(self, request):
        f = open(os.path.join(here, "r-penta64.png"))
        def fin():
            f.close()
        request.addfinalizer(fin)
        return f


    @pytest.fixture
    def target(self):
        from tinycms.validators import image
        return image

    def test_image_valid(self, target, dummy_image):
        value = {'fp': dummy_image}
        result = target(None, value)
    
        assert result

    def test_image_invalid(self, target):
        from io import BytesIO
        value = {'fp': BytesIO(b'testing')}
        result = target(None, value)
    
        assert not result
        
