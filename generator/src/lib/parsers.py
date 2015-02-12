# -*- coding: utf-8 -*-

import os
import json
import requests
import sys

from .printer import Printer
from .managers import TaskManager
from .utils import Utils

ENTRY_POINT = '/api-docs'
SCHEMA_FILEPATH = '/schema'
SWAGGER_APIS = 'apis'
SWAGGER_APIVERSION = 'apiVersion'
SWAGGER_PATH = 'path'


class SwaggerParser(object):
    """ Factory class

    """
    @classmethod
    def factory(cls, url=None, path=None, apiversion=None):
        """ Return the appropriate Parser according to the url or path given

        """
        if path:
            return SwaggerFileParser(path=path, apiversion=apiversion)

        return SwaggerURLParser(url=url, apiversion=apiversion)

    def grab_all(self):
        """ Ensure method name

        """
        raise Exception("Should be implemented by developer.")


class SwaggerURLParser(object):
    """ Swagger Parser grabs all information from a JSON File

    """
    def __init__(self, url, apiversion):
        """ Initializes a new URL parser

        """
        self.url = url
        self.apiversion = apiversion

    def grab_all(self):
        """ Read a JSON file and returns a dictionnary

            Args:
                url: the URL of to grab all swagger information

            Returns:
                Returns a dictionary containing all models definition

            Example:
                if url is set to http://host:port/V3_0, it will grab all information
                described in http://host:port/V3_0/schema/api-docs according to swagger
                specification
        """

        if self.apiversion is None:
            Printer.raiseError("Please specify your apiversion using -v option")

        base_url = '%sV%s' % (self.url, str(self.apiversion).replace(".", "_"))
        schema_url = '%s%s%s' % (base_url, SCHEMA_FILEPATH, ENTRY_POINT)

        response = requests.get(schema_url, verify=False)

        if response.status_code != 200:
            Printer.raiseError("[HTTP %s] Could not access %s" % (response.status_code, schema_url))

        data = response.json()

        if SWAGGER_APIS not in data:
            Printer.raiseError("No apis information found at %s" % schema_url)

        task_manager = TaskManager()

        models = dict()
        for api in data[SWAGGER_APIS]:
            path = base_url + SCHEMA_FILEPATH + api[SWAGGER_PATH]
            task_manager.start_task(method=self._grab_resource, resource_path=path, results=models)

        task_manager.wait_until_exit()

        return models

    def _grab_resource(self, resource_path, results=dict()):
        """ Grab resource information

            Args:
                resource_path: the path where to grab information
                results: the dictionary to fill with all information

            Returns:
                Fills result dictionary
        """
        names = resource_path.split(SCHEMA_FILEPATH)[1].rsplit('/', 1)
        package = names[0]
        resource_name = names[1]

        try:  # Ugly hack due to Java issue: http://mvjira.mv.usa.alcatel.com/browse/VSD-546
            response = requests.get(resource_path, verify=False)
        except requests.exceptions.SSLError:
            response = requests.get(resource_path, verify=False)

        if response.status_code != 200:
            Printer.raiseError("[HTTP %s] An error occured while retrieving %s at %s" % (response.status_code, resource_name, resource_path))

        results[resource_name] = response.json()
        results[resource_name]['package'] = package


class SwaggerFileParser(object):
    """ Parse Swagger files

    """
    def __init__(self, path, apiversion=None):
        """ Initializes a File parser

        """
        self.path = path
        self.apiversion = apiversion
        self.extension = ''

    def grab_all(self):
        """ Read a JSON file and returns a dictionnary

            Args:
                path: the path where to find the schema/api-docs

            Returns:
                Returns a dictionary containing all models definition
        """
        schema_path = '%s%s%s' % (self.path, ENTRY_POINT, self.extension)

        if not os.path.isfile(schema_path):
            Printer.raiseError("[File Path] Could not access %s" % (schema_path))

        try:
            data = json.load(open(schema_path))
        except Exception:
            e = sys.exc_info()[1]
            Printer.raiseError("[File Path] Could load json file %s due to following error:\n%s" % (schema_path, e.args[0]))

        if SWAGGER_APIS not in data:
            Printer.raiseError("No apis information found in %s" % schema_path)

        if SWAGGER_APIVERSION not in data:
            Printer.raiseError("No api version found in %s" % schema_path)

        # Grab version from JSON file if not specified
        if self.apiversion is None:
            self.apiversion = Utils.get_version(data[SWAGGER_APIVERSION])

        task_manager = TaskManager()

        models = dict()
        for api in data[SWAGGER_APIS]:
            file_path = '%s%s%s' % (self.path, api[SWAGGER_PATH], self.extension)
            task_manager.start_task(method=self._grab_resource, file_path=file_path, results=models)

        task_manager.wait_until_exit()

        return models

    def _grab_resource(self, file_path, results=dict()):
        """ Grab resource information

            Args:
                file_path: the path where to the file
                results: the dictionary to fill with all information

            Returns:
                Fills result dictionary
        """
        names = file_path.split(self.path)[1].rsplit('/', 1)
        package = names[0]
        resource_name = names[1]

        if not os.path.isfile(file_path):
            Printer.raiseError("[File Path] Could not access %s" % (file_path))

        try:
            data = json.load(open(file_path))
        except Exception:
            e = sys.exc_info()[1]
            Printer.raiseError("[File Path] Could load json file %s due to following error:\n%s" % (file_path, e.args[0]))

        results[resource_name] = data
        results[resource_name]['package'] = package
