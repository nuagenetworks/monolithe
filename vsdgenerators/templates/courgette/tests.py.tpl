# -*- coding: utf-8 -*-
{% set required_attributes = [] %}{% for attribute in model.attributes %}{% if attribute.is_required %}{% do required_attributes.append(attribute) %}{% endif %}{% endfor %}
from courgette.lib import ContextUser
from courgette.lib import {% if 'GET' in allowed_methods %}NuageGetAllTests, NuageGetTests, {% endif %}{% if 'PUT' in allowed_methods %}NuageUpdateTests, {% endif %}{% if 'DELETE' in allowed_methods %}NuageDeleteTests, {% endif %}{% if 'POST' in allowed_methods %}NuageCreateTests{% endif %}
from courgette.environments import NU{{model.environment_name}}Environment, NU{{model.getall_environment_name}}Environment

{% if 'POST' in allowed_methods %}
class Create(NuageCreateTests):
    """ NU{{model.name}} creation tests"""

    def environment(self):
        """ Get test environment """

        return NU{{model.environment_name}}Environment

    def get_allowed_users(self):
        """ Returns all users that should be allowed """

        # Complete the list with all users that are allowed
        # to create a NU{{model.name}} object
        return [ContextUser.CSPROOT]

    def get_push_allowed_users(self):
        """ Returns all users that should receive a push notification """

        # Complete the list with all users that are allowed
        # to receive a push notification after object creation
        return [ContextUser.CSPROOT]

    def set_up(self):
        """ Set up environement """

        env = self.environment()
        {{model.instance_name}} = env.get_instance()
        env.initialize(self, {{model.instance_name}})

    def tear_down(self):
        """ Clean up environement """

        self.environment().clean(self){% endif %}

{% if 'PUT' in allowed_methods %}
class Update(NuageUpdateTests):
    """ NU{{model.name}} edition tests"""

    def environment(self):
        """ Get test environment """

        return NU{{model.environment_name}}Environment

    def get_allowed_users(self):
        """ Returns all users that should be allowed """

        # Complete the list with all users that are allowed
        # to update a NU{{model.name}} object
        return [ContextUser.CSPROOT]

    def get_push_allowed_users(self):
        """ Returns all users that should receive a push notification """

        # Complete the list with all users that are allowed
        # to receive a push notification after object modification
        return [ContextUser.CSPROOT]

    def set_up(self):
        """ Set up environement """

        env = self.environment()

        # Set valid attributes values that are different from those
        # you have entered for get_instance method of environment NU{{model.environment_name}}Environment
        {{model.instance_name}} = env.get_instance({% for attribute in required_attributes %}{{attribute.local_name}}=None{% if not loop.last %}, {% endif %}{% endfor %})
        env.initialize(self, {{model.instance_name}}, True)

    def tear_down(self):
        """ Clean up environement """

        self.environment().clean(self){% endif %}

{% if 'DELETE' in allowed_methods %}
class Delete(NuageDeleteTests):
    """ NU{{model.name}} deletion tests"""

    def environment(self):
        """ Get test environment """

        return NU{{model.environment_name}}Environment

    def get_allowed_users(self):
        """ Returns all users that should be allowed """

        # Complete the list with all users that are allowed
        # to delete a NU{{model.name}} object
        return [ContextUser.CSPROOT]

    def get_push_allowed_users(self):
        """ Returns all users that should receive a push notification """

        # Complete the list with all users that are allowed
        # to receive a push notification after object deletion
        return [ContextUser.CSPROOT]

    def set_up(self):
        """ Set up environement """

        env = self.environment()
        {{model.instance_name}} = env.get_instance()
        env.initialize(self, {{model.instance_name}}, True)

    def tear_down(self):
        """ Clean up environement """

        self.environment().clean(self){% endif %}

{% if 'GET' in allowed_methods %}
class Get(NuageGetTests):
    """ NU{{model.name}} get tests"""

    def environment(self):
        """ Get test environment """

        return NU{{model.environment_name}}Environment

    def get_allowed_users(self):
        """ Returns all users that should be allowed """

        # Complete the list with all users that are allowed
        # to retrieve a NU{{model.name}} object
        return [ContextUser.CSPROOT]

    def get_push_allowed_users(self):
        """ Returns all users that should receive a push notification """

        # Complete the list with all users that are allowed
        # to receive a push notification after object retrieval
        return []

    def set_up(self):
        """ Set up environement """

        env = self.environment()
        {{model.instance_name}} = env.get_instance()
        env.initialize(self, {{model.instance_name}}, True)

    def tear_down(self):
        """ Clean up environement """

        self.environment().clean(self)


class GetAll(NuageGetAllTests):
    """ NU{{model.name}} get tests"""

    def environment(self):
        """ Get test environment """

        return NU{{model.getall_environment_name}}Environment

    def get_allowed_users(self):
        """ Returns all users that should be allowed """

        # Complete the list with all users that are allowed
        # to retrieve all NU{{model.name}} objects
        return [ContextUser.CSPROOT]

    def get_push_allowed_users(self):
        """ Returns all users that should receive a push notification """

        # Complete the list with all users that are allowed
        # to receive a push notification after retrieval all objects
        return []

    def set_up(self):
        """ Set up environement """

        # Set valid attributes values that are different from those
        # you have entered for get_instance method of environment NU{{model.environment_name}}Environment
        {{model.instance_name}}1 = NU{{model.environment_name}}Environment.get_instance({% for attribute in required_attributes %}{{attribute.local_name}}=None{% if not loop.last %}, {% endif %}{% endfor %})
        {{model.instance_name}}2 = NU{{model.environment_name}}Environment.get_instance({% for attribute in required_attributes %}{{attribute.local_name}}=None{% if not loop.last %}, {% endif %}{% endfor %})
        {{model.instance_name}}3 = NU{{model.environment_name}}Environment.get_instance({% for attribute in required_attributes %}{{attribute.local_name}}=None{% if not loop.last %}, {% endif %}{% endfor %})

        {{model.instance_plural_name}} = [{{model.instance_name}}1, {{model.instance_name}}2, {{model.instance_name}}3]

        env = self.environment()
        env.initialize(self, {{model.instance_plural_name}})

    def tear_down(self):
        """ Clean up environement """

        self.environment().clean(self)
{% endif %}
