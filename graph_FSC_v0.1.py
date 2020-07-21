#!/home/zuben/miniconda3/bin/python3
from lxml import etree
import matplotlib.pyplot as plt

import argparse

# Read xml files
X = []
Y= []


parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)

args = parser.parse_args()

title_and_filename = args.filename

tree = etree.parse(title_and_filename)

for Xvalues in tree.xpath("/fsc/coordinate/x"):
  X.append(float(Xvalues.text))

for Yvalues in tree.xpath("/fsc/coordinate/y"):
  Y.append(float(Yvalues.text))

plt.ylim(-0.1,1.1)
plt.plot(X,Y)
plt.xlabel("1/Resolution ($\AA$)")
plt.ylabel("Correlation")

#plt.title(title_and_filename)

plt.hlines(y=0.143, xmin=min(X), xmax=max(X), colors='red')
#plt.savefig("{0}.png".format(title_and_filename))
plt.show()
