#!/usr/bin/env python

from setuptools import setup, find_packages
import os

pkg_root = os.path.dirname(__file__)

# Error-handling here is to allow package to be built w/o README included
try: readme = open(os.path.join(pkg_root, 'README.md')).read()
except IOError: readme = ''

setup(

	name = 'nflog-zmq-pcap-pipe',
	version = '12.05.5',
	author = 'Mike Kazantsev',
	author_email = 'mk.fraggod@gmail.com',
	license = 'WTFPL',
	keywords = 'nflog pcap zeromq traffic analysis ids',
	url = 'http://github.com/mk-fg/nflog-zmq-pcap-pipe',

	description = 'Tool to collect nflog and pipe it to a pcap stream/file'
		' over network (0mq) for real-time (or close to that) analysis',
	long_description = readme,

	classifiers = [
		'Development Status :: 4 - Beta',
		'Environment :: No Input/Output (Daemon)',
		'Intended Audience :: Developers',
		'Intended Audience :: System Administrators',
		'Intended Audience :: Telecommunications Industry',
		'License :: OSI Approved',
		'Operating System :: POSIX :: Linux',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 2 :: Only',
		'Programming Language :: Python :: Implementation :: CPython',
		'Topic :: Internet',
		'Topic :: Security',
		'Topic :: System :: Networking :: Monitoring',
		'Topic :: System :: Operating System Kernels :: Linux' ],

	install_requires = ['pyzmq'],

	packages = find_packages(),
    entry_points = {'console_scripts': [
      'nflog-zmq-send = nflog_zmq_pcap_pipe.nflog_zmq_send:main',
      'nflog-pcap-recv = nflog_zmq_pcap_pipe.nflog_pcap_recv:main',
      'nflog-zmq-compress = nflog_zmq_pcap_pipe.nflog_zmq_compress:main',
      'nflog-zmq-decompress = nflog_zmq_pcap_pipe.nflog_zmq_decompress:main',
      'nflog-pcap-query = nflog_zmq_pcap_pipe.nflog_pcap_query:main']
      } )
