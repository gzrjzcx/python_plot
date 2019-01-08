#single bar chart
def plot_acc():
	#single bar chart
	x=("1", "4", "8", "16", "32", "64")
	bar_width = 0.3
	fig, ax = plt.subplots()
	y=(0.19429,0.14208,0.08174,0.05649)
	index = np.arange(len(y))
	rects2=plt.bar(index,y,bar_width,color='IndianRed')

	ax.set_ylabel('Runtime(s)')
	ax.set_xticks(index)
	ax.set_xticklabels(x)
	#ax.legend()

	plt.ylim(ymax=0.21,ymin=0.04)

	def autolabel(rects, xpos='center'):
	    """
	    Attach a text label above each bar in *rects*, displaying its height.

	    *xpos* indicates which side to place the text w.r.t. the center of
	    the bar. It can be one of the following {'center', 'right', 'left'}.
	    """

	    xpos = xpos.lower()  # normalize the case of the parameter
	    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
	    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

	    for rect in rects:
	        height = rect.get_height()
	        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.02*height,
	                '{}'.format(height), ha=ha[xpos], va='bottom')


	autolabel(rects2, "center")

	plt.savefig("single_bar.pdf")
