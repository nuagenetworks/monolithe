<!DOCTYPE html>
<html lang="en">
<head>
    <title>{{model.name}} API Reference</title>
    <link rel="stylesheet" href="css/bootstrap.css">
    <link rel="stylesheet" href="css/style.css">
</head>

<body data-spy="scroll" data-target="#navbarmain">

    <nav class="navbar navbar-default navbar-fixed-top" id="navbarmain">
        <div class="container-fluid">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="index.html">VSD API Documentation</a>
            </div>
            <div class="collapse navbar-collapse" id="navbar">
                <ul class="nav navbar-nav">
                    <li><a data-id="intro" href="#intro">Top</a></li>
                    <li><a data-id="apiresources" href="#apiresources">API Resources</a></li>
                    <li><a data-id="overview" href="#overview">Overview</a></li>
                    <li><a data-id="parents" href="#parents">Parents</a></li>
                    <li><a data-id="children" href="#children">Children</a></li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Attributes <span class="caret"></span></a>
                        <ul class="dropdown-menu" role="menu">
                            {% for attribute in model.attributes|sort(attribute='local_name') %}
                            <li><a data-id="attr_{{attribute.remote_name}}" href="#attr_{{attribute.remote_name}}" class="fixed-text">{{attribute.remote_name}}</a></li>
                            {% endfor %}
                        </ul>
                    </li>
                </ul>
                <form class="navbar-form navbar-right" role="search">
                    <div class="form-group dropdown">
                        <input type="text" class="form-control" placeholder="Search" id="searchfield">
                        <ul class="dropdown-menu dropdown-menu-left" role="menu" id="searchresult" style="display: none"></ul>
                    </div>
                </form>
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
    {% set local_apis = [] %}
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
    {% do local_apis.append({"path": api.path.replace("{id}", "id"), "methods": methods}) %}
    {% endif %}
    {% endfor %}

    <div class="container">

        <section id="intro">
            <h2>{{model.name}}</h2>
            <p>{{model.description}}</p>
        </section>

        <section id="apiresources">
            <h3>API Resource</h3>
            {% if local_apis|count %}
            <table class="table">
                {% for local_api in local_apis %}
                <tr>
                    <td>
                        <span class="fixed-text">{{local_api.path}}</span>
                    </td>
                    <td style="text-align: right; font-size: 13px">
                        {% for method in local_api.methods %}
                        {{label_for_method(method)}}
                        {% endfor %}
                    </td>
                </tr>
                {% endfor %}
                <tr><td></td><td></td></tr>
            </table>
            {% else %}
            <p>This object is not dircetly accessible.</p>
            {% endif %}
        </section>

        <section id="overview">
            <h3>Object overview</h3>
            <div class="well well-sm fixed-text">
                {
                <ul style="padding-left: 10px">
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
                            {% set allowed_values = " (" + allowed|join(" | ") + ")" %}
                        {% endif %}
                    {% endif %}
                    <li style="list-style: none">
                        <a href="#attr_{{attribute.remote_name}}" title="{{description}}">{{attribute.remote_name}}</a>:
                        <span class="type_{{type}}">{{type}}{{allowed_values}}</span>
                        {% if required %}
                        <span class="label label-primary fixed-text">required</span>
                        {% endif %}
                    </li>
                {% endfor %}
                </ul>
                }
            </div>
        </section>

        <section id="parents">
            <h3>Parents</h3>
            <table class="table">
                {% if parent_apis|count %}
                {% for api in parent_apis %}
                <tr>
                    <td>
                        <span class="fixed-text">/<a href="{{api.parent_url}}.html">{{api.parent_resource}}</a>/id/{{api.model_name}}</span>
                    </td>
                    <td style="text-align: right; font-size: 13px">
                        {% for method in api.methods %}
                        {{label_for_method(method)}}
                        {% endfor %}
                    </td>
                </tr>
                {% endfor %}
                <tr><td></td><td></td></tr>
            </table>
            {% else %}
            <p>This object has no parent API.</p>
            {% endif %}
        </section>

        <section id="children">
            <h3>Children</h3>
            {% if model.apis['children']|count %}
            <table class="table">
                {% for path, api in model.apis['children'].iteriterms()|sort %}
                {% set methods = [] %}
                {% set object_name = model.resource_name %}
                {% set remote_name = api.remote_name %}
                {% set resource_name = api.resource_name %}
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
                        <div style="pull-right">
                        {% for method in methods|sort|reverse %}
                        {{label_for_method(method)}}
                        {% endfor %}
                        </div>
                    </td>
                </tr>
                {% endfor %}
                <tr><td></td><td></td></tr>
            </table>
            {% else %}
            <p>This object has no child.</p>
            {% endif %}
        </section>

        <section id="attributes">
            <h3>Attributes documentation</h3>
            {% for attribute in model.attributes|sort(attribute='local_name') %}
            <section id="attr_{{attribute.remote_name}}" class="filterable" data-filter-keyword="{{attribute.remote_name}}" style="padding-top: 60px; margin-top: -60px;">
                <div class="panel panel-default">
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
            </section>
            {% endfor %}
        </section>

    </div>


    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/search.js"></script>

    <script>
        $(document).ready(function()
        {
            initialize_search("attr_");
            initialize_scrollspy();
        });
    </script>
</body>
</html>
