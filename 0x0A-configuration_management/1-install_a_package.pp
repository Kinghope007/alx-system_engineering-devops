# Define a package resource for Flask
package { 'Flask':
  # Ensure that the package is installed
  ensure   => '2.1.0',
  # Specify that the package should be installed using pip3
  provider => 'pip3',
}

package { 'Werkzeug':
  ensure   => '2.1.1', # Specify a version compatible with Flask 2.1.0
  provider => 'pip3',
}
