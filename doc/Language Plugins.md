# Monolithe Language Plugins

Monolithe is not monolitic. It is actually the oposite. While it comes with three default languages (Python, Go and HTML), it is possible to develop support for new languages or transformations in separate python packages. Using the Python entry points system, by simply naming correctly some values and by providing a few writers and templates, you can create your own plugin.

In this document, we will go through the creation of a very simple plugin, that will translate a Specifications Set to a very simple markdown documentation.

## Write the plugin

### Create the directory structure

First let's create a folder for our project

```bash
cd ~/Desktop
mkdir -p monolithe-markdown/monolithemarkdown/{templates,writers}
touch monolithe-markdown/{setup.py,MANIFEST.in}
touch monolithe-markdown/monolithemarkdown/__init__.py
touch monolithe-markdown/monolithemarkdown/templates/document.md.tpl
touch monolithe-markdown/monolithemarkdown/writers/{__init__.py,apiversionwriter.py}
touch monolithe-markdown/monolithemarkdown/writers/apiversionwriter.py
```

You will get something like this:

```
tree monolithe-markdown
monolithe-markdown
├── MANIFEST.in
├── monolithemarkdown
│   ├── __init__.py
│   ├── templates
│   │   └── document.md.tpl
│   └── writers
│       ├── __init__.py
│       └── apiversionwriter.py
└── setup.py
```

### Creation of the template

First, we will create our template. Let's edit `monolithe-markdown/monolithemarkdown/templates/document.md.tpl` and make it look like:

```jinja
# {{ specification.entity_name }}

specification.description

## Attributes

{% for attribute in specification.attributes %}
### {{ attribute.name }}

{{ attribute.description }}

{% endfor %}
```

### Creation of the writer

Now we have a template, we need to create a writer that will use it. Let's edit `monolithe-markdown/monolithemarkdown/writers/apiversionwriter.py` and make it looks like:

```python
from monolithe.generators.lib import TemplateFileWriter


class APIVersionWriter(TemplateFileWriter):

    def __init__(self, monolithe_config, api_info):
        super(APIVersionWriter, self).__init__(package="monolithemarkdown")
        output = monolithe_config.get_option("output", "transformer")
        self.output_directory = "%s/markdown/%s" % (output, api_info["version"])

    def perform(self, specifications):
        for rest_name, specification in specifications.iteritems():
            self._write_document(specification=specification)

    def _write_document(self, specification):
        filename = '%s.md' % specification.rest_name
        self.write(destination=self.output_directory, filename=filename, template_name="document.md.tpl",
                   specification=specification)
```

### Write the init file

You now need to declare the plugin information in the main init file. Let's edit the `monolithe-markdown/monolithemarkdown/__init__.py` and make it look like:

```python
__all__ = ['APIVersionWriter', 'plugin_info']

from .writers.apiversionwriter import APIVersionWriter


def plugin_info():
    return {
        'VanillaWriter': None,
        'APIVersionWriter': APIVersionWriter,
        'PackageWriter': None,
        'CLIWriter': None,
        'get_idiomatic_name': None,
        'get_type_name': None
    }
```

### Write the MANIFEST

We need to declare our static file in the manifest file. Let's edit the `monolithe-markdown/MANIFEST.in` and make it look like:

```
recursive-include monolithemardown/templates *
```

### Write the setup file

Finally, we need to write the setup file. Let's edit the `monolithe-markdown/setup.py` and make it look like:

```python
from setuptools import setup, find_packages

setup(name='monolithemarkdown',
      version='1.0',
      description='simple marddown generator for monolithe',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests', '.git', '.gitignore', 'README.md']),
      include_package_data=True,
      entry_points={'monolithe.plugin.lang.markdown': ['info=monolithemarkdown:plugin_info']},
      )
```

Voilà!

## Try your package

> This assumes you have Monolithe installed and monogen-sdk command in your path.

Simply install your package by doing in the `monolithe-markdown` directory:

```
python setup.py install
```

Now you can run `monogen-sdk` on a Specifications Set:

```
monogen-sdk -f monolithe/examples/specifications -L markdown
> [log] retrieving specifications from folder "/monolithe/examples/specifications"
> [log] 5 specifications retrieved from folder "monolithe/examples/specifications" (api version: 1.0)
> [log] transforming specifications into markdown for version 1.0...
> [log] assembling...
> [success] tdldk generation complete and available in "codegen/markdown"
```

As the guy just said, the generated data is now available in `codegen/markdown`.

Of course, this is a very simple example, and you can of course do way more. For a more extensive example, you can have a look to the source code of Monolithe.

