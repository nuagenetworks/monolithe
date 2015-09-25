{% set title = "%s API %s Reference" % (sdk_name.upper(),  version) %}
{{ title }}
{{"=" * title|length }}

**Models**

.. toctree::
    :maxdepth: 1
    :glob:

    {{ sdk_name }}/{{ version }}/models.*

**Fetchers**

.. toctree::
    :maxdepth: 1
    :glob:

    {{ sdk_name }}/{{ version }}/fetchers.*

