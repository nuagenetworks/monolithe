{
    "children": {
        "/lists/{id}/tasks": {
            "rest_name": "task",
            "entity_name": "Task",
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
            "resource_name": "tasks"
        }
    },
    "parents": {
        "/lists": {
            "rest_name": "list",
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
            "resource_mame": "lists"
        }
    },

    "rest_name": "list",
    "attributes": {},
    "description": "Represent a a list of task to do",
    "entity_name": "List",
    "extends": ["@description", "@title"],
    "package": "todo-list",
    "resource_name": "lists",
    "allows_get": true,
    "allows_create": true
}
