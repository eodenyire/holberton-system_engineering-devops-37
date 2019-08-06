# creates a manifest that kill killmenow
exec { 'pkill':
  command => 'pkill killmenow',
  path    => '/usr/bin',
}