project('mamolinux-settings',
  version : run_command('head', '-1', 'debian/changelog', check: true).stdout().split(' ')[1].strip('(').strip(')'),
  default_options : ['warning_level=3',
                      'prefix=/usr',
  ]
)

application_id = meson.project_name()
i18n = import('i18n')
fs = import('fs')

prefix = get_option('prefix')
datadir = get_option('datadir')
sysconfdir = get_option('sysconfdir')
mamolinuxdir = join_paths(datadir, 'mamolinux')

subdir('data')
subdir('po')
subdir('src')
