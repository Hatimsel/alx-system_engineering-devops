# Resolve 500 error triggered by GET HTTP method request to Apache web server

exec { 'fix_apache_500_error':
  provider => 'shell',
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  notify   => Service['apache'],
}
