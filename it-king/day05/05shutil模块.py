__author__ = "Peter"

# 进行文件copy

import shutil

# f1 = open("test_file/本节笔记",encoding="utf-8")
#
# f2 = open("test_file/笔记2","w",encoding="utf-8")
# shutil.copyfileobj(f1,f2)

# shutil.copyfile("test_file/笔记2","笔记3")
# shutil.copystat("test_file/本节笔记","笔记3")

# shutil.copytree("test4","test_file/new_test4")
# shutil.rmtree("test_file/new_test4")

# shutil.make_archive("test_file/shutil_archive_test", "zip","E:\Work\MyCode\python3\it-king\day04")


# make_archive 内部用的就是zipfile
import zipfile

# 压缩
z = zipfile.ZipFile("test_file/day5.zip", "w")
z.write("package_import_test.py")
print("-----")
z.write("test_file/笔记2")
z.close()


# # 解压
# z = zipfile.ZipFile('laxi.zip', 'r')
# z.extractall()
# z.close()




# import tarfile
#
# # 压缩
# tar = tarfile.open('your.tar','w')
# tar.add('/Users/wupeiqi/PycharmProjects/bbs2.zip', arcname='bbs2.zip')
# tar.add('/Users/wupeiqi/PycharmProjects/cmdb.zip', arcname='cmdb.zip')
# tar.close()
#
# # 解压
# tar = tarfile.open('your.tar','r')
# tar.extractall()  # 可设置解压地址
# tar.close()