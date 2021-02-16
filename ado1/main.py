import math
from plot_graph import plotWithYAxis

def main():
  currentTime = 0
  step = 0.1
  limit = 2

  exerciseOneFunction = []
  a = []
  b = []
  c = []
  d = []
  e = []

  while(currentTime < limit):
    exerciseOneFunction.append(ex1(5,currentTime,1,3,30))
    a.append(exA(currentTime))
    b.append(exB(currentTime))
    c.append(exC(currentTime))
    d.append(exD(currentTime))
    e.append(exE(currentTime))
    currentTime += step
  
  print("Ex 1:\n")
  plotWithYAxis(exerciseOneFunction,"x(t)", "1. A - Vinicius Lima Fernandes", "EX 1 - A")
  print("\n Com esse tipo de equação podemos modelar o funcionamento de uma onda senoidal de uma tomada, podemos notar uma diferença ao compararmos uma tomada 110v com uma 220v, onde a de maior tensão possui uma amplitude maior.")

  print("\nEx 2:\n")
  plotWithYAxis(a,"x(t)", "2. A - Vinicius Lima Fernandes", "EX 2 - A")
  plotWithYAxis(b,"x(t)", "2. B - Vinicius Lima Fernandes", "EX 2 - B")
  plotWithYAxis(c,"x(t)", "2. C - Vinicius Lima Fernandes", "EX 2 - C")
  plotWithYAxis(d,"x(t)", "2. D - Vinicius Lima Fernandes", "EX 2 - D")
  plotWithYAxis(e,"x(t)", "2. E - Vinicius Lima Fernandes", "EX 2 - E")

  print("\nEx 3:\n")
  print("\nA = Amplitude da onda, o Alpha também irá influenciar na amplitude devido ao Euler aplicado logo em sequencia. w0 é a frequencia angular, geralmente acompanhada do T = instante de tempo na senoidal. O Theta é o angulo de fase")


def ex1(a,t,alpha,w0,omega):
  return a*(math.exp(-alpha*t)*math.cos((w0*t)+omega))

def exA(t):
  return 3*(math.exp(-t)*math.cos((9*t)-30))

def exB(t):
  return 3*(math.exp(-t)*math.cos((9*t)+30))

def exC(t):
  return math.exp(-0.1*t)*math.cos((4*t)-45)

def exD(t):
  return 10*(math.exp(-6*t)*math.cos((4*t)-45))

def exE(t):
  return 5*(math.exp(-t)*math.cos(t-0))

main()
