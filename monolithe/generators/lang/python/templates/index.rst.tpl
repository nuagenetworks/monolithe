VSPK Documentation
==================

.. toctree::
    :caption: Quickstart

    quickstart

{% for version in apiversions %}
.. toctree::
    :caption: {{ version }} reference
    :maxdepth: 1
    :glob:

    {{ version }}/*

{% endfor %}
