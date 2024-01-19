# Installing flask from pip3

exec { 'apt-get update':
    command => '/bin/apt-get update',
}

package { 'flask':
    ensure => 'installed',
    require => Exec['apt-get update'],
    provider => pip3,
}
