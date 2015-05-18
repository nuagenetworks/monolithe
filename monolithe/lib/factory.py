# -*- coding: utf-8 -*-

import importlib

from utils import Utils
from bambou import NURESTFetcher, NURESTObject


class VSDKFactory(object):
    """ Deals with VSDK Object models

    """
    _resources = dict()
    _version = None

    @classmethod
    def init(cls, version):
        """ Loads all VSDK objects in memory to
            enable retrieve each class according
            to its remote name.

        """
        cls._version = Utils.get_vspk_version(version)
        vsdk = cls.get_vsdk_package()
        classnames = [name for name in dir(vsdk) if name.startswith('NU') and not name.endswith('Fetcher')]

        for classname in classnames:
            klass = getattr(vsdk, classname)

            if issubclass(klass, NURESTObject):
                resource_name = klass.rest_resource_name
                cls._resources[resource_name] = klass

    @classmethod
    def get_vsdk_package(cls):
        """ Returns vsdk package

        """
        vsdk = None
        try:
            vsdk = importlib.import_module('vspk.vsdk.%s' % cls._version)
        except ImportError:
            vsdk = importlib.import_module('vsdk')
        except ImportError as error:
            raise ImportError('Could not found vspk or vsdk library. Please install requirements using command line `pip install -r requirements.txt`.\n%s' % error)

        return vsdk

    @classmethod
    def has_resource(cls, name):
        """ Check if the resource name is known

            Args:
                name: the resource name

            Returns:
                Returns True if the resouce is known.
                Otherwise False
        """
        return name in cls._resources

    @classmethod
    def class_from_resource(cls, name):
        """ Get the class related to the resource name

            Args:
                name: the resource name

            Returns:
                Returns the class object or None if
                no resource name matches.
        """
        if cls.has_resource(name):
            return cls._resources[name]

        return None

    @classmethod
    def class_from_model(cls, model):
        """ Create a NURESTObject from the given specification

            Args:
                spec: the specification

        """
        def init(self, **kwargs):
            """ """
            NURESTObject.__init__(self)

            for attribute in model.attributes:
                setattr(self, '_%s' % attribute.local_name.lower(), None)
                allowed_choices = attribute.allowed_choices.sort() if attribute.allowed_choices and len(attribute.allowed_choices) > 0 else None
                self.expose_attribute(local_name=attribute.local_name.lower(), remote_name=attribute.remote_name, attribute_type=attribute.local_type, is_required=attribute.required, choices=allowed_choices)

            self._compute_args(**kwargs)

        classname = "NU%s" % model.name
        klass = type(str(classname), (NURESTObject, ), {"__init__": init})
        klass.__rest_name__ = model.remote_name

        cls._resources[model.resource_name] = klass  # Override

        return klass

    @classmethod
    def update_fetchers_for_object(cls, parent, child, model):
        """

        """
        def fetcher_init(self, **kwargs):
            """"""
            NURESTFetcher.__init__(self)

        fetcher_classname = 'NU%sFetcher' % model.plural_name
        fetcher_klass = type(str(fetcher_classname), (NURESTFetcher, ), {"__init__": fetcher_init})

        def managed_class(cls):
            """"""
            return child.__class__

        setattr(fetcher_klass, 'managed_class', classmethod(managed_class))

        fetcher = fetcher_klass()
        setattr(parent, model.instance_plural_name, fetcher.fetcher_with_object(parent_object=parent))

    @classmethod
    def get_fetcher_instance(cls, parent, child):
        """ Get the fetcher instance from the parent that contains the child

        """
        return parent.fetcher_for_rest_name(child.rest_name)

    @classmethod
    def get_instance(cls, resource_name, **attributes):
        """ Get instance of a object related to its resource name

            Args:
                resource_name: the resource name
                attributes: additionnal attributes

            Returns:
                Returns the instance or None if
                no resource name matches.
        """
        klass = cls.class_from_resource(resource_name)

        if klass:
            python_attributes = cls._convert_attributes(attributes)
            return klass(**python_attributes)

        return None

    @classmethod
    def get_instance_from_model(cls, model, **attributes):
        """ Get instance of a object related to its resource name

            Args:
                model: the model
                attributes: attributes default values

            Returns:
                Returns the instance or None if
                no resource name matches.
        """
        klass = cls.class_from_model(model)

        if klass:
            python_attributes = cls._convert_attributes(attributes)
            return klass(**python_attributes)

        return None

    @classmethod
    def get_instance_copy(cls, instance):
        """ Creates a brand new copy of the instance

        """
        klass = instance.__class__
        return klass(data=instance.to_dict())

    @classmethod
    def _convert_attributes(cls, attributes):
        """ Convert attributes to with Python names

            Args:
                attributes: a dictionary of attributes

        """
        converted_attributes = dict()

        for attribute_name, attribute_value in attributes.iteritems():
            python_name = Utils.get_python_name(attribute_name)
            converted_attributes[python_name] = attribute_value

        return converted_attributes

    @classmethod
    def parent_has_child(cls, parent_resource, child_resource):
        """ Verify if the parent resource has a child
            of resource child_resource

            Args:
                parent_resource: the parent resource name
                child_resource: the child resource name

            Return:
                Returns True or False
        """
        parent = cls.class_from_resource(parent_resource)

        if parent is None:
            return False

        return hasattr(parent, child_resource)

    @classmethod
    def update_instance(cls, instance, **attributes):
        """ Update instance of an object with attributes values

            Args:
                instance: the object instance
                attributes: attributes values

            Returns:
                Returns the updated instance.
        """
        for attribute_name, attribute_value in attributes.iteritems():
            if hasattr(instance, attribute_name):
                setattr(instance, attribute_name, attribute_value)

        return instance
