netplandir = join_paths(prefix, 'lib', 'netplan')
install_data('00-network-manager-all.yaml',
			  install_dir: netplandir,
			  install_mode: 'rw-------')

aptprefdir = join_paths(sysconfdir, 'apt', 'preferences.d')
install_data('mamolinux-apt.pref',
			  install_dir: aptprefdir,
			  install_mode: 'rw-r--r--')

greeterprefdir = join_paths(sysconfdir, 'lightdm')
install_data('slick-greeter.conf',
			  install_dir: greeterprefdir,
			  install_mode: 'rw-r--r--')
