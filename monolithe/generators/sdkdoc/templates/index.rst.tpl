{% set title= "%s Documentation" % sdk_name.upper() %}
{{title}}
{{"=" * title|length}}


{% for section in pages_info %}
{{section["name"]}}
{{"=" * section["name"]|length}}
.. toctree::
    :maxdepth: {{section["toc_depth"]}}
    :glob:

{% for page in section["pages"] %}
    {{page}}
{% endfor %}
{% endfor %}


{% set title= "%s API Reference" % sdk_name.upper() %}
{{title}}
{{"=" * title|length}}

This section describes all models and fetchers from the `{{sdk_name}}`.

.. toctree::
    :maxdepth: 1
    :glob:

    {{sdk_name}}_*_reference



Bambou API Reference
--------------------

This section describes the underlying Bambou module.

.. toctree::
    :maxdepth: 1
    :glob:

    bambou_reference


Indices and tables
==================

* :ref:`genindex`
* :ref:`search`

