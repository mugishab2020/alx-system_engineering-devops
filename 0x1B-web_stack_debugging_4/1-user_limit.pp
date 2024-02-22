#Change the OS configuration so that it is possible to login with the holberton
#user and open a file without any error message
exec { 'changing soft limit':
  command  => "sed -i 's/^holberton soft nofile.*/holberton soft nofile 5000/' /etc/security/limits.conf",
  provider => 'shell',
}

exec { 'changing hard limit':
  command  => "sed -i 's/^holberton hard nofile.*/holberton hard nofile 5000/' /etc/security/limits.conf",
  provider => 'shell',
}
