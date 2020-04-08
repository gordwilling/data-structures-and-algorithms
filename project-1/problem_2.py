import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if not path:
        path = "."

    def find_files_loop(suffix, path, file_list):
        files = os.listdir(path)
        for file in files:
            absolute_path = f"{path}/{file}"
            if os.path.isfile(absolute_path):
                if file.endswith(suffix):
                    file_list.append(absolute_path)
            else:
                find_files_loop(suffix, absolute_path, file_list)
        return file_list

    return find_files_loop(suffix, path, [])


if __name__ == '__main__':
    cwd = os.getcwd()
    print(find_files(".c", f"{cwd}/problem_2_files/testdir"))
    # [
    #   '{cwd}/problem_2_files/testdir/subdir1/a.c',
    #   '{cwd}/problem_2_files/testdir/subdir3/subsubdir1/b.c',
    #   '{cwd}/problem_2_files/testdir/subdir5/a.c',
    #   '{cwd}/problem_2_files/testdir/t1.c'
    # ]

    print(find_files("", f"{cwd}/problem_2_files/testdir"))
    # [
    #   '{cwd}/problem_2_files/testdir/subdir1/a.c',
    #   '{cwd}/problem_2_files/testdir/subdir1/a.h',
    #   '{cwd}/problem_2_files/testdir/subdir2/.gitkeep',
    #   '{cwd}/problem_2_files/testdir/subdir3/subsubdir1/b.c',
    #   '{cwd}/problem_2_files/testdir/subdir3/subsubdir1/b.h',
    #   '{cwd}/problem_2_files/testdir/subdir4/.gitkeep',
    #   '{cwd}/problem_2_files/testdir/subdir5/a.c',
    #   '{cwd}/problem_2_files/testdir/subdir5/a.h',
    #   '{cwd}/problem_2_files/testdir/t1.c',
    #   '{cwd}/problem_2_files/testdir/t1.h'
    # ]

    print(find_files("", ""))
    # [
    #   './problem_1.py',
    #   './problem_2.py',
    #   './problem_2_files/testdir/subdir1/a.c',
    #   './problem_2_files/testdir/subdir1/a.h',
    #   './problem_2_files/testdir/subdir2/.gitkeep',
    #   './problem_2_files/testdir/subdir3/subsubdir1/b.c',
    #   './problem_2_files/testdir/subdir3/subsubdir1/b.h',
    #   './problem_2_files/testdir/subdir4/.gitkeep',
    #   './problem_2_files/testdir/subdir5/a.c',
    #   './problem_2_files/testdir/subdir5/a.h',
    #   './problem_2_files/testdir/t1.c',
    #   './problem_2_files/testdir/t1.h',
    #   './__init__.py'
    # ]
