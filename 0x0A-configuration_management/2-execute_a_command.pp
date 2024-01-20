# Define an exec resource to kill the process named "killmenow"
exec { 'pkill killmenow':
  path        => '/usr/bin:/usr/sbin:/bin',
}
