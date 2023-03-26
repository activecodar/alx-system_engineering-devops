#automate the ssh process with puppet
file { '/etc/ssh/ssh_config':
  ensure => present,
}
