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

srcs = ['10_linux', 'grub', 'lsb-release', 'os-release']
foreach i : range(srcs.length())
	src = srcs[i]
	if src == '10_linux'
		mode = 'rwxr--r--'
	else
		mode = 'rw-r--r--'
	endif
	install_data(src,
    install_dir: mamolinuxdir,
    install_mode: mode,
	)
endforeach