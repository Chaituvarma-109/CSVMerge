import pytest
from src.CSVMerge.csvauto import CSV


class TestFile:
    def test_dir_not_found(self):
        with pytest.raises(FileNotFoundError):
            CSV("test_di", 'output.csv')

    def test_dirs_not_found(self):
        with pytest.raises(FileNotFoundError):
            CSV("test_dir2", 'output.csv').merge()

    def test_output_filename(self):
        with pytest.raises(FileNotFoundError):
            CSV("test_dir").write_file()

    def test_not_csv(self):
        assert CSV("test_dir", 'output.csv').check_file('hi.txt') is False

    def test_is_csv(self):
        assert CSV("test_dir", 'output.csv').check_file('dataset1.csv') is True
