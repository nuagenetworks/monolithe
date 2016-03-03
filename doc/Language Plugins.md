# Monolithe Language Plugins

Monolithe is not monolithic. It is actually the opposite. While it comes with three default languages (Python, Go and HTML), it is possible to develop support for new languages or transformations in separate python packages. Using the Python entry points system, by simply naming correctly some values and by providing a few writers and templates, you can create your own plugin.

In this document, we will go through the creation of a very simple plugin, that will translate a Specifications Set to a little markdown documentation.

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
    """ This class is reponsible to write files for a particular api version. """

    def __init__(self, monolithe_config, api_info):
        # be sure to give your package name here, or the TemplateWriter won't find the templates
        super(APIVersionWriter, self).__init__(package="monolithemarkdown")
        
        # the plugin is reponsible for placing the generated file.
        # unless you have a really good reason to do so, you should always
        # put everything you generate in codegen/<language>.
        output = monolithe_config.get_option("output", "transformer")
        self.output_directory = "%s/markdown/%s" % (output, api_info["version"])
    
    def perform(self, specifications):
        """ This method is the entry point of the writer. Monolithe will call it when it need
            your plugin to generate some stuff.
        """
        for rest_name, specification in specifications.iteritems():
            # You have some ways to parallelize using a TaskManager to speed
            # up the generation process, but here we keep things simple.
            self._write_document(specification=specification)

    def _write_document(self, specification):
        """ This method writes the ouput for a particular specification.
        """
        filename = '%s.md' % specification.rest_name
        
        # write will actually write a file using a template.
        # you need to pass the destination folder, the destination file name, and the name of your template.
        # Then you can pass whatever you want that you need from inside the Jinja template.
        self.write(destination=self.output_directory, filename=filename, template_name="document.md.tpl",
                   specification=specification)
```

### Write the init file

You now need to declare the plugin information in the main init file. Let's edit the `monolithe-markdown/monolithemarkdown/__init__.py` and make it look like:

```python
__all__ = ['APIVersionWriter', 'plugin_info']

from .writers.apiversionwriter import APIVersionWriter


def plugin_info():
    """ Entry point of your plugin. This will be called by Monolithe to check if
        it should use this plugin to generate a particular language.
    """
    
    return {
        # 'VanillaWriter' is used to copy some vanilla files.
        'VanillaWriter': None, 
        
        # 'APIVersionWriter' is reponsible to write files for a particular api version.
        'APIVersionWriter': APIVersionWriter, 
        
        # 'PackageWriter' is reponsible to assemble all the file created by APIVersionWriter if needed
        'PackageWriter': None,
        
        # 'CLIWriter' is reponsible to write a CLI if needed
        'CLIWriter': None,
        
        # 'get_idiomatic_name' is a function that will be call to when a word from the specification
        # might need to get adjusted to respect the idioms of your language. for instance HelloWorld in Python
        # should be translated to hello_world
        'get_idiomatic_name': None,
        
        # 'get_type_name' is needed to translate a type from a specification to the name of the type used
        # by your language. For instance, a spec type "list" needs to be translated to "[]<subtype>" in Go.
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
      
      # This is very important!
      #
      # This is how Monolithe will find and decide to use your plugin.
      # The entry point *MUST* be 'monolithe.plugin.lang.xxx' where 'xxx'
      # is what the user will enter as value for the '--language' option.
      # The the value *MUST* be an 'info:name_of_the_package:name_of_info_function'
      # keep things simple, and always use these names. Just adapt the package name.
      entry_points={'monolithe.plugin.lang.markdown': ['info=monolithemarkdown:plugin_info']},
      )
```

Voilà!

## Try your package

> This assumes you have Monolithe installed and monogen-sdk command in your path.

From the `monolithe-markdown` folder, simply install your package by running:

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

Again, this is a very simple example. You can of course do a lot more. For an extensive example, you can have a look at the source code of Monolithe, in the `generators/lang` package.

