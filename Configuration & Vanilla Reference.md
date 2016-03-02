# Monolithe Configuration & Vanilla Reference

In order to generate sdks/clis and documentation, Monolithe uses some Specifications. But it also need informations that does not belong to these Specifications. For instance, what class names to use when generating a Python SDK, what would be the name of the SDK, additional API documentation pages and so on.

All that information are given to Monolithe through a configuration file. This file is a `ini` file, and it is given either as a parameter of the `monogen` command line interfaces, or through  a `MonolitheConfig` object, when using Monolithe as a library.

It also uses what we call some `vanilla` data. It is a folder that contains static files, or overrides and other things like that.

This document describe all the parameters of the configuration file, and what can be done using the `vanilla`.


## Monolithe Configuration File

The configuration file is a `ini` file that is divided into several sections.

> All configuration tokens are mandatory. If the value is optional, simply leave it empty.

### The [monolithe] Section

This section contains general information about the sdk and documentation you want to generate.

#### product_name

Usually the full name of your product. It can contain spaces, is used in various places, especially in the generated documentation.

For example:

	product_name=Virtualized Service Directory

#### product_accronym

The accronym of your product. It is used when generating some classes, like the ReST Session, or some doc strings.

It **must not** contain any space and **must** be uppercase

For example:

	product_accronym=VSD

#### copyright

Your copyright. It will be used in various places.

For example:

	copyright=Copyright (c) 2042, Nuage Networks


### The [sdk] Section

This section contains informations related to the sdk generation.

#### sdk_name

The name of your sdk. This will be used to generate the Python package, and in a lot of places.

it **must not** contain any space

For example:

	sdk_name=vspk

#### sdk_version
The version of your sdk. This will be used when generating the `setup.py`

For example:

	sdk_version=1.0


#### sdk_output

The path where the generation of the sdk will be created.

If you don’t provide an initial `/`, it will be created relatively to the current folder.

If you provide an initial `/` then it will be created using the absolute path.

For example:

	sdk_output=codegen

#### sdk_class_prefix

Prefix used by all classes. This is a general good practice, that helps identify the origin of an object in your code. All classes will be prefixed with it.

For example:

	sdk_class_prefix=NU

So if you have a Specification File describing an object with an `entity_name` set to `Unicorn`, the equivalent SDK object will be:

	NUUnicorn

And the fetchers of that objects from the parents will be:

	NUUnicornsFetcher

> For more information about these objects fetchers, please read the Bambou documentation.

#### sdk_bambou_version

The bambou version to use. This will be used to generate the `requirements.txt`.

For example:

	sdk_bambou_version=1.0.1

Note that this will be used a strict version and will be translated to `bambou==1.0.1`

#### sdk_url, sdk_author, sdk_email, sdk_description, sdk_license_name

Informatino related to your sdk. All of these will be used to generate the `setup.py`

For example:

	sdk_url=http://nuagenetworks.github.io/vspk
	sdk_author=Antoine Mercadal, Christophe Serafin
	sdk_email=opensource@nuagenetworks.net
	sdk_description=awesome sdk for vsd
	sdk_license_name=BSD-3

#### sdk_user_vanilla

The path the sdk vanilla folder (see next chapter).

If you don’t provide an initial `/`, it will be found relatively to the current folder.

If you provide an initial `/` then it will be found using the absolute path.

For example:

	sdk_user_vanilla=vsdk/vanilla/sdk

#### sdk_cli_name

The name of the command line interface of the sdk

It **must not** contain any space

For example:

	sdk_cli_name=todolist

#### sdkdoc_output

The path where the generation of the sdk documentation will be created.

If you don’t provide an initial `/`, it will be created relatively to the current folder.

If you provide an initial `/` then it will be created using the absolute path.

For example:

	sdkdoc_output=sdkdoc


## The vanilla folder

Vanilla folder allows you to add some data to the generated sdk and documentation. There is one vanilla that can be used for the sdk generation, one for the api documentation and one for the sdk documentation.

### The sdk vanilla

The structure of the sdk vanilla is the following:

	<sdk_user_vanilla>/LICENSE
	<sdk_user_vanilla>/README.md
	<sdk_user_vanilla>/__attributes_defaults/attrs_defaults.ini
	<sdk_user_vanilla>/__overrides/<object-rest-name>.override.py


#### License & Readme

- `LICENSE`: the license file that will be added to the Python package
- `README.md`: the readme that will be added to the Python package

#### Default Attributes Configuration

Bambou can use a file in order to populate default values for the attributes of an object. You can provide your own default attribute by adding a folder named `__attributes_defaults` that contains an `attrs_defaults.ini` file.

For example:

	$ cat __attributes_defaults/attrs_defaults.ini
	[enterprise]
	name=“New Enterprise“
	description=“A cool enterprise“

For more information, please read the bambou documentation.

As Monolithe handles multiple version of the api a same sdk, it is possible that some objects doesn’t exist accross all the version. So it is possible to create a specific `attrs_defaults.ini` for specific api version. To do so, simply prefix the file name with `<major.minor>_`

For example:

	3.2_attrs_defaults.ini # will be used for 3.2 api version
	3.1_attrs_defaults.ini # will be used for 3.1 api version
	attrs_defaults.ini # will be used for all other api versions


#### Object Model Overrides

Monolithe generates everything for you from Specifications. But sometimes it could be useful to add custom methods to the objects. You might want to transform a value of an exposed attribute, or do some more complexe operations.

For instance, you might want a simple way to get the full name of a user object that has a first name and last name attributes. Overrides as made for this.

In order to add the full name accessors to an object with a `rest_name` set to `user`, add a file in the `__overrides` folder and name it using the following model:

	<sdk_class_prefix|lower><rest-name>.override.py

And add methods. You don’t need to redeclare a class. Those methods will be added to the correct class. So the keyword `self` and all other properties are accessible.

For instance:

	$ cat __overrides/nuuser.override.py
		def get_full_name(self):
			return “%s %s” % (self.first_name, self.last_name)

		def get_full_name(self, full_name):
			# definitely not a good way to split that…
			self.first_name, self.last_name = full_name.split()

You can add as many overrides you want, one per object in the model.

Like the default attributes, you can prefix the override file using the same schema in order to use an override file for a specific version only (see previous section)

For instance:

	3.2_nuuser.override.py # will be used for 3.2 api version
	3.1_nuuser.override.py # will be used for 3.1 api version
	nuuser.override.py # will be used for all other api versions



### The ReST API Documentation vanilla

The API Documentation vanilla is fairly straightforward.

### Custom HTML Pages

To add some html files, simply add them to the root vanilla directory. They will be embeded in the API documentation. The entry point page in your customized pages **must** be named `usage.html` and **must** be placed in the root vanilla folder.

#### Custom CSS

To add your custom CSS, create a folder named `css` in the root vanilla folder, and add a `style.css` file.

> this will override the entire style of the documentation. Also not that the api documentation uses bootstrap.

#### Custom javascript

To add custom javascript, create a folder named `js` in the root vanilla folder, and add your scripts. You can use them from your custom html files.
