# -*- coding: utf-8 -*-

import os
import inspect
import sys
import pkg_resources

classes = []

for module in os.listdir(os.path.dirname(__file__)):
    if module.startswith('nu') and module.endswith('.py'):

        module_name = module[:-3]
        package_name = __name__

        import_name = '%s.%s' % (package_name, module_name)

        # Import module
        __import__(import_name)

        members = inspect.getmembers(sys.modules[import_name], lambda member: inspect.isclass(member) and member.__module__.startswith(package_name))
        names = [member[0] for member in members]

        if len(names) > 0:
            # Execute import with classnames
            exec('from %s import %s' % (module_name, ', '.join(names)), globals(), locals())

        classes.extend(names)

__all__ = classes


from bambou import BambouConfig
default_attrs = pkg_resources.resource_filename(__name__, '/resources/attrs_defaults.ini')
BambouConfig.set_default_values_config_file(default_attrs)
