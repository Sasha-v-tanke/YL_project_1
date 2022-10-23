class FileException(Exception):
    '''file exception'''
    def __str__(self):
        return self.__doc__


class DirectoryFileException(FileException):
    '''wrong format of UI file'''
    pass


class NameFileException(FileException):
    """wrong name or directory of UI file"""
    pass



