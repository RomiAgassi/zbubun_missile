vel= float(input("what is the starting velucity (m/s)?"))
angle=float(input("what is the starting angle compered the the horizon (degrees)?"))
hight=float(input("what is the starting hight (m)"))

from math import sin,cos,pi,atan,sqrt
angle_radians= angle * 2 * pi / 360.0

vel_x= vel*cos(angle_radians)
vel_y = vel*sin(angle_radians)


t1= (-vel_y + ((vel**2*(sin(angle_radians))**2)-2*-9.8*hight)**0.5)/-9.8
t2= (-vel_y - ((vel**2*(sin(angle_radians))**2)-2*-9.8*hight)**0.5)/-9.8

if(t1>t2):
    t_ground=t1
else:
    t_ground=t2


if(t_ground<0):
    print("check the data you entered")
else:
    x= vel_x*t_ground
    print("location when hitting the ground", x)

    v_ground= sqrt(vel_x**2 + (vel_y+(-9.8)*t_ground)**2)
    print("the speed of impact with the ground is", v_ground)

    angle_ground= atan((vel_y+9.8*t_ground)/(vel_x))
    angle_ground2= (angle_ground*180)/ pi
    print("the angle of impact with the ground is", angle_ground2)





