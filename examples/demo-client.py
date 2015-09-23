#!/usr/bin/env python
import sys
import importlib
import pprint
sys.path.append("codegen/tdldk")

tdldk = importlib.import_module("tdldk.v1_0")

session = tdldk.GATDLSession("", "", "http://127.0.0.1:5000", "")
session.start()

lists = session.root.lists.get()

print "\nLists\n=====\n"
for l in lists:

    print "\033[93m%s\033[0m: %s\n" % (l.title, l.description)

    for t in l.tasks.get():
        print "   [%s] \033[94m%s\033[0m: %s" % ("\033[92mx\033[0m" if t.is_complete() else " ", t.title, t.description)

        t.save()
    print "\n"

print "> Press enter to mark switch some task status"
sys.stdin.readline()

for t in session.root.lists[1].tasks:
    t.status = "TODO" if t.is_complete() else "DONE"
    t.save()

print "Done! restart this script to see your changes :)\n"