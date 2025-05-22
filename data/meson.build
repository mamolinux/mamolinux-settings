desktop_dir = join_paths(datadir, 'applications')
autostartdir = join_paths(sysconfdir, 'xdg', 'autostart')
app_icon_dir = join_paths(datadir, 'icons', 'hicolor', 'scalable', 'apps')

# install icon
install_emptydir(app_icon_dir)
install_data(
  join_paths(meson.current_source_dir(), 'mamolinux-release-upgrader.svg'),
  install_dir: app_icon_dir,
)

subdir('mamolinux')
subdir('schemas')
