
class CP_Helper:


    def listdir(, self, location):
        from os import listdir
        return lisdir(location)

    def isfile(self, location):
        from os.path import isfile
        return isfile(location)

    def md5sum(self, filename):
        from hashlib import md5
        with open(filename) as fh:
            return md5(fh.read()).hexdigest()

    def list_nested_dirs(self, dir_path, file_with_path=[], file_with_names=[]):
        '''
        Method to get list of nested files or dirs
        Will return two list
            file_with_names,  Contains all file names in nested folder
            file_with_path  Contains all file paths in nested folder
        '''
        for child in self.listdir(dir_path):
            path = path.join(dir_path, child)
            if not self.isfile(path):
                self.list_nesed_dirs(path)
            else:
                file_with_path.append(path)
                file_with_names.append(child)

        return file_with_names, file_with_path


