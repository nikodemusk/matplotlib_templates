#  Template for plotting a function graph with Python and Matplotlib.
#  Axes intersection in origo. Function definition around line 59.
#  Domain definition on line 70. Remove or edit text around line 92
#  and Graph title at line 108. Enjoy :-) 
 
import sys
import os
import matplotlib.pyplot as plt
import numpy as np

### Define the file name and paths(s) ###
# If use of Digital Ocean Spaces, there is an option to
# upload the plot there as well as save to disc.
# More about Spaces: https://www.digitalocean.com/docs/spaces/
uploadToSpace = True
if uploadToSpace:
    sys.path.insert(1, os.environ['PWD'] + '/spaceslib')
    # Need to place that module in the path above if Spaces is used
    import tospace
    remotePath = "matplotlib_templates/"
    
localPath = os.environ['PWD'] + '/plots/'

# The extension may be png, eps, pdf or svg
fileName = "function_graph_template.png"

### Define the size and aspect ratio of image ###
dpi, width = 100, 640 # Matplotlib default, 100 dpi, 640 pixels wide
w = width / dpi       # w is with in in inches
h = w * 3/4           # Heigh, from a given ratio

### Font parameteres for normal text,axes and math ###
# See also https://matplotlib.org/3.1.1/gallery/text_labels_and_annotations/fonts_demo.html
# or https://matplotlib.org/users/text_props.html?highlight=configuring%20font%20family
font = {'family' : 'DejaVu Serif',
        'weight' : 'normal',
        'size'   : 10}
plt.rc('font', **font)

plt.rcParams['mathtext.fontset']='cm' # cm is a serif font

### Define spines (axes) with intersection in origo ###
# Other intersection exemples at
# https://matplotlib.org/examples/pylab_examples/spine_placement_demo.html
def setSpines():
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_smart_bounds(True)
    ax.spines['bottom'].set_smart_bounds(True)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

### Define the grid. The grid space follows the tickmarks, defined later on. ###
def setGrid():
    ax.grid(b=True, which='major', color='lightgrey', linestyle='-', linewidth=0.3)

### Define the function ###
def f(x):
    return 22  - x**2

### Define what the line will look like ###
lineopts = {'color':'black', 'linewidth':1,
            'linestyle':'-'}

# Define the plot domain, and maybe the plot range
# Often it's the best option to  don't touch the plot range
# in this way. Alternative in line 79.
xLower, xUpper, xStep = -6, 6, 2 # xStep is the dense the xticks.
#yLower, yUpper, yStep = -10, 30, 10
density =  100 # Number of x values  in domain

### Create the x values ###
x = np.linspace(xLower, xUpper , density)

### All about the plot below ###
fig, ax = plt.subplots(1, 1) # Instantiate the plot

ax.plot(x, f(x), **lineopts) # Do the plot

# A trick to extend the y axis is to plot a
# transparent point somewhere. Here, I plot
# an invisible "x" at (0, 30).
ax.plot(0, 30, marker='x', alpha=0)

# Want spines and grid?
setSpines()
setGrid()

# Maybe some extra text in diagram?
plt.text(1, 10, r'$y=22-x^2$'+'\nSome arbitrary text', fontsize=10,
         fontweight='normal', fontfamily='sans-serif',
         color='red', rotation=30,
         horizontalalignment='left',
         verticalalignment='center')
plt.text(3, -15 , 'Made with Matplotlib', fontsize=8, fontfamily='monospae',
         fontname='sans-serif', fontweight=10, color='grey' )

# Axes labels. The positions is relative to the lower left
# corner. The upper / right side is 1.
ax.xaxis.set_label_coords(1.05, 0.3)
ax.yaxis.set_label_coords(0.38, 0.9 )
ax.set_xlabel('$x$', fontsize=12)
ax.set_ylabel('$y$', fontsize=12, rotation=0)

# A title?
ax.set_title('Function Graph Template')

# Tick markers for x-axis?
ax.set_xlim(xLower, xUpper)
plt.xticks(np.arange(ax.get_xlim()[0], ax.get_xlim()[1] + 1, xStep))
# You can control the y axis too, but often the default settings are quite good.
#ax.set_ylim(yLower, yUpper)
#plt.yticks(np.arange(ax.get_ylim()[0], ax.get_ylim()[1] + 1, yStep))

### Some settings for the image and plot ###
# Note that some parameteres may interfere with other.
#plt.axis('scaled') # May be "scaled" or "equal"
#ax.set_aspect(aspect=0.4 ) # Each step in x is aspect * y

### Figure size. Edit around line 26, not here ###
fig.set_size_inches(w, h)
fig.set_dpi(dpi)

### Save plot ###
plt.savefig(localPath + fileName, transparent=False)
# There is also an option bbox_inches='tight' in the
# call to plt.savefig(). This option makes a plot with
# narrower margins, i.e less white space around.

### Upload plot ###
if uploadToSpace:
    url = tospace.upload(fileName, localPath, remotePath)
    print(f'Your graph at: {url}')
