<html>
<header>
    <link href="css/bootstrap.min.css" rel="stylesheet">
</header>

<body style="padding-top: 70px">

    <nav class="navbar navbar-inverse navbar-fixed-top">
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
                    <li class="active"><a href="#">Home</a></li>
                    <li class=""><a href="usage.html">API Usage</a></li>

                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Components <span class="caret"></span></a>
                        <ul class="dropdown-menu" role="menu">
                            {% for package_name, model_names in packages|dictsort %}
                            <li class="divider"></li>
                            <li><a href="#section-{{package_name}}">{{package_name}}</a></li>
                            {% endfor %}
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <div class="container">

        {% for package_name, model_names in packages|dictsort %}
        <div class="panel panel-default" id="section-{{package_name}}">
            <div class="panel-heading"><b>{{package_name}}</b></div>
            <ul class="list-group">
            {% for model_name in model_names|sort %}
                {% set model = models[model_name] %}
                <li class="list-group-item"><a name="{{model.name}}" href="{{model.remote_name}}.html" title="API reference for {{model.name}}"> {{model.resource_name}}</a></li>
            {% endfor %}
            </ul>
        </div>
        {% endfor %}

    </div>

    <footer class="footer">
        <div class="container">
            <p class="text-muted">Copyright 2015 Nuage Networks.</p>
        </div>
    </footer>


    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>

</body>
</html>
