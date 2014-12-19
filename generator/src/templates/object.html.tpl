<html>
<header>
    <link rel="stylesheet" type="text/css" href="css/style.css" />
</header>

<body>

    <div class="header">
        <div class="summary">
            <h1>{{model['name']}}</h1>
            <p>{{model['description']}}</p>
        </div>
        <div class="nav">
            <table>
                <tr>
                    <td><a href="index.html">API Reference</a></td>
                    <td><a href="#cat1">Accessing {{model['plural_name']}}</a></td>
                    <td><a href="#cat2">Attributes Overview</a></td>
                    <td><a href="#cat3">Child Objects</a></td>
                    <td><a href="#cat4">Attributes Documentation</a></td>
                </tr>

            </table>
        </div>
    </div>


    <div class="main">

        <a class="anchor" name="cat1"></a>
        <h2>Accessing {{model['plural_name']}}</h2>
        <div class="box">
            <ul>
            {% for api in model['apis']|sort(attribute='path') %}

                {% set methods = [] %}
                {% for operation in api['operations']|sort %}
                    {% do methods.append('<span title="' + operation['summary'] + '">' + operation['method'] + '</span>') %}
                {% endfor %}

                {% if 'parent' in api %}
                    {% set parent_resource = api['parent']['resource_name'] %}
                    {% set parent_url = api['parent']['remote_name'] %}
                    {% set model_name = model['resource_name'] %}
                    <li>/<a href="{{parent_url}}.html">{{parent_resource}}</a>/{id}/{{model_name}} <span class="httpmethods">[{{methods|join("|")}}]</span><li>
                {% else %}
                    <li>{{api['path']}} <span class="httpmethods">[{{methods|join("|")}}]</span><li>
                {% endif %}

            {% endfor %}
            </ul>

        </div>

        <a class="anchor" name="cat2"></a>
        <h2>Attributes Overview</h2>
        <div class="box">
            {
            <ul>
            {% for name, attribute in model['properties']|dictsort %}
                {% set type = attribute['type'] %}
                {% set description = attribute['description'] %}
                {% set required = attribute['required'] == 'true' %}
                {% set allowed = [] %}
                {% set allowed_values = "" %}

                {% if attribute['enum'] %}
                    {% for value in attribute['enum']|sort %}
                        {% do allowed.append(value) %}
                    {% endfor %}
                    {% if allowed|count > 0 %}
                        {% set allowed_values = " (" + allowed|join("|") + ")" %}
                    {% endif %}
                {% endif %}

                <li>
                    <a href="#{{name}}" title="{{description}}">{{name}}</a>: <span class="type_{{type}}">{{type}}{{allowed_values}}</span>{% if required %} <span class="required tag">required</span>{% endif %}{% if not loop.last %},{% endif %}
                </li>
            {% endfor %}
            </ul>
            }
        </div>


        <a class="anchor" name="cat3"></a>
        <h2>Child Objects</h2>

        <div class="box">
            {% if model['relations']|count == 0 %}
            <p> This object has no children</p>
            {% endif %}

            <ul>
            {% for relation in model['relations']|sort %}

            {% set api = relation['api'] %}

            {% set methods = [] %}
            {% set object_name = model['resource_name'] %}
            {% set remote_name = relation['remote_name'] %}
            {% set resource_name = relation['resource_name'] %}
            {% set path = api['path'] %}

            {% for operation in api['operations'] %}
                {% do methods.append('<span title="' + operation['summary'] + '">' + operation['method'] + '</span>') %}
            {% endfor %}


            <li>/{{object_name}}/{id}/<a href="{{remote_name}}.html">{{resource_name}}</a> <span class="httpmethods">[{{methods|join("|")}}]</span></li>
            {% endfor %}
            </ul>
        </div>


        <a class="anchor" name="cat4"></a>
        <h2>Attributes Documentation</h2>

        {% for name, attribute in model['properties']|dictsort %}
        <a name="{{name}}" class="anchor"></a>
        <div class="box">
            <div class="attributedescription">
                <div class="titlebanner">
                    <span class="name">{{name}} <span class="type_{{attribute['type']}}">{{attribute['type']}}</span></span>
                    <span class="metainformation">
                        {% if attribute['required'] == 'true' %} <span class="required tag">required</span>{% endif %}
                        {% if attribute['uniqueItems'] == 'true' %} <span class="unique tag">unique</span>{% endif %}
                    </span>

                </div>

                <div class="content">

                    <div class="description">
                        <h3>Description</h3>
                        <p>{{attribute['description']}}</p>
                    </div>

                    {% if attribute['enum'] %}
                    <div class="enumvalues">
                        <h3>Allowed values</h3>
                        <ul>
                            {% for value in attribute['enum']|sort %}
                                <li>{{value}}</li>
                            {% endfor %}
                        </ul>
                    </div>
                    {% endif %}

                </div>
            </div>
        </div>
        {% endfor %}

    </div>
</body>
</html>
