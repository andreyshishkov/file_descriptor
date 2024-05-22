import os
import time


class FileDescriptor:

    @staticmethod
    def get_file_create_time(path: str):
        return os.path.getctime(path)

    @staticmethod
    def get_last_access_time(path: str):
        return os.path.getatime(path)

    @staticmethod
    def get_last_change_time(path: str):
        return os.path.getmtime(path)

    @staticmethod
    def get_file_size(path: str):
        return os.path.getsize(path)

    def get_full_file_descr(self, path):
        return {
            'Access time': time.ctime(self.get_last_access_time(path)),
            'Modified time': time.ctime(self.get_last_change_time(path)),
            'Change time': time.ctime(self.get_file_create_time(path)),
            'Size': self.get_file_size(path)
        }

    def print_decr(self, path: str):
        file_description = self.get_full_file_descr(path)
        for indicator, value in file_description.items():
            print(f'{indicator:20}:\t{value}')


class DirectoryDescriptor:

    def __init__(self):
        self._single_file_descriptor = FileDescriptor()

    def get_only_files_descr(self, dir_path):
        filenames = os.listdir(dir_path)
        for filename in filenames:
            file_path = os.path.join(dir_path, filename)
            if os.path.isfile(file_path):
                print(f'File\t:\t{filename}')
                self._single_file_descriptor.print_decr(file_path)
                print('-----------------------------------------')

    def get_only_dirs_descr(self, dir_path):
        filenames = os.listdir(dir_path)
        for filename in filenames:
            file_path = os.path.join(dir_path, filename)
            if os.path.isdir(file_path):
                print(f'File\t:{filename}')
                self._single_file_descriptor.print_decr(file_path)
                print('-----------------------------------------')

    def get_all_files_descr(self, dir_path):
        filenames = os.listdir(dir_path)
        for filename in filenames:
            file_path = os.path.join(dir_path, filename)
            print(f'File\t:{filename}')
            self._single_file_descriptor.print_decr(file_path)
            print('-----------------------------------------')


if __name__ == '__main__':
    dir_path = input('Enter dir path: ')
    dir_descriptor = DirectoryDescriptor()

    dir_descriptor.get_only_files_descr(dir_path)
