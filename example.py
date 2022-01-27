from src.csvauto import CSVMerge


def main():
    path = r"C:\Users\chait\Desktop\CSV_Automation_pkg\test_dir"

    start = CSVMerge(path, 'output.csv', r"C:\Users\chait\Desktop\CSV_Automation_pkg")
    start.merge()


if __name__ == "__main__":
    main()
