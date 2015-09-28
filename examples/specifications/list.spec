{
  "apis": {
    "children": {
        "/lists/{id}/tasks": {
          "RESTName": "task",
          "resourceName": "tasks",
          "entityName": "Task",
          "operations": [
              { "availability": null, "method": "GET" },
              { "availability": null, "method": "POST" }
          ]
        }
    },
    "parents": {
        "/lists": {
            "RESTName": "list",
            "resourceName": "lists",
            "operations": [
            {"availability": null, "method": "GET" },
            {"availability": null, "method": "POST"}
            ]
        }
    },
    "self": {
      "/lists/{id}": {
        "RESTName": "list",
        "resourceName": "lists",
        "entityName": "List",
        "operations": [
            { "availability": null, "method": "PUT" },
            { "availability": null, "method": "DELETE" },
            { "availability": null, "method": "GET" }
        ]
      }
    }
  },
  "model": {
    "extends": ["@description", "@title"],
    "RESTName": "list",
    "description": "Represent a a list of task to do",
    "entityName": "List",
    "package": "todo-list",
    "resourceName": "lists",
    "attributes": {}
  }
}