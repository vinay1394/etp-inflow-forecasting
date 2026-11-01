from etp_inflow_forecasting import __version__


def test_package_version():
    assert isinstance(__version__, str)
    assert __version__
