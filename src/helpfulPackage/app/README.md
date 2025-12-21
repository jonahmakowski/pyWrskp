# pyWrkspPackage
## Installation

This command should work on my local network.
```
pip install --index-url https://git.jonahmakowski.ca/api/packages/jonahmakowski/pypi/simple/ pyWrkspPackage
```

However, you can also add the project to your pip index urls, and then you don't need the --index-url flag. The following commands do that:
```
pip config set global.index-url https://git.jonahmakowski.ca/api/packages/jonahmakowski/pypi/simple/
pip config set global.extra-index-url https://pypi.org/simple # Still use regular pypi
```

After that you can install the package by simply running
```
pip install pyWrkspPackage
```
