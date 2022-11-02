from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name = 'basque_events',         # How you named your package folder (MyLib)
  packages = ['basque_events'],   # Chose the same as "name"
  version = '1.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Package for interpretation of Event data in Euskadi',   # Give a short description about your library
  author = 'Mikel Madariaga & Naroa Barrutia',                   # Type in your name
  author_email = 'naroa.barrutia@alumni.mondragon.edu',      # Type in your E-Mail
  url = 'https://github.com/naroabarrutia/basque_events',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/naroabarrutia/basque_events/archive/refs/tags/v_1.1.tar.gz',    # I explain this later on
  keywords = ['Events', 'Basque', 'Opendata'],   # Keywords that define your package best
  long_description=long_description,
  long_description_content_type="text/markdown",
  install_requires=[      
          'requests',
          'pandas',
          'seaborn',
          'matplotlib'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)