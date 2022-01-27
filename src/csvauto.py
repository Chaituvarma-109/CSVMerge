import csv
import os


class CSVMerge:
    """
    Custom CSV Automation class for merging  CSV files.
    Mainly used, when the data is stored in multiple CSV files.
    This programme combines all data in MULTIPLE CSV files into ONE CSV file.
    """

    def __init__(self, csv_dir_path: str, output_csv_filename: str, output_csv_filepath: str, header: bool = True):
        """

        Args:
            csv_dir_path: Path to directory where CSV files are located.
            output_csv_filename: Name of the result file.
            output_csv_filepath: Path to where output csv file is located.
            header: if True first row of all the csv files except for first files.If it is not True then it will merge
                    all files as they are.
        """
        self.path = csv_dir_path
        self.dest_filename = output_csv_filename
        self.dest_file_path = output_csv_filepath
        self.header = header

        self.dirs = os.listdir(csv_dir_path)
        self.dir_lst = list()
        self.all_csv_files: list = list()
        self.content_lst = list()
        self.fields = list()

    def directory_path(self, dirname: str):
        """
        Creates path for directory.
        Path is already specified in example.py file.
        Path is OS independent.

        Args:
            dirname: Name of the directory to create a path.

        Returns:
            Directory path
        """
        dir_path = os.path.join(self.path, dirname)
        return dir_path

    @staticmethod
    def file_path(dirpath, filename: str):
        """
        Creates path for files present in a specified directory.

        Args:
            dirpath: Path for directory.
            filename: Name of the file to create a path.

        Returns:
            File path.
        """
        file_path = os.path.join(dirpath, filename)
        return file_path

    @staticmethod
    def check_file(filename: str):
        """
        This will check weather it is csv file.
        Args:
            filename: Name of the file to check

        Returns:
            Returns a boolean value.
            True if it is a CSV file
            False if it is not a CSV file.
        """
        if filename.endswith('.csv'):
            return True
        raise ValueError("Not a CSV file.")

    def check_dir(self, dirname: str):
        """
        Checks weather it is a Directory.
        Args:
            dirname: Directory name.

        Returns:
            Returns a boolean value.
            True if it is a Directory
            False if it is not a Directory.
        """
        dir_path = os.path.join(self.path, dirname)
        if os.path.isdir(dir_path):
            return True
        raise ValueError("Not Directory.")

    def read_file(self) -> None:
        """
        Reads the contents in the files and appends to content_lst list.
        Returns: None

        """
        for i, file in enumerate(self.all_csv_files):
            with open(file, 'r', newline='') as fp:
                content = csv.reader(fp, delimiter=',')
                if i != 0 and self.header:
                    next(content)
                for row in content:
                    self.content_lst.append(row)

    def write_file(self) -> None:
        """
        Writes into the output_csv_file from the content_lst.
        Returns: None

        """
        with open(self.dest_filename, 'a', newline='') as fp:
            content_write = csv.writer(fp)
            content_write.writerows(self.content_lst)

    def get_csv_files(self, dir_list: list) -> None:
        """
        get_csv_files method takes dir_list as input, which consists of list of directories present in the csv_dir_path.
        From this list it will finds the path of csv files present in the directories and appends
        to all_csv_files list.
        Args:
            dir_list: list directories present in the path.

        Returns: None

        """
        for dirs_ in dir_list:
            dirs_path = self.directory_path(dirs_)
            files = os.listdir(dirs_path)
            for file in files:
                files_path = self.file_path(dirs_path, file)
                self.all_csv_files.append(files_path)

    def merge(self) -> None:
        """
        Merge method will merge all the csv files into single file.
        Returns: None

        """
        if self.dirs:
            for dir_ in self.dirs:
                if self.check_dir(dir_):
                    self.dir_lst.append(dir_)
                elif self.check_file(dir_):
                    file_path = self.file_path(self.path, dir_)
                    self.all_csv_files.append(file_path)
            self.get_csv_files(self.dir_lst)
        else:
            raise FileNotFoundError
        self.read_file()
        self.write_file()
