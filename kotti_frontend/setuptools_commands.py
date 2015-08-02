# TODO: improve me (first try/hack)
from setuptools import Command
import distutils
import pkg_resources
import os


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
      command = distutils.spawn.find_executable(self.executable)
      if not command:
          raise DistutilsArgError(
              "npm not found. You must specify --executable or -e"
              " with the npm instance_dir"
              )
      if not os.path.isdir(self.instance_dir):
          raise DistutilsArgError(
              "project dir not found. You must specify --instance_dir or -p"
              " with the project instance_dir"
              )
  
    def run(self):
      command = '{0} install --prefix {1} {1}'.format(
          self.executable,
          self.instance_dir,
          )
      self.announce(
          'Running command: {0}'.format(command),
          level=distutils.log.INFO)
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
      executable = distutils.spawn.find_executable(self.executable)
      if not executable:
          raise DistutilsArgError(
              "bower not found. You must specify --executable or -e"
              " with the bower path"
              )
  
    def run(self):
      command = '{0} install {1}'.format(self.executable, self.instance_dir)
      if self.production:
        command = '{0} -p'.format(command)
      self.announce(
          'Running command: {0}'.format(command),
          level=distutils.log.INFO)
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
      self.gulpfile_path = os.path.join(self.instance_dir, self.gulpfile)
  
    def finalize_options(self):
      executable = distutils.spawn.find_executable(self.executable)
      if not executable:
          raise DistutilsArgError(
              "gulp not found. You must specify --executable or -e"
              " with the gulp path"
              )
      if not os.path.isdir(self.instance_dir):
          raise DistutilsArgError(
              "project dir not found. You must specify --instance_dir or -p"
              " with the project instance_dir"
              )
      if not os.path.isfile(self.gulpfile_path):
          raise DistutilsArgError(
              "gulpfile not found. You must specify --gulpfile or -g"
              " with the gulpfile name"
              )
  
    def run(self):
      command = '{0} build --base {1} --gulpfile {2}'.format(
          self.executable,
          self.instance_dir,
          self.gulpfile_path,
          )
      self.announce(
          'Running command: {0}'.format(command),
          level=distutils.log.INFO)
      self.spawn(command.split(' '))
