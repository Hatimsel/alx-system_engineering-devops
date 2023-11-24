# Execute a command


exec { 'killmenow':
    command  => 'pkill killmenow',
    provider => 'shell',
    path     => '/usr/bin',
    onlyif   => 'pgrep killmenow',
}
