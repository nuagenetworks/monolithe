{
    "rest_name": "list",
    "description": "Represent a a list of task to do",
    "entity_name": "List",
    "extends": ["@description", "@title"],
    "package": "todo-list",
    "resource_name": "lists",
    "get": true,
    "update": true,

    "children": [
        {
            "specification": "task",
            "get": true,
            "create": true
        }
    ]
}
