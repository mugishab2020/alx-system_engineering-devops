# killing the procces with pkill
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin/'
}
