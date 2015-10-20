{

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

    "RESTName": "list",
    "attributes": {},
    "description": "Represent a a list of task to do",
    "entityName": "List",
    "extends": ["@description", "@title"],
    "package": "todo-list",
    "resourceName": "lists",
    "allowsGet": true,
    "allowsCreate": true,
    "allowsUpdate": false
}
