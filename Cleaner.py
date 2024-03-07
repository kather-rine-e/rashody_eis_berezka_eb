from pathlib import Path
import os,re,sys

def clean():
    files_patterns = [r'^Сведения о всех типах закупок [0-9]{2}\.[0-9]{2}\.[0-9]{4}', r'^ContractSearch\(.*\)_[0-9]{2}\.[0-9]{2}\.[0-9]{4}', r'^PrintScroller_.+?']

    def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    temp_folder = resource_path(str(Path.home() / "Downloads"))

    paths = []

    import openpyxl

    for files_pattern in files_patterns:
        for file_name in os.listdir(path=temp_folder):
                if os.path.isfile(temp_folder + "\\" + file_name):
                    if  re.compile(files_pattern).search(file_name) is not None:
                        paths.append(temp_folder + "\\" + file_name)

    for one_path in paths:
        print(one_path)
        os.remove(one_path)

#clean()