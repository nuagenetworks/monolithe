{
    "resource_name": "root", 
    "description": "Root object of the API", 
    "entity_name": "Root", 
    "get": true, 
    "package": "todo-list", 
    "rest_name": "root", 
    "root": true, 
    "children": [
        {
            "specification": "list", 
            "create": true, 
            "relationship": "root", 
            "get": true
        }, 
        {
            "specification": "user", 
            "create": true, 
            "relationship": "root", 
            "get": true
        }
    ]
}