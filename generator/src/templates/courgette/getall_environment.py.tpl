# -*- coding: utf-8 -*-
{% set parent_object = None %}
from courgette.lib import Environment{% if model.parent %}{% if model.parent == 'csproot' %}{% set parent_object = 'ContextUser.get(ContextUser.CSPROOT)' %}, ContextUser
{% elif model.parent.remote_name == 'enterprise' %}, ContextEnterprise{% set parent_object = 'ContextEnterprise.get(ContextEnterprise.ENTERPRISE1)' %}
{% else %}
from courgette.environments.nu{{model.parent.environment_name|lower}} import NU{{model.parent.environment_name}}Environment{% set parent_object = 'NU%sEnvironment.create_instance()' % model.parent.environment_name %}{% endif %}
{% endif %}
from vsdk import NU{{model.name}}

class NU{{model.getall_environment_name}}Environment(Environment):
    """ Environment for GET all NU{{model.name}} objects.

    """
    @classmethod
    def target_class(cls):
        """ Returns the target class of the environment

            Returns:
                The class of the VSD model

        """
        return NU{{model.name}}

    @classmethod
    def initialize(cls, target, expected_objects):
        """ Initializes the environment.

            Set expected_objects in target.

            Args:
                target: the TestCase
                expected_objects: all the expected objects in case of a list

        """
        current_object = {{parent_object}}
        super(NU{{model.getall_environment_name}}Environment, cls).initialize(target=target,
                                                     current_object=current_object,
                                                     parent_object=None,  # Explicitly set parent to None.
                                                     expected_objects=expected_objects)