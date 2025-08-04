from tfr.tree_manager import make_phase_name, parse_phase_name


class DescribeMakePhaseName:
    def test_works(self):
        assert make_phase_name(0) == "base"
        assert make_phase_name(1) == "phase-01"
        assert make_phase_name(2) == "phase-02"
        assert make_phase_name(10) == "phase-10"


class DescribeParsePhaseName:
    def test_valid(self):
        assert parse_phase_name("base") == 0
        assert parse_phase_name("phase-01") == 1
        assert parse_phase_name("phase-02") == 2
        assert parse_phase_name("phase-10") == 10

    def test_invalid(self):
        assert parse_phase_name("BASE") == None
        assert parse_phase_name("phase") == None
        assert parse_phase_name("phase--01") == None
        assert parse_phase_name("phase-01-02") == None
        assert parse_phase_name("/cool/phase-01") == None
