include *.txt
include README.md
include LICENSE
{% for apiversion in apiversions %}
include {{sdk_name}}/{{apiversion}}/resources/*.ini
{% endfor %}