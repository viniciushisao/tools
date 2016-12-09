"""
Rename all the file names of current folders and its subfolders
changing hyphens by underlines and upper to lowercase

Usage:
python fix_resources_names.py
"""

import os


def rename(folder=os.getcwd()):
    """Rename all the file names of current folders and its subfolders
    changing hyphens by underlines and upper to lowercase
    (1) Changes hyphens to underlines
    (2) Makes lowercase (not a Unix requirement, just looks better ;)
    """
    print 'Renaming files of ' + folder + ' and its subfolders...'
    for dirpath, _, filenames in os.walk(folder, topdown=True):
        print '\nRenaming files from', dirpath, '\n'
        if filenames:
            for filename in filenames:
                replaced_name = filename.replace("-", "_").lower()
                print filename, "->", replaced_name
                os.rename(
                    dirpath + '/' + filename, dirpath + '/' + replaced_name)
    print '\nAll files renamed!'

if __name__ == "__main__":
    rename()
