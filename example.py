from src.CSVMerge.csvauto import CSVMerge


def main():
    path = "test_dir"

    start = CSVMerge(path, 'output.csv')
    start.merge()


if __name__ == "__main__":
    main()
