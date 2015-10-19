{
    "apis": {
        "children": {
            "/lists": {
                "RESTName": "list",
                "entityName": "List",
                "relationship": "root",
                "operations": [
                    {
                        "availability": null,
                        "method": "GET"
                    },
                    {
                        "availability": null,
                        "method": "POST"
                    }
                ],
                "resourceName": "lists"
            },
            "/users": {
                "RESTName": "user",
                "entityName": "User",
                "relationship": "root",
                "operations": [
                    {
                        "availability": null,
                        "method": "GET"
                    },
                    {
                        "availability": null,
                        "method": "POST"
                    }
                ],
                "resourceName": "users"
            }
        },
        "parents": {},
        "self": {}
    },
    "model": {
        "RESTName": "root",
        "attributes": {},
        "description": "Root object of the API",
        "entityName": "Root",
        "package": "todo-list",
        "resourceName": "root"
    }
}
