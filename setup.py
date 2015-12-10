# This setup is usable by catkin, or on its own as usual python setup.py

_CATKIN = False
try:
    from distutils.core import setup
    from catkin_pkg.python_setup import generate_distutils_setup
    _CATKIN = True
except Exception, e:
    from setuptools import setup

# CAREFUL distutils and setuptools take different arguments and have different behaviors
if _CATKIN:  # using distutils : https://docs.python.org/2/distutils
    # fetch values from package.xml
    setup_args = generate_distutils_setup(
        packages=[
            'celeros',
            'celeros.celerybeatredis',
            'celery', 'celery.app', 'celery.apps', 'celery.backends', 'celery.backends.database', 'celery.bin', 'celery.concurrency', 'celery.contrib', 'celery.events', 'celery.fixups', 'celery.loaders', 'celery.security', 'celery.task', 'celery.utils', 'celery.utils.dispatch', 'celery.worker',
            'kombu', 'kombu.async', 'kombu.transport', 'kombu.transport.sqlalchemy', 'kombu.transport.virtual', 'kombu.utils',
            'billiard', 'billiard.dummy', 'billiard.py2', 'billiard.py3',
            'flower', 'flower.api', 'flower.utils', 'flower.utils.backports', 'flower.views',
            'tornado_cors',
        ],
        package_dir={
            'celeros': 'celeros',
            'celery': 'deps/celery/celery',
            'kombu': 'deps/kombu/kombu',
            'billiard': 'deps/billiard/billiard',
            'flower': 'deps/flower/flower',
            'tornado_cors': 'deps/tornado-cors/tornado_cors',
        },
        py_modules=[
            'flask_celery',
        ],
        package_data={
            'flower': ['templates/*', 'static/**/*', 'static/*.*']
        },
    )
    setup(**setup_args)

else:  # using setuptools : http://pythonhosted.org/setuptools/

    setup(name='celeros',
        version='0.0.1',
        description='Celery as a scheduler for ROS systems',
        url='http://github.com/asmodehn/celeros',
        author='AlexV',
        author_email='asmodehn@gmail.com',
        license='BSD',
        packages=[
            'celeros',
            'celeros.celerybeatredis',
            'celery', 'celery.app', 'celery.apps', 'celery.backends', 'celery.backends.database', 'celery.bin', 'celery.concurrency', 'celery.contrib', 'celery.events', 'celery.fixups', 'celery.loaders', 'celery.security', 'celery.task', 'celery.utils', 'celery.utils.dispatch', 'celery.worker',
            'kombu', 'kombu.async', 'kombu.transport', 'kombu.transport.sqlalchemy', 'kombu.transport.virtual', 'kombu.utils',
            'billiard', 'billiard.dummy', 'billiard.py2', 'billiard.py3',
            'flower', 'flower.api', 'flower.utils', 'flower.utils.backports', 'flower.views',
        ],
        package_dir={
            'celeros': 'celeros',
            'celery': 'deps/celery/celery',
            'kombu': 'deps/kombu/kombu',
            'billiard': 'deps/billiard/billiard',
            'flower': 'deps/flower/flower',
        },
        package_data={
            'flower': ['templates/*', 'static/**/*', 'static/*.*']
        },
        # this is better than using package data ( since behavior is a bit different from distutils... )
        include_package_data=True,  # use MANIFEST.in during install.
        install_requires=[  # External dependencies only. the ones that match package.xml. others are included in here already.
        ],
        zip_safe=False,  # TODO testing...
    )
