plank_dockitem = []
plank_dockitem += files(
  run_command(
    'find',
    meson.current_source_dir(),
    '-name', '*.dockitem',
    check: true
  ).stdout().strip().split('\n')
)

foreach i : range(plank_dockitem.length())
  src = plank_dockitem[i]
  install_data(fs.name(src),
    install_dir: join_paths(mamolinuxdir, 'plank'),
    install_mode: 'rw-r--r--',
  )
endforeach

plankautostart = i18n.merge_file(
        input: 'plank.desktop.in',
       output: 'plank.desktop',
         type: 'desktop',
       po_dir: '../po',
      install: true,
  install_dir: autostartdir
)
