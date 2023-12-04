# Adds a custom HTTP header with Puppet

exec {'update':
  command => '/usr/bin/apt-get update',
}
package {'nginx':
  ensure  => 'installed',
  require => Exec['apt-update'],
}
file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  line  => "add_header X-Served-By \"${hostname}\";",
}
service { 'nginx':
  ensure  => 'running',
  enable => true,
  require => [Package['nginx'], File_line['http_header']],
}
