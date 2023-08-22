import os
import multiprocessing
import shutil

class Functions():
    isCopy = False
    isSpam = False

    @staticmethod
    def copy_files(directory: str, destination: str, ext: str):
        sl = os.listdir(directory)
        dl = os.listdir(destination)
        
        files_to_copy = []
        for f in sl:
            if ext != "":
                if f not in dl and f.endswith(ext):
                    files_to_copy.append(f)
            elif f not in dl:
                files_to_copy.append(f)

        if files_to_copy:
            for f in files_to_copy:
                directory_path = os.path.join(directory, f)
                destination_path = os.path.join(destination, f)
                shutil.copy2(directory_path, destination_path)

    @staticmethod
    def create_file(directory: str, name: str, ext: str, file_num: int, size: int, isSpam: bool):
        if isSpam:
            file_path = os.path.join(directory, f"{name}_{file_num+1}.{ext}")
            print(file_path)
            with open(file_path, 'x') as f:
                if size > 0:
                    f.write("1" * size)
                pass

    @staticmethod
    def create_files(directory: str, name: str, ext: str, files: int, size: int):
        print(multiprocessing.cpu_count() // 2, "\n\n\n\n\n")

        if not os.path.exists(directory):
            exit()

        if Functions.isSpam:
            Functions.isSpam = False
            
        else:
            Functions.isSpam = True
            pool = multiprocessing.Pool(processes=(multiprocessing.cpu_count() // 2))
            arguments = [(directory, name, ext, i, size, Functions.isSpam) for i in range(int(files))]
            pool.starmap(Functions.create_file, arguments)
            pool.close()
            pool.join()
        Functions.isSpam = False
