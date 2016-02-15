#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Essa é uma função que faz a transformada de Fourier e plota no domínio da freguência.

[X, freq] = fftf(x, Fs)

onde,

x = Sinal de Entrada
Fs = Frequência de amostragem do sinal
X = Modulo do sinal no domínio da freguência
freq = Vetor de Freguências

Requisitos: sudo apt-get install python numpy matplotlib scipy ffmpeg

 """

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy.fftpack

# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Eu'), bitrate=1800)

def update_line(num, data, line):
	line.set_data(data[..., :num])
	return line,


def plot_sinal(x, y, interval=25):
	x = x.astype(float).tolist() #Sinal
	y = y.astype(float).tolist() #Time or Frequence
	fig = plt.figure()
	line, = plt.plot([], [], 'r-')
	plt.xlim(0, max(y))
	plt.ylim(0, max(x))
	data = (np.array([y, x])).astype(float)
	line_ani = animation.FuncAnimation(fig, update_line, len(x), fargs=(data, line),interval=interval, blit=True)
	#line_ani.save('sinals.mp4', writer=writer)
	plt.show()

def fftf(x, Fs):#output[ X, freq ]
	N = len(x)
	k = np.arange(0, N)
	T = N/float(Fs)
	freq = k/T
	X = scipy.fftpack.fft(x)/N
	cutoff = np.ceil(N/2)
	X = X[0: cutoff]
	freq = freq[0:cutoff]
	return X, freq


#Exemplo
Fs = 100
time = np.arange(0, 5, 1/float(Fs))

#Sinais
x = np.sin(2 * np.pi * 10 * time)
y = 2 * np.sin(2 * np.pi * 60 * time)
z = 20 * np.sin(2 * np.pi * 200 * time)
w = 15 * np.sin(2 * np.pi * 350 * time)
ruido = np.random.rand(len(time.tolist()))

sinal = x + y + z + w + ruido

#plotar sinal do dominio do tempo
plot_sinal(sinal, time, 2)

#aplicar a Transformada de Fourier
#sinal, freq = fftf(sinal, Fs)

#plotar sinal do dominio da feguência
#plot_sinal(np.abs(sinal), freq, 2)
