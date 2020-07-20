from __future__ import unicode_literals

from setuptools import find_packages
from reviewboard.extensions.packaging import setup


setup(
    name='email_followers',
    version='0.1.1',
    description='Extension for Review Board to email p4 reviews when a review is posted',
    author='Scot Salmon',
    author_email='scot.salmon@ni.com',
    maintainer='Scot Salmon',
    maintainer_email='scot.salmon@ni.com',
    packages=find_packages(),
    entry_points={
        'reviewboard.extensions': [
            'email_followers = email_followers.extension:FollowersEmailExtension',
        ],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Review Board',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
