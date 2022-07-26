# plugin_example
Example problem for creating python plugins

# how to use this example
First install "main_plugin_arch" using pip. This example package represents an existing python pakage
```commandline
cd main_program
pip install .
```

Now install the example plugin
```commandline
cd test_plugin
pip install .
```

Now that the plugin is installed, it is discoverable by the `main_plugin_arch` package. The class `FancyHelloWorld`
is discovered during the `from main_plugin_arch import plugin` call.

run `example.py` to check out how it works.
