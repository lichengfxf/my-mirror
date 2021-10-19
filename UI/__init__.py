import os,sys

# 当前文件全路径
fp = os.path.abspath(__file__)
print(fp)
# 当前文件所在目录
fd = os.path.dirname(fp)
print(fd)
# 项目根目录
root_dir = fd + "/.."
print(root_dir)

#
# 确保从根目录开始搜索
#
sys.path.insert(0, root_dir)

#
# 导入所有模块
#
__all__ = {"MainFrame"}
