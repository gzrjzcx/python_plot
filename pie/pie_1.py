def plot_pie():
	fig, ax = plt.subplots(figsize=(8, 4), subplot_kw=dict(aspect="equal"))

	recipe = ["update_animal\n(46.67%)",
	          "run_simulation\n(45.69%)",
	          "output_ppm (7.67%)",
	          "create_animals (0.02%)",
	          "get_space_data (0.01%)",
	          "others (0.01%)"]

	data = [46.67, 45.69, 7.67, 2, 1, 1]
	print(sum(data))

	color=("IndianRed","sandybrown","darkseagreen","palevioletred","darkcyan","mediumpurple")
	wedges, texts = ax.pie(data, wedgeprops=dict(width=1), startangle=-30, colors=color)

	bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
	kw = dict(xycoords='data', textcoords='data', arrowprops=dict(arrowstyle="-"),
	          bbox=bbox_props, zorder=0, va="center")

	for i, p in enumerate(wedges):
	    ang = (p.theta2 - p.theta1)/2. + p.theta1
	    y = np.sin(np.deg2rad(ang))
	    x = np.cos(np.deg2rad(ang))
	    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
	    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
	    kw["arrowprops"].update({"connectionstyle": connectionstyle})
	    if i == 2:
	    	ax.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), (1.4+0.25)*y),
	                 horizontalalignment=horizontalalignment, **kw)
	    elif i == 3:
	    	ax.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), (1.4 + 0.35)*y),
	                 horizontalalignment=horizontalalignment, **kw)
	    elif i == 4:
	    	ax.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), (1.4 + 0.11)*y),
	                 horizontalalignment=horizontalalignment, **kw)	 
	    elif i == 5:
	    	ax.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), (1.4 - 0.25)*y),
	                 horizontalalignment=horizontalalignment, **kw)	 	    	
	    else:
	    	ax.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
	                 horizontalalignment=horizontalalignment, **kw)

#	ax.set_title("Runtime")

	plt.savefig("pie.eps", format='eps', dpi=1000)