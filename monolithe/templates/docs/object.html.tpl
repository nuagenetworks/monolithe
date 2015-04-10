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
                            <li class=""><a href="#accessing">Accessing the Object</a></li>
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


    <div class="container" id="top">

        <h1>{{model.name}}</h1>
        <p>{{model.description}}</p>

        <h2 id="accessing">Accessing the object</h2>
        <ul class="list-group">
        {% for api in model.apis|sort(attribute='path') %}

            {% set methods = [] %}
            {% for operation in api.operations|sort %}
                {% do methods.append(operation['method']) %}
            {% endfor %}

            <li class="list-group-item">
                <span class="fixed-text">
                {% if api.parent_resource_name and api.parent_resource_name != 'me' %}
                {% set parent_resource = api.parent_resource_name %}
                {% set parent_url = api.parent_remote_name %}
                {% set model_name = model.resource_name %}
                    /<a href="{{parent_url}}.html">{{parent_resource}}</a>/{id}/{{model_name}}
                {% else %}
                    {{api.path}}
                {% endif %}
                </span>

                {% for method in methods|sort|reverse %}
                {% if method == "GET" %}
                {% set label_class = "label-primary" %}
                {% elif method == "POST" %}
                {% set label_class = "label-info" %}
                {% elif method == "PUT" %}
                {% set label_class = "label-success" %}
                {% elif method == "DELETE" %}
                {% set label_class = "label-danger" %}
                {% endif %}
                <span class="label {{label_class}} float-right" style="margin-left: 5px">{{method.lower()}}</span>
                {% endfor %}

            </li>

        {% endfor %}
        </ul>

        <h2 id="overview">Object overview</h2>
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

        <h2>Children of the object</h2>
        {% if model.relations|count == 0 %}
        <p> This object has no children</p>
        {% endif %}
        <ul class="list-group">
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

            <li class="list-group-item">
                <span class="fixed-text">
                    /{{object_name}}/{id}/<a href="{{remote_name}}.html">{{resource_name}}</a>
                </span>
                {% for method in methods|sort|reverse %}
                {% if method == "GET" %}
                {% set label_class = "label-primary" %}
                {% elif method == "POST" %}
                {% set label_class = "label-info" %}
                {% elif method == "PUT" %}
                {% set label_class = "label-success" %}
                {% elif method == "DELETE" %}
                {% set label_class = "label-danger" %}
                {% endif %}

                <span class="label {{label_class}} float-right" style="margin-left: 5px">{{method.lower()}}</span>
                {% endfor %}
            </li>
        {% endfor %}
        </ul>


        <h2 id="attributes">Attributes documentation</h2>
        {% for attribute in model.attributes|sort(attribute='local_name') %}
        <div class="panel panel-default" id="attr_{{attribute.remote_name}}">
            <div class="panel-heading fixed-text"><b>{{attribute.remote_name}}</b>
                <span class="type_{{attribute.remote_type}} fixed-text">{{attribute.remote_type}}</span>
                {% if attribute.is_required %}
                <span class="label label-default float-right">required</span>
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
