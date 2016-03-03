#!/usr/bin/env python
from __future__ import print_function
import sys
import os
import importlib


# Ho, Hi There!
# I guess you are coming from my good friend, the README file
# He's a nice guy, and I'm glad you have listen to him :)
# Please go through this example, and you'll uncover a bit of
# of the awesomeness of Monolithe!


# manually import the tlddk
# you should not do this like that of course. this is for the demo
# We don't want to you to have to install the tlddk on your system
# so we simply use some python magic. You don't need to undersand that
# you would normally write somehing like
#
#   from tlddk import v1_0 as tlddk
sys.path.insert(0, "%s/codegen/python" % os.path.abspath(os.path.dirname(__file__)))
tdldk = importlib.import_module("tdldk.v1_0")


# uncomment the two following lines to log the ReST communication.
# but don't do that now, it will screw up the output.
# continue to read ;)
#
# tdldk_utils = importlib.import_module("tdldk.utils")
# tdldk_utils.set_log_level(logging.DEBUG)


# create a session. The demo server doesn't care about your credentials,
# we put junk. The only important thing is of course the api_url
session = tdldk.GATDLSession(username="root", enterprise="nuagenetworks", password="password", api_url="http://127.0.0.1:5555")

# now we start the session. This would normally authenticate your credentials and return your root api object with an
# api key. But again, here we don't validate anything.
session.start()

# we now get the complete list of todo "GATLDList"
lists = session.root.lists.get()

# we print them
print()
print("Lists")
print("=====")
print()

# we loop on GATLDLists
for l in lists:

    # we use the SDK to access the properties
    print("\033[93m%s\033[0m: %s" % (l.title, l.description))
    print()

    tasks = l.tasks.get()
    if tasks:
        for t in tasks:
            print("   [%s] \033[94m%s\033[0m: %s" % ("\033[92mx\033[0m" if t.is_complete() else " ", t.title, t.description))

    print()
    print()

# we ask for the user to press enter to continue this demo
print("> Press enter to mark switch some task status")
sys.stdin.readline()


# then we loop on the tasks of the second list, and switch the status from DONE to TODO or vice versa
# you'll notice that we are using the is_complete() method. This convenience method has been added to the
# overrides comming from the user sdk vanilla.
# yep, it's cool

# you aslo notice that we are not using the lists variables, but we directly
# use the internal object list. This list has been populated during the get process.
# but of course, you can set a flag to not internally commit what you just fetched.
for t in session.root.lists[1].tasks:

    # we  update the attribute "status"
    t.status = "TODO" if t.is_complete() else "DONE"

    # then we simply save the changes
    t.save()

# and we are done. You can restart the script and you'll see that
# some tasks have been marked as DONE.
print("Done! restart this script to see your changes :)\n")


# did you notice that you never saw a ReST call, or a json structure?
# but you can, by uncommenting the logging, near the top of the this file :)
