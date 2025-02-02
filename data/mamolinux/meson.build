subdir('os-conf')
subdir('plank')
subdir('synapse')
subdir('third-party')

desktop_file = i18n.merge_file(
        input: 'mamolinux-release-upgrade.desktop.in',
       output: 'mamolinux-release-upgrade.desktop',
         type: 'desktop',
       po_dir: '../../po',
      install: true,
  install_dir: desktop_dir
)

install_data('theme-manager-config.cfg',
  install_dir: join_paths(mamolinuxdir, 'theme-manager'),
       rename: 'config.cfg'
)

install_data('cinnamon/calendar_config.json',
  install_dir: join_paths(mamolinuxdir, 'cinnamon')
)
