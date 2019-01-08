#triple bar chart
def triple_bar():
	import matplotlib as mpl
	mpl.use('Agg')
	import matplotlib.pyplot as plt
#	plt.style.use('fivethirtyeight')
	font_size = 10
	x=("Layers=2", "Layers=4", "Layers=6")
	rule=("Filters=16", "Filters=32", "Filters=64")
	bar_width = 0.17
	mpl.rcParams['font.size'] = font_size
	fig, ax = plt.subplots()
	y=((0.8553, 0.8767, 0.8763),(0.8749, 0.8855, 0.8849),(0.8815, 0.8862, 0.8877))
	index = np.arange(len(y[0]))
	rects1=ax.bar(index - bar_width,y[0],bar_width,color='lightseagreen',label=rule[0])
	rects2=plt.bar(index,y[1],bar_width,color='sandybrown',label=rule[1])
	rects3=plt.bar(index + bar_width,y[2],bar_width,color='IndianRed',label=rule[2])

	ax.set_ylabel('Validation Accuracy')
	ax.set_xticks(index)
	ax.set_xticklabels(x)
	ax.legend()

	plt.ylim(ymax=0.895,ymin=0.85)

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
	        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.002*height,
	                '{}'.format(height), ha=ha[xpos], va='bottom', fontsize = 10)


	autolabel(rects1, "center")
	autolabel(rects2, "center")
	autolabel(rects3, "center")

	plt.savefig("triple-test.pdf")
