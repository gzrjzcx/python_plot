#2 lines graph
def line():
	#line graph
	plt.style.use('ggplot')
	nf = [2,3,4,"i+1"]
	x = np.arange(4)

	time_32 = [11.1133, 9.0016, 8.5105, 31.2036]
	time_64 = [21.1188, 15.75, 15.7521, 84.5158]
	fig_1 = plt.figure(figsize=(8, 4))
	ax_1 = fig_1.add_subplot(111)

	ax_1.set_xticks(x)
	ax_1.xaxis.set_ticks(x)
	ax_1.xaxis.set_ticklabels(nf)
	# ax_1.plot(x,static_1)

	ax_1.plot(x,time_32,label="Number_of_Filter = 32",linewidth=2,
	         marker='x')
	ax_1.plot(x,time_64,label="Number_of_Filter = 64",linewidth=2,
	         marker='o')

	ax_1.legend(loc=0)
	ax_1.set_ylabel('Runtime Per Epoch (seconds)')
	ax_1.set_xlabel('Stride Value')
	#ax_1.show()
	plt.savefig("line.pdf")