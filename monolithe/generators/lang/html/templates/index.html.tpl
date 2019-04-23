<!DOCTYPE html>
<html lang="en">
<head>
    <title>{{ product_name }} API Reference {{ apiversion }}</title>
    <link rel="stylesheet" href="../css/bootstrap.css">
    <link rel="stylesheet" href="../css/style.css">
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
                <a class="navbar-brand" href="index.html">{{ product_name }} API Documentation {{ apiversion }}</a>

            </div>
            <div class="collapse navbar-collapse" id="navbar">
                <ul class="nav navbar-nav">
                    <li><a href="../usage.html">API Usage</a></li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Components <span class="caret"></span></a>
                        <ul class="dropdown-menu" role="menu">
                            {%- set package_name = [None] %}
                            {%- for specification in specifications|sort(attribute='package') %}
                                {%- if package_name[0] != specification.package %}
                                    {%- set _ = package_name.pop() %}
                                    {%- set _ = package_name.append(specification.package) %}
                                    <li class="divider"></li>
                                    <li><a data-id="section-{{ package_name[0]| replace(" ", "_")}}" href="#section-{{ package_name[0] | replace(" ", "_")}}">{{ package_name[0] }}</a></li>
                                {%- endif %}
                            {%- endfor %}
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

    <div class="container" id="content">
        {%- set package_name = [None] %}
        {%- for specification in specifications|sort(attribute='package') %}
            {%- if package_name[0] != specification.package %}
                {%- if package_name[0] %}
                    </section>
                {% endif %}
                {%- set _ = package_name.pop() %}
                {%- set _ = package_name.append(specification.package) %}
                <section id="section-{{ package_name[0] | replace(" ", "_")}}">
                <h3>{{ package_name[0] }}</h3>
            {%- endif %}
            {%- if specification.rest_name != None %}
                {%- set link_name = specification.rest_name|lower %}
            {%- else %}
                {%- set link_name = specification.entity_name|lower %}
            {%- endif %}
            {%- if specification.resource_name != None %}
                {%- set resource_name = specification.resource_name|lower %}
            {%- else %}
                {%- set resource_name = specification.entity_name|lower %}
            {%- endif %}
            <div class="row bordered-row">
                <div class="col-xs-12">
                    <a class="filterable" data-filter-keyword="{{ resource_name }}" id="{{ resource_name }}" href="{{ link_name }}.html" title="API reference for {{ link_name }}">{{ resource_name }}</a>
                    <br>
                    {%- if specification.description %}
                        <small>{{ specification.description }}</small>
                    {%- else %}
                        <small>No description available</small>
                    {%- endif %}
                </div>
            </div>
        {%- endfor %}
    </div>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <script src="../js/bootstrap.min.js"></script>
    <script src="../js/search.js"></script>

    <script>
        $(document).ready(function() {
            initialize_search("");
            initialize_scrollspy();
        });
    </script>

</body>
</html>
