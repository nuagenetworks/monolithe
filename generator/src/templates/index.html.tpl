<html>
<header>
    <link rel="stylesheet" type="text/css" href="css/style.css" />
        <link href='http://fonts.googleapis.com/css?family=Open+Sans:800,700,400' rel='stylesheet' type='text/css'>
        <link href='http://fonts.googleapis.com/css?family=Source+Code+Pro:400,700' rel='stylesheet' type='text/css'>
</header>

<body>
    <div class="header">
        <div class="summary">
            <h1>Virtualized Services Directory API Reference</h1>
        </div>
        <div class="nav">
            <table>
                <tr>
                    <td><a href="usage.html">API Usage</a></td>
                </tr>

            </table>
        </div>
    </div>

    <div class="main">
        <div class="box">
            {% for package_name, model_names in packages|dictsort %}
                <h2>{{package_name}}</h2>
                <ul>
                {% for model_name in model_names|sort %}
                    {% set model = models[model_name] %}
                    <li><a name="{{model['name']}}" href="{{model['remote_name']}}.html" title="API reference for {{model['name']}}">- {{model['resource_name']}}</a></li>
                {% endfor %}
                </ul>
            {% endfor %}
        </div>
    </div>
</body>
</html>
