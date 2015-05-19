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
                    <li><a data-id="overview" href="#overview">Overview</a></li>
                    <li><a data-id="apiresources" href="#apiresources">API Resource</a></li>
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
    {% set label_class = "label-default" %}
    {% elif method == "POST" %}
    {% set label_class = "label-primary" %}
    {% elif method == "PUT" %}
    {% set label_class = "label-success" %}
    {% elif method == "DELETE" %}
    {% set label_class = "label-danger" %}
    {% endif %}
    <span class="label {{label_class}}">{{method.lower()}}</span>
    {% endmacro %}

    {# macro to create allowed_choices list #}
    {% macro string_for_allowed_choices(attribute) %}
    {% set allowed = [] %}
    {% set allowed_values = "" %}
    {% if attribute.allowed_choices %}
    {% for value in attribute.allowed_choices|sort %}
    {% do allowed.append(value) %}
    {% endfor %}
    {% if allowed|count > 0 %}
    {% set allowed_values = " (" + allowed|join(" | ") + ")" %}
    {% endif %}
    {% endif %}
    {{allowed_values}}
    {% endmacro %}

    {# macro to create api list #}
    {% macro make_api_list(apis, mode, nothing_string) %}
    {% if apis|count %}
    {% for path, api in apis.iteritems()|sort %}
    <div class="row bordered-row">
        <div class="col-xs-7">
            {% if mode == "self" %}
            <span class="fixed-text">{{path.replace("{id}", "<span class=\"text-muted\">id</span>")}}</span>
            {% elif mode == "parents" %}
            <span class="fixed-text">/<a href="{{api.remote_name}}.html">{{api.resource_name}}</a>/<span class="text-muted">id</span>/{{model.resource_name}}</span>
            {% else %}
            <span class="fixed-text">/{{model.resource_name}}/<span class="text-muted">id</span>/<a href="{{api.remote_name}}.html">{{api.resource_name}}</a></span>
            {% endif %}
        </div>
        <div class="col-xs-5 text-right">
            {% for operation in api.operations|sort(attribute="method") %}
            {{label_for_method(operation.method)}}
            {% endfor %}
        </div>
    </div>
    {% endfor %}
    {% else %}
    <p>{{nothing_string}}</p>
    {% endif %}
    {% endmacro %}


    <div class="container">

        <section id="intro">
            <h2>{{model.name}}</h2>
            <p>{{model.description}}</p>
        </section>

        <section id="overview">
            <h3>Overview</h3>
                <table>
                    {% for attribute in model.attributes|sort(attribute='local_name') %}
                    <tr>
                        <td class="fixed-text">
                            <a href="#attr_{{attribute.remote_name}}" title="{{attribute.description}}">{{attribute.remote_name}}</a>
                        </td>
                        <td style="padding-left: 10px" class="fixed-text hide-xs">
                            <span class="type_{{attribute.type}}">{{attribute.type}}{{string_for_allowed_choices(attribute)}}</span>
                            {% if attribute.required %}
                            <span class="label label-primary fixed-text">required</span>
                            {% endif %}
                        </td>
                    </tr>
                    {% endfor %}
                </table>
        </section>

        <section id="apiresources">
            <h3>API Resource</h3>
            {{make_api_list(model.apis.self, "self", "This object is not directly accessible.")}}
        </section>

        <section id="parents">
            <h3>Parents</h3>
            {{make_api_list(model.apis.parents, "parents", "This object has no parents.")}}
        </section>

        <section id="children">
            <h3>Children</h3>
            {{make_api_list(model.apis.children, "children", "This object has no child.")}}
        </section>

        <section id="attributes">
            <h3>Attributes documentation</h3>
            {% for attribute in model.attributes|sort(attribute='local_name') %}
            <section id="attr_{{attribute.remote_name}}" class="filterable" data-filter-keyword="{{attribute.remote_name}}" style="padding-top: 60px; margin-top: -60px;">
                <div class="panel panel-default">
                    <div class="panel-heading fixed-text">
                        <b>{{attribute.remote_name}}</b>
                        <span class="type_{{attribute.type}} fixed-text">{{attribute.type}}</span>
                        {% if attribute.required %}
                        <span class="label label-danger float-right">required</span>
                        {% endif %}
                        {% if attribute.unique %}
                        <span class="label label-info float-right">unique</span>
                        {% endif %}
                    </div>

                    <div class="panel-body">
                        <p><b>Discussion</b></p>
                        <p>{{attribute.description}}</p>

                        {% if attribute.allowed_choices %}
                        <p><b>Allowed values</b></p>
                        <div class="panel panel-info">
                            <ul class="list-group fixed-text">
                            {% for value in attribute.allowed_choices|sort %}
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
