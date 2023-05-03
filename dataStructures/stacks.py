
# Stacks example:
# list of websites while you browse[considering them as STACK], and then navigate using `back` button. They follow "last in first out".


browsing_session = []

browsing_session.append("https://www.google.com")
browsing_session.append("https://www.reddit.com")
browsing_session.append("https://www.py4e.com/lessons")
browsing_session.append("https://learn.microsoft.com/")
browsing_session.append("https://www.databricks.com/learn")


# just a function to print each item to a new line. nothing related to stacks


def foreachPrint(collection):
    print("*****START******")
    for i in collection:
        print("redirecting to ", i)
    print("*******END******")
    print()


foreachPrint(browsing_session)

# When user pressed a `back` button, we remove last element from stack by `pop()`
# lets say he clicked on back button 3 times.
browsing_session.pop()
browsing_session.pop()
browsing_session.pop()
foreachPrint(browsing_session)
# redirecting to  https://www.google.com
# redirecting to  https://www.reddit.com

# lets say he clicked on back button one more times.
browsing_session.pop()
foreachPrint(browsing_session)
# redirecting to  https://www.google.com

# now user has only one last item . ie. google.com
browsing_session.pop()
foreachPrint(browsing_session)


# now there is nothing to go back on sites. i.e stack is empty.
# But if we still try to remove an element from this empty stack,
# browsing_session.pop()
# we will get : IndexError: pop from empty list

# so we should add saftey check by validating whether stack is empty or not before doing pop()

if browsing_session:  # IF stack is having any values / nonEmpty
    browsing_session.pop()  # then you can remove by pop()
else:
    print("stack is empty")  # else disable back button
