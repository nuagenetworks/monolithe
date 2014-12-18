<html>
<header>
    <link rel="stylesheet" type="text/css" href="css/style.css" />
</header>

<body>
    <div class="header">
        <h1>{{model['name']}}</h1>
        <p>{{model['description']}}</p>
    </div>


    <div class="summary">
        <h2>Attributes Summary</h2>
        <ul>
        {% for name, attribute in model['properties'].iteritems()|sort(case_sensitive=False) %}
            <li><a href="#{{name}}">- {{name}}</a></li>
        {% endfor %}
        <br>
        <a href="#childapis">- Child APIs</a>
        <br>
        <a href="#parentapis">- Parent APIs</a>
        </ul>
    </div>

    <div class="main">

        <h2>Attributes Documentation</h2>

        {% for name, attribute in model['properties'].iteritems()|sort(case_sensitive=False) %}
        <div class="attribute">

            <a name="{{name}}"></a>
            <div class="titlebanner">
                <span class="name">{{name}} <span class="type">&lt;{{attribute['type']}}&gt;</span></span>
                <span class="metainformation">
                    {% if attribute['required'] == 'true' %} <span class="required tag">required</span>{% endif %}
                    {% if attribute['uniqueItems'] == 'true' %} <span class="unique tag">unique</span>{% endif %}
                </span>

            </div>

            <div class="content">

                <div class="description">
                    <h3>Description</h3>
                    <p>{{attribute['description']}}</p>
                </div>

                {% if attribute['enum'] %}
                <div class="enumvalues">
                    <h3>Allowed values</h3>
                    <ul>
                        {% for value in attribute['enum']|sort %}
                            <li>{{value}}</li>
                        {% endfor %}
                    </ul>
                </div>
                {% endif %}

            </div>


        </div>
        {% endfor %}



        <a name="childapis"></a>
        <h2>Child APIs</h2>
        <div class="relation">

            {% if model['relations']|count == 0 %}
            <p> This object has no children</p>
            {% endif %}

            {% for relation in model['relations'] %}
            {% set api = relation['api'] %}

            <a href="{{api['operations'][0]['type']|lower}}.html">- {{api['operations'][0]['type']|lower}}</a>
            <ul>
            {% for operation in api['operations'] %}

                {% if operation['method'] == 'GET' %}
                    {% set method = 'GET    ' %}
                {% endif %}

                {% if operation['method'] == 'POST' %}
                    {% set method = 'POST   ' %}
                {% endif %}

                {% if operation['method'] == 'DELETE' %}
                    {% set method = 'DELETE ' %}
                {% endif %}

                <li><b>{{method}}</b>{{api['path']}}</li>

            {% endfor %}
             </ul>
            {% endfor %}

        </div>


        <a name="parentapis"></a>
        <h2>Parent APIs</h2>
        <div class="relation">

            {% if model['apis']|count == 0 %}
            <p> This object has no parent</p>
            {% endif %}

            {% for api in model['apis'] %}

            <ul>
            {% for operation in api['operations'] %}

            {% if operation['method'] == 'PUT' %}
                {% set method = 'PUT    ' %}
            {% endif %}

            {% if operation['method'] == 'GET' %}
                {% set method = 'GET    ' %}
            {% endif %}

            {% if operation['method'] == 'POST' %}
                {% set method = 'POST   ' %}
            {% endif %}

            {% if operation['method'] == 'DELETE' %}
                {% set method = 'DELETE ' %}
            {% endif %}

            <li><b>{{method}}</b>{{api['path']}}</li>

            {% endfor %}
            </ul>

            {% endfor %}
        </div>


    </div>
</body>
</html>
