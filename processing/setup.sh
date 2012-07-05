if [ ! -d virtualenv/ ]
then
        python virtualenv.py virtualenv
fi

. virtualenv/bin/activate
pip install --use-mirrors argparse flickrapi

#coverage doxypy lockfile python-daemon unittest-xml-reporting

