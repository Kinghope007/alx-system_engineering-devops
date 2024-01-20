# Define an exec resource to kill the process named "killmenow"
exec { 'killmenow':
  command     => 'pkill killmenow',
  path        => '/bin:/usr/bin',
  refreshonly => true,
}
