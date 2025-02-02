install_data('mamolinux-release-upgrader',
   install_dir: bindir,
  install_mode: 'rwxr--r--'
)

install_data('mamolinux_settings_setup',
   install_dir: mamolinuxdir,
  install_mode: 'rwxr--r--'
)

nemo_remote_term_files = []
nemo_remote_term_files += files(
  run_command(
    'find',
    meson.current_source_dir(),
    '-name', 'remote_terminal*',
    check: true
  ).stdout().strip().split('\n')
)

foreach i : range(nemo_remote_term_files.length())
  src = nemo_remote_term_files[i]
  if fs.name(src).endswith('py')
		mode = 'rwxr--r--'
	else
		mode = 'rw-r--r--'
	endif
	
  install_data(fs.name(src),
    install_dir: join_paths(datadir, 'nemo', 'actions'),
    install_mode: mode,
  )
endforeach
