# -*- coding: utf-8 -*-

import requests

from printer import Printer
from managers import TaskManager

SCHEMA_FILEPATH = '/schema'
ENTRY_PONT = '/api-docs'
SWAGGER_APIS = 'apis'
SWAGGER_PATH = 'path'


class SwaggerParser(object):
    """ Swagger Parser grabs all information from a JSON File """

    def grab_all(self, url, apiversion):
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
        base_url = '%s%s' % (url, apiversion)
        schema_url = '%s%s%s' % (base_url, SCHEMA_FILEPATH, ENTRY_PONT)

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

        resource_name = resource_path.split('/')[-1]

        response = requests.get(resource_path, verify=False)

        if response.status_code != 200:
            Printer.raiseError("[HTTP %s] An error occured while retrieving %s at %s" % (response.status_code, resource_name, resource_path))

        results[resource_name] = response.json()
