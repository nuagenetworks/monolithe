lists = [{
    "ID": "1",
    "title": "Shopping List",
    "description": "Things to buy"
},
{
    "ID": "2",
    "title": "Secret List",
    "description": "You should not see this"
}]

def get_list(lid):
    try:
        return filter((lambda l: l["ID"] == lid), lists)[0]
    except:
        return None

def insert_list(lst):
    lists.append(lst)

def delete_list(lst):
    lists.remove(lst)

def list_equals(l1, l2):
    return (l1["ID"] == l2["ID"] and l1["title"] == l2["title"] and l1["description"] == l2["description"])



tasks = [{
        "ID": "11",
        "parentID": "1",
        "parentType": "list",
        "title": "Buy Milk",
        "description": "because it is good",
        "status": "TODO"
    },
    {
        "ID": "12",
        "parentID": "1",
        "parentType": "list",
        "title": "Buy Chocolate",
        "description": "because it is even better",
        "status": "TODO"
    },
    {
        "ID": "21",
        "parentID": "2",
        "parentType": "list",
        "title": "Explain Monolithe",
        "description": "We are doing it right now",
        "status": "TODO"
    },
    {
        "ID": "22",
        "parentID": "2",
        "parentType": "list",
        "title": "Make Garuda popular",
        "description": "Almost done",
        "status": "TODO"
    },

    {
        "ID": "23",
        "parentID": "2",
        "parentType": "list",
        "title": "Dominate the world",
        "description": "That is the plan",
        "status": "TODO"
    }
]

def get_tasks_of_lists(lid):
    try:
        return filter((lambda t: t["parentID"] == lid), tasks)
    except:
        return None

def get_task(tid):
    try:
        return filter((lambda t: t["ID"] == tid), tasks)[0]
    except:
        return None

def insert_task(task):
    tasks.append(task)

def delete_task(task):
    tasks.remove(task)

def task_equals(t1, t2):
    return t1["ID"] == t2["ID"] and t1["title"] == t2["title"] and t1["description"] == t2["description"] and t1["status"] == t2["status"]






