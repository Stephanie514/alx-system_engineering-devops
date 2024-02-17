# 0-strace_is_your_friend.pp

# Define the file to edit
$file_to_edit = '/var/www/html/wp-settings.php'

# Replace line containing "phpp" with "php"
exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => ['/bin','/usr/bin'],
}

# Define Apache service
service { 'apache2':
  ensure  => running,
  enable  => true,
  require => Exec['replace_line'],
}
