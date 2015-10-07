# -*- coding: utf-8 -*-

from monolithe import MonolitheConfig
from monolithe.lib import SDKUtils
from monolithe.generators.lib import TemplateFileWriter


class CLIWriter(object):
    """
    """

    def __init__(self, monolithe_config):
        """
        """
        self.writer = None

        self.monolithe_config = monolithe_config


    def write(self):
        """
        """
        self.writer = _CLIFileWriter(monolithe_config=self.monolithe_config)
        self.writer.write_init()
        self.writer.write_cli()
        self.writer.write_commands()
        self.writer.write_printer()
        self.writer.write_utils()


class _CLIFileWriter(TemplateFileWriter):
    """
    """

    def __init__(self, monolithe_config):
        """
        """
        super(_CLIFileWriter, self).__init__(package="monolithe.generators.sdk")

        self.monolithe_config = monolithe_config
        self._sdk_output = self.monolithe_config.get_option("sdk_output", "sdk")
        self._sdk_name = self.monolithe_config.get_option("sdk_name", "sdk")
        self._sdk_cli_name = self.monolithe_config.get_option("sdk_cli_name", "sdk")
        self._sdk_class_prefix = self.monolithe_config.get_option("sdk_class_prefix", "sdk")
        self._product_accronym = self.monolithe_config.get_option("product_accronym")
        self._product_name = self.monolithe_config.get_option("product_name")
        self.output_directory = "%s/%s/cli" % (self._sdk_output, self._sdk_name)

        with open("%s/__code_header" % self._sdk_output, "r") as f:
            self.header_content = f.read()

    def write_init(self):
        """
        """
        self.write( destination=self.output_directory, filename="__init__.py", template_name="cli__init__.py.tpl",
                    header=self.header_content)

    def write_cli(self):
        """
        """
        self.write( destination=self.output_directory, filename="cli.py", template_name="cli.py.tpl",
                    product_accronym=self._product_accronym,
                    product_name=self._product_name,
                    header=self.header_content)

    def write_commands(self):
        """
        """
        self.write( destination=self.output_directory, filename="commands.py", template_name="cli_commands.py.tpl",
                    product_accronym=self._product_accronym,
                    product_name=self._product_name,
                    sdk_cli_name=self._sdk_cli_name,
                    header=self.header_content)

    def write_printer(self):
        """
        """
        self.write( destination=self.output_directory, filename="printer.py", template_name="cli_printer.py.tpl",
                    header=self.header_content)

    def write_utils(self):
        """
        """
        self.write( destination=self.output_directory, filename="utils.py", template_name="cli_utils.py.tpl",
                    product_accronym=self._product_accronym,
                    sdk_class_prefix=self._sdk_class_prefix,
                    sdk_name=self._sdk_name,
                    header=self.header_content)