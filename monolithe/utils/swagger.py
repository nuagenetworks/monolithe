
class SwaggerUtils(object):
    """ URL Utilities

    """
    @classmethod
    def split_resource_path(self, resource_path, reference_path=None):
        """ Split resource path to retrieve the package and the resource name

            Args:
                resource_path (string): the resource path

            Returns:
                (package, resource_name)

            Example:
                split_resource_path('/usermgmt/User')
                >>> (/usermgmt, User)
        """

        if resource_path and resource_path.startswith(reference_path):
            return resource_path.split(reference_path)[1].rsplit('/', 1)

        return resource_path.rsplit('/', 2)[-2:]