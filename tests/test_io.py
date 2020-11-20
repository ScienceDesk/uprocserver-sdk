import pytest
from upserver_sdk.io import Files, UpServerIo


def test_files_class():
    f_ = [
        "/inputs/image1.jpg",
        "/inputs/image2.jpg",
        "/inputs/image3.jpg",
        "/inputs/image4.jpg",
    ]
    files = Files(f_)

    assert [f for f in files] == f_
    assert files[0] == "/inputs/image1.jpg"
    assert files[1] == "/inputs/image2.jpg"
    assert files[2] == "/inputs/image3.jpg"
    assert files[3] == "/inputs/image4.jpg"

    with pytest.raises(IndexError):
        files[4]

    assert files.image1_jpg == "/inputs/image1.jpg"
    assert files.image2_jpg == "/inputs/image2.jpg"
    assert files.image3_jpg == "/inputs/image3.jpg"
    assert files.image4_jpg == "/inputs/image4.jpg"
