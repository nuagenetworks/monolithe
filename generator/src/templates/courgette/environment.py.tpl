# -*- coding: utf-8 -*-
{% set parent_object = None %}
from courgette.lib import Environment{% if model.parent %}{% if model.parent == 'csproot' %}{% set parent_object = 'ContextUser.get(ContextUser.CSPROOT)' %}, ContextUser
{% elif model.parent.remote_name == 'enterprise' %}, ContextEnterprise{% set parent_object = 'ContextEnterprise.get(ContextEnterprise.ENTERPRISE1)' %}
{% else %}
from courgette.environments.nu{{model.parent.environment_name|lower}} import NU{{model.parent.environment_name}}Environment{% set parent_object = 'NU%sEnvironment.create_instance()' % model.parent.environment_name %}{% endif %}
{% endif %}
from vsdk import NU{{model.name}}

class NU{{model.environment_name}}Environment(Environment):
    """ Define an environment for NU{{model.name}} object

    """
    @classmethod
    def target_class(cls):
        """ Returns the target class of the environment

            Returns:
                The class of the VSD model

        """
        return NU{{model.name}}

    @classmethod
    def get_instance(cls{% for attribute in model.attributes %}{% if attribute.is_required %}, {{attribute.local_name}}=None{% endif %}{% endfor %}):
        """ Get an object instance of the NU{{model.name}}

            The instance has not been sent to the server. If you need an
            instance that as been saved, use `create_instance` instancestead.

            This method sould provide a valid instance of NU{{model.name}}

        """
        # Courgette is using this method to create a valid instance of NU{{model.name}} object.
        # Please fill required attributes values in parameters and other below.
        # Remove None and set whatever you want. That's easy, you can do it ! :)
        raise Exception('Please specify default attributes of %s in method get_instance of the environment %s' % (NU{{model.name}}, NU{{model.name}}Environment))

        {% for attribute in model.attributes %}{% if not attribute.is_required %}{{attribute.local_name}} = None{% endif %}
        {% endfor %}
        return super(NU{{model.environment_name}}Environment, cls).get_instance({% for attribute in model.attributes %}{{attribute.local_name}}={{attribute.local_name}}{% if not loop.last %},
                                                                    {% endif %}{% endfor %})

    @classmethod
    def create_instance(cls):
        """ Create an object instance of NU{{model.name}}

            The instance is already created on the server side. If you need an
            instance that as not been saved, use `get_instance` instead.

            This method sould provide a valid instance of NU{{model.name}}

        """
        parent = {{parent_object}}
        return super(NU{{model.environment_name}}Environment, cls).create_instance(parent=parent)

    @classmethod
    def initialize(cls, target, current_object, create_current_object=False):
        """ Initializes the environment.

            Set current_object in target.

            Args:
                target: the TestCase
                current_object: the current object

        """
        parent_object = {{parent_object}}
        super(NU{{model.environment_name}}Environment, cls).initialize(target=target,
                                                current_object=current_object,
                                                create_current_object=create_current_object,
                                                parent_object=parent_object)

