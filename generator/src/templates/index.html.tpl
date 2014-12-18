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
        <ul>
        {% for filename, name in filenames|dictsort %}
            <li>
                <a name="{{name}}" href="{{filename}}" title="API reference for {{name}}">{{name}}</a>
            </li>
        {% endfor %}
        </ul>
    </div>
</body>
</html>
