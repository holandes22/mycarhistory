### Common ###
$project_name = "mycarhistory"

Exec { path => "/usr/bin:/bin:/usr/sbin:/sbin" }

exec { "apt-get-update": 
    command => "apt-get update",
}

exec { "pg-apt-key": 
    command => "wget --quiet -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | sudo apt-key add -"
}


### APT settings ###
class { "apt": }

# APT pg 9.3
apt::source { "pgdg":
  location    => "http://apt.postgresql.org/pub/repos/apt/",
  release     => "squeeze-pgdg",  # Using debian squeeze seems to work fine in Ubuntu 13.04
  repos       => "main",
  include_src => false,
  require     => Exec["pg-apt-key"],      
}


### Packages ###
$needed_packages = [ "build-essential", "postgresql-9.3", "postgresql-server-dev-9.3", "pgadmin3", "libpq-dev", "libevent-dev"]
$enhancer_packages = [ "git", "vim"]

package { "all-packages" : 
    name    => [$needed_packages, $enhancer_packages],
    ensure  => present,
    require => [Exec["apt-get-update"], Class["apt"]]
}


### DB settings ###
include postgresql::server

postgresql::db { "${project_name}_db":
  user     => "vagrant",
  password => "vagrant",
}


### Python ###
class { "python":
    version    => "system",
    dev        => true,
    virtualenv => true,
    gunicorn   => false,
}

python::virtualenv { "/home/vagrant/virtualenvs/${project_name}":
  ensure       => present,
  version      => "system",
  requirements => "/vagrant/requirements.txt",
  require      => Package["all-packages"],
}
