#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
FPS = 60
from OpenGL.GL import *
from OpenGL.GLU import *
from loadObj import dump as mdump
surfaces = (
    (0, 1, 2, 3),
    (3, 2, 4, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6),
    )
verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
    )

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7),
    )
#	glBegin(GL_LINES)
#	for edge in edges:
#		for vertex in edge:
#			glColor3fv((0.3,1,0.3))
#			glVertex3fv(verticies[vertex])
#	glEnd()

def organizeTest():
  dat = mdump('untitled.obj')
  faces = dat[2]
  tris = []
  quads = []
  for item in faces:
    length = len(item)
    if length == 3:
      tris.append(item)
    elif length == 4:
      quads.append(item)
  
  return tris, quads


def Cube():

    # (vertices, edges, surfaces, obj_name)

    dat = mdump('untitled.obj')
    vertices = dat[0]
    edges = dat[1]
    surfaces = dat[2]

    quads = []
    tris = []
    
    glBegin(GL_QUADS)
    iter = False
    for surface in surfaces:
        color = ((1, 1, 1) if iter else (0.5, 0.5, 0.5))
        for vertex in surface:
            if len(surface) != 4:
                continue
            glColor3fv(color)
            glVertex3fv(vertices[vertex])
            iter = not iter
    glEnd()

    glBegin(GL_TRIANGLES)
    for surface in surfaces:
        color = ((1, 1, 1) if iter else (0.5, 0.5, 0.5))
        for vertex in surface:
          if len(surface) != 3:
            continue
          glColor3fv(color)
          print(f" '{vertices};;  '{vertex}: {len(vertices)}")
          glVertex3fv(vertices[vertex])  # Pick up here
        iter = not iter
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, display[0] / display[1], 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(1)


test = organizeTest()
print(f"tris: {len(test[0])}")
print(f"quads: {len(test[1])}")
dat = mdump('untitled.obj')
print(dat[0])
print(dat[1])

main()
