from setuptools import setup, find_packages
  
with open('requirements.txt') as f: 
    requirements = f.readlines() 

long_description = 'Kishor-dl is a downloader script for kishorkantha magazine. It uses web scrapping to download more than 150 volumes of the magazine.' 

setup(name='kishor-dl',
      version='0.2',
      description='Download 150+ Kishorekantha PDF in one command!',
      url='http://github.com/nahid18/kishor-dl',
      author='Abdullah Al Nahid',
      author_email='nahidpatwary1@gmail.com',
      long_description = long_description, 
      long_description_content_type ="text/markdown", 
      license='MIT',
      packages=find_packages(),
      entry_points={
        'console_scripts': ['kishor-dl=kishor.download:start'],
      },
      zip_safe=False, install_requires=['requests', 'beautifulsoup4'])