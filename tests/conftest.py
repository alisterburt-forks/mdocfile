import pytest
from pathlib import Path


@pytest.fixture
def tilt_series_mdoc_file():
    return Path(__file__).parent / 'test_data' / 'tilt_series.mdoc'


@pytest.fixture
def montage_section_mdoc_file():
    return Path(__file__).parent / 'test_data' / 'montage_section.mdoc'


@pytest.fixture
def montage_section_multiple_mdoc_file():
    return Path(__file__).parent / 'test_data' / 'montage_section_multiple.mdoc'


@pytest.fixture
def frame_set_single_mdoc_file():
    return Path(__file__).parent / 'test_data' / 'frame_set_single.mdoc'


@pytest.fixture
def frame_set_multiple_mdoc_file():
    return Path(__file__).parent / 'test_data' / 'frame_set_multiple.mdoc'
