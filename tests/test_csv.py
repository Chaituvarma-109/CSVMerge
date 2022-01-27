import pytest

from src.csvauto import CSVMerge


class TestFile:
    def test_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            CSVMerge(r"C:\Users\chait\Desktop\CSV_Automation_pkg\test_di", 'output.csv',
                          r"C:\Users\chait\Desktop\CSV_Automation_pkg")

    def test_dirs_not_found(self):
        with pytest.raises(FileNotFoundError):
            CSVMerge(r"C:\Users\chait\Desktop\CSV_Automation_pkg\test_dir", 'output.csv',
                          r"C:\Users\chait\Desktop\CSV_Automation_pkg").merge()

    def test_not_csv(self):
        with pytest.raises(ValueError):
            CSVMerge(r"C:\Users\chait\Desktop\CSV_Automation_pkg\test_dir", 'output.csv',
                          r"C:\Users\chait\Desktop\CSV_Automation_pkg").check_file('hi.txt')

    def test_is_csv(self):
        res = CSVMerge(r"C:\Users\chait\Desktop\CSV_Automation_pkg\test_dir", 'output.csv',
                            r"C:\Users\chait\Desktop\CSV_Automation_pkg").check_file('dataset1.csv')
        assert res is True
