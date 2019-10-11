# will fix the limit to 4096
exec { 'fix limit':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => 'sed -i \'s/\"\-n\ 15\"/\"\-n\ 4096\"/g\'  /etc/default/nginx \
  && service nginx restart'
}
