# Creates a manifest that kills a process named killmenow

exec { 'Terminate killmenow process':
  command => 'pkill -f killmenow',
  path    => '/usr/bin/:/usr/local/bin/:/bin/'
}
