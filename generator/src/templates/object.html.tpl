<html>
<header>
    <link rel="stylesheet" type="text/css" href="css/style.css" />
</header>

<body>
    <div class="header">
        <h1>{{model['name']}}</h1>
        <p>{{model['description']}}</p>
    </div>


    <div class="main">

        <div class="summary">
            <h2>Accessing {{model['plural_name']}}</h2>
            <div class="content">
                <ul>
                {% for api in model['apis']|sort(attribute='path') %}

                    {% set methods = [] %}
                    {% for operation in api['operations']|sort %}
                        {% do methods.append(operation['method']) %}
                    {% endfor %}

                    <li>{{api['path']}} <span class="httpmethods">[{{methods|join("|")}}]</span><li>
                {% endfor %}
                </ul>

            </div>


            <h2>{{model['name']}} Object Attributes Overview</h2>
            <div class="content">
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
                        <a href="#{{name}}" title="{{description}}">{{name}}</a>: <span class="type_{{type}}">{{type}}{{allowed_values}}
                        {% if required %}
                            <span class="required tag">required</span>
                        {% endif %}
                    </li>
                {% endfor %}
                </ul>
                }
            </div>
            <br/>


            <h2>Child Objects</h2>

            <div class="content">
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
                    {% do methods.append(operation['method']) %}
                {% endfor %}


                <li>/{{object_name}}/{id}/<a href="{{remote_name}}.html">{{resource_name}}</a> <span class="httpmethods">[{{methods|join("|")}}]</span></li>
                {% endfor %}
                </ul>
            </div>

        </div>


        <h2>Attributes Documentation</h2>

        {% for name, attribute in model['properties']|dictsort %}
        <div class="attribute">

            <a name="{{name}}"></a>
            <div class="titlebanner">
                <span class="name">{{name}} <span class="type_{{attribute['type']}}">&lt;{{attribute['type']}}&gt;</span></span>
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
        {% endfor %}

    </div>
</body>
</html>
