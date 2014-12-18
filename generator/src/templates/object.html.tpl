<html>
<header>
    <link rel="stylesheet" type="text/css" href="../../src/templates/style.css" />
</header>

<body>
    <div class="header">
        <h1>{{model['name']}}</h1>
        <p>{{model['description']}}</p>
    </div>


    <div class="summary">
        <h2>Attributes Summary</h2>
        <ul>
        {% for name, attribute in model['properties'].iteritems() %}
            <li><a href="#{{name}}">{{name}}</a></li>
        {% endfor %}
        </ul>
    </div>

    <div class="main">

        <h2>Attributes Documentation</h2>

        {% for name, attribute in model['properties'].iteritems() %}
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
                        {% for value in attribute['enum'] %}
                            <li>{{value}}</li>
                        {% endfor %}
                    </ul>
                </div>
                {% endif %}

            </div>


        </div>
        {% endfor %}


        <h2>Child APIs</h2>


        <div class="relation">
            {% for api in model['apis'] %}
            <ul>
            {% for operation in api['operations'] %}

            {% if operation['method'] == 'GET' %}
                <li><b>GET   </b> {{api['path']}}</li>
            {% endif %}

            {% if operation['method'] == 'POST' %}
                <li><b>POST  </b> {{api['path']}}</li>
            {% endif %}

            {% if operation['method'] == 'DELETE' %}
                <li><b>DELETE</b> {{api['path']}}</li>
            {% endif %}

            {% endfor %}
            </ul>
            {% endfor %}
        </div>



        <h2>Parent APIs</h2>

        <div class="relation">
            {% for relation in model['relations'] %}
            {% set api = relation['api'] %}
            <ul>
            {% for operation in api['operations'] %}

            {% if operation['method'] == 'GET' %}
                <li><b>GET   </b> {{api['path']}}</li>
            {% endif %}

            {% if operation['method'] == 'POST' %}
                <li><b>POST  </b> {{api['path']}}</li>
            {% endif %}

            {% if operation['method'] == 'DELETE' %}
                <li><b>DELETE</b> {{api['path']}}</li>
            {% endif %}

            {% endfor %}
             </ul>
            {% endfor %}

        </div>
    </div>
</body>
</html>
