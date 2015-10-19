{
    "apis": {
        "children": {
            "/lists/{id}/tasks": {
                "RESTName": "task",
                "entityName": "Task",
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
                "resourceName": "tasks"
            }
        },
        "parents": {
            "/lists": {
                "RESTName": "list",
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
            }
        },
        "self": {
            "/lists/{id}": {
                "RESTName": "list",
                "entityName": "List",
                "operations": [
                    {
                        "availability": null,
                        "method": "PUT"
                    },
                    {
                        "availability": null,
                        "method": "DELETE"
                    },
                    {
                        "availability": null,
                        "method": "GET"
                    }
                ],
                "resourceName": "lists"
            }
        }
    },
    "model": {
        "RESTName": "list",
        "attributes": {},
        "description": "Represent a a list of task to do",
        "entityName": "List",
        "extends": [
            "@description",
            "@title"
        ],
        "package": "todo-list",
        "resourceName": "lists"
    }
}
