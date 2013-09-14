### Common ###

Exec { path => '/usr/bin:/bin:/usr/sbin:/sbin' }

exec { "apt-get update": }


### APT settings ###

class { 'apt':
  always_apt_update    => true,
  disable_keys         => undef,
  proxy_host           => false,
  proxy_port           => '8888',
  purge_sources_list   => false,
  purge_sources_list_d => false,
  purge_preferences_d  => false
}


# APT pg 9.3
exec { "wget --quiet -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | sudo apt-key add -": }

apt::source { 'pgdg':
  location          => 'http://apt.postgresql.org/pub/repos/apt/',
  release           => 'squeeze-pgdg',
  repos             => 'main',
  include_src       => false

}


### Packages ###

$needed_packages = [ "build-essential", "postgresql-9.3", "pgadmin3", "libevent-dev"]
$enhancer_packages = [ "git", "vim"]

package { [$needed_packages, $enhancer_packages] : 
    ensure => present,
    require => Exec["apt-get update"],
}


### DB settings ###


### Python ###

class { 'python':
    version    => 'system',
    dev        => true,
    virtualenv => true,
    gunicorn   => false,
}


python::virtualenv { '/home/vagrant/virtualenvs/mycarhistory':
  ensure       => present,
  version      => 'system',
  requirements => '/vagrant/requirements.txt',
}

