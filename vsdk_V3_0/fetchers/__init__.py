#!/usr/bin/env python
"""Add all of the modules in the current directory to __all__"""

import os
import inspect
import sys

classes = []

for module in os.listdir(os.path.dirname(__file__)):
    if module != '__init__.py' and module[-3:] == '.py':

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

