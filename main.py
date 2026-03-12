from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import sin, cos

earth_angle = 0
moon_angle = 0

camX = 12
camY = 8
camZ = 12


def init():
    glClearColor(0, 0, 0, 1)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, 1, 1, 50)

    glMatrixMode(GL_MODELVIEW)


def draw_sun():
    glColor3f(1, 1, 0)
    glutSolidSphere(1.0, 50, 50)


def draw_earth():
    glColor3f(0, 0, 1)
    glutSolidSphere(0.5, 50, 50)


def draw_moon():
    glColor3f(0.8, 0.8, 0.8)
    glutSolidSphere(0.2, 50, 50)


def draw_orbit(radius):
    glColor3f(1, 1, 1)

    glBegin(GL_LINE_LOOP)

    for i in range(100):
        angle = 2 * 3.14159 * i / 100
        x = radius * cos(angle)
        z = radius * sin(angle)

        glVertex3f(x, 0, z)

    glEnd()


def display():

    global earth_angle, moon_angle
    global camX, camY, camZ

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(camX, camY, camZ,
              0, 0, 0,
              0, 1, 0)

    # SUN
    glPushMatrix()
    draw_sun()

    # EARTH ORBIT
    draw_orbit(4)

    glRotatef(earth_angle, 0, 1, 0)
    glTranslatef(4, 0, 0)

    # EARTH
    glPushMatrix()
    draw_earth()

    # MOON ORBIT
    draw_orbit(1.5)

    glRotatef(moon_angle, 0, 1, 0)
    glTranslatef(1.5, 0, 0)

    # MOON
    glPushMatrix()
    draw_moon()
    glPopMatrix()

    glPopMatrix()

    glPopMatrix()

    glutSwapBuffers()


def update(value):

    global earth_angle, moon_angle

    earth_angle += 1
    moon_angle += 4

    glutPostRedisplay()
    glutTimerFunc(25, update, 0)


def keyboard(key, x, y):

    global camX, camY, camZ

    speed = 0.5

    if key == b'w':
        camZ -= speed

    elif key == b's':
        camZ += speed

    elif key == b'a':
        camX -= speed

    elif key == b'd':
        camX += speed

    elif key == b'q':
        camY += speed

    elif key == b'e':
        camY -= speed

    glutPostRedisplay()


def main():

    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 800)
    glutCreateWindow(b"Hierarchical Solar System")

    init()

    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutTimerFunc(25, update, 0)

    glutMainLoop()


main()