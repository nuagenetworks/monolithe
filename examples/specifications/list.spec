{
    "model": {
        "resource_name": "lists",
        "description": "Represent a a list of task to do",
        "entity_name": "List",
        "package": "todo-list",
        "get": true,
        "update": true,
        "delete": true,
        "rest_name": "list",
        "extends": [
            "@description",
            "@title"
        ]
    },
    "children": {
        "task": {
            "create": true,
            "relationship": "child",
            "get": true
        }
    }
}