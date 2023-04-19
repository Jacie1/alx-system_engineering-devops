file { '/etc/nginx/conf.d/custom-http-response-header.conf':
  content => "add_header X-Served-By $hostname;",
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure => 'running',
  enable => true,
}
