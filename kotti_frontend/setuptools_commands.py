# TODO: improve me (first try/hack)
from setuptools import Command
import distutils
import pkg_resources
import os


class NpmCommand(Command):
    """ Run bower commands """

    description = 'run npm commands'
    user_options = [
        ('command=', 'c', 'command path'),
        ('path=', 'p', 'path'),
        ('options=', 'o', 'options'),
    ]

    def initialize_options(self):
      self.command = 'npm'
      self.options = 'install'
      self.path = pkg_resources.resource_filename(
          'kotti_frontend',
          'templates'
          )
  
    def finalize_options(self):
      command = distutils.spawn.find_executable(self.command)
      if not command:
          raise DistutilsArgError(
              "npm not found. You must specify --command or -c"
              " with the npm path"
              )
  
    def run(self):
      command = self.command
      if self.options:
        command = '{0} {1} {2}'.format(command, self.options, self.path)
      self.announce(
          'Running command: %s' % str(command),
          level=distutils.log.INFO)
      self.spawn((self.command, self.options, self.path))


class BowerCommand(Command):
    """ Run bower commands """

    description = 'run bower commands'
    user_options = [
        ('command=', 'c', 'command path'),
        ('path=', 'p', 'path'),
        ('options=', 'o', 'options'),
    ]

    def initialize_options(self):
      self.command = 'bower'
      self.options = 'install'
      self.path = pkg_resources.resource_filename(
          'kotti_frontend',
          'templates'
          )
  
    def finalize_options(self):
      command = distutils.spawn.find_executable(self.command)
      if not command:
          raise DistutilsArgError(
              "bower not found. You must specify --command or -c"
              " with the bower path"
              )
  
    def run(self):
      command = self.command
      if self.options:
        command = '{0} {1} {2}'.format(command, self.options, self.path)
      self.announce(
          'Running command: %s' % str(command),
          level=distutils.log.INFO)
      self.spawn((self.command, self.options, self.path))


class GulpCommand(Command):
    """ Run gulp commands """

    description = 'run gulp commands'
    user_options = [
        ('command=', 'c', 'command path'),
        ('path=', 'p', 'path'),
        ('options=', 'o', 'options'),
    ]

    def initialize_options(self):
      self.command = 'gulp'
      self.path = pkg_resources.resource_filename(
          'kotti_frontend',
          'templates'
          )
      self.options = 'build --base {0} --gulpfile {1}'.format(
          self.path,
          os.path.join(
              self.path,
              'gulpfile.babel.js'
              )
          )
  
    def finalize_options(self):
      command = distutils.spawn.find_executable(self.command)
      if not command:
          raise DistutilsArgError(
              "gulp not found. You must specify --command or -c"
              " with the gulp path"
              )
  
    def run(self):
      command = self.command
      if self.options:
        command = '{0} {1}'.format(command, self.options)
      self.announce(
          'Running command: %s' % str(command),
          level=distutils.log.INFO)
      self.spawn([self.command] + self.options.split(' '))
