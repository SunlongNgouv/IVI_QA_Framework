from src.ivi_system import IVISystem
import pytest

@pytest.fixture
def ivi_system():
    return IVISystem()