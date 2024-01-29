# Adding a custom header with Puppet
exec { 'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install Nginx'],
}

exec { 'install Nginx':
  provider => shell,
  command  => 'sudo apt-get install nginx -y',
  before   => Exec['add_header'],
}

exec { 'add_header':
  provider    => shell,
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\default;/include \/etc\/nginx\/sites-enabled\/\default;\n\tadd_header X-Served-By \"$hostname\";/" /etc/nginx/nginx.conf',
  before      => Exec['hostname'],
  before      => Exec['restart Nginx'],
}

exec { 'hostname':
    provider => shell,
    command  => 'hostname',
}

exec { 'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
