import sys

if sys.version_info < (3, 10):
    from importlib_metadata import entry_points
else:
    from importlib.metadata import entry_points

this_module = sys.modules[__name__]
eps = entry_points(group="test_plugins.plugin")
installed_plugins = {}
for ep in eps:
    _x = ep.load()
    setattr(this_module, ep.name, _x())
    installed_plugins[ep.name] = _x()

