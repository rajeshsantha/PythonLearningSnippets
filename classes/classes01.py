# class is a blueprint of an object.

# GENERAL UNDERSTANDING IN PLAIN/LAYMAN LANGUAGE:

# car is a class/concept/idea. `Toyata Fortuner` is an object/blueprint/instance of the class `car`
# when you get a good idea to build some car called `X` :
# Then ->
# you have to first explain to your factory engineers about
#   1. what should be features [sunroof,hill-assist,rear-ac-vents,music-system,360 camera..etc]
#   2. how it should work [ automatic/manual gears, 6 gears/5 gears, 4 wheel drive or 2 wheel drive,...] {these are behaviour. i.e METHODs/FUNCTIONs}
#   3. what kind physical properties it will have [engine capcity(cc), size of the car, number of seats, boot space, ground clearance ..] {These are properties. i.e VARIABLES}
# Until, here you idea is just an idea/blueprint
# Once the build/manufacture is completed and relased into the market and on-road, then only it will be a real CAR
# i.e Only when you create an object, people can see its a will have usability. By using object/CAR only you can execute methods like,
# how to open sunroof, how to turn on 360 camera, how to go on from point A to point B at certain speed...etc
# As an end-user/car-user, you don't need to know how engine will work. You just need to use the engine by calling its function
# Eg: By switching on START button of the car [ In code its carObject.tunrOnEngine() ; you dont need to know how tunrOnEngine() is implemented. Its called `abstraction` (hiding the complexe things from user) ]

# When you think of class, you dont need to think technically. You think in objects.
# When you want to implement college register kind app, You can think who will be there in it.
# There will be students,teachers,principle,...those will be the classes.
# Lets take STUDENT
#    -> student registration form in pdf format will be a class.
#    -> A student 'rajesh' took a printout of it and fill it with his details and submitted to college.
#           {  val rajesh = new Student("rajesh", 28, "IT",...)  }
#    -> Now `rajesh` is an real student (object), and many other students follow the same.
#   n number students mean n number of objects of class `STUDENT`

# This is object oriented/based programming.


# TL;DR;

# Animal is a class. Dog,Cat are objects

# class will have what properties(variables) and behaviours(methods). But its kind of plan of a building/.
# Object will make the class into reality.
# Which means class is concept but has no existence until an object is created.
# only objects will have memory allocation.

x = 1
print(type(x))
