# Create a file
file { '/tmp/school':
  # Ensure that the resource is a file
  ensure  => file,
  # Set the file permissions to 0744
  mode    => '0744',
  # Set the file owner to www-data
  owner   => 'www-data',
  # Set the file group to www-data
  group   => 'www-data',
  # Specify the content of the file
  content => 'I love Puppet',
}
