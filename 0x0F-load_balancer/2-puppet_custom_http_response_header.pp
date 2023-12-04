# Adds a custom HTTP header with Puppet

exec { 'update':
  command => 'sudo apt-get -y update',
  path    => '/usr/bin',
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update'],
}

file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => template('module_name/nginx.conf.erb'), # Use a template for the nginx.conf file
  notify  => Exec['restart Nginx'],
}

exec { 'restart Nginx':
  command  => '/usr/sbin/service nginx restart',
  refreshonly => true,
}
