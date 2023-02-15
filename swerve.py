import math

x = 1
y = 0
t = 1
l = 9
w = 9
r = math.hypot(l, w)

print("Joystick Vectors: (" + str(x) + ", " + str(y) + ", " + str(t) + ")")

def invKinematics():
    A = y - t * l/r
    B = y + t * l/r
    C = x - t * w/r
    D = x + t * w/r

    ws1 = math.sqrt(B**2+C**2) 
    ws2 = math.sqrt(B**2+D**2) 
    ws3 = math.sqrt(A**2+D**2)
    ws4 = math.sqrt(A**2+C**2) 

    wa1 = math.atan2(B,C)*180/math.pi
    wa2 = math.atan2(B,D)*180/math.pi
    wa3 = math.atan2(A,D)*180/math.pi
    wa4 = math.atan2(A,C)*180/math.pi

    speeds = [ws1, ws2, ws3, ws4]
    angles = [wa1, wa2, wa3, wa4]

    speeds = [i/max(speeds) for i in speeds]

    print("Speeds: " + str(speeds))
    print("Angles: " + str(angles))

    return [speeds, angles]

new = invKinematics()

