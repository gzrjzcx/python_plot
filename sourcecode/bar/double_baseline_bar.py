#double bar + baseline
def plot_acc2():
	import matplotlib as mpl
	mpl.use('Agg')
	import matplotlib.pyplot as plt
#	plt.style.use('fivethirtyeight')
	font_size = 10
	x=("Stride=2", "Stride=3", "Stride=4", "Stride=i+1")
	xd=("Dilation=2", "Dilation=3", "Dilation=4", "Dilation=i+1")
	rule=("Filters=32", "Filters=64")
	bar_width = 0.2
	mpl.rcParams['font.size'] = font_size
	fig, ax = plt.subplots()
	baseline = 0.8855
	plt.axhline(baseline, alpha = 0.7, linewidth = 0.7, linestyle='--', color='dimgrey')

	yd=((0.8938,0.8896,0.8841,0.8930), (0.8957,0.8919,0.889,0.8927))
	index = np.arange(len(yd[0]))
	rects1=ax.bar(index - bar_width/2,yd[0],bar_width,color='lightseagreen',label=rule[0])
	rects2=plt.bar(index+bar_width/2,yd[1],bar_width,color='IndianRed',label=rule[1])
	plt.text(len(index)-1 + 0.4,baseline - 0.0003,"Baseline", fontsize=8, color='dimgrey')

	ax.set_ylabel('Validation Accuracy')
	ax.set_xticks(index)
	ax.set_xticklabels(xd)
	ax.legend()

	plt.ylim(ymax=0.8980,ymin=0.88)

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
	        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.0005*height,
	                '{}'.format(height), ha=ha[xpos], va='bottom', fontsize = 8)


	autolabel(rects1, "center")
	autolabel(rects2, "center")

	plt.savefig("double_baseline_bar.pdf")
