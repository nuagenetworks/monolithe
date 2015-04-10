<html>
<header>
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/style.css" rel="stylesheet">
</header>

<body>


    <nav class="navbar navbar-inverse navbar-static-top">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#">VSD API Documentation</a>
            </div>

            <div id="navbar" class="collapse navbar-collapse">
                <ul class="nav navbar-nav">
                    <li class=""><a href="index.html">Home</a></li>
                    <li class=""><a href="usage.html">API Usage</a></li>
                    <li class="#top"><a href="#top">Top</a></li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Navigation <span class="caret"></span></a>
                        <ul class="dropdown-menu" role="menu">
                            <li class=""><a href="#parents">Parents</a></li>
                            <li class="divider"></li>
                            <li class=""><a href="#overview">Overview</a></li>
                            <li class="divider"></li>
                            <li class=""><a href="#children">Children</a></li>
                            <li class="divider"></li>
                            <li class=""><a href="#attributes">Attributes</a></li>
                            {% for attribute in model.attributes|sort(attribute='local_name') %}
                            <li class=""><a href="#attr_{{attribute.remote_name}}"><span class="fixed-text">{{attribute.remote_name}}</span></a></li>
                            {% endfor %}
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    {# macro to create a method label #}
    {% macro label_for_method(method) %}
    {% if method == "GET" %}
    {% set label_class = "label-primary" %}
    {% elif method == "POST" %}
    {% set label_class = "label-info" %}
    {% elif method == "PUT" %}
    {% set label_class = "label-success" %}
    {% elif method == "DELETE" %}
    {% set label_class = "label-danger" %}
    {% endif %}
    <span class="label {{label_class}}">{{method.lower()}}</span>
    {% endmacro %}

    {# formatting information #}
    {% set local_api = [] %}
    {% set parent_apis = [] %}
    {% for api in model.apis|sort(attribute='path') %}
    {% set methods = [] %}
    {% for operation in api.operations|sort %}
    {% do methods.append(operation['method']) %}
    {% do methods.sort() %}
    {% endfor %}
    {% if api.parent_resource_name and api.parent_resource_name != 'me' %}
    {% do parent_apis.append({"parent_resource": api.parent_resource_name, "parent_url": api.parent_remote_name, "model_name": model.resource_name, "methods": methods}) %}
    {% else %}
    {% do local_api.append({"path": api.path, "methods": methods}) %}
    {% endif %}
    {% endfor %}

    <div class="container" id="top">

        <h1>{{model.name}}</h1>
        <p>{{model.description}}</p>




        <h3 id="self">API</h3>
        {% if local_api|count %}
        <table class="table">
            <tr>
                <td>
                    <span class="fixed-text">{{local_api[0].path}}</span>
                </td>
                <td>
                <td style="text-align: right; font-size: 13px">
                    {% for method in local_api[0].methods %}
                    {{label_for_method(method)}}
                    {% endfor %}
                </td>
            </tr>
        </table>
        {% else %}
        <p>This object is not dircetly accessible.</p>
        {% endif %}


        <h3 id="overview">Object overview</h3>
        <div class="well well-sm fixed-text">
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
                <li style="list-style: none">
                    <a href="#attr_{{attribute.remote_name}}" title="{{description}}">{{attribute.remote_name}}</a>:
                    <span class="type_{{type}}">{{type}}{{allowed_values}}</span>
                    {% if required %}
                    <span class="label label-primary fixed-text">required</span>
                    {% endif %}{% if not loop.last %},{% endif %}
                </li>
            {% endfor %}
            </ul>
            }
        </div>


        <h3 id="parents">Parents</h3>
        <table class="table">

        {% if parent_apis|count %}
        {% for api in parent_apis %}
            <tr>
                <td>
                    <span class="fixed-text">/<a href="{{parent_url}}.html">{{api.parent_resource}}</a>/id/{{api.model_name}}</span>
                </td>
                <td style="text-align: right; font-size: 13px">
                    {% for method in api.methods %}
                    {{label_for_method(method)}}
                    {% endfor %}
                </td>
            </tr>
        {% endfor %}
        </table>
        {% else %}
        <p>This object has no parent API.</p>
        {% endif %}



        <h3 id="children">Children</h2>
        <table class="table">
        {% for relation in model.relations|sort %}

        {% set api = relation.api %}

        {% set methods = [] %}
        {% set object_name = model.resource_name %}
        {% set remote_name = relation.remote_name %}
        {% set resource_name = relation.resource_name %}
        {% set path = api.path %}

            {% for operation in api.operations %}
                {% do methods.append(operation['method']) %}
            {% endfor %}

            <tr>
                <td>
                    <span class="fixed-text">
                        /{{object_name}}/id/<a href="{{remote_name}}.html">{{resource_name}}</a>
                    </span>
                </td>
                <td style="text-align: right; font-size: 13px">
                    {% for method in methods|sort|reverse %}
                    {{label_for_method(method)}}
                    {% endfor %}
                </td>
            </tr>
        {% endfor %}
        </table>


        <h3 id="attributes">Attributes documentation</h3>
        {% for attribute in model.attributes|sort(attribute='local_name') %}
        <div class="panel panel-default" id="attr_{{attribute.remote_name}}">
            <div class="panel-heading fixed-text">
                <b>{{attribute.remote_name}}</b>
                <span class="type_{{attribute.remote_type}} fixed-text">{{attribute.remote_type}}</span>
                {% if attribute.is_required %}
                <span class="label label-danger float-right">required</span>
                {% endif %}
                {% if attribute.is_unique %}
                <span class="label label-info float-right">unique</span>
                {% endif %}
            </div>

            <div class="panel-body">
                <p><b>Discussion</b></p>
                <p>{{attribute.description}}</p>

                {% if attribute.choices %}
                <p><b>Allowed values</b></p>
                <div class="panel panel-info">
                    <ul class="list-group fixed-text">
                    {% for value in attribute.choices|sort %}
                        <li class="list-group-item">{{value}}</li>
                    {% endfor %}
                    </ul>
                </div>
                {% endif %}

                <p><b>vsdk attribute</b></p>
                <p class="fixed-text">{{attribute.local_name}}</p>
            </div>
        </div>
        {% endfor %}


    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>

</body>
</html>
