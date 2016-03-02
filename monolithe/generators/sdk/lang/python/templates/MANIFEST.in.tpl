include *.txt
include README.md
include LICENSE
{% for apiversion in apiversions %}
include {{ name }}/{{ apiversion }}/resources/*.ini
{% endfor %}
