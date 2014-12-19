<html>
<header>
    <link rel="stylesheet" type="text/css" href="css/style.css" />
</header>

<body>
    <div class="header">
        <h1>Virtualized Services Directory API Reference</h1>
        <p>Welcome to VSD API Reference for version X.X</p>
    </div>

    <div class="summary">
        <div class="content">

            {% for package_name, model_names in packages|dictsort %}
                <h3>{{package_name}}</h3>
                <ul>
                {% for model_name in model_names|sort %}
                    {% set model = models[model_name] %}
                    <li><a name="{{model['name']}}" href="{{model['resource_name']}}.html" title="API reference for {{model['name']}}">{{model['name']}}</a></li>
                {% endfor %}
                </ul>
            {% endfor %}

        </div>
    </div>
</body>
</html>
