plankschema = i18n.merge_file(
        input: 'net.launchpad.plank.gschema.xml.in',
       output: 'net.launchpad.plank.gschema.xml',
         type: 'xml',
       po_dir: '../../po',
      install: true,
  install_dir: mamolinuxdir
)

schemaoverrides = []
schemaoverrides += files(
  run_command(
    'find',
    meson.current_source_dir(),
    '-name', '*.override',
    check: true
  ).stdout().strip().split('\n')
)

foreach i : range(schemaoverrides.length())
  src = schemaoverrides[i]
  install_data(fs.name(src),
    install_dir: join_paths(datadir, 'glib-2.0', 'schemas'),
    install_mode: 'rw-r--r--',
  )
endforeach
