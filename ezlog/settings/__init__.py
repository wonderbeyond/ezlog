import os

# load basci settings
from base import *

#load specific settings in condition
try:
    if 'DATABASE_URL' in os.environ:
        # Heroku
        from for_heroku import *
    elif 'SERVER_SOFTWARE' in os.environ:
        # SAE
        from for_sae import *
    elif 'VCAP_SERVICES' in os.environ:
        from for_af import *
except ImportError as e:
    print e
    pass

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
