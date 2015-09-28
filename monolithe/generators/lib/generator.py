import os
import shutil

from monolithe.lib import Printer
from monolithe.specifications import RepositoryManager, FolderManager

class Generator(object):

    def __init__(self, monolithe_config):
        """
        """
        self.monolithe_config = monolithe_config


    def generate_from_folder(self, folder):
        """
        """
        specification_info = {}

        Printer.log("retrieving specifications from folder \"%s\"" % (folder))
        self.folder_manager = FolderManager(folder=folder, monolithe_config=self.monolithe_config)
        apiversion = self.folder_manager.get_api_version()
        specification_info[apiversion] = self.folder_manager.get_all_specifications()
        Printer.log("%d specifications retrieved from folder \"%s\" (api version: %s)" % (len(specification_info[apiversion]), folder, apiversion))

        self.generate(specification_info=specification_info)

    def generate_from_repo(self, api_url, login_or_token, password, organization, repository, repository_path, branches):
        """
        """
        specification_info = {}
        self.repository_manager = RepositoryManager(monolithe_config=self.monolithe_config,
                                                    api_url=api_url,
                                                    login_or_token=login_or_token,
                                                    password=password,
                                                    organization=organization,
                                                    repository=repository,
                                                    repository_path=repository_path)

        for branch in branches:
            Printer.log("retrieving specifications from github \"%s/%s%s@%s\"" % (organization.lower(), repository.lower(), repository_path, branch))
            apiversion = self.repository_manager.get_api_version(branch=branch)
            specifications = self.repository_manager.get_all_specifications(branch=branch)
            specification_info[apiversion] = specifications
            Printer.log("%d specifications retrieved from branch \"%s\" (api version: %s)" % (len(specifications), branch, apiversion))

        self.generate(specification_info=specification_info)

    def generate(self, specification_info):
        """
        """
        pass


    def install_system_vanilla(self, current_file, output_path):
        """
        """
        if os.path.exists(output_path):
            shutil.rmtree(output_path)

        system_vanilla_path = os.path.join(os.path.dirname(current_file), "vanilla");
        shutil.copytree(system_vanilla_path, output_path)


    def install_user_vanilla(self, user_vanilla_path, output_path):
        """
        """
        if not user_vanilla_path or not len(user_vanilla_path):
            return

        if not os.path.exists(user_vanilla_path):
            Printer.raiseError("Could not find user vanilla folder at path %s" % user_vanilla_path)

        for item in os.listdir(user_vanilla_path):
            s = os.path.join(user_vanilla_path, item)
            d = os.path.join(output_path, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, False, None)
            else:
                shutil.copy2(s, d)
