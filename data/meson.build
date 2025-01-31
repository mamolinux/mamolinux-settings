desktop_dir = join_paths(datadir, 'applications')
autostartdir = join_paths(sysconfdir, 'xdg', 'autostart')

desktop_file = i18n.merge_file(
        input: 'mamolinux/mamolinux-release-upgrade.desktop.in',
       output: 'mamolinux-release-upgrade.desktop',
         type: 'desktop',
       po_dir: '../po',
      install: true,
  install_dir: desktop_dir
)

plankschema = i18n.merge_file(
        input: 'schemas/net.launchpad.plank.gschema.xml',
       output: 'net.launchpad.plank.gschema.xml',
         type: 'xml',
       po_dir: '../po',
      install: true,
  install_dir: mamolinuxdir
)

subdir('mamolinux')
subdir('schemas')
