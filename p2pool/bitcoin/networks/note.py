import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'f4e5ede3'.decode('hex')
P2P_PORT = 16158
ADDRESS_VERSION = 111
RPC_PORT = 9332
RPC_CHECK =RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
#            'note' in (yield bitcoind.rpc_help()) 
            (yield helper.check_block_header(bitcoind, '854125f6e3994feb859e79588485e5eff93aaf9b2729bffb6f159ef4dd42de3b')) and
                          (yield bitcoind.rpc_getblockchaininfo())['chain'] == 'main'
        ))
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//1051200
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 30 # 30 seconds
SYMBOL = 'NTBC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Note') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Note/') if platform.system() == 'Darwin' else os.path.expanduser('~/.note'), 'note.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://explorer.notebc.io/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://explorer.notebc.io/address/'
TX_EXPLORER_URL_PREFIX = 'http://explorer.notebc.io/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
