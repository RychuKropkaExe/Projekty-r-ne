import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as FuncAnimation

x_data = []
y1_data = []
y2_data= []
y3_data= []
y4_data= []
y5_data = []
y6_data = []
y7_data = []
y8_data = []
y9_data = []
fig= plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax2 = fig.add_subplot(1,1,1)
ax3 = fig.add_subplot(1,1,1)
ax4 = fig.add_subplot(1,1,1)
ax5 = fig.add_subplot(1,1,1)
ax6 = fig.add_subplot(1,1,1)
ax7 = fig.add_subplot(1,1,1)
ax8 = fig.add_subplot(1,1,1)
ax9 = fig.add_subplot(1,1,1)
ax1.set_xlim(0, 20)
ax1.set_ylim(0, 1)
line, = ax1.plot(0, 0, label ='1m/s')
ax2.set_xlim(0, 20)
ax2.set_ylim(0, 1)
line2, = ax2.plot(0, 0, label = '~1.3m/s')
ax3.set_xlim(0, 20)
ax3.set_ylim(0, 1)
line3, = ax3.plot(0, 0, label = '~0.7m/s')
ax4.set_xlim(0, 20)
ax4.set_ylim(0, 1)
line4, = ax4.plot(0, 0,label = '~0.9m/s')
ax5.set_xlim(0, 20)
ax5.set_ylim(0, 1)
line5, = ax5.plot(0, 0, label = '~1.1m/s')
ax6.set_xlim(0, 20)
ax6.set_ylim(0, 1)
line6, = ax6.plot(0, 0, label = '~1.2m/s')
ax7.set_xlim(0, 20)
ax7.set_ylim(0, 1)
line7, = ax7.plot(0, 0, label = '~0.8m/s')
ax8.set_xlim(0, 20)
ax8.set_ylim(0, 1)
line8, = ax8.plot(0, 0, label = '~1.15m/s')
ax9.set_xlim(0, 20)
ax9.set_ylim(0, 1)
line9, = ax9.plot(0, 0, label = '~0.85m/s')
ax1.set_title('Zależność położenia piłki od czasu')
ax1.set_xlabel('Czas(s)')
ax1.set_ylabel('Wychylenie względem punktu 0 (m)')


def animation_frame(i):
	ax1.set_xlim(i/50-1,0.2+i/50)
	ax2.set_xlim(i/50-1,0.2+i/50)
	ax3.set_xlim(i/50-1,0.2+i/50)
	ax4.set_xlim(i/50-1,0.2+i/50)
	ax5.set_xlim(i/50-1,0.2+i/50)
	ax6.set_xlim(i/50-1,0.2+i/50)
	ax7.set_xlim(i/50-1,0.2+i/50)
	ax8.set_xlim(i/50-1,0.2+i/50)
	ax9.set_xlim(i/50-1,0.2+i/50)
	x_data.append(i/50)
	y1_data.append(2*np.abs(0.5*(i/50)-np.floor(0.5*(i/50)+0.5)))
	line.set_xdata(x_data)
	line.set_ydata(y1_data)
	y4_data.append(2*np.abs(0.5*(i/55)-np.floor(0.5*(i/55)+0.5)))
	line4.set_xdata(x_data)
	line4.set_ydata(y4_data)
	y6_data.append(2*np.abs(0.5*(i/41)-np.floor(0.5*(i/41)+0.5)))
	line6.set_xdata(x_data)
	line6.set_ydata(y6_data)
	y7_data.append(2*np.abs(0.5*(i/62)-np.floor(0.5*(i/62)+0.5)))
	line7.set_xdata(x_data)
	line7.set_ydata(y7_data)
	y8_data.append(2*np.abs(0.5*(i/43)-np.floor(0.5*(i/43)+0.5)))
	line8.set_xdata(x_data)
	line8.set_ydata(y8_data)
	y9_data.append(2*np.abs(0.5*(i/58)-np.floor(0.5*(i/58)+0.5)))
	line9.set_xdata(x_data)
	line9.set_ydata(y9_data)
	y5_data.append(2*np.abs(0.5*(i/45)-np.floor(0.5*(i/45)+0.5)))
	line5.set_xdata(x_data)
	line5.set_ydata(y5_data)
	y2_data.append(2*np.abs(0.5*(i/38)-np.floor(0.5*(i/38)+0.5)))
	line2.set_xdata(x_data)
	line2.set_ydata(y2_data)
	y3_data.append(2*np.abs(0.5*(i/71)-np.floor(0.5*(i/71)+0.5)))
	line3.set_xdata(x_data)
	line3.set_ydata(y3_data)
	# return line, line2, line3,

animation = FuncAnimation.FuncAnimation(fig, func=animation_frame, frames=1000, interval=50)
plt.legend(title='Legenda',  loc='upper left')
plt.show()
FFMpegWriter = FuncAnimation.writers['ffmpeg']
FFwriter = FFMpegWriter(fps=30)
animation.save('zadanie10.mp4',writer=FFwriter)