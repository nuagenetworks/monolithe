<html>
<header>
    <link rel="stylesheet" type="text/css" href="css/style.css" />
</header>

<body>
    <div class="header">
        <div class="summary">
            <h1>Virtualized Services Directory API Reference</h1>
            <p>Welcome to VSD API Reference for version X.X</p>
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
        <h2>Available APIs</h2>
        <div class="box">
            <ul>
            {% for filename, name in filenames|dictsort %}
                <li><a name="{{name}}" href="{{filename}}" title="API reference for {{name}}">{{name}}</a></li>
            {% endfor %}
            </ul>
        </div>
    </div>
</body>
</html>
