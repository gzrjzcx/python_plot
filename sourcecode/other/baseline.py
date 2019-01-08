#baseline bar
def baseline():
	import matplotlib.pyplot as plt
	import matplotlib.ticker as mtick

	baseline = 1
	data = [1.1,2.0,1.4,0.9,1.6,0.7,0.1]
	plt.bar(range(len(data)),[x-baseline for x in data])
	plt.gca().yaxis.set_major_formatter(mtick.FuncFormatter(lambda x,_: x+baseline))

	plt.savefig("baseline.pdf")