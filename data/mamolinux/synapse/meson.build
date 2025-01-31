install_data('synapse-config.json',
			 rename: ['config.json'],
	install_dir: join_paths(mamolinuxdir, 'synapse')
)

synapseautostart = i18n.merge_file(
        input: 'synapse.desktop.in',
       output: 'synapse.desktop',
         type: 'desktop',
       po_dir: '../../../po',
      install: true,
  install_dir: autostartdir
)
