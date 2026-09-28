from day01.practice import machine_status


def test_status_line_for_the_example_machine():
    assert machine_status("M-12", "running") == "M-12: running"


def test_status_line_keeps_argument_order():
    assert machine_status("running", "M-12") == "running: M-12"


def test_status_line_for_a_stopped_boiler():
    assert machine_status("Boiler-3", "stopped") == "Boiler-3: stopped"


def test_status_line_for_an_idle_conveyor():
    assert machine_status("Conveyor-7", "idle") == "Conveyor-7: idle"
