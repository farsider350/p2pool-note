from p2pool.bitcoin import networks

PARENT = networks.nets['note']
SHARE_PERIOD = 20 # seconds
CHAIN_LENGTH = 2*24*60 # shares
REAL_CHAIN_LENGTH = 2*24*60 # shares
TARGET_LOOKBEHIND = 60 # shares
SPREAD = 8 # blocks
IDENTIFIER = 'e036d5b8c6923410'.decode('hex')
PREFIX = '7207c1a53ef629b0'.decode('hex')
P2P_PORT = 4544
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 4545
BOOTSTRAP_ADDRS = '161.43.201.255'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-note'
VERSION_CHECK = lambda v: None if 000001 <= v else 'Note version too old. Upgrade to 0.0.1 or newer!'
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['bip65', 'csv', 'segwit'])
MINIMUM_PROTOCOL_VERSION = 3301
NEW_MINIMUM_PROTOCOL_VERSION = 3301
SEGWIT_ACTIVATION_VERSION = 17
BLOCK_MAX_SIZE = 1000000
BLOCK_MAX_WEIGHT = 4000000
