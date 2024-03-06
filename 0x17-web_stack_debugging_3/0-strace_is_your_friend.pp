# Resolve 500 error triggered by GET HTTP method request to Apache web server

exec {'correcting_typo':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
