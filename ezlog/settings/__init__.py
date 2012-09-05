import os

# load basci settings
from base import *

#load specific settings in condition
if 'DATABASE_URL' in os.environ:
    # Heroku
    from for_heroku import *

if 'SERVER_SOFTWARE' in os.environ:
    # SAE
    from for_sae import *

try:
    import switcher
except ImportError:
    pass
else:
    exec 'from %s import *' % switcher.SELECTION

try:
    from local import *
except ImportError:
    pass
