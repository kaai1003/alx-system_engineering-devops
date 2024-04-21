# write ssh cobfig file
file_line {'Turn off passwd auth':
  ensure => 'present',
  line   => '  BatchMode yes',
  path   => '/etc/ssh/ssh_confi',
}

file_line {'Declare identity file':
  ensure => 'present',
  line   => '  IdentityFile ~/.ssh/school',
  path   => '/etc/ssh/ssh_confi',
}
