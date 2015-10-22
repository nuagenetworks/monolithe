{
    "resource_name": "lists", 
    "description": "Represent a a list of task to do", 
    "entity_name": "List", 
    "package": "todo-list", 
    "get": true, 
    "update": true, 
    "rest_name": "list", 
    "extends": [
        "@description", 
        "@title"
    ], 
    "children": [
        {
            "specification": "task", 
            "create": true, 
            "relationship": "child", 
            "get": true
        }
    ], 
    "delete": true
}