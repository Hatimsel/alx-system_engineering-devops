# Define the new user
user { 'holberton':
	ensure => present,
	managehome => true,
	shell => '/bin/bash',
}

# Add the user to the sudo group
group { 'sudo':
	ensure => present,
	members => ['holberton'],
}

# Allow passwordless sudo for holberton
file { '/etc/sudoers.d/holberton':
	ensure => present,
	content => 'holberton ALL=(ALL) NOPASSWD: ALL',
	mode => '0440',
	owner => 'root',
	group => 'root',
}
