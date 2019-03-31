def stem(*args, **kwargs):
    """Plot discrete sequence data

    A proper stem plot that mimic matlab's stem function.

    stem(y) plots the data sequence, y, as stems that extend from a baseline along the x-axis. The data values are indicated by circles terminating each stem.

    Parameters
    ----------
    args :
        Identical to matplotlib.pyplot.plot(*args).
    ax : matplotlib axis
        Optinal.
    baseline: float
        Optinal. y-level of baseline.
    kwargs:
        Identical to matplotlib.pyplot.plot(**kwargs).
    """
    import matplotlib.pyplot as plt
    from copy import copy

    if len(args) == 0:
        return {}

    # Remove string styling for ploting
    if type(args[-1]) is type(' '):
        args = args[:-1]

    # If x is not given, generate x
    if len(args) == 1:
        x = list(range(len(args[0])))
        args = (x, args[0])

    x = args[0]
    y = args[1]

    # Get current axis if ax is not defined
    ax = kwargs.pop('ax', plt.gca())

    # Set color to next in cycle if not defined
    kwargs['c'] = kwargs.pop('c', next(ax._get_lines.prop_cycler)['color'])

    # Set label to nothing if not defined
    kwargs['label'] = kwargs.pop('label', '')

    # Set baseline to min of y if not defined
    baseline = kwargs.pop('baseline', min(y))

    # Plot baseline
    kwargs_bl = copy(kwargs)
    del kwargs_bl['label']
    ax.plot([min(x), max(x)], [baseline, baseline], **kwargs_bl)

    # Plot stem line from baseline to marker
    for xi, yi in zip(x, y):
        kwargs_l = copy(kwargs)
        del kwargs_l['label']
        ax.plot([xi, xi], [baseline, yi], **kwargs_l)

    # Plot stem marker
    kwargs_o = copy(kwargs)
    kwargs_o['marker'] = 'o'
    kwargs_o['linestyle'] = ''
    ax.plot(x, y, **kwargs_o)

    '''
    TODO: Fix Stem handles.  Hint:
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels)
    https://matplotlib.org/users/legend_guide.html
    '''

from sys import modules
modules[__name__] = stem
