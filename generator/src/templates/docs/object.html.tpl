<html>
<header>
    <link rel="stylesheet" type="text/css" href="css/style.css" />
    <link href='http://fonts.googleapis.com/css?family=Open+Sans:800,700,400' rel='stylesheet' type='text/css'>
    <link href='http://fonts.googleapis.com/css?family=Source+Code+Pro:400,700' rel='stylesheet' type='text/css'>
</header>

<body>

    <div class="header">
        <div class="summary">
            <h1>{{model.name}}</h1>
        </div>
        <div class="nav">
            <table>
                <tr>
                    <td><a href="index.html">API Reference</a></td>
                    <td><a href="#cat0">Description</a></td>
                    <td><a href="#cat1">Accessing the object</a></td>
                    <td><a href="#cat2">Object overview</a></td>
                    <td><a href="#cat3">Children of the object</a></td>
                    <td><a href="#cat4">Attributes documentation</a></td>
                    <td><a href="#cat5">Python SDK documentation</a></td>
                </tr>
            </table>
        </div>
    </div>

    <div class="main">
        <h1 class="compact-title">{{model.name}}</h1>

        <a class="anchor" name="cat0"></a>
        <h2>Description</h2>
        <div class="box">
            <p>{{model.description}}</p>
        </div>

        <a class="anchor" name="cat1"></a>
        <h2>Accessing the object</h2>
        <div class="box">
            <ul>
            {% for api in model.apis|sort(attribute='path') %}

                {% set methods = [] %}
                {% for operation in api.operations|sort %}
                    {% do methods.append('<span title="' + operation['summary'] + '">' + operation['method'] + '</span>') %}
                {% endfor %}

                {% if api.parent_resource_name %}
                    {% set parent_resource = api.parent_resource_name %}
                    {% set parent_url = api.parent_remote_name %}
                    {% set model_name = model.resource_name %}
                    <li>/<a href="{{parent_url}}.html">{{parent_resource}}</a>/{id}/{{model_name}} <span class="httpmethods">[{{methods|join("|")}}]</span><li>
                {% else %}
                    <li>{{api.path}} <span class="httpmethods">[{{methods|join("|")}}]</span><li>
                {% endif %}

            {% endfor %}
            </ul>
        </div>

        <a class="anchor" name="cat2"></a>
        <h2>Object overview</h2>
        <div class="box">
            {
            <ul>
            {% for attribute in model.attributes|sort(attribute='local_name') %}
                {% set type = attribute.remote_type %}
                {% set description = attribute.description %}
                {% set required = attribute.is_required %}
                {% set allowed = [] %}
                {% set allowed_values = "" %}

                {% if attribute.choices %}
                    {% for value in attribute.choices|sort %}
                        {% do allowed.append(value) %}
                    {% endfor %}
                    {% if allowed|count > 0 %}
                        {% set allowed_values = " (" + allowed|join("|") + ")" %}
                    {% endif %}
                {% endif %}
                <li>
                    <a href="#{{attribute.remote_name}}" title="{{description}}">{{attribute.remote_name}}</a>: <span class="type_{{type}}">{{type}}{{allowed_values}}</span>{% if required %} <span class="tagrequired tag">required</span>{% endif %}{% if not loop.last %},{% endif %}
                </li>
            {% endfor %}
            </ul>
            }
        </div>

        <a class="anchor" name="cat3"></a>
        <h2>Children of the object</h2>
        <div class="box">
            {% if model.relations|count == 0 %}
            <p> This object has no children</p>
            {% endif %}

            <ul>
            {% for relation in model.relations|sort %}

            {% set api = relation.api %}

            {% set methods = [] %}
            {% set object_name = model.resource_name %}
            {% set remote_name = relation.remote_name %}
            {% set resource_name = relation.resource_name %}
            {% set path = api.path %}

            {% for operation in api.operations %}
                {% do methods.append('<span title="' + operation['summary'] + '">' + operation['method'] + '</span>') %}
            {% endfor %}


            <li>/{{object_name}}/{id}/<a href="{{remote_name}}.html">{{resource_name}}</a> <span class="httpmethods">[{{methods|join("|")}}]</span></li>
            {% endfor %}
            </ul>
        </div>

        <a class="anchor" name="cat4"></a>
        <h2>Attributes documentation</h2>
        {% for attribute in model.attributes|sort(attribute='local_name') %}
        <a name="{{attribute.remote_name}}" class="anchor"></a>
        <div class="box">
            <div class="attributedescription">
                <div class="titlebanner">
                    <span class="name">{{attribute.remote_name}} <span class="type_{{attribute.remote_type}}">{{attribute.remote_type}}</span></span>
                    <span class="metainformation">
                        {% if attribute.is_required %} <span class="tagrequired tag">required</span>{% endif %}
                        {% if attribute.is_unique %} <span class="tagunique tag">unique</span>{% endif %}
                    </span>
                </div>
                <div class="content">
                    <div class="description">
                        <p>{{attribute.description}}</p>
                    </div>
                    {% if attribute.choices %}
                    <div class="enumvalues">
                        <h3>Allowed values</h3>
                        <ul>
                            {% for value in attribute.choices|sort %}
                                <li>{{value}}</li>
                            {% endfor %}
                        </ul>
                    </div>
                    {% endif %}
                </div>
            </div>
        </div>
        {% endfor %}

        <a class="anchor" name="cat5"></a>
        <h2>Python SDK Documentation</h2>
        <div class="box">
            class <i>vsdk.</i>NU{{model.name}}

            <h3>Attribute names</h3>
            <ul>
            {% for attribute in model.attributes|sort(attribute='local_name') %}
                <li><a href="#{{attribute.remote_name}}" title="{{attribute.description}}">{{attribute.local_name}}</a></li>
            {% endfor %}
            </ul>

            <h3>Fetcher names</h3>
            <ul>
            {% for relation in model.relations|sort %}
                <li><a href="{{relation.remote_name}}.html">{{relation.instance_plural_name}}</a>_fetchers</li>
            {% endfor %}
            </ul>
        </div>
    </div>
</body>
</html>
