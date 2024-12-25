thirdpartysrcs = []
thirdpartysrcs += files(
  run_command(
    'find',
    meson.current_source_dir(),
    '-name', '*-source',
    check: true
  ).stdout().strip().split('\n')
)

foreach i : range(thirdpartysrcs.length())
  src = thirdpartysrcs[i]
  install_data(fs.name(src),
    install_dir: join_paths(datadir, 'mamolinux', 'thirdpartysrcs'),
    install_mode: 'rwxr--r--',
  )
endforeach
