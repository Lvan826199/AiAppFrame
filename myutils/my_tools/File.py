import os

root_dir = os.path.dirname(os.path.abspath(__file__))

class bbs:
    root_tmp = 'tmp'
    base_dir = os.path.join(root_dir, '..', root_tmp)

    # 创建应用目录（完整路径：../tmp/app）
    app_dir = os.path.join(base_dir, 'app')
    apks_dir = os.path.join(base_dir, 'apks')
    prolist_dir = os.path.join(base_dir, 'prolist')

    ##adb目录
    utils_tmp = 'base'
    base_dir = os.path.join(root_dir, '..', utils_tmp, 'adb')
    adb = os.path.join(base_dir, 'windows')

    # java

    java_dir = os.path.join(root_dir, '..', utils_tmp, 'java', 'jbr', 'bin')
    java = os.path.join(java_dir, 'java.exe')

    sign_dir = os.path.join(root_dir, '..', utils_tmp, 'signature')
    bundletool = os.path.join(sign_dir, 'bundletool-all-1.14.0.jar')
    keystore = os.path.join(sign_dir, 'signature.keystore')
    hugeWinKeyStore = os.path.join(sign_dir, 'hugewin.keystore')
    def __init__(self):
        pass


    def _getAppFileName(self,fileName):
        """
        读取应用的文件名
        :param fileName:
        :return:
        """
        try:
            for root, _, files in os.walk(self.app_dir):
                if fileName in files:
                    return os.path.join(root, fileName)
        except Exception as e:
            raise f'应用文明名读取异常{e}'

    @classmethod
    def scan_for_target_image(cls, project=None, deviceFolder=None, dataset=None,target=None):
        """
        扫描项目目录下的图片文件
        :param project: 项目名称（用于路径过滤）
        :param deviceFile: 设备文件名（未使用，可删除）
        :param target: 目标参数（未使用，可删除）
        :return: 图片文件路径列表
        :raises: FileNotFoundError 如果项目目录不存在
        """

        try:
            target_project_path = os.path.join(cls.prolist_dir, project)
            res = os.path.isdir(target_project_path)
            if not res:
                raise FileNotFoundError(f"项目目录 '{project}' 不存在于路径中: {cls.prolist_dir}")

            target_deviceFolder_path = os.path.join(target_project_path, deviceFolder)
            res = os.path.isdir(target_deviceFolder_path)
            if not res:
                raise FileNotFoundError(f"设备归类集 '{deviceFolder}' 不存在于路径中: {target_project_path}")

            target_dataset_path = os.path.join(target_deviceFolder_path, dataset)
            res = os.path.isdir(target_dataset_path)
            if not res:
                raise FileNotFoundError(f"归类图片集 '{dataset}' 不存在于路径中: {target_dataset_path}")



            for root, _, files in os.walk(target_dataset_path):
                # print(root,files)
                if target not in files:
                    raise  FileNotFoundError(f"文件不存在: {target}")


            img = os.path.join(target_dataset_path, target)
            return img



        except Exception as e:
            # 正确抛出异常（继承自 BaseException）
            raise RuntimeError(f"扫描图片失败: {str(e)}") from e

    @classmethod
    def scan_for_images(cls, project=None, deviceFolder=None, dataset=None):
        """
        扫描项目目录下的图片文件
        :param project: 项目名称（用于路径过滤）
        :param deviceFile: 设备文件名（未使用，可删除）
        :param target: 目标参数（未使用，可删除）
        :return: 图片文件路径列表
        :raises: FileNotFoundError 如果项目目录不存在
        """
        import os
        from airtest.aircv import cv2
        from airtest.aircv.cal_confidence import cal_ccoeff_confidence
        from airtest.core.api import Template

        try:
            target_project_path = os.path.join(cls.prolist_dir, project)
            res = os.path.isdir(target_project_path)
            if not res:
                raise FileNotFoundError(f"项目目录 '{project}' 不存在于路径中: {cls.prolist_dir}")

            target_deviceFolder_path = os.path.join(target_project_path, deviceFolder)
            res = os.path.isdir(target_deviceFolder_path)
            if not res:
                raise FileNotFoundError(f"设备归类集 '{deviceFolder}' 不存在于路径中: {target_project_path}")

            target_dataset_path = os.path.join(target_deviceFolder_path, dataset)
            res = os.path.isdir(target_dataset_path)
            if not res:
                raise FileNotFoundError(f"归类图片集 '{dataset}' 不存在于路径中: {target_dataset_path}")

            filecmp = []
            template_dir = None
            for root, _, files in os.walk(target_dataset_path):
                # print(root,files)
                template_dir = root
                filecmp = files

            # print(filecmp)
            template_paths = []
            for file  in filecmp:
                if file.endswith('png'):
                    template_paths.append(os.path.join(template_dir, file))




            if not template_paths:
                print(f"警告: 文件夹 {template_dir} 中未找到PNG模板图片")
                return False

            # print(template_paths)

            return template_paths



        except Exception as e:
            # 正确抛出异常（继承自 BaseException）
            raise RuntimeError(f"扫描图片失败: {str(e)}") from e


if __name__ == '__main__':
    bbs = bbs()
    print(bbs.adb)
    apkPath = bbs._getAppFileName("29.apk")
    print(apkPath)
    # print( bbs._getAppFileName("com.bingo.scape.android.free-Production.aab"))
    print(bbs.scan_for_target_image('cashhoard','R28M405TJBX','alert','tpl1599189033537.png'))
    print(bbs.scan_for_images('mania', 'R28M405TJBX', 'home', ))
    #D:\newNodeProject\newSlave\utils\signature\signature.keystore
    # print(a.keystore)
