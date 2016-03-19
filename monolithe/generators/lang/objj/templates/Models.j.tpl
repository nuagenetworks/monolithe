{{ header }}

@import <Bambou/NURESTModelController.j>
@import "Fetchers/Fetchers.j"

{% for filename, classname in filenames.iteritems() -%}
@import "{{ filename }}"
{% endfor %}

{% for filename, classname in filenames.iteritems() -%}
[[NURESTModelController defaultController] registerModelClass:{{ class_prefix }}{{ classname }}];
{% endfor %}
