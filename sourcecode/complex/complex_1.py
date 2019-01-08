def plot_acc():
	#single bar chart + line + baseline + 2-y axies
	x=("dsss", "sdss", "ssds", "sssd", "dsds", "ddss", "sdsd", "ssdd", "dssd", "sdds", "ddds", "ddsd", "dsdd", "sddd")
	bar_width = 0.4
	fig, ax = plt.subplots()
	y=(0.8844,0.8879,0.8791,0.8795,0.888,0.8861,0.8873,0.8813,0.8859,0.8932,0.8932,0.8896,0.8909,0.8901)
	ytime=(18.9275,12.6869,11.7486,11.0955,19.9795,24.6282,12.7664,11.5947,20.1973,13.0857,29.5648,25.9743,19.9849,13.3105)
	index = np.arange(len(y))

	baseline = 0.8855
	plt.axhline(baseline, alpha = 0.7, linewidth = 0.7, linestyle='--', color='dimgrey')
	plt.text(2-bar_width/2,baseline - 0.0002,"Baseline", fontsize=8, color='dimgrey')
	
	rects2=plt.bar(index,y,bar_width,color='IndianRed')

	ax.set_xticks(index)
	ax.set_xticklabels(x,fontsize=9)
	ax.set_xlabel("Different Combinations of Strided Layer(s) And Dilation Layer(d)")
	#plt.ylim(ymax=np.max(y)+0.005,ymin=np.min(y)-0.001)
	ax.set_ylim(ymax=np.max(y)+0.005,ymin=np.min(y)-0.001)
	ax.tick_params(axis='y', labelcolor='IndianRed')
	ax.set_ylabel('Accuracy', color="IndianRed")

	ax2 = ax.twinx()
	ax2.set_ylim(np.min(ytime)-30, np.max(ytime)+2)
	ax2.set_ylabel('Runtime', color="lightseagreen")
	plt.plot(x,ytime,label="Runtime",linewidth=1.5,marker='1',color="lightseagreen")
	ax2.tick_params(axis='y', labelcolor="lightseagreen")

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
	                '{}'.format(height), ha=ha[xpos], va='bottom', fontsize=7)


	autolabel(rects2, "center")

	plt.savefig("exp3.pdf")
