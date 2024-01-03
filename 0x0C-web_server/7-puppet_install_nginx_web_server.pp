# Ensure Nginx is installed and running

package { 'nginx':
  ensure => 'installed',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file_line { 'redirect_me_config':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  after  => 'listen 80 default_server;',
  notify => Service['nginx'],
}

file { '/etc/nginx/sites-available/default':
  ensure => file,
  content => "
server {
    listen 80 default_server;
    root /var/www/html;
    index index.html;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location = /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
}
",
  notify => Service['nginx'],
}

service { 'nginx':
  ensure => 'running',
  enable => true,
  require => Package['nginx'],
}

