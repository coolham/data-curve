import pytest
from forms.rt_control_area import RtCurveControl


@pytest.fixture
def status_control_area():
    status_control_area = RtCurveControl()
    status_control_area.show()
    yield status_control_area
    status_control_area.close()


def test_initial_status(status_control_area):
    assert status_control_area.status_label.text() == "Status: Ready"


def test_start_button_click(status_control_area):
    status_control_area.start_button.click()
    assert status_control_area.status_label.text() == "Status: Running"
    assert not status_control_area.start_button.isEnabled()
    assert status_control_area.stop_button.isEnabled()


def test_stop_button_click(status_control_area):
    status_control_area.start_button.click()
    status_control_area.stop_button.click()
    assert status_control_area.status_label.text() == "Status: Stopped"
    assert status_control_area.start_button.isEnabled()
    assert not status_control_area.stop_button.isEnabled()


def test_start_signal(status_control_area):
    from PyQt6.QtCore import QSignalSpy

    signal_spy = QSignalSpy(status_control_area, status_control_area.startSignal)
    status_control_area.start_button.click()
    assert signal_spy.count() == 1


def test_stop_signal(status_control_area):
    from PyQt6.QtCore import QSignalSpy

    signal_spy = QSignalSpy(status_control_area, status_control_area.stopSignal)
    status_control_area.start_button.click()
    status_control_area.stop_button.click()
    assert signal_spy.count() == 1