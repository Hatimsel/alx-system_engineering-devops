
file { '/etc/default/nginx':
	ensure  => file,
	content => inline_template("<%= File.read('/etc/default/nginx').gsub('15', '4096') %>"),
	notify  => Service['nginx'],
}
service { 'nginx':
	ensure    => running,
	enable    => true,
	subscribe => File['/etc/default/nginx'],
}
