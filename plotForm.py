import matplotlib.pyplot as plt


def configure_matplotlib():
    plt.figure(figsize=(10, 6), dpi=300)
    plt.style.use("default")
    plt.rcParams.update({"font.size": 14})
    plt.tick_params(axis="both", direction="in", top=True, right=True)


legend_params = {
    "frameon": True,
    "fancybox": True,
    "shadow": True,
    "framealpha": 0.9,
    "edgecolor": "black",
}
