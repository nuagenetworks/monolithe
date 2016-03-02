<!DOCTYPE html>
<html lang="en">
<head>
    <title>{{ product_name }} API Reference</title>
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
                <a class="navbar-brand" href="index.html">{{ product_name }} API Documentation</a>

            </div>
        </div>
    </nav>

    <div class="container" id="content">
        <h1>Available Versions</h1>
        {% for version, path in apiversion.iteritems() %}
            <div class="row bordered-row">
                <div class="col-xs-12">
                    <a href="{{ path }}/index.html" title="{{ product_name}} API version {{ version }}">{{ product_name}} API version {{ version }}</a>
                </div>
            </div>
        {% endfor %}

    </div>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/search.js"></script>

</body>
</html>
