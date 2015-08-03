import os
import pkg_resources
from distutils.errors import DistutilsArgError
from distutils.spawn import find_executable
from distutils.log import INFO
from setuptools import Command


class NpmCommand(Command):
    """ Run npm install command """

    description = 'run npm install command'
    user_options = [
        ('executable=', 'e', 'executable path'),
        ('instance-dir=', 'i', 'instance dir of the project'),
    ]

    def initialize_options(self):
      self.executable = 'npm'
      self.instance_dir = pkg_resources.resource_filename(
          'kotti_frontend',
          'templates'
          )
  
    def finalize_options(self):
      command = find_executable(self.executable)
      if not command:
          raise DistutilsArgError(
              "{0} not found. You must specify --executable or -e"
              " with the npm instance_dir".format(self.executable)
              )
      if not os.path.isdir(self.instance_dir):
          raise DistutilsArgError(
              "project dir {0} not found."
              " You must specify --instance_dir or -p"
              " with the project instance_dir".format(self.instance_dir)
              )
  
    def run(self):
      command = '{0} install --prefix {1} {1}'.format(
          self.executable,
          self.instance_dir,
          )
      self.announce(
          'Running command: {0}'.format(command),
          level=INFO)
      self.spawn(command.split(' '))


class BowerCommand(Command):
    """ Run bower install command """

    description = 'run bower install command'
    user_options = [
        ('executable=', 'e', 'executable path'),
        ('instance-dir=', 'i', 'instance dir of the project'),
        ('production=', 'p', 'production mode'),
    ]

    def initialize_options(self):
      self.executable = 'bower'
      self.production = False
      self.instance_dir = pkg_resources.resource_filename(
          'kotti_frontend',
          'templates'
          )
  
    def finalize_options(self):
      executable = find_executable(self.executable)
      if not executable:
          raise DistutilsArgError(
              "{0} not found. You must specify --executable or -e"
              " with the bower path".format(self.executable)
              )
  
    def run(self):
      command = '{0} install {1}'.format(self.executable,
                                         self.instance_dir)
      if self.production:
        command = '{0} -p'.format(command)
      self.announce(
          'Running command: {0}'.format(command),
          level=INFO)
      self.spawn(command.split(' '))


class GulpCommand(Command):
    """ Run gulp build command """

    description = 'run gulp build command'
    user_options = [
        ('executable=', 'e', 'executable path'),
        ('instance-dir=', 'i', 'instance dir of the project'),
        ('gulpfile=', 'g', 'name of the gulpfile'),
    ]

    def initialize_options(self):
      self.executable = 'gulp'
      self.instance_dir = pkg_resources.resource_filename(
          'kotti_frontend',
          'templates'
          )
      self.gulpfile = 'gulpfile.babel.js'
      self.gulpfile_path = os.path.join(self.instance_dir,
                                        self.gulpfile)
  
    def finalize_options(self):
      executable = find_executable(self.executable)
      if not executable:
          raise DistutilsArgError(
              "{0} not found. You must specify --executable or -e"
              " with the gulp path".format(self.executable)
              )
      if not os.path.isdir(self.instance_dir):
          raise DistutilsArgError(
              "project dir {0} not found."
              " You must specify --instance_dir or -p"
              " with the project instance_dir".format(self.instance_dir)
              )
      if not os.path.isfile(self.gulpfile_path):
          raise DistutilsArgError(
              "gulpfile {0} not found."
              " You must specify --gulpfile or -g"
              " with the gulpfile name".format(self.gulpfile_path)
              )
  
    def run(self):
      command = '{0} build --base {1} --gulpfile {2}'.format(
          self.executable,
          self.instance_dir,
          self.gulpfile_path,
          )
      self.announce(
          'Running command: {0}'.format(command),
          level=INFO)
      self.spawn(command.split(' '))
