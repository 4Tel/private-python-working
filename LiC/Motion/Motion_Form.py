import matplotlib.pyplot as plt
import scipy.constants as sc
import sys

sys.path.append("../../")
import plotForm
import constants


def pre_plot():
    plotForm.configure_matplotlib()


def post_plot(title, yscale=1):
    for line in plt.gca().get_lines():
        xdata = line.get_xdata()
        line.set_xdata(xdata / 10000 * constants.Ry2v * sc.pico / sc.angstrom)
        line.set_ydata(line.get_ydata() * yscale)
    plt.gca().set_xlim(10, 60)
    plt.gca().set_ylim(0, 5)
    plt.gca().autoscale_view()

    plt.legend(loc="upper left")
    plt.title(title)
    plt.xlabel("initial velocity ($\AA$/ps)")
    plt.ylabel("displacement\n(2.44$\AA$)")
