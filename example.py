from src.CSVMerge.csvauto import CSV


def main():
    path = "test_dir"

    start = CSV(path, 'output.csv')
    start.merge()


if __name__ == "__main__":
    main()
