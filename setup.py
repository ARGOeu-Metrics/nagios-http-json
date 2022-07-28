from distutils.core import setup


NAME = 'nagios-plugins-http-json'


def get_ver():
    try:
        for line in open(NAME + '.spec'):
            if "Version:" in line:
                return line.split()[1]

    except IOError:
        raise SystemExit(1)


setup(
    name=NAME,
    version=get_ver(),
    description='Nagios plugin which checks json for a given endpoint.',
    url="https://github.com/ARGOeu-Metrics/nagios-http-json",
    data_files=[('/usr/lib64/nagios/plugins', ['check_http_json.py'])]
)
