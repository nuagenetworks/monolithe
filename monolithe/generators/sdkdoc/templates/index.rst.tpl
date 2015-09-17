{% set title= "%s Documentation" % sdk_name.upper() %}
{{title}}
{{"=" * title|length}}

Getting Started
---------------

This section contains all the concepts to use `{{sdk_name}}` and a lot of tutorials and examples.

.. toctree::
    :maxdepth: 1
    :glob:

    license
    general_concepts
    installation
    getting_started


Sample Code
-----------

.. toctree::
    :maxdepth: 2
    :glob:

    sample_code


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

