# Execute a command

exec { 'killmenow':
    command => '/bin/pkill killmenow',
}
