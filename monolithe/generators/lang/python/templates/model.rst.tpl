.. _{{ class_prefix|lower }}{{ specification.entity_name|lower }}:

{{ class_prefix|lower }}{{ specification.entity_name|lower }}
===========================================

.. class:: {{ class_prefix|lower }}{{ specification.entity_name|lower }}.{{ class_prefix }}{{ specification.entity_name }}(bambou.nurest_object.NUMetaRESTObject,):

{{ specification.description }}


Attributes
----------

{% for attribute in specification.attributes %}
- ``{{ attribute.local_name|lower }}``{% if attribute.required %} (**Mandatory**){% endif %}: {{ attribute.description }}
{% endfor %}


{% if specification.child_apis|length > 0 %}
Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**
{% for api in specification.child_apis %}{% set child_spec = specification_set[api.rest_name] %}
:ref:`{{ class_prefix|lower }}{{ child_spec.entity_name|lower }}.{{ class_prefix }}{{ child_spec.entity_name }}<{{ class_prefix|lower }}{{ child_spec.entity_name|lower }}>`{% for char in range(151 - 3*(class_prefix|length + child_spec.entity_name|length)) %} {% endfor %}``{{ child_spec.instance_name_plural }}`` {% endfor %}
================================================================================================================================================               ==========================================================================================
{% endif %}

{% if parent_apis|length > 0 %}
Parents
--------

{% for api in parent_apis %}
- :ref:`{{ class_prefix|lower }}{{ api.entity_name|lower }}.{{ class_prefix }}{{ api.entity_name }}<{{ class_prefix|lower }}{{ api.entity_name|lower }}>`
{% endfor %}
{% endif %}
