import os

from PIL import Image


def resize_rename_rotate(srcdir, srcfile, targetdir="", size=(128, 128)):
    # srcfile_path : the complete path to source file
    src_path = srcdir + srcfile

    targetfile = os.path.splitext(srcfile)
    extension = os.path.splitext(srcfile)[1]

    if srcfile != targetfile:
        try:
            im = Image.open(src_path)  # open file
            im = im.rotate(90)  # degrees counter-clockwise
            im = im.resize(size)  # resize the file
            im.save(targetdir + targetfile[0] + ".jpeg")
        except IOError:
            print("cannot change image for ", srcfile)


if __name__ == "__main__":
    targetdir = "./target_pics/"
    srcdir = "./src_pics/"

    for file in os.listdir(srcdir):
        resize_rename_rotate(srcdir, file, targetdir)