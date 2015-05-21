# -*- coding: utf-8 -*-

import os
import requests

from copy import deepcopy
from monolithe.utils.printer import Printer
from .managers import TaskManager

from monolithe.utils.vsdk import VSDKUtils
from monolithe.utils.urls import URLUtils
from monolithe.utils.parse import ParsingUtils


API_DOCS = '/api-docs'
SCHEMA_FILEPATH = '/schema'
SWAGGER_APIS = 'apis'
SWAGGER_APIVERSION = 'apiVersion'
SWAGGER_PATH = 'path'
SPEC_EXTENSION = '.spec'


class SwaggerParser(object):
    """ Parser for Swagger description file.

        Works for both local and remote files depending on the option that are passed

    """

    def __init__(self, vsdurl, path, apiversion):
        """ Initializes the parser

            Args:
                vsdurl (string): url to the vsd
                path (string): path to a local schema folder
                apiversion (float): api version to use
        """
        self.vsdurl = vsdurl
        self.path = path
        self.apiversion = apiversion

    def run(self, filters=[]):
        """ Run the parser to grab all swagger resources

        """
        if URLUtils.is_url(self.vsdurl):
            base_path = '%s%s' % (VSDKUtils.get_vsd_url(self.vsdurl, self.apiversion), SCHEMA_FILEPATH)
            function_name = '_get_swagger_resource'
        else:
            base_path = self.path  # No need to compute a version here
            function_name = '_read_swagger_resource'

        models = self._run(base_path=base_path, function_name=function_name, filters=filters)

        return ParsingUtils.order(models)

    # Utilities

    def _run(self, base_path, function_name, filters):
        """ Run the server on the remote vsd

        """
        func = getattr(self, function_name)
        api_docs = func(base_path=base_path, path=API_DOCS)

        if SWAGGER_APIS not in api_docs or len(api_docs[SWAGGER_APIS]) == 0:
            Printer.raiseError("No apis information found in api-docs")

        if SWAGGER_APIVERSION not in api_docs:
            Printer.raiseError("No api version found in api-docs")

        if self.apiversion is None:
            self.apiversion = VSDKUtils.get_float_version(api_docs[SWAGGER_APIVERSION])

        filters = ParsingUtils.reverse_filters(filters)

        models = dict()
        task_manager = TaskManager()

        for api in api_docs[SWAGGER_APIS]:
            path = api[SWAGGER_PATH]
            task_manager.start_task(method=self._get_resource, base_path=base_path, path=path, function_name=function_name, results=models, filters=filters)

        task_manager.wait_until_exit()

        return models

    def _get_resource(self, base_path, path, function_name, results=dict(), filters=[]):
        """ Grab resource information

            Args:
                base_path: the base path where to grab information
                path: the path where to grab information
                results: the dictionary to fill with all information
                filters: list of filters

            Returns:
                Fills result dictionary
        """

        (package, model_name) = URLUtils.split_package_path(path)

        model_name = ParsingUtils.get_correct_name(model_name)
        rest_name = VSDKUtils.get_singular_name(model_name.lower())

        if len(filters) > 0 and not ParsingUtils.have_similar_strings(rest_name, filters):
            return

        func = getattr(self, function_name)
        swagger_resource = func(base_path=base_path, path=path)
        swagger_resource['package'] = package

        if model_name == 'Metadata':
            # Sadly I have to split this particular entity myself :(
            self._add_metadata_copies(resource=swagger_resource, results=results)
        else:
            results[model_name] = swagger_resource

    def _add_metadata_copies(self, resource, results):
        """ Metadata is splitted into:
            * Metadata
            * Global Metadata
            * Aggregate Metadata
        """
        metadata_info = deepcopy(resource)
        global_metadata_info = deepcopy(resource)
        aggregate_metadata_info = deepcopy(resource)

        metadata_info['apis'] = []
        global_metadata_info['apis'] = []
        aggregate_metadata_info['apis'] = []

        metadata_info['models']['Metadata']['id'] = u'Metadata'

        global_metadata_info['models']['GlobalMetadata'] = global_metadata_info['models']['Metadata']
        global_metadata_info['models'].pop('Metadata')
        global_metadata_info['models']['GlobalMetadata']['id'] = u'GlobalMetadata'


        aggregate_metadata_info['models']['AggregateMetadata'] = aggregate_metadata_info['models']['Metadata']
        aggregate_metadata_info['models'].pop('Metadata')
        aggregate_metadata_info['models']['AggregateMetadata']['id'] = u'AggregateMetadata'


        for api in resource['apis']:
            api_copy = deepcopy(api)
            if 'aggregatemetadatas' in api['path']:
                aggregate_metadata_info['apis'].append(api_copy)
            elif 'globalmetadatas' in api['path']:
                global_metadata_info['apis'].append(api_copy)
            else:
                metadata_info['apis'].append(api_copy)

        results['Metadata'] = metadata_info
        results['GlobalMetadata'] = global_metadata_info
        results['AggregateMetadata'] = aggregate_metadata_info

    # Specific methods

    def _get_swagger_resource(self, base_path, path):
        """ Make an HTTP request to retrieve information

        """
        url = '%s%s' % (base_path, path)

        try:  # Ugly hack due to Java issue: http://mvjira.mv.usa.alcatel.com/browse/VSD-546
            response = requests.get(url=url, verify=False)
        except requests.exceptions.SSLError:
            response = requests.get(url=url, verify=False)

        if response.status_code != 200:
            Printer.raiseError("[HTTP %s] An error occured while trying to retrieve information at url: %s" % (response.status_code, url))

        data = None
        try:
            data = response.json()
        except:
            Printer.raiseError("Could not load properly json from %s" % url)

        return data

    def _read_swagger_resource(self, base_path, path):
        """ Read the file to retrieve information

        """
        filepath = '%s%s' % (base_path, path)
        return ParsingUtils.parseJSON(filepath)


class SpecificationParser(object):
    """ Parse specifications directory

    """

    @classmethod
    def run(cls, directory):
        """ Grab all specification in given directory and return a dictionary of specs.

            Returns:
                A dictionary of specification

        """

        if not os.path.isdir(directory):
            Printer.raiseError("[File Path] Not a directory %s" % (directory))

        specs = dict()
        filenames = []
        for filename in os.listdir(directory):
            if filename.endswith(SPEC_EXTENSION):
                filenames.append(filename)
                filepath = '%s/%s' % (directory, filename)

                data = ParsingUtils.parseJSON(filepath)
                name = data['model']['entityName']

                specs[name] = data

        Printer.success('Parsed %s specifications' % len(filenames))
        return ParsingUtils.order(specs)
