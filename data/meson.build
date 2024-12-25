desktop_dir = join_paths(datadir, 'applications')

install_data('mamolinux/os-conf/00-network-manager-all.yaml',
              install_dir: '/lib/netplan',
              install_mode: 'rw-------')

desktop_file = i18n.merge_file(
        input: 'mamolinux/mamolinux-release-upgrade.desktop.in',
       output: 'mamolinux-release-upgrade.desktop',
         type: 'desktop',
       po_dir: '../po',
      install: true,
  install_dir: desktop_dir
)

subdir('mamolinux/third-party')
