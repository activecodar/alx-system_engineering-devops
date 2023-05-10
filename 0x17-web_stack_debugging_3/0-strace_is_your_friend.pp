# This file ensures that the wp-settings.php file exists and contains the correct content.

file { '/var/www/html/wp-settings.php':
  ensure  => file,
  content => file('/var/www/html/wp-settings.php').content.gsub('phpp', 'php'),
  path    => '/usr/local/bin/:/bin/',
}
