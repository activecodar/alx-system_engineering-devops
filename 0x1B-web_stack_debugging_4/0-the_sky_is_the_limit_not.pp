# Increase the amount of traffic an Nginx server can handle.

exec { 'increase-nginx-ulimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
  onlyif  => 'test -f /etc/default/nginx'
}

exec { 'restart-nginx':
  command => 'service nginx restart',
  path    => '/etc/init.d/',
  onlyif  => 'service nginx status'
}
