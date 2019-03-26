from OpenGL.GL import*
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *


car_x = 0
forward = True
angle = 0


def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 1, 50)
    gluLookAt(8, 9, 10,
              0, 0, 0,
              0, 1, 0)
    glClearColor(0.6, 1, 1, 1)


def draw():
    global car_x
    global forward
    global angle

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glEnable(GL_DEPTH_TEST)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    #terrain
    glColor3f(0.6, 1, 0.2)
    glBegin(GL_QUADS)
    glVertex(-50, -1.25 * 0.5 - 0.6, -15)
    glVertex(-50, -1.25 * 0.5 - 0.6, 10)
    glVertex(30, -1.25 * 0.5 - 0.6, 10)
    glVertex(30, -1.25 * 0.5 - 0.6, -15)
    glEnd()

    #road
    glColor3f(0.4, 0.4, 0.4)
    glBegin(GL_QUADS)
    glVertex(-30, -1.25 * 0.5 - 0.5, -4.5)
    glVertex(-30, -1.25 * 0.5 - 0.5, 4.5)
    glVertex(10, -1.25 * 0.5 - 0.5, 4.5)
    glVertex(10, -1.25 * 0.5 - 0.5, -4.5)
    glEnd()

    #lanes
    for i in range(-30, 11, 4):
        for (R, G, B, type) in ((1, 1, 1, GL_QUADS), (0, 0, 0, GL_LINE_LOOP)):
            glLineWidth(3)
            glColor3f(R, G, B)
            glBegin(type)
            glVertex(i, -1.25 * 0.5 - 0.4, -0.5)
            glVertex(i, -1.25 * 0.5 - 0.4, 0.5)
            glVertex(i + 3, -1.25 * 0.4 - 0.5, 0.5)
            glVertex(i + 3, -1.25 * 0.4 - 0.5, -0.5)
            glEnd()


    #sidewalk
    for i in range (-30, 10, 2):
        for j in -5, 5:
            if(i % 4 == 0):
                glColor3f(0, 0, 0)
                glLoadIdentity()
                glTranslate(i, -1, j)
                glScale(2, 0.5, 1)
                glutSolidCube(1)
                glutWireCube(1)
            else:
                glColor3f(1, 1, 1)
                glLoadIdentity()
                glTranslate(i, -1, j)
                glScale(2, 0.5, 1)
                glutSolidCube(1)
                glColor3f(0, 0, 0)
                glutWireCube(1)

   #trees
    for z in -7, 7:
        for x in range(-21, 10, 10):
            glColor3f(0.4, 0.2, 0.1)
            for y in np.arange(-1, 4, 0.1):
                glLoadIdentity()
                glTranslate(x, y, z)
                glutSolidSphere(0.4, 10, 10)
            glColor3f(0.5, 0.7, 0)
            glLoadIdentity()
            glTranslate(x, 4, z)
            glutSolidSphere(2, 10, 10)



    #lower cube
    glColor3f(0.12, 0.18, 0.32)
    glLoadIdentity()
    glTranslate(car_x, 0, 2.5)
    glScale(1, 0.25, 0.5)
    glutSolidCube(5)
    glColor3f(0, 0, 0)
    glutWireCube(5)


    #upper cube
    glColor3f(0.12, 0.18, 0.32)
    glLoadIdentity()
    glTranslate(car_x, 5*0.25, 2.5)
    glScale(0.5, 0.25, 0.5)
    glutSolidCube(5)
    glColor3f(0, 0, 0)
    glutWireCube(5)


    glLoadIdentity()
    for (R, G, B, type) in (0.9, 0.9, 0.9, GL_POLYGON), (0, 0, 0, GL_LINE_LOOP):
        glColor3f(R, G, B)
        glBegin(type)
        glVertex(car_x + 2.5 / 2, 1.25 / 2, 2.5 + 1.25)
        glVertex(car_x + 2.5 / 2, 1.25 / 2 + 1.25, 2.5 + 1.25)
        glVertex(car_x + 2.5 / 2 + 1.25, 1.25 / 2, 2.5 + 1.25)
        glEnd()
        glBegin(type)
        glVertex(car_x + 2.5 / 2, 1.25 / 2, 2.5 - 1.25)
        glVertex(car_x + 2.5 / 2, 1.25 / 2 + 1.25, 2.5 - 1.25)
        glVertex(car_x + 2.5 / 2 + 1.25, 1.25 / 2, 2.5 - 1.25)
        glEnd()
        glBegin(type)
        glVertex(car_x + 2.5 / 2, 1.25 / 2 + 1.25, 2.5 + 1.25)
        glVertex(car_x + 2.5 / 2 + 1.25, 1.25 / 2, 2.5 + 1.25)
        glVertex(car_x + 2.5 / 2 + 1.25, 1.25 / 2, 2.5 - 1.25)
        glVertex(car_x + 2.5 / 2, 1.25 / 2 + 1.25, 2.5 - 1.25)
        glEnd()

    #front right wheel
    glLoadIdentity()
    glColor3f(0.9, 0.8, 0.8)
    glTranslate(car_x + 0.5 * 5, -0.5* 1.25, 2.5*0.5 + 2.5)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.2, 0.5, 10, 10)


    #front left wheel
    glLoadIdentity()
    glColor3f(0.9, 0.8, 0.8)
    glTranslate(car_x + 0.5 * 5, -0.5* 1.25, -2.5*0.5 + 2.5)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.2, 0.5, 10, 10)

    #back right wheel
    glLoadIdentity()
    glColor3f(0.9, 0.8, 0.8)
    glTranslate(car_x - 0.5 * 5, -0.5* 1.25, 2.5*0.5 + 2.5)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.2, 0.5, 10, 10)

    #back left wheel
    glLoadIdentity()
    glColor3f(0.9, 0.8, 0.8)
    glTranslate(car_x - 0.5 * 5, -0.5* 1.25, -2.5*0.5 + 2.5)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.2, 0.5, 10, 10)

    #right light
    glLoadIdentity()
    glColor3f(1, 1, 0.4)
    glTranslate(car_x + 0.5 * 5, 0, 0.25 * 2.5 + 2.5)
    glutSolidSphere(0.2, 10, 10)

    #left light
    glLoadIdentity()
    glColor3f(1, 1, 0.4)
    glTranslate(car_x + 0.5 * 5, 0,- 0.25 * 2.5 + 2.5)
    glutSolidSphere(0.2, 10, 10)

    glutSwapBuffers()

    if forward:
        car_x += 0.1
        angle -= 5
        if car_x > 5:
            forward = False
    else:
        car_x -= 0.1
        angle += 5
        if car_x < -5:
            forward = True






glutInit()
glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Car")
myInit()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()