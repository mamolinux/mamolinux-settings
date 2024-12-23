project('mamolinux-settings',
  version : run_command('head', '-1', 'debian/changelog', check: true).stdout().split(' ')[1].strip('(').strip(')'),
  default_options : ['warning_level=3',
  ]
)

application_id = meson.project_name()
i18n = import('i18n')

datadir = get_option('datadir')

subdir('data')
subdir('po')
