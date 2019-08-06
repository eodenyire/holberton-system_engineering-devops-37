# creates a manifest that kill killmenow
exec { 'killmenow' :
  command  => 'pkill -f ./killmenow',
  provider => 'shell',
}