# write ssh cobfig file
file_line {'Turn off passwd auth':
  ensure => 'present',
  line   => '  BatchMode yes',
  path   => '~/.ssh/config',
}

file_line {'Declare identity file':
  ensure => 'present',
  line   => '  IdentityFile ~/.ssh/school',
  path   => '~/.ssh/config',
}
