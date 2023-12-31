# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import errno
from setuptools import setup, find_packages
from setuptools.command.install import install
from subprocess import check_call


VERSION = "0.0.0"
PLUGIN_VERSION = "0.0.0"

class InstallPluginCommand(install):
    def run(self):
        install.run(self)
        try:
            check_call(['pulumi', 'plugin', 'install', 'resource', 'fly', PLUGIN_VERSION, '--server', 'github://api.github.com/dirien/pulumi-fly'])
        except OSError as error:
            if error.errno == errno.ENOENT:
                print(f"""
                There was an error installing the fly resource provider plugin.
                It looks like `pulumi` is not installed on your system.
                Please visit https://pulumi.com/ to install the Pulumi CLI.
                You may try manually installing the plugin by running
                `pulumi plugin install resource fly {PLUGIN_VERSION}`
                """)
            else:
                raise


def readme():
    try:
        with open('README.md', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "fly Pulumi Package - Development Version"


setup(name='ediri_fly',
      python_requires='>=3.7',
      version=VERSION,
      description="A Pulumi package for creating and managing Fly.io resources.",
      long_description=readme(),
      long_description_content_type='text/markdown',
      cmdclass={
          'install': InstallPluginCommand,
      },
      keywords='pulumi fly category/cloud',
      url='https://github.com/dirien/pulumi-fly',
      project_urls={
          'Repository': 'https://github.com/dirien/pulumi-fly'
      },
      license='Apache-2.0',
      packages=find_packages(),
      package_data={
          'ediri_fly': [
              'py.typed',
              'pulumi-plugin.json',
          ]
      },
      install_requires=[
          'parver>=0.2.1',
          'pulumi>=3.0.0,<4.0.0',
          'semver>=2.8.1'
      ],
      zip_safe=False)
