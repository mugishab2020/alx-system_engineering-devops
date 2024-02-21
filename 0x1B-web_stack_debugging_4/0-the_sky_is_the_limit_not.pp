#Sky is the limit, let's bring that limit highe

exec { 'fix--for-nginx':
  command => ['/bin/sed', '-i', 's/15/4096/', '/etc/default/nginx'],
  path    => ['/usr/local/bin/', '/bin'],
}

# Restart Nginx
exec { 'nginx-restart':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/',
  require => Exec['fix--for-nginx'], 
}
