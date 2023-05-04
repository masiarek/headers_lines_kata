import pytest

from Header import H

def test_create_header_positive():
    # Create an H object
    h = H(h_desc='test_desc')

    # Assert that the hdr_n attribute is incremented correctly
    # This is first header record - we should receive the 1st number as 901
    assert h.hdr_n == 901

        # Assert that the h_desc attribute is set correctly
    assert h.h_desc == 'test_desc'

@pytest.mark.xfail
def test_create_header_negative():
    # Create an H object
    h = H(h_desc='test_desc')

    # Assert that the hdr_n attribute is incremented correctly
    assert h.hdr_n == 909

    # Assert that the h_desc attribute is set correctly
    assert h.h_desc == 'test_desc'

