{
    "rest_name": "root",
    "attributes": {},
    "description": "Root object of the API",
    "entity_name": "Root",
    "package": "todo-list",
    "resource_name": "root",
    "get": true,
    "root": true,

    "children": [
        {
            "specification": "list",
            "relationship": "root",
            "get": true,
            "create": true
        },
        {
            "specification": "user",
            "relationship": "root",
            "get": true,
            "create": true
        }
    ]
}
