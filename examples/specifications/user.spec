{
    "resource_name": "users",
    "description": "Represent a user",
    "entity_name": "User",
    "get": true,
    "package": "todo-list",
    "update": true,
    "rest_name": "user",
    "attributes": {
        "userName": {
            "min_length": 1,
            "description": "the login",
            "exposed": true,
            "filterable": true,
            "required": true,
            "uniqueScope": "no",
            "max_length": 1024,
            "orderable": true,
            "unique": true,
            "type": "string"
        },
        "lastName": {
            "min_length": 1,
            "description": "The last name",
            "exposed": true,
            "filterable": true,
            "required": true,
            "uniqueScope": "no",
            "max_length": 1024,
            "orderable": true,
            "type": "string"
        },
        "firstName": {
            "min_length": 1,
            "description": "The first name",
            "exposed": true,
            "filterable": true,
            "required": true,
            "uniqueScope": "no",
            "max_length": 1024,
            "orderable": true,
            "type": "string"
        }
    },
    "delete": true
}