<h1>{{model['remote_name']}}</h1>
{{model['description']}}

<h2>Attributes</h2>

<table>
{% for name, attribute in model['properties'].iteritems() %}
<tr>
    <td>{{name}}</td>
    <td>
        <li>Type: {{attribute['type']}}</li>

        {% if attribute['enum'] %}
        <li>Values:
        {% for value in attribute['enum'] %}
            {{value}}{% if loop.index != 0 %}, {% endif %}
        {% endfor %}
        </li>
        {% endif %}

        {% if attribute['required'] == 'true' %}
        <li>Required: {{attribute['required']}}</li>
        {% endif %}
        {% if attribute['uniqueItems'] == 'true' %}
        <li>Required: {{attribute['uniqueItems']}}</li>
        {% endif %}
    </td>
    <td>{{attribute['description']}}</td>
</tr>
{% endfor %}
</table>

<h2>Services</h2>

<ul>
{% for api in model['apis'] %}
{% for operation in api['operations'] %}
    <li>
        {{operation['method']}} {{api['path']}}
    </li>
{% endfor %}
{% endfor %}
</ul>

<h2>Relations</h2>

<ul>
{% for relation in model['relations'] %}
{% set api = relation['api'] %}
{% for operation in api['operations'] %}
    <li>
        {{operation['method']}} {{api['path']}}
    </li>
{% endfor %}
{% endfor %}
</ul>